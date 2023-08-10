# %%
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision import (
    ImageBoxes,
    OCR,
    detect_text, detect_text_full, detect_text_boxes, detect_text_element, detect_text_elements,
    model_dispatch,
    AnnoDraw,
    ImageTransform,
    COLOR,
    Chrono,
)
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_dark'


# %%
img_fp = '/home/test/code/image2layout_computer_vision/data/inputs/Coterie benefits.png'
img_fp = '/home/test/code/image2layout_computer_vision/data/inputs/Screenshot 2023-07-13 at 11.03.48.png'
img = Image.open(img_fp).convert('RGB')
image_np = np.array(img)
img.size
# img

# %%
data_merged, data_raw = detect_text_full(
    img,
    # row_hdist_max=0.6,
    # row_vdist_max=1.4,
    # row_height_ratio_min=0.8,
)
data_merged, data_raw

img_anno_merged = AnnoDraw.draw_anno_text_overlay(
    img=img,
    boxes=[v['box'] for v in data_merged],
    texts=[v['text'] for v in data_merged],
    width=2,
    text_pad=None,
    # color='#00FF88',
    color_text='#000000',
    # font=None,
    # font='data/OpenSans_Condensed-Medium.ttf',
    opacity=0.75,
)

img_anno_raw = AnnoDraw.draw_anno_text_overlay(
    img=img,
    boxes=[v['box'] for v in data_raw],
    texts=[v['text'] for v in data_raw],
    width=2,
    text_pad=None,
    # color='#00FF88',
    color_text='#000000',
    # font='OpenSans_Condensed-Medium.ttf',
    # font='data/OpenSans_Condensed-Medium.ttf',
    opacity=0.75,
)

img_anno_merged.convert('RGB')

# %%
img_anno_dual = ImageTransform.concatenate(
    [img_anno_merged],
    # [img_anno_merged, img_anno_raw],
    # [img, img_anno_merged],
    # [img, img_anno_raw, img_anno_merged],
    columns=1,
    spacing=10,
)
img_anno_dual.convert('RGB')


# %%
data_merged, data_raw = OCR.detect_text_boxes(
    img,
)
img_anno_boxes = AnnoDraw.draw_anno_text_overlay(
    img=img,
    boxes=[v['box'] for v in data_raw],
    texts=[v['text'] for v in data_raw],
    width=2,
    text_pad=None,
    # color='#00FF88',
    color_text='#000000',
    # font='OpenSans_Condensed-Medium.ttf',
    # font='data/OpenSans_Condensed-Medium.ttf',
    opacity=0.75,
)
img_anno_boxes.convert('RGB')

# %%
data_raw = OCR.detect_text_element(
    img,
)

img_anno_element = AnnoDraw.draw_anno_text_overlay(
    img=img,
    boxes=[v['box'] for v in data_raw],
    texts=[v['text'] for v in data_raw],
    width=2,
    text_pad=None,
    # color='#00FF88',
    color_text='#000000',
    # font='OpenSans_Condensed-Medium.ttf',
    # font='data/OpenSans_Condensed-Medium.ttf',
    opacity=0.75,
)
img_anno_element.convert('RGB')


# %%
# results = model_dispatch.paddle_ocr.ocr(image_np, cls=True)
results = model_dispatch.paddle_ocr.ocr(image_np, rec=False)
# results = model_dispatch.paddle_detect.ocr(image_np, rec=False)
results

# %%





# %% compare boxes vs element
fps = glob.glob('/home/test/code/image2layout_computer_vision/data/inputs/*.png')[:3]
data = []
for i, fp in enumerate(fps):
    _img = Image.open(fp).convert('RGB')
    
    for j in list(range(2)):
        detection_only = (i % 2 == j)
        time_start = time.perf_counter()
        if detection_only:
            data_merged, data_raw = OCR.detect_text_boxes(
                _img,
            )
        else:
            data_raw = OCR.detect_text_element(
                _img,
            )
        time_cost = time.perf_counter() - time_start
        data.append({
            'image_index': i,
            'detection_only': detection_only,
            'time_cost': time_cost,
        })
    
    print(f'\r[{i+1}/{len(fps)}]      ', end='')

df = pd.DataFrame(data)
df

# %%
px.scatter(
    df,
    x='image_index',
    y='time_cost',
    color='detection_only',
)

# %%










# %% compare batch vs loop
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision import (
    ImageBoxes,
    OCR,
    detect_text, detect_text_full, detect_text_boxes, detect_text_element, detect_text_elements,
    model_dispatch,
    AnnoDraw,
    ImageTransform,
    COLOR,
    Chrono,
)
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_dark'

