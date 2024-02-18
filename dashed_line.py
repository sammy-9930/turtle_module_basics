from turtle import Turtle, Screen

tim = Turtle(shape="arrow")
screen = Screen()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
