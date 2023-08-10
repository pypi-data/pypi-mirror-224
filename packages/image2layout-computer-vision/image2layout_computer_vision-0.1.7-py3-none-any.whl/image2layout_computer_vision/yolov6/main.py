# %%
# from .hubconf import Detector, process_image
import torch
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import colorsys
import yaml
from typing import Union, Any, List, Dict, Tuple

from ..utils import get_image, ImageConvert
from .model_yolov6 import ModelDispatch_Yolov6


# %%
PATH_CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

# %%
# data_config = {}
# with open(os.path.join(PATH_CURRENT_DIR, 'data_image2layoutH.yaml'), 'r') as stream:
#     try:
#         data_config = yaml.safe_load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)

# class_names = data_config.get('names', [])
# class_count = len(class_names)

# # %%
# ckpt_path = '/home/test/code/image2layout/runs/train/H_yolov6m6_g11/weights/best_ckpt.pt'
# os.path.isfile(ckpt_path)

# %%
class Detection:
    model_dispatch_element = None
    loaded = False
    class_names = [
        'text','button','image','input','icon','textarea','row','heading','hero_banner',
        'icon_list_horizontal','icon_list_vertical','countdown_timer','product','p_title',
        'p_desc','p_price','p_quantity','p_images','p_variant','p_button','p_list']
    
    @classmethod
    def _load(cls,
                ckpt_path='/home/test/code/image2layout/runs/train/H_yolov6m6_g11/weights/best_ckpt.pt',
                class_names=None,
                img_size=1280,
                conf_thres=0.5,
                ):
        # TODO: move to logging
        assert img_size in [640, 1280]
        class_names = cls.class_names if class_names is None else class_names
        assert isinstance(class_names, list)
        print(f'[Detection] > loading model with {len(class_names)} classes, from [{ckpt_path}]')
        cls.model_dispatch_element = ModelDispatch_Yolov6(
            device=DEVICE,
            auto_load=False,
            log_telemetry=False,
            ckpt_path=ckpt_path,
            conf_thres=conf_thres,
            img_size=img_size,
            stride=64 if img_size == 1280 else 32,
            class_names=class_names,
        )
        cls.model_dispatch_element._load()
        cls.loaded = True
    
    @classmethod
    def detect_element(cls, image:Image.Image) -> pd.DataFrame:
        if not cls.loaded:
            cls._load()
        img = get_image(image, 'RGB')
        
        df_pred = cls.model_dispatch_element.forward_df(img)
        
        return df_pred
    