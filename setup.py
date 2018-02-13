import numpy as np
from setuptools import setup
from Cython.Build import cythonize

setup(
  name='mmview',
  ext_modules=cythonize("mmview.pyx",
                        gdb_debug=True,
                        include_path=[np.get_include()]),
)
