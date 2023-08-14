from setuptools import setup, find_packages

setup(
    name='video_writer_package',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'opencv-python'
    ],
)
