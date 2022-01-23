
import pytest
import main
def add(a,b):
    return a+b



def test_add():
    assert main.add(4,3) == 7
    assert main.add(4,6) == 10
    assert main.add(5,7) == 12
