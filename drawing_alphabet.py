#Turtle basics

from math import asin, sqrt
import turtle
import random

TK_SILENCE_DEPRECATION=1

screen = turtle.Screen()
screen.setup(startx = 0, starty = 0)
  
# set the background color
# screen.bgcolor("blue")

t1 = turtle.Turtle()
# t1.shape("turtle")
top_x = -200
left_y = 200
horiz_len = 50
vert_len = 100
right_angle = 90
LEFT = 0
RIGHT = 180
UP = 90
DOWN = 270
diag_angle = 90 - (100*asin((horiz_len/4) / vert_len))
diag_len = sqrt((vert_len**2) + ((horiz_len/2)**2))
space = 30
def goToPos(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.setheading(LEFT)
    t1.pendown()

#A
def draw_A(start_x, start_y):
    goToPos(start_x + (horiz_len/2), start_y)
    t1.right(diag_angle)
    t1.forward(diag_len)
    goToPos(start_x + (horiz_len/2), start_y)
    t1.setheading(RIGHT)
    t1.left(diag_angle)
    t1.forward(diag_len)
    goToPos(start_x + (horiz_len/3.5), start_y - (vert_len/2))
    t1.setheading(LEFT)
    t1.forward(horiz_len/2.5)
    
#B
def draw_B(start_x, start_y):
    goToPos(start_x, start_y)
    t1.right(right_angle)
    t1.forward(vert_len)
    t1.left(right_angle)
    goToPos(start_x, start_y)
    for i in range(2):
        t1.forward(horiz_len/2)
        t1.setheading(RIGHT)
        t1.circle(horiz_len/2, -180)
        t1.setheading(RIGHT)
        t1.forward(horiz_len/2)
        t1.setheading(LEFT)

#C
def draw_C(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4)
    t1.setheading(90)
    t1.circle(horiz_len/2, 180)
    t1.forward(vert_len/2)
    t1.circle(horiz_len/2, 180)

#D
def draw_D(start_x, start_y):
    goToPos(start_x, start_y)
    t1.right(right_angle)
    t1.forward(vert_len)
    t1.left(right_angle)
    goToPos(start_x, start_y)
    t1.setheading(RIGHT)
    t1.circle(horiz_len, -180)
    

#E
def draw_E(start_x, start_y):
    draw_F(start_x, start_y)
    goToPos(start_x, start_y - vert_len)
    t1.forward(horiz_len)
    
#F
def draw_F(start_x, start_y):
    goToPos(start_x, start_y)
    t1.right(right_angle)
    t1.forward(vert_len)
    t1.left(right_angle)
    goToPos(start_x, start_y)
    t1.forward(horiz_len)
    goToPos(start_x, start_y - (vert_len/2))
    t1.forward(horiz_len)
    
#G
def draw_G(start_x, start_y):
    draw_C(start_x, start_y)
    t1.forward(horiz_len/4)
    t1.setheading(RIGHT)
    t1.forward(horiz_len/2)

draw_A(top_x, left_y)
draw_B(top_x + horiz_len + space, left_y)
draw_C(top_x + 2*horiz_len + 2*space, left_y)
draw_D(top_x, left_y - vert_len - space)
draw_E(top_x + horiz_len + space, left_y - vert_len - space)
draw_F(top_x  + 2*horiz_len + 2*space, left_y - vert_len - space)
draw_G(top_x + 3*horiz_len + 3*space, left_y - vert_len - space)


turtle.done()
turtle.exitonclick()