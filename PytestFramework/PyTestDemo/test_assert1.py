import re
import sys

import pytest

@pytest.mark.smoke
def test_simple_assertion():
    assert 1+1==2

@pytest.mark.regression
def test_simple_assertion1():
    assert 3>=3
