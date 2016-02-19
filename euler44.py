# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:37:38 2015

@author: hielke
"""

def pentagon(n):
    return n*(3*n-1)/2

pent = []
for i in range(1,3000):
    pent.append(int(pentagon(i)))

D =[]
for j in pent:
    for k in pent:
        if (j+k) in pent and (abs(j-k)) in pent:
            D.append(abs(j-k))
print D