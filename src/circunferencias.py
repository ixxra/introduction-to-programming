# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:28:04 2015

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

def circ(x0, y0, r):
    theta = np.linspace(0, 2*np.pi, 50)
    x = r*np.cos(theta) + x0
    y = r*np.sin(theta) + y0
    return x, y



r = 3.0
x0 = 0
y0 = 5


x, y = circ(x0, y0, r)
x1, y1 = inversion(x, y)

xinv, yinv = circ(0,0, 2)

xbig, ybig = circ(9,0,9)
xbig_inv, ybig_inv = inversion(xbig, ybig)


x0 = 6
r = np.sqrt(x0**2 - 4)
xort, yort = circ(0, -x0, r)
xort_inv, yort_inv = inversion(xort, yort)



plt.plot(
    xinv, yinv, 'g', 
    x, y, 'r', 
    x1, y1, 'r',
    xbig, ybig, 'b',
    xbig_inv, ybig_inv, 'b',
    xort, yort, 'rp',
    xort_inv, yort_inv, 's')
plt.grid()
plt.title('Circunferencias de inversion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend([
    'Circ de inversion',
    'Osculatoria',
    'Pasa por el origen',
    'Ortogonal'])


#plt.axis([-3, 3, -8, 8])