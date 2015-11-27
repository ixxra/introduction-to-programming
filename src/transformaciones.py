# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:23:40 2015

@author: usuario
"""

import numpy as np

theta = np.deg2rad(60)

x = np.array([0, 5, 5, 6, 5, 0, -1, 0, 0])
y = np.array([0, 0, 3, 3, 4, 4, 3, 3, 0])

M = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

X = np.array([
    [0, 5, 5, 6, 5, 0, -1, 0, 0],
    [0, 0, 3, 3, 4, 4, 3, 3, 0]
])

Xp = M.dot(X)
xp = Xp[0,:]
yp = Xp[1,:]

