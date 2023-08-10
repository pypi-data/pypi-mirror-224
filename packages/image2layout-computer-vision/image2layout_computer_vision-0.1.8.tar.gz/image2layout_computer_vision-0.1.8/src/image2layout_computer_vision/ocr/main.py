# %%
import time
import json
import os
import numpy as np
import pandas as pd
from PIL import Image
from typing import Union, Any, List, Dict, Tuple
from ..utils import get_image, ImageConvert
from .imagebox import ImageBoxes, BoxMerge
from .model_paddle import ModelDispatch_Paddle
# from .model_layoutmlv2 import ModelDispatch_LayoutMLv2

DEVICE = 'cpu'

# %%
import logging
debug_logger = logging.getLogger('ocr')
c_handler = logging.StreamHandler()
debug_logger.addHandler(c_handler)
debug_logger.setLevel(logging.WARNING)

# %%
class OCR:
    model_dispatch = ModelDispatch_Paddle(
        device=DEVICE,
    )
    # model_dispatch = ModelDispatch_LayoutMLv2(
    #     device=DEVICE,
    # )
    
    @classmethod
    def _load(cls, *args, **kwargs):
        return cls.model_dispatch._load()
    
    @classmethod
    def detect_text_raw(cls, image: Union[Image.Image, np.ndarray], recognition=True) -> ImageBoxes:
        '''predict boxes for text in the image, returning raw ImageBoxes object
        Parameters:
            image: (PIL.Image.Image, np.ndarray) RGB image
            recognition: (bool) whether to run ocr recognition for text values, default = True
        Returns:
            imageboxes_raw:    (ImageBoxes) object containing raw prediction boxes
        '''
        _image = get_image(image).convert('RGB')
        # debug_logger.debug(msg=f'detect_text_raw | input[{_image.size}]')
        
        result_df = cls.model_dispatch(_image, detection_only=not recognition)
        
        imageboxes_raw = ImageBoxes(
            image=_image,
            boxes=result_df['box'].tolist(),
        )
        imageboxes_raw.set_texts(result_df['text'].tolist())
        return imageboxes_raw
        
    
    @classmethod
    def detect_text(cls, image: Union[Image.Image, np.ndarray], recognition=True, group_boxes=True, **kwargs) -> Tuple[ImageBoxes]:
        '''predict boxes for text in the image, returning ImageBoxes object(s)
        Parameters:
            image: (PIL.Image.Image, np.ndarray) RGB image
            recognition: (bool) whether to run ocr recognition for text values, default = True
            group_boxes: (bool) whether to group boxes, default = True
            **kwargs:
                line_dist_max:          max distance between boxes to be in the same sentence (as a ratio of line height)
                line_dist_min:          min (negative) distance between boxes to be in the same sentence (as a ratio of line height)
                line_iou_min:           min vertical iou between boxes to be on the same line
                row_hdist_max:          max horizontal offset between rows to aligned as a column (as a ratio of line height)
                row_vdist_max:          max vertical distance between rows to be in the same column (as a ratio of line height)
                row_height_ratio_min:   min ratio between heights of rows to be in the same column
        Returns:
            imageboxes_merged: (ImageBoxes) object containing merged prediction boxes
            imageboxes_raw:    (ImageBoxes) object containing raw prediction boxes
        '''
        _image = get_image(image).convert('RGB')
        # debug_logger.debug(msg=f'detect_text | input[{_image.size}]')
        
        imageboxes_raw = cls.detect_text_raw(_image, recognition=recognition)
        
        imageboxes_merged = None
        if group_boxes:
            imageboxes_merged = imageboxes_raw.to_grouped_imageboxes(**kwargs)
            # debug_logger.debug(msg=f'detect_text | merged[{len(imageboxes_raw.boxes_top)} -> {len(imageboxes_merged.boxes_top)}]')
        
        return imageboxes_merged, imageboxes_raw
    
    @classmethod
    def detect_text_data(cls, image: Union[Image.Image, np.ndarray], recognition=True, group_boxes=True, **kwargs) -> Tuple[List[Dict]]:
        '''detect and recognize text in the image and merge them, returning raw and merged data
        Parameters: (same as detect_text)
        Returns:
            data_merged: (list of dicts) merged result texts, boxes and scores
            data_raw:    (list of dicts) raw result texts, boxes and scores
        '''
        imageboxes_merged, imageboxes_raw = cls.detect_text(
            image,
            recognition=recognition,
            group_boxes=group_boxes,
            **kwargs)
        data_merged = imageboxes_merged.df_top.to_dict('records') if imageboxes_merged is not None else None
        data_raw = imageboxes_raw.df_top.to_dict('records') if imageboxes_raw is not None else None
        
        return data_merged, data_raw
    
    @classmethod
    def detect_text_elements(cls, images: List) -> List[List[Dict]]:
        '''detect texts in multiple images
        Parameters:
            images: (list) list of images
        Returns:
            data_raw_multi:    (list of lists of dicts) raw result texts, boxes and scores
        '''
        # TODO: run multiple detection processes in parallel
        
        data_raw_multi = []
        for image in images:
            _, data_raw = cls.detect_text_data(image, group_boxes=False)
            data_raw_multi.append(data_raw)
        
        return data_raw_multi


# %%