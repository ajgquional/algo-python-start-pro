from turtle import *
from random import randint
from time import sleep

finish = 200

def drawLines(t):
    t.color('lightgray')
    t.speed(50)
    t.penup()
    x = -200
    y = 200
    t.goto(x, y)
    t.right(90)
    t.pendown()
    for i in range(20):
        t.forward(400)
        t.penup()
        x += 20
        t.goto(x, y)
        t.pendown()
    t.left(90)


def startRace(t, x, y, color):
    t.color(color)
    t.shape('turtle')
    t.speed(100)
    t.penup()
    t.goto(x, y)


def dance(t):
    t.speed(15)
    t.left(randint(0, 90))
    j = 0
    while j < 8:          
        t.penup()
        t.goto(0, 0)
        t.pendown()
        i = 1
        while i < 32:
            t.forward(i)
            t.left(i/2+5)
            i += 1
        j += 1
    t.penup()
    t.goto(0, 0)


# Start of the main program:
# Creating racers:
t1 = Turtle()
t2 = Turtle()

# start of the race
drawLines(t2)
startRace(t1, -200, -20, 'red')
startRace(t2, -200, 20, 'blue')

sleep(1)

while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
sleep(1)
  
# calculating totals:
t1.clear()
t2.clear()

max_x = max(t1.xcor(), t2.xcor())

if t1.xcor() == max_x:
   dance(t1)

if t2.xcor() == max_x:
   dance(t2)
