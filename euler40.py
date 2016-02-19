# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:22:06 2015

@author: hielke
"""

d = "0"
i =0
while len(d) < 1000001:
    i+=1
    d += str(i)
print int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])
