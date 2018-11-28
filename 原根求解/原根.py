#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 20:04
# @Author  : wkend
# @File    : 原根.py
# @Software: PyCharm

import gmpy2
import sys


def euler_fun(m):
    """欧拉函数"""
    count = 0
    for i in range(1, m):
        if gmpy2.gcd(i, m) == 1:
            count += 1
    return count


def get_prime_factor(euler_value):
    """求素因子"""
    prime_factor = []
    for i in range(1, m):
        if gmpy2.c_mod(euler_value,i) == 0 and gmpy2.is_prime(i):
            prime_factor.append(i)
    return prime_factor


def get_min_prime_root(euler_value,prime_factors,m):
    """求最小的原根"""
    a = 1
    i = 0
    while(a<m):
        for prime_factor in prime_factors:
            if gmpy2.powmod(a, gmpy2.div(euler_value, prime_factor), m) == 1:
                a = gmpy2.add(a,1)
            else:
                i = gmpy2.add(i,1)
            break
        if i == len(prime_factors):
            break
    return a


if __name__ == '__main__':
    m = int(input("输入正整数m:"))
    print(gmpy2.is_prime(m))
    if not gmpy2.is_prime(m):
        sys.exit(1)
    # euler_value = euler_fun(m)
    euler_value = m -1
    print('φ(m)='+str(euler_value))
    prime_factors = get_prime_factor(euler_value)
    print(prime_factors)
    min_prime_root = get_min_prime_root(euler_value,prime_factors,m)
    print(str(m)+'的最小原根：'+str(min_prime_root))