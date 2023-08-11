from Cython.Build import cythonize
from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src", exclude=["tests"]),
    ext_modules=cythonize("src/third_python_package/harmonic_mean.pyx"),
)