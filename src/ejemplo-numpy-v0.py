# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 05:00:35 2015

@author: usuario
"""
import matplotlib.pyplot as plt
import numpy as np

A = np.array([
    [3, 4, 5],
    [6, 7, 8],
    [0, 1, 0]
])

L = 10
T = 2

n = 10
m = 50

x = np.linspace(0, L, m)
t = np.linspace(0, T, n)

A = np.zeros((n,m))

for i,ti in enumerate(t):
    A[i,:] = np.sin(x - ti)
    
for i in range(n):
    plt.plot(x, A[i,:])
    plt.savefig('animacion/figura%02d.png' % i)