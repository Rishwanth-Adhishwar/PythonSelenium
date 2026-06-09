import pytest


def test_soft():
    print("Start")
    assert 1 == 2
    print("first")
    assert 3 == 4
    print("second")
    assert 5 == 6
    print("End")
