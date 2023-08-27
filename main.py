# import colorgram
#
# colors = colorgram.extract('images.jpeg', 42)
# l = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_tuple=(r,g,b)
#     l.append(new_tuple)
# print(l)
import turtle

color_list = [(100, 49, 38), (27, 106, 165), (230, 157, 63),
              (232, 213, 91), (191, 40, 82), (219, 136, 173), (139, 103, 55), (111, 188, 212), (203, 165, 31),
              (213, 72, 97), (158, 24, 66), (19, 57, 134), (118, 191, 145), (8, 184, 160), (236, 87, 52),
              (141, 209, 227), (105, 106, 195), (13, 150, 85), (25, 162, 202), (230, 165, 184), (84, 42, 27),
              (25, 42, 88), (26, 85, 91), (241, 207, 7), (236, 167, 159), (150, 213, 196), (173, 184, 222),
              (99, 16, 49), (28, 88, 87), (8, 78, 78)]
import random
from turtle import Turtle, Screen
import turtle as tm
tm.colormode(255)
t = Turtle()
t.pu()
t.hideturtle()
t.setheading(225)
t.forward(320)
t.setheading(0)


def dots():
    for _ in range(10):
        t.dot(15, random.choice(color_list))
        t.forward(50)


for _ in range(10):
    dots()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
    
my_screen = Screen()
my_screen.exitonclick()
