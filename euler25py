# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:51:56 2015

@author: hielke
"""

from math import *


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b
def check(n):
    a = fib()
    i=0
    while True:
        i++
        b = a.next()
        if len(str(b))>=n:
            return i, b

print(check(5))