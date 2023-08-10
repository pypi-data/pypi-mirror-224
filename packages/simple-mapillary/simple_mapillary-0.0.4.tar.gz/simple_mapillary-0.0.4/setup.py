from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as build_py_orig

package_name = 'simple_mapillary'
exclude = ['__token__.py']
class build_py(build_py_orig):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [(pkg, mod, file, ) for (pkg, mod, file, ) in modules
                if not any(file.endswith(pattern)
                for pattern in exclude)]


# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=package_name,
    version='0.0.4',
    license='MIT',
    description='Simplified Python library for accessing the Mapillary API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ibai Gorordo',
    url='https://github.com/ibaiGorordo/simple-mapillary-python-sdk',
    packages=find_packages(),
    cmdclass={'build_py': build_py},
    install_requires=[
        'numpy',
        'opencv-python',
        'imread-from-url',
        'requests',
        'mapbox-vector-tile',
    ],
    include_package_data=True,
)