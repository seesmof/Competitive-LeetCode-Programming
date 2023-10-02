import turtle

screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw the letter N
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(135)
my_turtle.forward(140)
my_turtle.right(-135)
my_turtle.forward(100)

my_turtle.penup()
my_turtle.goto(50, 120)
my_turtle.pendown()
my_turtle.left(180)
my_turtle.forward(150)

# Hide the turtle
my_turtle.hideturtle()
turtle.done()
