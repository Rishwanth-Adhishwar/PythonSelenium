import pytest_check as c
import pytest


def test_soft():
    print("Start")
    c.equal(1, 1)
    print("first")
    c.assert_equal("hi", "hi")
    print("second")
    c.equal(5, 6)
    print("End")
