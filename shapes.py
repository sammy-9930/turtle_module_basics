from turtle import Turtle, Screen
import random
list_of_colors = ["blue", "green", "red", "yellow", "cyan", "pink", "purple"]

tim = Turtle(shape="arrow")
screen = Screen()

for number_of_sides in range(3, 11):
    tim.color(random.choice(list_of_colors))
    for _ in range(number_of_sides):
        tim.forward(50)
        tim.left(360/number_of_sides)

screen.exitonclick()
