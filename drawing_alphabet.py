#Turtle basics

from math import asin, sqrt, atan, degrees
import turtle
import random
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame

TK_SILENCE_DEPRECATION=1

# Screen and turtle setup
screen = turtle.Screen()
screen.setup(startx = 0, starty = 0)
t1 = turtle.Turtle()
t1.speed(speed=10)

  
# set the background color
# screen.bgcolor("blue")

top_x = -250
left_y = 200
horiz_len = 30
vert_len = 60
right_angle = 90
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
space = 10

def goToPos(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.setheading(RIGHT)
    t1.pendown()
    
def draw_vert_line(start_x, start_y):
    goToPos(start_x, start_y)
    t1.setheading(DOWN)
    t1.forward(vert_len)
    
def draw_horiz_line(start_x, start_y):
    goToPos(start_x, start_y)
    t1.forward(horiz_len)

def draw_diag_line(start_x, start_y, horiz_len, vert_len, dir="right"):
    goToPos(start_x, start_y)
    t1.setheading(DOWN)
    diag_angle = degrees(atan(horiz_len / vert_len))
    if(dir == "left"):
        t1.right(diag_angle)
    elif(dir == "up"):
        t1.setheading(UP)
        t1.right(diag_angle)
    else:
        t1.left(diag_angle)
    # print(diag_angle)
    diag_len = sqrt(vert_len**2 + horiz_len**2)
    t1.forward(diag_len)

def draw_loop(start_x, start_y):
    goToPos(start_x, start_y)
    t1.forward(horiz_len/2)
    t1.setheading(LEFT)
    t1.circle(horiz_len*(horiz_len/vert_len), -180)
    t1.setheading(LEFT)
    t1.forward(horiz_len/2)
    
#A
def draw_A(start_x, start_y):
    draw_diag_line(start_x + (horiz_len/2), start_y, horiz_len/2, vert_len) #right line
    draw_diag_line(start_x + (horiz_len/2), start_y, horiz_len/2, vert_len, "left") #left line
    goToPos(start_x + (horiz_len/3.6), start_y - (vert_len/2)) # middle line
    t1.setheading(RIGHT)
    t1.forward(4*horiz_len/9)
    
#B
def draw_B(start_x, start_y):
    draw_P(start_x, start_y) #P
    draw_loop(start_x, start_y - vert_len/2) # second loop

#C
def draw_C(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    t1.setheading(UP)
    t1.circle(horiz_len/2, 180)
    t1.forward(vert_len/2)
    t1.circle(horiz_len/2, 180)

#D
def draw_D(start_x, start_y):
    draw_vert_line(start_x, start_y)
    goToPos(start_x, start_y)
    t1.setheading(LEFT)
    t1.circle(horiz_len, -180)
    
#E
def draw_E(start_x, start_y):
    draw_F(start_x, start_y)
    draw_horiz_line(start_x, start_y - vert_len)
    
#F
def draw_F(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_horiz_line(start_x, start_y)
    draw_horiz_line(start_x, start_y - (vert_len/2))
    
#G
def draw_G(start_x, start_y):
    draw_C(start_x, start_y)
    t1.forward(horiz_len/3)
    t1.setheading(LEFT)
    t1.forward(horiz_len/2)
    
#H
def draw_H(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_horiz_line(start_x, start_y - (vert_len/2))
    draw_vert_line(start_x + horiz_len, start_y)

#I
def draw_I(start_x, start_y):
    draw_T(start_x, start_y)
    draw_horiz_line(start_x, start_y - vert_len)
    
#J
def draw_J(start_x, start_y):
    draw_horiz_line(start_x, start_y)
    goToPos(start_x + horiz_len/2, start_y)
    t1.setheading(DOWN)
    t1.forward(7*vert_len/8)
    t1.setheading(UP)
    t1.circle(horiz_len/4, -180)
    
#K
def draw_K(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_diag_line(start_x, start_y - vert_len/2, horiz_len, vert_len/2, "up")
    draw_diag_line(start_x, start_y - vert_len/2, horiz_len, vert_len/2)


#L
def draw_L(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_horiz_line(start_x, start_y - vert_len)
    
#M
def draw_M(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_diag_line(start_x, start_y, horiz_len/2, vert_len/2)
    draw_diag_line(start_x + horiz_len/2, start_y - vert_len/2, horiz_len/2, vert_len/2, "up")
    draw_vert_line(start_x + horiz_len, start_y)
    
#N
def draw_N(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_diag_line(start_x, start_y, horiz_len, vert_len)
    draw_vert_line(start_x + horiz_len, start_y)
    
#O
def draw_O(start_x, start_y):
    draw_C(start_x, start_y)
    t1.forward(vert_len/2)
 
#P
def draw_P(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_loop(start_x, start_y)
    
#Q
def draw_Q(start_x, start_y):
    draw_O(start_x, start_y)
    draw_diag_line(start_x + horiz_len/2, start_y - vert_len/2, horiz_len/2, vert_len/2)

#R
def draw_R(start_x, start_y):
    draw_vert_line(start_x, start_y)
    draw_loop(start_x, start_y)
    draw_diag_line(start_x + horiz_len/2, start_y - vert_len/2, horiz_len/2, vert_len/2)

#S
def draw_S(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    t1.setheading(UP)
    t1.circle(horiz_len/2, 180)
    draw_diag_line(start_x, start_y - vert_len/4, horiz_len, vert_len/2)
    t1.setheading(UP)
    t1.circle(horiz_len/2, -180)

#T
def draw_T(start_x, start_y):
    draw_horiz_line(start_x, start_y)
    draw_vert_line(start_x + horiz_len/2, start_y)

#U
def draw_U(start_x, start_y):
    goToPos(start_x, start_y)
    t1.setheading(DOWN)
    t1.forward(3*vert_len/4)
    t1.circle(horiz_len/2, 180)
    t1.forward(3*vert_len/4)

#V
def draw_V(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    
#W
def draw_W(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    
#X
def draw_X(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    
#Y
def draw_Y(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    
#Z
def draw_Z(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)

############### WRITING ALPHABET ##################
next_letter = horiz_len + space
next_line = vert_len + space
# draw_A(top_x, left_y)
# draw_B(top_x + next_letter, left_y)
# draw_C(top_x + 2*next_letter, left_y)
# draw_D(top_x + 3*next_letter, left_y)
# draw_E(top_x + 4*next_letter, left_y)
# draw_F(top_x + 5*next_letter, left_y)
# draw_G(top_x, left_y - next_line)
# draw_H(top_x + next_letter, left_y - next_line)
# draw_I(top_x + 2*next_letter, left_y - next_line)
# draw_J(top_x + 3*next_letter, left_y - next_line)
# draw_K(top_x + 4*next_letter, left_y - next_line)
# draw_L(top_x + 5*next_letter, left_y - next_line)
# draw_M(top_x, left_y - 2*next_line)
# draw_N(top_x + next_letter, left_y - 2*next_line)
# draw_O(top_x + 2*next_letter, left_y - 2*next_line)
# draw_P(top_x + 3*next_letter, left_y - 2*next_line)
# draw_Q(top_x + 4*next_letter, left_y - 2*next_line)
# draw_R(top_x + 5*next_letter, left_y - 2*next_line)
draw_S(top_x, left_y - 3*next_line)
draw_T(top_x + next_letter, left_y - 3*next_line)
draw_U(top_x + 2*next_letter, left_y - 3*next_line)
# draw_V(top_x + 3*next_letter, left_y - 3*next_line)
# draw_W(top_x + 4*next_letter, left_y - 3*next_line)
# draw_X(top_x + 5*next_letter, left_y - 3*next_line)
# draw_X(top_x, left_y - 4*next_line)
# draw_Y(top_x + next_letter, left_y - 4*next_line)
# draw_Z(top_x + 2*next_letter, left_y - 4*next_line)


turtle.done()
turtle.exitonclick()