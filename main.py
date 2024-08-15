# import colorgram
#
# # Extract 6 colors from an image.
# colours = colorgram.extract('image.jpg', 20)
# rgb_colours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
tim.penup()
colour_list = [(236, 35, 108), (221, 231, 238), (145, 28, 66), (230, 237, 232), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35)]

tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()
