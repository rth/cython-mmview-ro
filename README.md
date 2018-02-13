# mmview

Tests for read only memoryviews in Cython (see [cython/cython#1869](https://github.com/cython/cython/pull/1869))


### Steps to reproduce

1. Clone this repository
3. (optional) Setup a virtual env,
   ```
   conda create -y -n cython-dev-env numpy python=3.6
   conda activate cython-dev-env
   ```
3. [Install the dev version of Cython](http://cython.readthedocs.io/en/latest/src/quickstart/install.html) from [cython#1869](https://github.com/cython/cython/pull/1869):
   ```
   pip install git+https://github.com/scoder/cython@readonly_buffers
   ```
4. Compile this module,
   ```
   cd cython-mmview-ro
   python setup.py build_ext --inplace
   ```
5. Run tests,
   ```
   pytest
   ```
