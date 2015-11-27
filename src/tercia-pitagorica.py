# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:23:30 2015

@author: usuario
"""

def tercia():
    '''
    tercia()
    
    Calcula una tercia pitagorica (a, b, c) tal que
    a + b + c = 1000.
    Este es el problema 9 del proyecto Euler
    '''
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    return a, b, c, a*b*c
