from Cython.Build import cythonize
from setuptools import find_packages, setup

setup(
    packages=find_packages(where="src", exclude=["tests"]),
    ext_modules=cythonize("src/brohub/compiled.pyx"),
)
