# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 09:23:27 2015

@author: usuario
"""
import sympy as sp
import math as m


def conjecture(n):
    cota = int(m.sqrt((n-2.0)/2.0)) + 1
    primos = list(sp.primerange(2, n))
    assert n%2==1 and not n in primos, 'n no cumple las hipotesis'
    for p in primos:
        for x in range(1, cota):
            if n == p + 2*x**2:
                return (p, x)

for n in range(9, 100000, 2):
    if sp.isprime(n):
      continue
    if conjecture(n) is None:
        print 'la conjetura fallo en', n
        break