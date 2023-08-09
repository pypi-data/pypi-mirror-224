from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='simple_mapillary',
    version='0.0.1',
    license='MIT',
    description='Simplified Python library for accessing the Mapillary API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ibai Gorordo',
    url='https://github.com/ibaiGorordo/simple-mapillary-python-sdk',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'imread-from-url',
        'requests',
    ],
)