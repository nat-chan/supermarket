#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import *
from data import product_list
from math import ceil, floor

"""
## お題4 割引
リンゴは1個100円だが、3つ買うと280円になる。
## お題5 おまけ
なんでも、同じものを10個買うと、1個おまけでもらえる。11個で10個ぶんの金額（12個で11個分、20個で19個分、22個で20個ぶん、...)という形で実現しよう。
## お題6 おまけのライター
タバコを1カートン(10個)買うと、ライターがおまけでもらえる。引数にライターがあったら無料になるというふうに実現しよう。
## お題7 お弁当
弁当類と飲み物(お茶とコーヒー)をいっしょに買うと、20円引きになる。
## お題8 サービスしすぎない
お題4～7のようなサービスは、同じ商品については重複しない。一番安くなるものをひとつだけ適用する。
## お題9 タイムセール
お弁当は20時を過ぎると半額になる。
## お題10 タイムセールとサービス
お弁当のタイムセールは、他のサービスと重複してよい。
"""

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
    ) -> int: # 消費税8％を足した合計金額
    """
    ## お題2 消費税
    商品リストの金額は外税なので、合計金額に消費税8％を足して、支払金額を返すようにしよう。
    """
    # 小数点以下は切り下げ
    ans = floor(solve1(input_list)*1.08)
    return ans

def solve3(
        input_list: List[Tuple[int, int]] # (商品番号, 個数)のリスト
    ) -> int:
    """
    ## お題3 タバコの消費税
    タバコの価格には消費税が含まれているので(内税)、消費税の計算からタバコは除かないといけない。
    natsuki: 解釈、タバコいがいの値段に1.08をかければよい？
    """
    ans = 0
    for id, quantity in input_list:
        if product_list[id].name == "タバコ":
            ans += product_list[id].price*quantity * 1.0
        else:
            ans += product_list[id].price*quantity * 1.08
    ans = floor(ans)
    return ans

def solve4(
        input_list: List[Tuple[int, int]] # (商品番号, 個数)のリスト
    ) -> int:
    """
    ## お題4 割引
    リンゴは1個100円だが、3つ買うと280円になる。
    """
    ans = 0
    for id, quantity in input_list:
        if product_list[id].name == "りんご":
            """
            q: Quotient 商
            r: remainder 余
            n == p * q + r
            """
            q = quantity//3
            r = quantity%3
            assert quantity == 3*q + r
            assert r in range(3)
            tmp = 0
            tmp += r * 100
            tmp += q * 280
            ans += tmp
        else:
            ans += product_list[id].price*quantity * 1.08
    ans = floor(ans)

def solve5(
        input_list: List[Tuple[int, int]] # (商品番号, 個数)のリスト
    ) -> int:
    """
    ## お題5 おまけ
    なんでも、同じものを10個買うと、1個おまけでもらえる。
    11個で10個ぶんの金額（12個で11個分、20個で19個分、22個で20個ぶん、...)
    という形で実現しよう。
    """
    ans = 0
    for id, quantity in input_list:
            """
            q: Quotient 商
            r: remainder 余
            n == p * q + r
            """
            q = quantity//11
            r = quantity%11
            assert quantity == 11*q + r
            assert r in range(11)
            """
            num:〇個数分の価格
            """
            num = 0
            num += q * 10
            num += r
            ans += product_list[id].price* num * 1.08
    ans = floor(ans)
    pass


def test_solve1() -> bool:
    pass

def main():
    pass

if __name__ == '__main__':
    main()
