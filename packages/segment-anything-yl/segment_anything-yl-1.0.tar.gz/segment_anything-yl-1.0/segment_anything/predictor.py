# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
import functools
import numpy as np
import torch
import torch.nn.functional as F

from .modeling import Sam

from typing import Optional, Tuple

from .utils.transforms import ResizeLongestSide


def postprocess_masks(
        img_size: int,
        masks: torch.Tensor,
        input_size: Tuple[int, ...],
        original_size: Tuple[int, ...],
) -> torch.Tensor:
    """
    Remove padding and upscale masks to the original image size.

    Arguments:
      masks (torch.Tensor): Batched masks from the mask_decoder,
        in BxCxHxW format.
      input_size (tuple(int, int)): The size of the image input to the
        model, in (H, W) format. Used to remove padding.
      original_size (tuple(int, int)): The original size of the image
        before resizing for input to the model, in (H, W) format.

    Returns:
      (torch.Tensor): Batched masks in BxCxHxW format, where (H, W)
        is given by original_size.
    """
    masks = F.interpolate(
        masks,
        (img_size, img_size),
        mode="bilinear",
        align_corners=False,
    )
    masks = masks[..., : input_size[0], : input_size[1]]
    masks = F.interpolate(masks, original_size, mode="bilinear", align_corners=False)
    return masks

