#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import *
import problem1


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
    assert problem1.solve3(testArr) == 1704
def test_4():
    testArr = [(1,3), (1,8)]
    return problem1.solve4(testArr) == 302
def test_5():
    testArr = [(1,11)]
    return problem1.solve5(testArr) == 1080

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()