############## TURTLE TYPEWRITER ##############
# Turtle drawing practice

from math import sqrt, atan, degrees
import turtle

# ask for user input
# user_input = input("What would you like me to write out? (Press enter to submit): ")

# # set the background and pen color based on user input
# bkgdclr = ""
# while bkgdclr == "":
#     bkgdclr = input("What color background would you like me to write on? (e.g., black, blue, etc...) ")
# penclr = ""
# while penclr == "":
#     penclr = input("What color would you like me to write in? ")
# while(penclr == bkgdclr):
#     penclr = input("What color would you like me to write in? (Please choose a different color than the background color) ")

# screen and turtle setup
screen = turtle.Screen()
screen.setup(startx = 0, starty = 0)
t1 = turtle.Turtle()
t1.speed(speed=0)
t1.hideturtle() # hide turtle pointer

# try:
#     screen.bgcolor(bkgdclr)
# except turtle.TurtleGraphicsError as err:
#     print(str(err) + " is not a valid color; color set to white")
#     screen.bgcolor("white")

# try:
#     t1.pencolor(penclr)
#     t1.fillcolor(penclr)
# except turtle.TurtleGraphicsError as err:
#     print(str(err) + " is not a valid color; color set to black")
#     t1.pencolor("black")
#     t1.fillcolor("black")

top_x = -350 # starting x
left_y = 300 # starting y 
horiz_len = 30 # character width
vert_len = 60 # character height
space = 10 # space between characters

# turtle direction headings
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

############### COMMON MARKS ##################
#puts pen into position without drawing
def goToPos(x, y, towards=RIGHT):
    t1.penup() # stop drawing
    t1.goto(x, y) # move to x, y
    t1.setheading(towards) # set direction
    t1.pendown() # start drawing
    
def getCurrX():
    return int(t1.position()[0]) # current X coord

def getCurrY():
    return int(t1.position()[1]) # current Y coord

# draws vertical line of length v_len top to bottom
def draw_vert_line(x, y, v_len=vert_len):
    goToPos(x, y, DOWN)
    t1.forward(v_len)
    
# draws horizontal line of length h_len
# default draws towards RIGHT (left to right)
def draw_horiz_line(x, y, h_len=horiz_len, towards=RIGHT):
    goToPos(x, y, towards)
    t1.forward(h_len)

# draws diagonal line based on h_len and v_len
# default draws towards RIGHT (left to right)
def draw_diag_line(x, y, h_len=horiz_len, v_len=vert_len, towards="right"):
    goToPos(x, y, DOWN) # start facing downward
    diag_angle = degrees(atan(h_len / v_len))
    if(towards == "left"):
        t1.right(diag_angle) # turn left to draw towards right
    elif(towards == "up"): # if going upwards, turn right to draw towards right
        t1.setheading(UP)
        t1.right(diag_angle)
    else:
        t1.left(diag_angle) # turn left to draw towards right
    diag_len = sqrt(v_len**2 + h_len**2)
    t1.forward(diag_len)

# draws 
def draw_loop(x, y, h_len=horiz_len, towards="right"):
    if towards == "right":
        head = RIGHT
        tail = LEFT
    else:
        head = LEFT
        tail = RIGHT
    goToPos(x, y, head)
    t1.forward(h_len/2)
    t1.setheading(tail)
    t1.circle(h_len*(h_len/vert_len), -180)
    t1.setheading(tail)
    t1.forward(h_len/2)
    
def draw_small_loop(x, y, h_len=horiz_len, towards="left"):
    if towards == "left":
        goToPos(x, y, 120)
        t1.circle(h_len/2, 300)
    else:
        goToPos(x, y, -120)
        t1.circle(h_len/2, -300)
    
    
############### UPPERCASE LETTERS ##################
#A
def draw_A(start_x, start_y):
    draw_diag_line(start_x + horiz_len/2, start_y, horiz_len/2, vert_len) #right line
    draw_diag_line(start_x + horiz_len/2, start_y, horiz_len/2, vert_len, "left") #left line
    draw_horiz_line(start_x + horiz_len/3.6, start_y - vert_len/2, 4*horiz_len/9) # middle line
    
#B
def draw_B(start_x, start_y):
    draw_P(start_x, start_y) #P
    draw_loop(start_x, start_y - vert_len/2) # second loop

