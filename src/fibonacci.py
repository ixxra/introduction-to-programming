# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:58:05 2015

@author: usuario
"""
def fibonacci(n):
    '''
    Regresa el termino $a_n$ de la sucesion
    de Fibonacci.
    '''
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)