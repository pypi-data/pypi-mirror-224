
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision.ocr import OCR
# from image2layout_computer_vision import (
#     OCR,
#     ImageBoxes,
#     detect_text, detect_text_full, detect_text_boxes, detect_text_element, detect_text_elements,
#     model_dispatch,
#     AnnoDraw,
#     ImageTransform,
#     COLOR,
#     Chrono,
# )
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_dark'

# %%
data_merged, data_raw = OCR.detect_text_data(
    '/home/test/code/image2layout_computer_vision/data/inputs/Coterie benefits.png',
    recognition=False,
)

data_raw_multi = OCR.detect_text_elements(
    [
        '/home/test/code/image2layout_computer_vision/data/inputs/Screenshot 2023-07-13 at 11.03.48.png',
        '/home/test/code/image2layout_computer_vision/data/inputs/SCR-20230710-khrl.jpeg',
    ]
)

# %%
print(len(data_merged), len(data_raw), len(data_raw_multi))