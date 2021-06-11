#!/usr/bin/env python3
from typing import *
from data import product_list
from math import ceil, floor

def solve1(
        input_list: List[Tuple[int, int]] # (商品番号, 個数)のリスト
    ) -> int: # 合計金額
    """
    お題1 合計金額
    商品番号と個数を複数組、引数として受け取り、合計金額を計算する関数を書いてみよう。
    ヒント: 複数のものを受け取るために、配列やリストで一括で渡す方法がある。
    あるいは、1つ渡す関数を何回も呼び出して、
    最後に合計金額を計算する関数を呼び出すという形式もある。
    両方のアプローチをTDDで実装し見比べて、どちらが良いか判断してみよう。
    いきなり書くのが難しかったら、以下の補題をやってみるとよい。
    """
    ans = 0
    for id, quantity in input_list:
        ans += product_list[id].price*quantity
    return ans

def solve2(
        input_list: List[Tuple[int, int]] # (商品番号, 個数)のリスト
    ) -> int: # 合計金額
    """
    ## お題2 消費税
    商品リストの金額は外税なので、合計金額に消費税8％を足して、支払金額を返すようにしよう。
    """
    # 小数点以下は切り下げ
    ans = floor(solve1(input_list)*1.08)
    return ans

def solve3() -> int:
    """
    ## お題3 タバコの消費税
    商品リストの金額は外税なので、合計金額に消費税8％を足して、支払金額を返すようにしよう。
    """
    pass

def solve4() -> int:
    """
    ## お題4 割引
    リンゴは1個100円だが、3つ買うと280円になる。
    """
    pass

def solve5() -> int:
    """
    ## お題5 おまけ
    なんでも、同じものを10個買うと、1個おまけでもらえる。
    11個で10個ぶんの金額（12個で11個分、20個で19個分、22個で20個ぶん、...)
    という形で実現しよう。
    """
    pass


def test_solve1() -> bool:
    pass

def main():
    pass

if __name__ == '__main__':
    main()
