# This program displays my first name and last name initials.
# Import the turtle module.
import turtle

# Assign a name to the turtle and set the turtle speed.
mame = turtle.Turtle()
mame.speed(5)

# Hide the turtle, raise the pen and set the starting position.
mame.hideturtle()
mame.penup()
mame.goto(-100, 0)
# Set the pen size and start the design of my first name initial.
mame.pensize(5)
mame.pendown()
mame.left(90)
mame.forward(100)
mame.right(135)
mame.forward(45)
mame.left(90)
mame.forward(45)
mame.right(135)
mame.forward(100)

# Start the design of my last name.
mame.penup()
mame.left(90)
mame.forward(40)
mame.left(90)
mame.pendown()
mame.forward(100)
mame.right(180)
mame.forward(100)
mame.left(90)
mame.circle(50, 180)




turtle.done()
