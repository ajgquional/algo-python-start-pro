from turtle import*

pensize(2)
goto(-50,-50)

def square ():
    for i in range(4):
        forward(200)
        left(90)


begin_fill()
square()    
end_fill() 
penup()
goto(170,-50)
pendown()
begin_fill()
circle(3)
end_fill() 
hideturtle()
exitonclick()
