from turtle import *

def red_light_on():
    color("red")
    penup()
    goto(0,100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def red_light_off():
    color("red")
    penup()
    goto(0,100)
    pendown()
    circle(35)


def yellow_light_on():
    color("yellow")
    penup()
    goto(0,0)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def yellow_light_off():
    color("yellow")
    penup()
    goto(0,0)
    pendown()
    circle(35)


def green_light_on():
    color("green")
    penup()
    goto(0,-100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def green_light_off():
    color("green")
    penup()
    goto(0,-100)
    pendown()
    circle(35)


answer = input("What traffic light is on now red/yellow/green? ")
if answer == "red":
    red_light_on()
    yellow_light_off()
    green_light_off()
if answer == "yellow":
    red_light_off()
    yellow_light_on()
    green_light_off()
if answer == "green":
    red_light_off()
    yellow_light_off()
    green_light_on()

hideturtle()
exitonclick()
