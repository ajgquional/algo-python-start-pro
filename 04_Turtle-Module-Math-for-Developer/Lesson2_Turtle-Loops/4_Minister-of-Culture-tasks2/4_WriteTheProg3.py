from turtle import*

def star ():
    pensize(2)
    color("darkblue")
    i=0
    begin_fill()
    while i<5:
        forward(150)
        left(144)
        i=i+1
    end_fill()


star()
hideturtle()     
exitonclick()  
