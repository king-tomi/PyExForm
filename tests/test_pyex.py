import sys
sys.path.append("/Users/mac/Desktop/Tomisin/PyExForm/")
import pytest
try:
    from main import pyexform
except (ImportError, ModuleNotFoundError):
    print("Module cannot be found in Python")
    print("goodbye")
    sys.exit()

import pandas as pd
from typing import Union

temporary = pd.read_csv("results.csv")

def condition(x: Union[float, int]) -> bool:
    return x > 0

def test_sumif_by_row_return_None():
    assert pyexform.sumif(temporary,condition, row_num=0) == None


def test_averageif_by_row_return_None():
    assert pyexform.averageif(temporary,condition, row_num=0) == None

tot_home_score = 0
sums = []

for i in temporary["home_score"]:
    if condition(i):
        sums.append(i)
        tot_home_score += i

def test_sumif_by_row_return_value():
    assert pyexform.sumif(temporary,condition, order=1, column="home_score") == tot_home_score

def test_averageif_by_row_return_value():
    assert pyexform.averageif(temporary,condition, order=1, column="home_score") == round(sum(sums) / len(sums), 2)

def test_match_return_minus_list():
    temp = list(temporary["home_team"].values)
    assert pyexform.match("Real Madrid", temp, 0) == -1



if __name__ == '__main__':
    pytest.main()
