import pytest 
from Function_CountPoints import function_CountPoints

def test_function_CountPoints():
    assert function_CountPoints(True,1) == 2
    assert function_CountPoints(True,5) == 6
    assert function_CountPoints(False,1) == 0