from turtle import*

def pizza():
    color("black","orange")
    begin_fill()
    left(60)
    forward(100)
    right(100)
    forward(100)
    right(110)
    forward(100)
    end_fill()

def pepperoni():
    begin_fill()
    color("black","brown")
    circle(10)
    end_fill()

pizza()
pepperoni()

hideturtle()
exitonclick()