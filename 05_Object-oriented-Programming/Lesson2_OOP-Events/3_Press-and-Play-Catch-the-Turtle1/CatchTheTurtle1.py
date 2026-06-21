# original solution:

# from turtle import *
# from time import sleep
# from random import randint

# w = 200
# h = 150
# v = 100
# points = 0

# t = Turtle()
# t.color('red')
# t.penup()
# t.shape('turtle')
# t.speed(v)
# t.points = 0

# def rand_move():
#     t.goto(randint(-w, w), randint(-h, h))


# def catch(x, y):
#     t.write('A!', font=('Arial', 14, 'normal'))
#     t.points = t.points + 1
#     rand_move()


# t.onclick(catch)

# while t.points < 3:
#     sleep(1.5)
#     rand_move()

# t.write('WOW!', font=('Arial', 16, 'bold'))
# t.hideturtle()

# alternative solution using ontimer() instead of sleep()
# this is to make the program more responsive when run locally
from turtle import *
from random import randint

w = 200
h = 150
points = 0

t = Turtle()
t.color('red')
t.penup()
t.shape('turtle')
t.speed(0)

def rand_move():
    t.goto(randint(-w, w), randint(-h, h))

def catch(x, y):
    global points
    t.write('A!', font=('Arial', 14, 'normal'))
    points += 1
    rand_move()

def play():
    if points < 3:
        rand_move()
        Screen().ontimer(play, 1500)
    else:
        t.write('WOW!', font=('Arial', 16, 'bold'))
        t.hideturtle()

t.onclick(catch)
play()
done()
