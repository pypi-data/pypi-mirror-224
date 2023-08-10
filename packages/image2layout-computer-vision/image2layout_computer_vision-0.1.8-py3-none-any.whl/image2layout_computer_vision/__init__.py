# from . import ocr, color_extract, utils

from .utils import get_image, ImageConvert, COLOR, PixelMask, ImageTransform, Chrono, Timer, AnnoDraw
from .color_extract import ColorExtractor, ExtractColor, extract_colors, extract_colors_multi
# from .ocr import ImageBoxes, BoxMerge, model_dispatch, OCR, ModelDispatch_Paddle
# from .yolov6 import Detection

# model_dispatch_element = Detection.model_dispatch_element
# detect_element = Detection.detect_element

# model_dispatch_ocr = OCR.model_dispatch
# detect_text = OCR.detect_text
# detect_text_full = OCR.detect_text_full
# detect_text_boxes = OCR.detect_text_boxes
# detect_text_element = OCR.detect_text_element
# detect_text_elements = OCR.detect_text_elements
