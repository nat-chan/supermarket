#!/usr/bin/env python3
from typing import *


class product(NamedTuple):
    id: int
    name: str
    price: int

product_list = {
    1: product(id=1, name="りんご", price=100),
    2: product(id=2, name="みかん", price=40),
    3: product(id=3, name="ぶどう", price=150),
    4: product(id=4, name="のり弁", price=350),
    5: product(id=5, name="しゃけ弁", price=400),
    6: product(id=6, name="タバコ", price=420),
    7: product(id=7, name="メンソールタバコ", price=440),
    8: product(id=8, name="ライター", price=100),
    9: product(id=9, name="お茶", price=80),
}

product_list2 = {
    1: product(id=1, name="りんご", price=100),
    2: product(id=2, name="みかん", price=40),
    3: product(id=3, name="ぶどう", price=150),
    4: product(id=4, name="のり弁", price=350),
    5: product(id=5, name="しゃけ弁", price=400),
    6: product(id=6, name="タバコ", price=420),
    7: product(id=7, name="メンソールタバコ", price=440),
    8: product(id=8, name="ライター", price=100),
    9: product(id=9, name="お茶", price=80),
}

def product_list():
    """
    名前付きタプルのデータ構造の使い方のテスト
    """
    ringo = product_list[1]
    print(ringo.id)    # 1
    print(ringo.name)  # りんご
    print(ringo.price) # 100