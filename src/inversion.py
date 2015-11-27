# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:07:41 2015

@author: usuario
"""
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0,np.pi,50)



x = [0, 5, 5, 6, 5, 0, -1, 0, 0]
y = [0, 0, 3, 3, 4, 4, 3, 3, 0]

z = [s+t*1.0J for s,t in zip(x,y)]
zp = [4.0/s.conjugate() for s in z if s != 0]


xp = [s.real for s in zp]
yp = [s.imag for s in zp]

circle_x = 2*np.cos(theta)
circle_y = 2*np.sin(theta)

plt.plot(x, y, 'ob', xp, yp, 'r*', circle_x, circle_y, 'g')