# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:37:24 2015

@author: usuario
"""

import turtle
import math as m


t = turtle.Turtle()

def triangulo(t, r, fill=False):
    t.fill(fill)
    t.forward(r)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.fill(False)


def bloque(t,r):
    triangulo(t, r)
    t.forward(r/2.0)
    t.left(60)
    triangulo(t, r/2.0, fill=True)
    t.right(60)
    t.backward(r/2.0)
    

def sierpinski(t, r, n=0):
    if n==0:
        bloque(t, r)
    else:
        #bloque(t, r/2.0)
        sierpinski(t, r/2.0, n-1)
        t.forward(r/2.0)
        #bloque(t, r/2.0)
        sierpinski(t, r/2.0, n-1)
        t.backward(r/2.0)
        t.left(60)
        t.forward(r/2.0)
        t.right(60)
        #bloque(t, r/2.0)
        sierpinski(t, r/2.0, n-1)
        t.left(60)
        t.backward(r/2.0)
        t.right(60)
        


























def bloqueWrong(t, r):
    '''
    This was the first try to paint a basic
    block. You can safely ignore this 
    function.
    '''
    triangulo(t, r/2.0, fill=True)
    t.forward(r/2.0)
    triangulo(t, r/2.0, fill=True)
    t.goto(r/4.0, r/4.0*m.sqrt(3))
    triangulo(t, r/2.0, fill=True)    




































