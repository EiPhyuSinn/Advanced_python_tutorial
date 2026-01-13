import pytest 
from calculator import *

def test_add():
    assert add(1,2) == 3 
    assert add(-1,2) == 1 

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

    assert divide(2,2) == 1 
