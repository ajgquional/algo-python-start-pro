from turtle import*

def sun ():
    pensize(2)
    color("yellow")
    i=0
    begin_fill()
    while i<18:
        forward(150)
        left(100)
        i=i+1
    end_fill()


sun()     
hideturtle()
exitonclick() 
