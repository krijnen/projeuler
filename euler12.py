# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:46:53 2015

@author: hielke
"""
from math import *

def binomial(n, r):
    ''' Binomial coefficient, nCr, aka the "choose" function 
        n! / (r! * (n - r)!)
    '''
    p = 1    
    for i in xrange(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p
    
def triangle(n):
    return binomial(n,2)
    
def divisors(x):
    n = 0    
    for i in range(1,int(sqrt(x)+1)):
        if x%i == 0:
            n+=2
    return n

for i in range(n0, n0 + 100000):
    a = triangle(i)
    if divisors(a) >= 500:
        print (a)        
        break
