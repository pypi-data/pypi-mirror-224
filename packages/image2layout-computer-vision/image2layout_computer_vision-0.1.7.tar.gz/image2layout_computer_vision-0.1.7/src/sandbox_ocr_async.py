# # %% outside of jupyter
# import concurrent
# import asyncio
# import functools
# import time
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# workers = 4
# count = 24

# mds = list(range(workers))
# # async def forward_single(md, image):
# def forward_single(md, image):
#     print('start >', md, image)
#     s = 0
#     for i in range(1_000_000):
#         s += i * (-1 if i % 2 else 1)
#     return s

# # async def forward_multi(images):
# def forward_multi(images):
#     # assert len(images) <= len(mds)
#     # forward_coroutines = [
#     #     forward_single(mds[i], images[i])
#     #     for i in range(len(images))
#     # ]
#     # outputs = await asyncio.gather(*forward_coroutines)
#     # return outputs
    
#     # loop = asyncio.get_event_loop()
#     # # with ProcessPoolExecutor(max_workers=workers) as pool:
#     # with ThreadPoolExecutor(max_workers=workers) as executor:
#     #     future_to_index = {
#     #         executor.submit(forward_single, mds[i], images[i]): i
#     #         for i in range(len(images))
#     #     }
#     #     for future in concurrent.futures.as_completed(future_to_index):
#     #         index = future_to_index[future]
#     #         try:
#     #             data = future.result()
#     #         except Exception as exc:
#     #             print(f'[{index}] generated an exception: {exc}')
#     #         else:
#     #             print(f'[{index}] output[{data}]')
    
#     with ProcessPoolExecutor(max_workers=workers) as executor:
#         outputs = executor.map(forward_single, (mds * 10)[:len(images)], images)
#         return list(outputs)
#         # for img, output in zip(images, executor.map(forward_single, mds, images)):
#         #     print(f'{img} > {output}')
                

# time_start = time.perf_counter()

# # result = asyncio.run(forward_multi(list(range(workers))))
# result = forward_multi(list(range(count)))

# print('result:', result)

# time_cost = time.perf_counter() - time_start
# print(f'time[{time_cost:.3f}s] speed[{count/time_cost:.1f}/s]')


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
imgs_element = [Image.open(fp).convert('RGB') for fp in fps_element][:24]
len(imgs_element)

workers = 4
mds = [ModelDispatch_Paddle(device='cpu') for i in range(workers * 2)]
for md in mds:
    md._load()

def forward_single(image, index):
    md = mds[index % len(mds)]
    # while md.running:
    #     time.sleep(0.1)
    return md(image)

def forward_multi(images):
    # with ProcessPoolExecutor(max_workers=workers) as executor:
    #     outputs = executor.map(forward_single, (mds * (len(images) // len(mds) + 1))[:len(images)], images)
    # return list(outputs)
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        print('queuing tasks')
        # _mds = (mds * (len(images) // len(mds) + 1))[:len(images)]
        futures = executor.map(forward_single, images, list(range(len(images))))
        # return futures.result()
        # futures = []
        # for i in range(len(images)):
        #     image = images[i]
        #     md = mds[i % len(mds)]
        #     future = executor.submit(forward_single, md, image)
        #     futures.append(future)
        
        print('awaiting tasks')
        outputs = []
        for output in futures:
            outputs.append(output)
        print('done tasks')
        return outputs

# %%
print(f'[loop] start')
time_start = time.perf_counter()
outputs = []
# mds[0](imgs_element[0])
# output = forward_single(imgs_element[0], 0)
for i, _img in enumerate(imgs_element):
    output = forward_single(_img, 0)
    outputs.append(output)
time_cost = time.perf_counter() - time_start
print(f'[loop] outputs[{len(outputs)}] time[{time_cost:.3f}s]')

# # %%
print(f'[pool] start')
time_start = time.perf_counter()
outputs = forward_multi(imgs_element)
time_cost = time.perf_counter() - time_start
print(f'[pool] outputs[{len(outputs)}] time[{time_cost:.3f}s]')
# print(outputs)

# %%