from turtle import *

pensize(3)
speed(10)
length = 10

for i in range(25):
    forward(length)
    length += 10
    left(90)

hideturtle()
exitonclick()
