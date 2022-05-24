import pytest
import sys
try:
    from main import pyexform
except (ImportError, ModuleNotFoundError):
    print("Module cannot be found in Python")
    print("goodbye")
    sys.exit()

import pandas as pd
from typing import Union

temporary = pd.read_csv("tests/results.csv")

def condition(x: Union[float, int]) -> bool:
    return x > 0

def test_sumif_by_row_return_error():
    assert pyexform.sumif(temporary,condition, row_num=0) == TypeError



if __name__ == '__main__':
    pytest.main()