#C
def draw_C(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4, UP)
    t1.circle(horiz_len/2, 180)
    t1.forward(vert_len/2)
    t1.circle(horiz_len/2, 180)

#D
def draw_D(start_x, start_y):
    draw_vert_line(start_x, start_y)
    goToPos(start_x, start_y, LEFT)
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
    t1.forward(vert_len/4)
    draw_horiz_line(start_x + horiz_len, start_y - vert_len/2, horiz_len/2, LEFT)
    
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
    draw_vert_line(start_x + horiz_len/2, start_y,7*vert_len/8)
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
    draw_P(start_x, start_y)
    draw_diag_line(start_x + horiz_len/2, start_y - vert_len/2, horiz_len/2, vert_len/2)

#S
def draw_S(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4, UP)
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
    draw_vert_line(start_x, start_y, 3*vert_len/4)
    t1.circle(horiz_len/2, 180)
    draw_vert_line(start_x + horiz_len, start_y, 3*vert_len/4)

#V
def draw_V(start_x, start_y):
    draw_diag_line(start_x, start_y, horiz_len/2, vert_len)
    draw_diag_line(getCurrX(), getCurrY(), horiz_len/2, vert_len, "up") #left line
    
#W
def draw_W(start_x, start_y):
    draw_diag_line(start_x, start_y, horiz_len/4, vert_len)
    draw_diag_line(getCurrX(), getCurrY(), horiz_len/4, vert_len, "up") #left line
    draw_diag_line(getCurrX(), getCurrY(), horiz_len/4, vert_len)
    draw_diag_line(getCurrX(), getCurrY(), horiz_len/4, vert_len, "up") #left line
    
#X
def draw_X(start_x, start_y):
    draw_diag_line(start_x, start_y, horiz_len, vert_len)
    draw_diag_line(start_x, start_y - vert_len, horiz_len, vert_len, "up")
    
#Y
def draw_Y(start_x, start_y):
    draw_diag_line(start_x, start_y, horiz_len/2, vert_len/2)
    draw_diag_line(start_x + horiz_len/2, start_y - vert_len/2, horiz_len/2, vert_len/2, "up")
    draw_vert_line(start_x + horiz_len/2, start_y - vert_len/2, vert_len/2)
    
#Z
def draw_Z(start_x, start_y, upper=True):
    if upper:
        v_len = vert_len
        draw_horiz_line(start_x, start_y)
    else:
        v_len = vert_len/2
        draw_horiz_line(start_x, start_y - v_len)
    draw_diag_line(start_x, start_y - vert_len, horiz_len, v_len, "up")
    draw_horiz_line(start_x, start_y - vert_len)
    
    
############### LOWERCASE LETTERS ##################
#a
def draw_lc_A(start_x, start_y):
    draw_vert_line(start_x + horiz_len, start_y - vert_len/2, vert_len/2)
    draw_lc_C(start_x, start_y)
    
#b
def draw_lc_B(start_x, start_y):
    draw_vert_line(start_x, start_y, vert_len)
    draw_lc_C(start_x, start_y, True)
   
#c
def draw_lc_C(start_x, start_y, flip=False):
    DIR = DOWN
    x = 0
    if(flip):
        DIR = UP
        x = horiz_len
    goToPos(start_x + x, start_y - 3*vert_len/4, DIR)
    t1.circle(vert_len/4, -155)
    goToPos(start_x + x, start_y - 3*vert_len/4, DIR)
    t1.circle(vert_len/4, 155)

#d
def draw_lc_D(start_x, start_y):
    draw_vert_line(start_x + horiz_len, start_y, vert_len)
    draw_lc_C(start_x, start_y)
    
#e
def draw_lc_E(start_x, start_y):
    draw_horiz_line(start_x, start_y - 3*vert_len/4)
    t1.setheading(UP)
    t1.circle(vert_len/4, 330)

#f
def draw_lc_F(start_x, start_y):
    draw_horiz_line(start_x, start_y - vert_len/2)
    goToPos(start_x + horiz_len, start_y - vert_len/4, UP)
    t1.circle(3*horiz_len/8, 180)
    # draw_lc_O(start_x, start_y + 3*vert_len/4 - vert_len/4, 180)
    draw_vert_line(getCurrX(), getCurrY(), 3*vert_len/4)

