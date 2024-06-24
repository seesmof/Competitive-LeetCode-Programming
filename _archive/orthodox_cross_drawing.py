"""
☦️💗🙏
♰
☧
✙
†
"""

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the vertical part of the cross
t.left(90)
t.forward(200)

t.back(30)
t.left(90)
t.forward(40)
t.left(180)
t.forward(80)
t.left(180)
t.forward(40)

t.left(90)
t.forward(40)

# Draw the horizontal part of the cross
t.left(90)
t.forward(80)
t.left(180)
t.forward(160)
t.left(180)
t.forward(80)

t.right(90)
t.forward(70)
t.left(60)
t.forward(40)
t.back(40)
t.left(180)
t.forward(40)

t.hideturtle()
turtle.done()
