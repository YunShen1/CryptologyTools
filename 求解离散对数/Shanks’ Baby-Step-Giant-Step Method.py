#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 15:07
# @Author  : wkend
# @File    : Shanks’ Baby-Step-Giant-Step Method.py
# @Software: PyCharm

import gmpy2
import sys


def get_ord(p):
    """求循环群的阶"""
    if gmpy2.is_prime(p):
        return gmpy2.sub(p, 1)
    else:
        print('输入错误，不是素数!')
        sys.exit(-1)


def get_baby_x(a, p, m):
    baby_x = []
    for i in range(0, m):
        baby_x.append(gmpy2.powmod(a, i, p))
    return baby_x


def get_giant_x(a, b, m, p):
    giant_x = []
    for i in range(0, m):
        tmp_1 = gmpy2.powmod(a, -m, p)
        tmp_2 = gmpy2.powmod(tmp_1, i, p)
        tmp_3 = gmpy2.powmod(gmpy2.mul(b, tmp_2), 1, p)

        giant_x.append(tmp_3)
    return giant_x


def get_result(baby_x, giant_x, m):
    for x_b in baby_x:
        for x_g in giant_x:
            if x_b == x_g:
                return gmpy2.add(gmpy2.mul(giant_x.index(x_g), m), baby_x.index(x_b))


if __name__ == '__main__':
    p = int(input('输入p:'))
    a = int(input('输入α：'))
    b = int(input('输入β：'))

    ord = get_ord(p)
    print('ord:' + str(ord))
    m = int(gmpy2.ceil(gmpy2.sqrt(ord)))
    print('m=' + str(m))
    baby_x = get_baby_x(a, p, m)
    print('x_b:' + str(baby_x))
    giant_x = get_giant_x(a, b, m, p)
    print('x_g:' + str(giant_x))
    result = get_result(baby_x, giant_x, m)
    print(result)
