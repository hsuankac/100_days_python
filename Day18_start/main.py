import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
colors = ["azure", "tan", "violet", "rosy brown", "dark red", "dark cyan", "midnight blue", "red"]
directions = [0, 90, 180, 270]


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# Challenge 1: draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Challenge2: draw a dash line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge3: drawing different shape
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Challenge4: Generate a random walk

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Challenge5: draw a Spirograph\
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
