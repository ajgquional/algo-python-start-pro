from turtle import *

def star ():
    pensize(2)
    color("red")
    begin_fill()
    for i in range(5):
        forward(100)
        left(144)
    end_fill()   
    
     
star()
hideturtle()    
exitonclick()