def preprocess(img_size: int, pixel_mean: torch.Tensor, pixel_std: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Normalize pixel values and pad to a square input."""
    # Normalize colors
    x = (x - pixel_mean) / pixel_std

    # Pad
    h, w = x.shape[-2:]
    padh = img_size - h
    padw = img_size - w
    x = F.pad(x, (0, padw, 0, padh))
    return x


class SamPredictor:
    original_sam_img_size: int = 1024
    pixel_mean = torch.Tensor([123.675, 116.28, 103.53]).view(-1, 1, 1)
    pixel_std = torch.Tensor([58.395, 57.12, 57.375]).view(-1, 1, 1)
    def __init__(
        self,
        sam_model: Sam,
    ) -> None:
        """
        Uses SAM to calculate the image embedding for an image, and then
        allow repeated, efficient mask prediction given prompts.

        Arguments:
          sam_model (Sam): The model to use for mask prediction.
        """
        super().__init__()
        self.model = sam_model
        self.image_encoder_type = self.model.image_encoder.__class__.__name__
        if self.image_encoder_type in ['TinyViT', 'FasterTinyViT', 'SAMEncoderViT', 'DINOSAMViT', 'FlashVisionTransformer']:
            self.multi_output = False
            if self.image_encoder_type in ['FasterTinyViT', 'SAMEncoderViT', 'DINOSAMViT', 'FlashVisionTransformer']:
                self.input_img_size = (self.model.image_encoder.img_size, self.model.image_encoder.img_size)
            else:
                self.input_img_size = (self.original_sam_img_size, self.original_sam_img_size)
        else:
            self.multi_output = True
            self.input_img_size = (self.original_sam_img_size, self.original_sam_img_size)
        self.transform = ResizeLongestSide(self.original_sam_img_size)
        self.preprocess = functools.partial(preprocess, self.original_sam_img_size, self.pixel_mean, self.pixel_std)
        self.postprocess_masks = functools.partial(postprocess_masks, self.original_sam_img_size)
        self.reset_image()

    def set_image(
        self,
        image: np.ndarray,
        image_format: str = "RGB",
    ) -> None:
        """
        Calculates the image embeddings for the provided image, allowing
        masks to be predicted with the 'predict' method.

        Arguments:
          image (np.ndarray): The image for calculating masks. Expects an
            image in HWC uint8 format, with pixel values in [0, 255].
          image_format (str): The color format of the image, in ['RGB', 'BGR'].
        """
        assert image_format in [
            "RGB",
            "BGR",
        ], f"image_format must be in ['RGB', 'BGR'], is {image_format}."
        # import pdb;pdb.set_trace()
        if image_format != self.model.image_format:
            image = image[..., ::-1]

        # Transform the image to the form expected by the model
        # import pdb;pdb.set_trace()
        input_image = self.transform.apply_image(image)
        input_image_torch = torch.as_tensor(input_image, device=self.device)
        input_image_torch = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]

        self.set_torch_image(input_image_torch, image.shape[:2])

    @torch.no_grad()
    def set_torch_image(
        self,
        transformed_image: torch.Tensor,
        original_image_size: Tuple[int, ...],
    ) -> None:
        """
        Calculates the image embeddings for the provided image, allowing
        masks to be predicted with the 'predict' method. Expects the input
        image to be already transformed to the format expected by the model.

        Arguments:
          transformed_image (torch.Tensor): The input image, with shape
            1x3xHxW, which has been transformed with ResizeLongestSide.
          original_image_size (tuple(int, int)): The size of the image
            before transformation, in (H, W) format.
        """
        assert (
            len(transformed_image.shape) == 4
            and transformed_image.shape[1] == 3
            # and max(*transformed_image.shape[2:]) == self.model.image_encoder.img_sizenot
        ), f"set_torch_image input must be BCHW with long side {self.model.image_encoder.img_size}."
        self.reset_image()

        self.original_size = original_image_size
        self.input_size = tuple(transformed_image.shape[-2:])
        input_image = self.preprocess(transformed_image.cpu()).to(self.model.device)
        if self.input_img_size != (1024, 1024):
            input_image = F.interpolate(input_image, size=self.input_img_size, mode='bilinear')
        if not self.multi_output:
            self.features = self.model.image_encoder(input_image)
            self.interm_features = None
        else:
            self.features, self.interm_features = self.model.image_encoder(input_image)
        # self.features, self.interm_features = self.model.image_encoder(input_image), None if self.use_mobile_sam else self.model.image_encoder(input_image)
        self.is_image_set = True

    def predict(
        self,
        point_coords: Optional[np.ndarray] = None,
        point_labels: Optional[np.ndarray] = None,
        box: Optional[np.ndarray] = None,
        mask_input: Optional[np.ndarray] = None,
        multimask_output: bool = True,
        return_logits: bool = False,
        hq_token_only: bool =False,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Predict masks for the given input prompts, using the currently set image.

        Arguments:
          point_coords (np.ndarray or None): A Nx2 array of point prompts to the
            model. Each point is in (X,Y) in pixels.
          point_labels (np.ndarray or None): A length N array of labels for the
            point prompts. 1 indicates a foreground point and 0 indicates a
            background point.
          box (np.ndarray or None): A length 4 array given a box prompt to the
            model, in XYXY format.
          mask_input (np.ndarray): A low resolution mask input to the model, typically
            coming from a previous prediction iteration. Has form 1xHxW, where
            for SAM, H=W=256.
          multimask_output (bool): If true, the model will return three masks.
            For ambiguous input prompts (such as a single click), this will often
            produce better masks than a single prediction. If only a single
            mask is needed, the model's predicted quality score can be used
            to select the best mask. For non-ambiguous prompts, such as multiple
            input prompts, multimask_output=False can give better results.
          return_logits (bool): If true, returns un-thresholded masks logits
            instead of a binary mask.

        Returns:
          (np.ndarray): The output masks in CxHxW format, where C is the
            number of masks, and (H, W) is the original image size.
          (np.ndarray): An array of length C containing the model's
            predictions for the quality of each mask.
          (np.ndarray): An array of shape CxHxW, where C is the number
            of masks and H=W=256. These low resolution logits can be passed to
            a subsequent iteration as mask input.
        """
        if not self.is_image_set:
            raise RuntimeError("An image must be set with .set_image(...) before mask prediction.")

        # Transform input prompts
        coords_torch, labels_torch, box_torch, mask_input_torch = None, None, None, None
        if point_coords is not None:
            assert (
                point_labels is not None
            ), "point_labels must be supplied if point_coords is supplied."
            point_coords = self.transform.apply_coords(point_coords, self.original_size)
            coords_torch = torch.as_tensor(point_coords, dtype=torch.float, device=self.device)
            labels_torch = torch.as_tensor(point_labels, dtype=torch.int, device=self.device)
            coords_torch, labels_torch = coords_torch[None, :, :], labels_torch[None, :]
        if box is not None:
            box = self.transform.apply_boxes(box, self.original_size)
            box_torch = torch.as_tensor(box, dtype=torch.float, device=self.device)
            box_torch = box_torch[None, :]
        if mask_input is not None:
            mask_input_torch = torch.as_tensor(mask_input, dtype=torch.float, device=self.device)
            mask_input_torch = mask_input_torch[None, :, :, :]

        masks, iou_predictions, low_res_masks = self.predict_torch(
            coords_torch,
            labels_torch,
            box_torch,
            mask_input_torch,
            multimask_output,
            return_logits=return_logits,
            hq_token_only=hq_token_only,
        )

        masks_np = masks[0].detach().cpu().numpy()
        iou_predictions_np = iou_predictions[0].detach().cpu().numpy()
        low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
        return masks_np, iou_predictions_np, low_res_masks_np

    @torch.no_grad()
    def predict_torch(
        self,
        point_coords: Optional[torch.Tensor],
        point_labels: Optional[torch.Tensor],
        boxes: Optional[torch.Tensor] = None,
        mask_input: Optional[torch.Tensor] = None,
        multimask_output: bool = True,
        return_logits: bool = False,
        hq_token_only: bool =False,
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Predict masks for the given input prompts, using the currently set image.
        Input prompts are batched torch tensors and are expected to already be
        transformed to the input frame using ResizeLongestSide.

        Arguments:
          point_coords (torch.Tensor or None): A BxNx2 array of point prompts to the
            model. Each point is in (X,Y) in pixels.
          point_labels (torch.Tensor or None): A BxN array of labels for the
            point prompts. 1 indicates a foreground point and 0 indicates a
            background point.
          boxes (np.ndarray or None): A Bx4 array given a box prompt to the
            model, in XYXY format.
          mask_input (np.ndarray): A low resolution mask input to the model, typically
            coming from a previous prediction iteration. Has form Bx1xHxW, where
            for SAM, H=W=256. Masks returned by a previous iteration of the
            predict method do not need further transformation.
          multimask_output (bool): If true, the model will return three masks.
            For ambiguous input prompts (such as a single click), this will often
            produce better masks than a single prediction. If only a single
            mask is needed, the model's predicted quality score can be used
            to select the best mask. For non-ambiguous prompts, such as multiple
            input prompts, multimask_output=False can give better results.
          return_logits (bool): If true, returns un-thresholded masks logits
            instead of a binary mask.

        Returns:
          (torch.Tensor): The output masks in BxCxHxW format, where C is the
            number of masks, and (H, W) is the original image size.
          (torch.Tensor): An array of shape BxC containing the model's
            predictions for the quality of each mask.
          (torch.Tensor): An array of shape BxCxHxW, where C is the number
            of masks and H=W=256. These low res logits can be passed to
            a subsequent iteration as mask input.
        """
        if not self.is_image_set:
            raise RuntimeError("An image must be set with .set_image(...) before mask prediction.")

        if point_coords is not None:
            points = (point_coords, point_labels)
        else:
            points = None

        # Embed prompts
        sparse_embeddings, dense_embeddings = self.model.prompt_encoder(
            points=points,
            boxes=boxes,
            masks=mask_input,
        )

        # Predict masks
        low_res_masks, iou_predictions = self.model.mask_decoder(
            image_embeddings=self.features,
            image_pe=self.model.prompt_encoder.get_dense_pe(),
            sparse_prompt_embeddings=sparse_embeddings,
            dense_prompt_embeddings=dense_embeddings,
            multimask_output=multimask_output,
            hq_token_only=hq_token_only,
            interm_embeddings=self.interm_features,
        )

        # Upscale the masks to the original image resolution
        # masks = self.model.postprocess_masks(low_res_masks, self.input_size, self.original_size)
        masks = self.postprocess_masks(low_res_masks, self.input_size, self.original_size)

        if not return_logits:
            masks = masks > self.model.mask_threshold

        return masks, iou_predictions, low_res_masks

    def get_image_embedding(self) -> torch.Tensor:
        """
        Returns the image embeddings for the currently set image, with
        shape 1xCxHxW, where C is the embedding dimension and (H,W) are
        the embedding spatial dimension of SAM (typically C=256, H=W=64).
        """
        if not self.is_image_set:
            raise RuntimeError(
                "An image must be set with .set_image(...) to generate an embedding."
            )
        assert self.features is not None, "Features must exist if an image has been set."
        return self.features

    @property
    def device(self) -> torch.device:
        return self.model.device

    def reset_image(self) -> None:
        """Resets the currently set image."""
        self.is_image_set = False
        self.features = None
        self.orig_h = None
        self.orig_w = None
        self.input_h = None
        self.input_w = None
class SamEncoder:
    def __init__(
            self,
            sam_model: Sam,
    ) -> None:
        super().__init__()
        self.image_encoder = sam_model.image_encoder
        self.transform = ResizeLongestSide(self.image_encoder.img_size)
        self.image_format = sam_model.image_format
        self.device = sam_model.device
        self.pixel_mean = sam_model.pixel_mean
        self.pixel_std = sam_model.pixel_std

        if self.image_encoder.__class__.__name__ == 'TinyViT':
            self.sam_features_dim: int = 256
            self.use_mobile_sam = True
            self.sam_interm_features_num: int = 0
            self.sam_interm_features_dim: int = 0
            self.sam_features_size: int = 64
        else:
            self.sam_features_dim: int = self.image_encoder.neck[2].out_channels
            self.use_mobile_sam = False
            blocks = self.image_encoder.blocks
            self.sam_interm_features_num: int = len([block for block in blocks if block.window_size == 0])
            self.sam_interm_features_dim: int = blocks[0].mlp.lin2.out_features
            self.sam_features_size: int = self.image_encoder.img_size // self.image_encoder.patch_embed.proj.kernel_size[0]
        del sam_model
        self.reset_image()
    def set_image(
        self,
        image: np.ndarray,
        image_format: str = "RGB",
    ) -> None:
        assert image_format in [
            "RGB",
            "BGR",
        ], f"image_format must be in ['RGB', 'BGR'], is {image_format}."
        # import pdb;pdb.set_trace()
        if image_format != self.image_format:
            image = image[..., ::-1]

        # Transform the image to the form expected by the model
        # import pdb;pdb.set_trace()
        input_image = self.transform.apply_image(image)
        input_image_torch = torch.as_tensor(input_image, device=self.device)
        input_image_torch = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]

        self.set_torch_image(input_image_torch, image.shape[:2])

    @torch.no_grad()
    def set_torch_image(
        self,
        transformed_image: torch.Tensor,
        original_image_size: Tuple[int, ...],
    ) -> None:
        assert (
            len(transformed_image.shape) == 4
            and transformed_image.shape[1] == 3
            and max(*transformed_image.shape[2:]) == self.image_encoder.img_size
        ), f"set_torch_image input must be BCHW with long side {self.image_encoder.img_size}."
        self.reset_image()
        self.original_size = original_image_size
        self.input_size = tuple(transformed_image.shape[-2:])
        input_image = preprocess(self.image_encoder.img_size, self.pixel_mean, self.pixel_std, transformed_image)
        self.features, self.interm_features = self.image_encoder(input_image), None if self.use_mobile_sam else self.image_encoder(input_image)
        self.is_image_set = True
    def reset_image(self) -> None:
        """Resets the currently set image."""
        self.is_image_set = False
        self.features = None
        self.orig_h = None
        self.orig_w = None
        self.input_h = None
        self.input_w = None
class SamDecoder:
    def __init__(
            self,
            sam_model: Sam,
    ) -> None:
        super().__init__()
        self.prompt_encoder = sam_model.prompt_encoder
        self.mask_decoder = sam_model.mask_decoder
        self.transform = ResizeLongestSide(sam_model.image_encoder.img_size)
        self.img_size = sam_model.image_encoder.img_size
        self.device = sam_model.device
        self.mask_threshold = sam_model.mask_threshold
        del sam_model
        self.reset_features()
    # def set_features(self, features, interm_features, original_size):
    #     self.original_size = original_size
    #     self.input_size = self.transform.get_preprocess_shape(self.original_size[0], self.original_size[1], self.img_size)
    #     self.features = features
    #     self.interm_features = interm_features
    #     self.is_features_set = True
    def set_features(self, features, original_size):
        self.original_size = original_size
        self.input_size = self.transform.get_preprocess_shape(self.original_size[0], self.original_size[1], self.img_size)
        self.features = features
        self.is_features_set = True
    def reset_features(self):
        self.original_size = None
        self.features = None
        self.is_features_set = False
    def predict(
        self,
        point_coords: Optional[np.ndarray] = None,
        point_labels: Optional[np.ndarray] = None,
        box: Optional[np.ndarray] = None,
        mask_input: Optional[np.ndarray] = None,
        multimask_output: bool = True,
        return_logits: bool = False,
        hq_token_only: bool =False,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        if not self.is_features_set:
            raise RuntimeError("features must be set with .set_features(...) before mask prediction.")

        # Transform input prompts
        coords_torch, labels_torch, box_torch, mask_input_torch = None, None, None, None
        if point_coords is not None:
            assert (
                point_labels is not None
            ), "point_labels must be supplied if point_coords is supplied."
            point_coords = self.transform.apply_coords(point_coords, self.original_size)
            coords_torch = torch.as_tensor(point_coords, dtype=torch.float, device=self.device)
            labels_torch = torch.as_tensor(point_labels, dtype=torch.int, device=self.device)
            coords_torch, labels_torch = coords_torch[None, :, :], labels_torch[None, :]
        if box is not None:
            box = self.transform.apply_boxes(box, self.original_size)
            box_torch = torch.as_tensor(box, dtype=torch.float, device=self.device)
            box_torch = box_torch[None, :]
        if mask_input is not None:
            mask_input_torch = torch.as_tensor(mask_input, dtype=torch.float, device=self.device)
            mask_input_torch = mask_input_torch[None, :, :, :]

        masks, iou_predictions, low_res_masks = self.predict_torch(
            coords_torch,
            labels_torch,
            box_torch,
            mask_input_torch,
            multimask_output,
            return_logits=return_logits,
            hq_token_only=hq_token_only,
        )

        masks_np = masks[0].detach().cpu().numpy()
        iou_predictions_np = iou_predictions[0].detach().cpu().numpy()
        low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
        return masks_np, iou_predictions_np, low_res_masks_np

    @torch.no_grad()
    def predict_torch(
        self,
        point_coords: Optional[torch.Tensor],
        point_labels: Optional[torch.Tensor],
        boxes: Optional[torch.Tensor] = None,
        mask_input: Optional[torch.Tensor] = None,
        multimask_output: bool = True,
        return_logits: bool = False,
        hq_token_only: bool =False,
        interm_embeddings: torch.Tensor = None
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        if not self.is_features_set:
            raise RuntimeError("features must be set with .set_features(...) before mask prediction.")

        if point_coords is not None:
            points = (point_coords, point_labels)
        else:
            points = None

        # Embed prompts
        sparse_embeddings, dense_embeddings = self.prompt_encoder(
            points=points,
            boxes=boxes,
            masks=mask_input,
        )

        # Predict masks
        low_res_masks, iou_predictions = self.mask_decoder(
            image_embeddings=self.features,
            image_pe=self.prompt_encoder.get_dense_pe(),
            sparse_prompt_embeddings=sparse_embeddings,
            dense_prompt_embeddings=dense_embeddings,
            multimask_output=multimask_output,
            hq_token_only=hq_token_only,
            interm_embeddings=interm_embeddings
        )

        # Upscale the masks to the original image resolution
        masks = postprocess_masks(self.img_size, low_res_masks, self.input_size, self.original_size)

        if not return_logits:
            masks = masks > self.mask_threshold

        return masks, iou_predictions, low_res_masks

# Prompting SAM with detected boxes
def segment(sam_predictor: SamPredictor, image: np.ndarray, xyxy: np.ndarray) -> np.ndarray:
    sam_predictor.set_image(image)
    result_masks = []
    for box in xyxy:
        masks, scores, logits = sam_predictor.predict(
            box=box,
            multimask_output=True
        )
        index = np.argmax(scores)
        result_masks.append(masks[index])
    return np.array(result_masks)
# def sam_decode(sam_decoder: SamDecoder, features: torch.Tensor, interm_features: list, original_size: tuple, xyxy: np.ndarray) -> np.ndarray:
#     sam_decoder.set_features(features, interm_features, original_size)
#     result_masks = []
#     for box in xyxy:
#         masks, scores, logits = sam_decoder.predict(
#             box=box,
#             multimask_output=True
#         )
#         index = np.argmax(scores)
#         result_masks.append(masks[index])
#     return np.array(result_masks)
def sam_decode(sam_decoder: SamDecoder, features: torch.Tensor, original_size: tuple, xyxy: np.ndarray) -> np.ndarray:
    sam_decoder.set_features(features, original_size)
    result_masks = []
    for box in xyxy:
        masks, scores, logits = sam_decoder.predict(
            box=box,
            multimask_output=True
        )
        index = np.argmax(scores)
        result_masks.append(masks[index])
    return np.array(result_masks)