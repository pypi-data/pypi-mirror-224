# %%
import time, os
import numpy as np
import pandas as pd
import string
import colorsys
from PIL import Image, ImageDraw, ImageFont
import torch
import cv2

# %%
def letterbox(im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleup=True, stride=32):
    '''Resize and pad image while meeting stride-multiple constraints.'''
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)
    elif isinstance(new_shape, list) and len(new_shape) == 1:
       new_shape = (new_shape[0], new_shape[0])

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better val mAP)
        r = min(r, 1.0)

    # Compute padding
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding

    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border

    return im, r, (left, top)


# %%
class ModelDispatch_Yolov6:
    PATH_CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
    
    def __init__(self,
                device='cpu',
                auto_load=False,
                log_telemetry=False,
                ckpt_path='',
                conf_thres=0.5,
                img_size=1280,
                stride=64,
                class_names=[],
                ):
        assert device in ['cpu', 'cuda']
        self.device = device
        self.use_gpu = self.device in ['cuda']
        
        self.model = None
        self.ckpt_path = ckpt_path
        
        self.conf_thres = conf_thres
        self.img_size = img_size
        self.stride = stride
        self.class_names = class_names
        self.class_count = len(class_names)
        
        self.loaded = False
        self.running = False
        self.log_telemetry = bool(log_telemetry)
        self.telemetry = {
            'load_time': None,
            'forward_time': [],
        }
        if auto_load:
            self._load()
    
    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
    
    @classmethod
    def _load_from_checkpoint(cls, ckpt_path:str, class_names:list):
        assert isinstance(ckpt_path, str)
        assert os.path.isfile(ckpt_path)
        assert isinstance(class_names, list)
        model = torch.hub.load(
            os.path.join(cls.PATH_CURRENT_DIR),
            'custom',
            ckpt_path=ckpt_path,
            class_names=class_names,
            source='local',
        )
        return model
    
    def _load(self):
        self.model = self._load_from_checkpoint(self.ckpt_path, self.class_names)
        self.model.conf_thres = self.conf_thres
        self.model.img_size = self.img_size
        self.loaded = True
    
    def _unload(self):
        del self.model
        self.model = None
        self.loaded = False
    
    def forward(self, *args, **kwargs):
        self.running = True
        '''default wrapper for _forward method
        '''
        if not self.loaded:
            self._load()
        
        time_start = time.perf_counter()
        
        _output = self._forward(*args, **kwargs)
        
        if self.log_telemetry:
            time_elapsed = time.perf_counter() - time_start
            self.telemetry['forward_time'].append(time_elapsed)
            self.telemetry['forward_time'] = self.telemetry['forward_time'][-20:]
        
        self.running = False
        return _output
    
    @classmethod
    def process_image(cls, path, img_size, stride):
        if isinstance(path, str):
            img_src = np.asarray(Image.open(path).convert('RGB'))
        elif isinstance(path, Image.Image):
            img_src = np.asarray(path.convert('RGB'))
        else:
            assert isinstance(path, np.ndarray)
            img_src = path
        
        image = letterbox(img_src, img_size, stride=stride)[0]
        image = image.transpose((2, 0, 1)) # HWC to CHW
        image = torch.from_numpy(np.ascontiguousarray(image))
        image = image.float()
        image /= 255
        return image, img_src
    
    def _forward(self, image:Image.Image) -> pd.DataFrame:
        img, img_src = self.process_image(image, self.img_size, self.stride)
        
        img = img.to(self.device)
        if len(img.shape) == 3:
            img = img[None]

        prediction = self.model.forward(img, img_src.shape)
        out = {k: v.cpu().numpy() for k, v in prediction.items()}
        out['classes'] = [self.class_names[i] for i in out['labels']]
        
        return out
    
    def forward_df(self, *args, **kwargs):
        out = self.forward(*args, **kwargs)
        
        columns = ['box', 'score', 'class_index', 'class_name']
        keys = ['boxes', 'scores', 'labels', 'classes']
        data = list(zip(*[out[k] for k in keys]))
        
        df = pd.DataFrame(
            columns=columns,
            data=data,
        )
        return df
        
        

# %%