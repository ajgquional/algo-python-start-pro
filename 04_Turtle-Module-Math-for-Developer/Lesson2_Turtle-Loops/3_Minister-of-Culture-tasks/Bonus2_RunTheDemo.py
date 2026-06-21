from turtle import *

pensize(2)
# speed(10)
speed(15) # to make the drawing faster

color("navy")
size = 10
for i in range(7):
    circle(size)
    size = size+10
left(90)

color("navy")
size = 10
for i in range(7):
    circle(size)
    size = size+10
left(90)

color("navy")
size = 10
for i in range(7):
    circle(size)
    size = size+10
left(90)

color("navy")
size = 10
for i in range(7):
    circle(size)
    size = size+10 

# alternative solution:
# for i in range(4):
#     color("navy") # can be taken out of the loop
#     size = 10
#     for i in range(7):
#         circle(size)
#         size = size+10 
#     left(90)
    
hideturtle()
exitonclick()