#g
def draw_lc_G(start_x, start_y):
    draw_lc_O(start_x, start_y)
    draw_vert_line(start_x + horiz_len, start_y - vert_len/2, 3*vert_len/4)
    t1.setheading(UP)
    t1.circle(horiz_len/2, -180)

#h
def draw_lc_H(start_x, start_y):
    draw_vert_line(start_x, start_y, vert_len)
    goToPos(start_x, start_y - 3*vert_len/4, DOWN)
    t1.circle(horiz_len/2, -180)
    # draw_lc_O(start_x, start_y + 3*vert_len/4 - vert_len/4, 180)
    draw_vert_line(getCurrX(), getCurrY(), vert_len/4)
  
#i
def draw_lc_I(start_x, start_y):
    draw_period(start_x + horiz_len/2 - period_sz, start_y + vert_len/2 + period_sz*2)
    draw_vert_line(start_x + horiz_len/2, start_y - vert_len/2, vert_len/2) 
    
#j
def draw_lc_J(start_x, start_y):
    draw_lc_I(start_x + horiz_len/2, start_y)
    draw_vert_line(start_x + horiz_len, start_y - vert_len/2, 3*vert_len/4)
    t1.setheading(UP)
    t1.circle(horiz_len/2, -180)

#o
def draw_lc_O(start_x, start_y, DEG=360):
    goToPos(start_x + horiz_len, start_y - 3*vert_len/4, UP)
    t1.circle(horiz_len/2, DEG)

#s
def draw_lc_S(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - 5*vert_len/8, 120)
    t1.circle(horiz_len/2, 120)
    draw_diag_line(getCurrX(), getCurrY(), 5*horiz_len/6, vert_len/4)
    goToPos(getCurrX(), getCurrY(), 60)
    t1.circle(horiz_len/2, -120)

#z
def draw_lc_Z(start_x, start_y):
    draw_Z(start_x, start_y, False)
    
################# NUMBERS ##################
#1
def draw_one(start_x, start_y):
    draw_diag_line(start_x, start_y - vert_len/4, horiz_len/2, vert_len/4, "up")
    draw_vert_line(start_x + horiz_len/2, start_y)
    draw_horiz_line(start_x, start_y - vert_len)
    
#2
def draw_two(start_x, start_y):
    goToPos(start_x + horiz_len, start_y - vert_len/4, UP)
    t1.circle(horiz_len/2, 180)
    draw_diag_line(start_x, start_y - vert_len, horiz_len, 3*vert_len/4, "up")
    draw_horiz_line(start_x, start_y - vert_len)

#3
def draw_three(start_x, start_y):
    draw_horiz_line(start_x, start_y)
    draw_diag_line(start_x, start_y - vert_len/2, horiz_len, vert_len/2, "up")
    draw_loop(start_x, start_y - vert_len/2)
    
    
############### PUNCTUATION ##################
#space
def draw_space(start_x, start_y):
    return

period_sz = 2
#period
def draw_period(start_x, start_y):
    goToPos(start_x + period_sz, start_y - vert_len + period_sz/2)
    t1.begin_fill()
    t1.circle(period_sz)
    t1.end_fill()

#comma
def draw_comma(start_x, start_y):
    draw_period(start_x, start_y)
    t1.setheading(LEFT)
    t1.circle(period_sz, -180)
     
    
#exclamation mark
def draw_exclam(start_x, start_y):
    draw_vert_line(start_x + horiz_len/2, start_y, 3*vert_len/4)
    draw_period(start_x + horiz_len/2 - period_sz, start_y)

#question mark
def draw_ques(start_x, start_y):
    return 

#dollar sign
def draw_dollar(start_x, start_y):
    draw_S(start_x, start_y)
    draw_vert_line(start_x + horiz_len/3, start_y)  
    draw_vert_line(start_x + 2*horiz_len/3, start_y)  
    
    
