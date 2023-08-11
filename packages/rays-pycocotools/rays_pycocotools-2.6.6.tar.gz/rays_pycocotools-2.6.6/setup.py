from setuptools import setup, Extension, find_packages
import numpy as np

# Define the C extension (setup to only install from PyPI/git branch)
ext_modules = [
    Extension(
        "rays_pycocotools._mask",
        sources=["common/maskApi.c", "rays_pycocotools/_mask.pyx"],
        include_dirs=[np.get_include(), "common"],
        extra_compile_args=["-Wno-cpp", "-Wno-unused-function", "-std=c99"],
    )
]

setup(
    name="rays_pycocotools",
    packages=find_packages(),
    description="Wrapper of pycocotools that correctly installs with pip.",
    long_description=open("README.md").read(),
    version="2.6.6",
    ext_modules=ext_modules,
    python_requires=">=3.6",
)
