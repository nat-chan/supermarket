#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import *
from problem1 import *
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
    for i in range(1, 5+1):
        f = globals()[f"solve{i}"]
        testdata = generate_testdata()
        ans = f(testdata)
        assert type(ans) is int, f"solve{i}() value is {ans}"

if __name__ == '__main__':
    random_test()