
from distutils.core import setup

setup(name='Distutils',
    version='0.1.8',
    description='Computer Vision and stuff',
    author='Felix Do',
    author_email='felix.do.1030@gmail.com',
    url='https://github.com/felix-do-wizardry/image2layout-computer-vision',
    # packages=['distutils', 'distutils.command'],
    packages=['image2layout_computer_vision'],
    package_dir={
        'image2layout_computer_vision': 'src/image2layout_computer_vision',
    },
    package_data={
        'image2layout_computer_vision': ['src/image2layout_computer_vision'],
    },
    data_files=[
        ('txt', [
            'src/image2layout_computer_vision/yolov6/class_names.txt',
        ]),
        ('yaml', [
            'src/image2layout_computer_vision/yolov6/data_image2layoutJ.yaml',
            'src/image2layout_computer_vision/yolov6/data_image2layoutH.yaml',
        ]),
    ],
    include_package_data=True,
)