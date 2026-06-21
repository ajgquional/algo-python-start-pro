from turtle import *

penup()
goto(0,-150)
pendown()
color("brown")
pensize(20)
left(90)
forward(200)

pensize(10)
length = 10
color("green")

for i in range(26):
    forward(length)
    length = length + 5
    left(90)

hideturtle()
exitonclick()  
