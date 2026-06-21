from turtle import *

def square1():
    color('black','white')
    pendown()
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)  
    end_fill()   


def square2():
    color('black')
    pendown()
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)  
    end_fill()    


pensize(2)

penup()
goto(-200,50)
for i in range(4):
    square2()
    forward(50)
    square1()
    forward(50)

penup()
goto(-200,0)   
for i in range(4):
    square1()
    forward(50)
    square2()
    forward(50)

penup()
goto(-200,-50)
for i in range(4):
    square2()
    forward(50)
    square1()
    forward(50)
    
hideturtle()
exitonclick()
