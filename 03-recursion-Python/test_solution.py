
import os,sys
sys.path.append(os.getcwd())
from recursion import get_fib
import pytest


@pytest.mark.parametrize("input_value, result",[(10, 34), (12, 89), (0, 0)])
def test_get_fib(input_value, result):    
    assert get_fib(input_value) == result

