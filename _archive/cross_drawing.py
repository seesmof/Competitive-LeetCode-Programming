"""
✝️💗🙏
♰
☧
✙
†
"""

import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw the vertical part of the cross
my_turtle.left(90)
my_turtle.forward(200)

# Draw the horizontal part of the cross
my_turtle.back(60)
my_turtle.left(90)
my_turtle.forward(80)
my_turtle.left(180)
my_turtle.forward(160)

my_turtle.hideturtle()
turtle.done()
