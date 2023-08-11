# %%
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image

# %%
from image2layout_computer_vision.yolov6 import Detection
from image2layout_computer_vision.ocr import OCR
from image2layout_computer_vision import (
    get_image, ImageConvert, ImageTransform, AnnoDraw
)

# %%
img_fp = '/home/test/code/image2layout_computer_vision/data/inputs/image 559.png'
img = Image.open(img_fp).convert('RGB')
img.size

# %%
df_out = Detection.detect_element(img)
df_out

# %%
AnnoDraw.draw_anno_box(
    img=img,
    boxes=df_out['box'].tolist(),
    texts=df_out['class_name'].tolist(),
    text_groups=Detection.class_names,
).convert('RGB')

# %%
