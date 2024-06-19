import turtle
from turtle import * 
import random


tim = Turtle()
#tim.shape("turtle")
#tim.color("firebrick")
tim.hideturtle()

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)



screen = Screen()
screen.exitonclick()