# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:58:03 2015

@author: usuario
"""

n = raw_input('Numero: ')
n = int(n)

x = 0

for i in range(2, n):
    while n%i**(x + 1) == 0:
        x += 1
    if x > 0:
        print i, x
    x = 0