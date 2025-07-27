# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)



import turtle as t
import random

# Constants
DOT_SIZE = 20
GAP = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10

color_list = [
    (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
    (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
    (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
    (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

def setup_turtle():
    t.colormode(255)
    tim = t.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()

    # center the grid:
    start_x = - (GAP * (GRID_WIDTH - 1)) / 2
    start_y = - (GAP * (GRID_HEIGHT - 1)) / 2
    tim.goto(start_x, start_y)

    return tim

def draw_dots(tim):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            tim.dot(DOT_SIZE, random.choice(color_list))
            tim.forward(GAP)
        tim.setheading(90)
        tim.forward(GAP)
        tim.setheading(180)
        tim.forward(GAP * GRID_WIDTH)
        tim.setheading(0)

tim = setup_turtle()
draw_dots(tim)

screen = t.Screen()
screen.exitonclick()
