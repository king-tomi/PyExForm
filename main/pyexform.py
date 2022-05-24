"""
A simple Python module that implements Microsoft Excel's most common formulas.

These formulas are implemented with the hope of ensuring python developers do not have to worry about implementing some Excel functions from scratch in their projects

This module can be used internally in projects across all fields.

Enjoy!!!

Author:  Ayodabo Tomisin Kolawole

Email: ayodabooluwatomisin@gmail.com
"""

import pandas as pd
from typing import Any, Union

def check_instance(x: Union[int,float]) -> bool:
    """checks if the parameter passed is an integer or float"""
    return isinstance(x,(int,float))

def sumif(series: Union[pd.DataFrame, list, pd.Series], condition: Any, order : int = 0, row_num: int = None, column: str = None) -> Union[int,float]:
    """
    calculates the sum of a list of values based on a condition
    
    params:
            `series: A table of values`

            `condition: A function that is asserted before the sum is calculated`

            `order: an integer indicating the order of summation. 0 for row and 1 for column (default value = 0)`

            `row_num: an ineger indicating the field to perform the operation on. defaults to None`

            `column: a string or integer indicating the name of the column to perform the operation on or the position of the items`
    returns:
            `An Integer or Float`
    """

    if order == 0:
        items = list(series.iloc[row_num,:].items)
        res = []


        for _, item in enumerate(items):
            if not check_instance(item):
                raise TypeError("Invalid cell value")
            
            if condition(item):
                res.append(item)
            else:
                continue
        return sum(res)
    else:
        items = series[column].items
        res = []
        for _, item in enumerate(items):
            if not check_instance(item):
                raise TypeError("Invalid cell value")
            
            if condition(item):
                res.append(item)
            else:
                continue
        return sum(res)


def averageif(series: pd.DataFrame, condition: Any, order : int = 0, row_num: int = None, column: str = None) -> float:
    """
    calculates the average of a list of values based on a condition
    
    params:
            `series: A table of values`

            `condition: A function that is asserted before the average is calculated`

            `order: an integer indicating the order of average. 0 for row and 1 for column (default value = 0)`

            `row_num: an ineger indicating the field to perform the operation on. defaults to None`

            `column: a string or integer indicating the name of the column to perform the operation on or the position of the items`
    returns:
            `An Integer or Float`
    """
    if order == 0:
        items = list(series.iloc[row_num,:].items)
        res = []


        for _, item in enumerate(items):
            if not check_instance(item):
                raise TypeError("Invalid cell value")
            
            if condition(item):
                res.append(item)
            else:
                continue
        return sum(res) / len(res)
    else:
        items = series[column].items
        res = []
        for _, item in enumerate(items):
            if not check_instance(item):
                raise TypeError("Invalid cell value")
            
            if condition(item):
                res.append(item)
            else:
                continue
        return sum(res) / len(res)


def vlookup(target: Any, range: pd.DataFrame, index: int) -> Any:
    """
    searches for an item in a range of values and returned the value in the specified index

    params:
        `target: item to look for`

        `range: the table to search`

        `index: index in the range of values to return the value if found (starts from 0)`

    returns:
            `A value in the specified index if the target item is found in the range of values`
    """
    if index > len(range.columns):
        raise IndexError("Index is out of range")
    items = list(range.iloc[:,index].items)
    found = False
    index = 0
    for col in range.columns:
        if target in list(range[col].items):
            found = True
            index = list(range[col].items).index(target)
            break
        else:
            continue
    
    if found:
        return items[index]
    else:
        raise ValueError("Item not in the range of vaues")


def match(target: Any, range: Union[pd.Series, list, pd.DataFrame], match_type: int, column: str = None) -> int:
    """
    Searches for an item in a list or a table of values and returns the index of the target value if found

    params:
        `target: the value to search`

        `range: the list of values or table`

        `column: the name of the column to search if it is a dataframe`

        `match_type: the type of search to do 1 for exact or near search, 0 for exact match, -1 for exact or near largest`

    returns:
        `An integer indicating the index of the target value if found`
    """
    if isinstance(range, pd.DataFrame):
        items = list(range[column].items)
        return items.index(target) if target in items else -1
    elif isinstance(range, pd.Series):
        items = list(range.items)
        return items.index(target) if target in items else -1
    else:
        return range.index(target) if target in range else -1


def index(array: Union[Any, list, pd.Series], index: int) -> Any:
    """
    returns item at the index in the array

    params:
        `array: the list or table of values to look`

        `index: the index of the value to return`
    """
    if isinstance(array, pd.Series):
        if index < 0 or index > len(array):
            raise IndexError("Index is out of the search range")
        return list(array.items)[index]
    else:
        if index < 0 or index > len(array):
            raise IndexError("Index is out of the search range")
        return array[index]

def countif(series: pd.DataFrame, condition: Any, column: str = None) -> int:
    """
    calculates the number of items in a list of values based on a condition
    
    params:
            `series: A table of values`

            `condition: A function that is asserted before the count is calculated`

            `column: a string or integer indicating the name of the column to perform the operation on or the position of the items`
    returns:
            `An Integer indicating the number of items that meets a condition`
    """
    data = list(series[column].values)
    count = 0
    for _,item in enumerate(data):
        if condition(item):
            count += 1
        else:
            continue
    return count