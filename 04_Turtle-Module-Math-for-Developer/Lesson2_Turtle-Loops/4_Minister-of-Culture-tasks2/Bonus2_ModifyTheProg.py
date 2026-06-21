from turtle import*

def star ():
    pensize(2)
    color("darkblue")
    i=0
    begin_fill()
    while i<5:
        forward(50)
        left(144)
        i=i+1
    end_fill()


speed(10)
coordinate_x =- 200
coordinate_y =- 100
for i in range(5):
    penup()
    goto(coordinate_x,coordinate_y)
    pendown()
    star()    
    coordinate_x += 80
    coordinate_y += 50
hideturtle()
exitonclick()  
