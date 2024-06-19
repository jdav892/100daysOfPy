import turtle
from turtle import * 
import random


tim = Turtle()
#tim.shape("turtle")
tim.color("firebrick")

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

colors = ["orchid1", "PeachPuff", "firebrick", "midnightblue", "maroon"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.speed("fastest")
    tim.pensize(5)
    tim.forward(20)
    tim.setheading(random.choice(directions))

#for i in range(100):
#    tim.pencolor(randint(0, 255),randint(0, 255),randint(0, 255))
#    steps = int(random() * 100)
#    angle = int(random() * 360)
#    tim.right(angle)
#    tim.fd(steps)
#



screen = Screen()
screen.exitonclick()
screen.colormode(255)
