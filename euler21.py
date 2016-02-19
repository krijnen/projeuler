# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:46:53 2015

@author: hielke
"""
from math import *


def divisors(x):
    n = []    
    for i in range(1,int(sqrt(x)+1)):
        if x%i == 0:
            n.append(i)
            if not i ==1:
                n.append(x/i)
    n.sort()
    return n

def d(x):
    return(sum(divisors(x)))

print d(220)
r =[]
for i in range(1,10001):
    a= d(i)
    if d(a) == i and not a==i:
        r.append(i)

print (r)
print (sum(r))