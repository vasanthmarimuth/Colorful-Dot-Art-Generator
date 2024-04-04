# import colorgram
#
#
# rgb_colors=[]
# colors=colorgram.extract('download.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

tim.speed("fastest")
number_of_dots = 100
colors = [(248, 246, 236), (237, 250, 244), (251, 239, 248), (236, 243, 250), (233, 222, 92), (211, 158, 105),
          (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111),
          (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43),
          (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206),
          (133, 215, 229), (175, 177, 227), (59, 16, 31)]
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
