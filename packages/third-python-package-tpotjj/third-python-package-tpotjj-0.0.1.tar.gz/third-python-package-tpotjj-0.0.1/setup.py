from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("src/third_python_package/harmonic_mean.pyx"),
)