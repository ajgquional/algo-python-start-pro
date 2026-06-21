from turtle import *

def day():
    pensize(2)
    color("yellow")
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()
    

def night():
    pensize(2)
    color("bisque")
    begin_fill()
    circle(50)
    end_fill()
    

answer = input("What time of day is it now (day/night)? ")
if answer == "day":
    day()
if answer == "night":
    night()    

hideturtle()
exitonclick()
