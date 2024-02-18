import random
import turtle
from turtle import Turtle, Screen
directions = [0, 90, 180, 270]

tim = Turtle("circle")
turtle.colormode(255)
tim.pensize(10)
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    tim.speed("slow")
    tim.color(random_color())
    tim.forward(random.randint(0, 50))
    tim.setheading(random.choice(directions))


screen.exitonclick()
