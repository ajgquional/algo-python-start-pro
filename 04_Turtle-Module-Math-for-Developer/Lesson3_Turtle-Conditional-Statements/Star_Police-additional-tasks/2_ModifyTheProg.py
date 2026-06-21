from turtle import*

def pizza():
    color("black","orange")
    begin_fill()
    left(60)
    forward(160)
    right(108)
    forward(100)
    right(108)
    forward(160)
    end_fill()


def pepperoni():
    begin_fill()
    color("black","salmon")
    circle(10)
    end_fill()


pensize(2)
penup()
goto(-50,-30)
pendown()
pizza()
penup()
goto(-10,15)
pendown()
pepperoni()
penup()
goto(45,40)
pendown()
pepperoni()
penup()
goto(20,65)
pendown()
pepperoni()

hideturtle()
exitonclick()
