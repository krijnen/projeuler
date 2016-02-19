# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:08:45 2015

@author: hielke
"""

n = 5
c = []

for i in range(2, 1000000):
    a = 0
    b = str(i)
    for x in b:
        a+= int(x)**n
    if int(a) == int(i):
        c.append(i)
print sum(c)