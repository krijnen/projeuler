# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:09:19 2015

@author: hielke



The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""



def gen_primes():
    primes = []
    i = 2
    while True:
        prime = True
        for p in primes:
            if not (i % p):
                prime = False
                break
        if prime:
            yield i
            primes.append(i)
        i += 1

def solver(N):
    primes = gen_primes()
    prime =[]
    maximum = (0,0)
    while prime[-1] < X:
        prime.append(primes.next())
        
        
        