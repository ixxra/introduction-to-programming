# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:59:14 2015

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt

def inversion(x, y):
    z = [s+t*1.0J for s,t in zip(x,y)]
    zp = [4.0/s.conjugate() for s in z if s != 0]
    xp = [s.real for s in zp]
    yp = [s.imag for s in zp]
    return xp, yp
    

M = np.random.random((3,3))
M[:,[0,1]] = 10*M[:, [0,1]] - 5
M[:, 2] = 10*M[:,2]

theta = np.linspace(0,2*np.pi, 50)

for i in range(3):
    x0, y0, r = M[i,:]
    x = r*np.cos(theta) + x0
    y = r*np.sin(theta) + y0
    xp, yp = inversion(x, y)
    plt.plot(x, y, xp, yp, '*')
    
