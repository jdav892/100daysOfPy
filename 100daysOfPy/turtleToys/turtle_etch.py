from turtle import Turtle, Screen

jay = Turtle()
screen = Screen()

def move_forward():
    jay.forward(10)

def move_backward():
    jay.backward(10)

def turn_counter_clockwise():
    new_heading = jay.heading() + 10
    jay.setheading(new_heading)

def turn_clockwise():
    new_heading = jay.heading() - 10
    jay.setheading(new_heading)
    
def clear_screen():
    jay.clear()
    jay.penup()
    jay.home()
    jay.pendown()
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick() 