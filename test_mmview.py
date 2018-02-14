import pytest
import numpy as np
from mmview import getmax, update_array
from mmview import getconst, outer_func


@pytest.fixture
def x():
    return np.arange(10).astype('float')


def test_mmview_rw(x):
    assert getmax(x) == 9


def test_mmview_ro(x):
    x.setflags(write=False)
    assert x.flags.writeable is False
    assert getmax(x) == 9


def test_update_mmview_rw(x):
    update_array(x)


def test_update_mmview_ro(x):
    x.setflags(write=False)
    assert x.flags.writeable is False
    with pytest.raises(ValueError,
                       message="buffer source array is read-only"):
        update_array(x)


def test_const_mmview_rw(x):
    with pytest.raises(Exception):
        getconst(x)


def test_const_mmview_ro(x):
    x.setflags(write=False)
    assert x.flags.writeable is False
    getconst(x)


def test_passing_func_rw(x):
    y = outer_func(x)
    assert y[0] == -99.
    assert y.base.flags.writeable is True


def test_passing_func_ro(x):
    x.setflags(write=False)
    assert x.flags.writeable is False
    y = outer_func(x)
    assert y[0] == -99.
    assert y.base.flags.writeable is False
