
import pytest

def add(a,b):
    return a+b



def test_add():
    assert add(4,3) == 7
    assert add(4,6) == 10
    assert add(5,7) == 12
    assert add(2,6) == 8
    assert add(9,7) == 16

