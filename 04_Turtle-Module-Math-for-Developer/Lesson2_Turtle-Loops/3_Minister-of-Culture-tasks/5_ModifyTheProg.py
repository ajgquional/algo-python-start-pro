from turtle import *

penup()
goto(-200, 0)
pendown()
pensize(10)

for i in range(4):
    color("indigo")
    left(70)
    forward(50)
    right(140)
    forward(50)
    left(140)
    color("thistle")
    forward(100)
    right(140)
    forward(100)
    left(70)

hideturtle()
exitonclick()
