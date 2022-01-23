import pytest 
def roz(a,b):
    return a-b

def test_roz():
    assert roz(3,1) == 2
    assert roz(3,2) == 1
