import sys

import pytest


@pytest.mark.skip(reason="I had disabled")
def test_Marker_1():
    assert 5 > 4


@pytest.mark.skipif(sys.version_info < (3, 8), reason="need python 3.8+")
def test_Marker_2():
    assert 5 > 2


@pytest.mark.xfail(reason="...")
def test_Marker_3():
    assert 2 * 3 == 7


@pytest.mark.xfail(reason="...")
def test_Marker_4():
    assert 2 * 3 == 6


@pytest.mark.parametrize("test_input,expected", [(1, 3), (3, 6), (5, 7)])
def test_addition(test_input, expected):
    assert test_input + 2 == expected
