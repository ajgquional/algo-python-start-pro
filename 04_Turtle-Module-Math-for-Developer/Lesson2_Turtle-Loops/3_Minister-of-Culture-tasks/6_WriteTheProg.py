from turtle import *

def triangle():
    pensize(2)
    color("blue")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)


speed(10)
for i in range(36):
    triangle()  
    right(10)
hideturtle()
exitonclick()
