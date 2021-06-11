#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import *
# from data test_product_list
from data import product_list
import problem1
from random import randint

ID_MAX = 9
QUANTITY_MAX = 100


def generate_testdata() -> List[Tuple[int, int]]:
    testdata = list()
    for id in range(1, ID_MAX):
        quantity = randint(1, QUANTITY_MAX)
        testdata.append( (id, quantity) )
    return testdata

def random_test():
    from problem1 import *
    for i in range(1, 5+1):
        print(
        locals()[f"solve{i}"]
        )


# print(ringo.id)    # 1
# print(ringo.name)  # りんご
# print(ringo.price) # 100
# data []
def test_1():
    testArr = [(1, 8), (1, 5)]
    assert problem1.solve1(testArr) == 1000
def test_2():
    testArr = [(1, 8), (1, 5)]
    assert problem1.solve2(testArr) == 1080
def test_3():
    testArr = [(6,2), (1,8)]
    assert == 1704
