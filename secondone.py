import math
from turtle import *


def draw_heart(turtle, size):
    turtle.fillcolor('pink')
    turtle.begin_fill()
    for i in range(200):
        k = i
        x = size * (15 * math.sin(k)**3)
        y = size * (12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k))
        turtle.goto(x, y)
        turtle.speed(8)  
    turtle.end_fill()


def write_text(turtle, text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align="center", font=("Arial", 24, "bold"))  


screen = Screen()
screen.bgcolor('black')


heart_turtle = Turtle()
heart_turtle.color('pink')


draw_heart(heart_turtle, 12)  


write_text(heart_turtle, "your txt", 0, -220)  


outside_text_turtle = Turtle()
outside_text_turtle.color('white')


write_text(outside_text_turtle, "your txt", 0, -350)  


done()
