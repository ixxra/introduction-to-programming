# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:51:27 2015

@author: usuario
"""

import turtle

turtle.bgpic('img/maze_77_.gif')

t = turtle.Turtle()
t.shape('turtle')
t.penup()
t.color('brown')




def move(x, y):
    t.goto(x, y)

    
def move_right():
    w = turtle.window_width()
    if t.xcor() < w/2 - 10:      
        t.seth(0)
        t.forward(10)

    
def move_left():
    w = turtle.window_width()
    if t.xcor() > -w/2 + 10:
        t.seth(180)
        t.forward(10)

        
def move_down():
    h = turtle.window_height()
    if t.ycor() > -h/2 + 10:      
        t.seth(270)
        t.forward(10)


def move_up():
    h = turtle.window_height()
    if t.ycor() < h/2 - 10:      
        t.seth(90)
        t.forward(10)


def paint():
    t.pendown()

def dont_paint():
    t.penup()
    
    
def spin(x, y):
    t.left(2*360)
    t.right(2*360)
    

t.onclick(spin)
turtle.onscreenclick(move)

turtle.onkey(move_right, 'Right')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.onkey(paint, 'U')
turtle.onkey(dont_paint, 'D')

turtle.listen()

