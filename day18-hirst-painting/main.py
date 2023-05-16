import turtle
import colorgram
import random
colors = colorgram.extract("image.jpg", 30)
selected_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    selected_colors.append((r, g, b))
color_list = selected_colors[2:]
tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

def hirst_painting(rows, cols, dot_size, dot_dis):
    screen = turtle.Screen()
    screen.colormode(255)
    screen.setup((dot_size + dot_size) * rows + 150, (dot_size + dot_size) * cols + 150)
    for i in range(cols):
        tim.setposition((-screen.window_width() / 2 + 50, -screen.window_height() / 2 + i * dot_dis + 50))
        for j in range(rows):
            tim.dot(dot_size, random.choice(color_list))
            tim.forward(dot_dis)
    screen.exitonclick()


hirst_painting(10, 10, 20, 50)