fps = glob.glob('/home/test/code/image2layout_computer_vision/data/inputs/*.png')
bs = 10
fps = (fps * 10)[:bs]
count = len(fps)
batch_count = int(count // bs)
data = []
OCR._load()

for i in range(batch_count):
    _fps = fps[i * bs : (i + 1) * bs]
    _imgs = [
        Image.open(fp).convert('RGB')
        for fp in _fps
    ]
    
    for j in list(range(2)):
        batched = (i % 2 == 1-j)
        print(f'\r[{i}/{batch_count}] batched[{batched}]     ', end='')
        time_start = time.perf_counter()
        data_raws = []
        
        if batched:
            data_raws = OCR.detect_text_elements(
                _imgs,
            )
        else:
            for _img in _imgs:
                data_raw = OCR.detect_text_element(
                    _img,
                )
                data_raws.append(data_raw)
        
        time_cost = time.perf_counter() - time_start
        data.append({
            'image_index': i,
            'batched': batched,
            'time_cost': time_cost,
            'data_raws_str': ' '.join([str(v) for v in data_raws])
        })
    

df = pd.DataFrame(data)
df

# %%
px.scatter(
    df,
    x='image_index',
    y='time_cost',
    color='batched',
)

# %%












# %% compare batch vs loop v2
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision import (
    ImageBoxes, OCR, model_dispatch,
    AnnoDraw, ImageTransform, COLOR,
)
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_dark'

img_fp = '/home/test/code/image2layout_computer_vision/data/inputs/Screenshot 2023-07-13 at 11.03.48.png'
img = Image.open(img_fp).convert('RGB')
img.size

# %%
OCR._load()

time_start = time.perf_counter()
# data_raw = OCR.detect_text_element(img)
data_merged, data_raw = OCR.detect_text_boxes(img)
time_cost = time.perf_counter() - time_start
imgs_element = []
for i, d in enumerate(data_raw):
    box = d['box']
    img_element = img.crop(box)
    imgs_element.append(img_element)
    img_element.save(os.path.join(f'/home/test/code/image2layout_computer_vision/data/elements/{i:03d}.png'))


imgs_np = [
    np.array(_img)
    for _img in imgs_element
]

print(f'whole image time[{time_cost:.3f}s]')
len(imgs_element)

# %%
time_start = time.perf_counter()
for i, _img in enumerate(imgs_element):
    _data_raw = OCR.detect_text_element(_img)
time_cost = time.perf_counter() - time_start

print(f'loop time[{time_cost:.3f}s]')

# %%
time_start = time.perf_counter()
results = model_dispatch.paddle_ocr.ocr(imgs_np, det=False)
time_cost = time.perf_counter() - time_start

print(f'batched det=False time[{time_cost:.3f}s]')

# %%











# %% dispatch multi
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision import (
    ImageBoxes, OCR, model_dispatch,
    AnnoDraw, ImageTransform, COLOR,
    ModelDispatch_Paddle,
)
import concurrent
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import asyncio
import functools

fps_element = glob.glob('/home/test/code/image2layout_computer_vision/data/elements/*.png')
fps_element
imgs_element = [Image.open(fp).convert('RGB') for fp in fps_element]
len(imgs_element)

# %%
class ModelDispatch_Manager:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
        self.model_dispatches = []
        for i in range(max_workers):
            self.model_dispatches.append(ModelDispatch_Paddle())
        self.index = 0
    
    def _load(self):
        for md in self.model_dispatches:
            md._load()
    
    # # TODO: implement async
    # def grab_available_dispatch(self):
    #     if not md.running:
    #         return md
    #     for i in range(self.max_workers):
    #         index = (self.index + i) % self.max_workers
    #         md = self.model_dispatches[index]
    #         if not md.running:
    #             self.index = (index + 1) % self.max_workers
    #             return md
    #     return None
    
    # def wait_and_grab_available_dispatch(self):
    #     # TODO: fix hardcoding of timeout
    #     timeout = 10.0
    #     time_start = time.time()
    #     while time.time() <= time_start + timeout:
    #         md = self.grab_available_dispatch()
    #         if md is not None:
    #             return md
    #     raise TimeoutError('grab timed-out')
    
    # async def _forward_single(self, image):
    #     md = self.wait_and_grab_available_dispatch()
    #     output = md(image)
    #     return output
    
    # async def _forward_pooled(self, image):
        
    #     loop = asyncio.get_event_loop()
    #     with concurrent.futures.ProcessPoolExecutor(max_workers=self.max_workers) as pool:
    #         output = await loop.run_in_executor(
    #             pool,
    #             # functools.partial(
    #             #     self._forward_pooled,
    #             #     *args,
    #             #     **kwargs,
    #             # ),
    #             self._forward_single,
    #             image,
    #         )
        
    #     return output
    
    # def forward(self, images):
    #     # def _detect_text_element(image):
    #     #     data_raw = detect_text_element(image)
    #     #     return data_raw
        
    #     # loop = asyncio.get_event_loop()
    #     # with concurrent.futures.ProcessPoolExecutor(max_workers=self.max_workers) as pool:
    #     #     output = await loop.run_in_executor(
    #     #         pool,
    #     #         # functools.partial(
    #     #         #     self._forward_pooled,
    #     #         #     *args,
    #     #         #     **kwargs,
    #     #         # ),
    #     #         self._forward_pooled,
    #     #         images,
    #     #     )
    #     outputs = [
    #         self._forward_pooled(image)
    #         for image in images
    #     ]
    #     return outputs

mdm = ModelDispatch_Manager(4)
mdm._load()

# mdm.forward(
#     imgs_element[:4]
# )

# %%
import time, os
import glob
import numpy as np
import pandas as pd
from PIL import Image
from image2layout_computer_vision import (
    ImageBoxes, OCR, model_dispatch,
    AnnoDraw, ImageTransform, COLOR,
    ModelDispatch_Paddle,
)
import concurrent
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import asyncio
import functools

fps_element = glob.glob('/home/test/code/image2layout_computer_vision/data/elements/*.png')
fps_element
imgs_element = [Image.open(fp).convert('RGB') for fp in fps_element]
len(imgs_element)

mds = [ModelDispatch_Paddle() for i in range(4)]

def forward_single(md, image):
    assert not md.running
    return md(image)

def forward_multi(images):
    with ProcessPoolExecutor(max_workers=4) as executor:
        outputs = executor.map(forward_single, (mds * (len(images) // len(mds) + 1))[:len(images)], images)
        return list(outputs)

outputs = forward_multi(imgs_element[:6])
print(f'outputs[{len(outputs)}]')
print(outputs)

# %%