############### ALPHABET DICT ##################
alphabet = {
    # " " : draw_space,
    # "." : draw_period,
    # "," : draw_comma,
    # "!" : draw_exclam,
    "?" : draw_ques,
    # "$" : draw_dollar,
    # "A" : draw_A,
    # "B" : draw_B,
    # "C" : draw_C,
    # "D" : draw_D,
    # "E" : draw_E,
    # "F" : draw_F,
    # "G" : draw_G,
    # "H" : draw_H,
    # "I" : draw_I,
    # "J" : draw_J,
    # "K" : draw_K,
    # "L" : draw_L,
    # "M" : draw_M,
    # "N" : draw_N,
    # "O" : draw_O,
    # "P" : draw_P,
    # "Q" : draw_Q,
    # "R" : draw_R,
    # "S" : draw_S,
    # "T" : draw_T,
    # "U" : draw_U,
    # "V" : draw_V,
    # "W" : draw_W,
    # "X" : draw_X,
    # "Y" : draw_Y,
    # "Z" : draw_Z,
    "a" : draw_lc_A,
    "b" : draw_lc_B,
    "c" : draw_lc_C,
    "d" : draw_lc_D,
    "e" : draw_lc_E,
    "f" : draw_lc_F,
    "g" : draw_lc_G,
    "h" : draw_lc_H,
    "i" : draw_lc_I,
    "j" : draw_lc_J,
    "o" : draw_lc_O,
    "s" : draw_lc_S,
    "z" : draw_lc_Z,
    "1" : draw_one,
    "2" : draw_two,
    "3" : draw_three,
}


############### SPACES AND LINE BREAKS ##################
next_letter = horiz_len + space
next_line = vert_len + space*4


############### TEST WRITING ALPHABET ##################
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
# draw_S(top_x, left_y - 3*next_line)
# draw_T(top_x + next_letter, left_y - 3*next_line)
# draw_U(top_x + 2*next_letter, left_y - 3*next_line)
# draw_V(top_x + 3*next_letter, left_y - 3*next_line)
# draw_W(top_x + 4*next_letter, left_y - 3*next_line)
# draw_X(top_x + 5*next_letter, left_y - 3*next_line)
# draw_Y(top_x, left_y - 4*next_line)
# draw_Z(top_x + next_letter, left_y - 4*next_line)
# draw_Z(top_x + 2*next_letter, left_y - 4*next_line)
# draw_a(top_x + 3*next_letter, left_y - 4*next_line)
# draw_b(top_x + 4*next_letter, left_y - 4*next_line)
# draw_c(top_x + 5*next_letter, left_y - 4*next_line)
# draw_d(top_x, left_y - 4*next_line)
# draw_d(top_x + next_letter, left_y - 4*next_line)

############### TEST WRITING NUMBERS ##################
# draw_one(top_x + 2*next_letter, left_y - 4*next_line)
# draw_two(top_x + 3*next_letter, left_y - 4*next_line)
# draw_three(top_x + 4*next_letter, left_y - 4*next_line)


############### TEST WRITING WORDS ##################
#ELY LAM
# draw_E(top_x, left_y)
# draw_L(top_x + next_letter, left_y)
# draw_Y(top_x + 2*next_letter, left_y)
# draw_L(top_x + 4*next_letter, left_y)
# draw_A(top_x + 5*next_letter, left_y)
# draw_M(top_x + 6*next_letter, left_y)
# w1 = "AB 3RJ21PWRBNG ELY LAM"
# w2 = "HELLO, MY nam3 ic ELY Lamb."
# w3 = "abcde,."


################# PRINTING ##################
line_end = 15
def test_print_alpha():
    line_break = 0
    nxt = 0
    for v in alphabet.values():
        v(top_x + nxt*next_letter, left_y - line_break*next_line)
        nxt += 1
        if nxt > line_end:
            nxt = 0
            line_break += 1


# printing user input
def prnt_input(user_in):
    line_break = 0
    nxt = 0
    for ch in user_in:
        if nxt > line_end:
            if ch != ' ':
                nxt = 0
                line_break += 1
        if ch in alphabet:
            alphabet[ch](top_x + nxt*next_letter, left_y - line_break*next_line)
            nxt += 1

# prnt_input(user_input)
test_print_alpha()

# goToPos(0, 0) # if pointer on, use to move pointer after finish drawing

turtle.done()
# turtle.exitonclick()
# import tkinter as tk
# tk.TK_SILENCE_DEPRECATION=1