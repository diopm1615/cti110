# This program will design the olympic rings
# 09/19/19
# CTI-110 P2HW2-Turtle graphic
# Mame Diop
#

import turtle # load the turtle module
print("This program will design the olympic rings.")# display a message in the command line window to start the design.
print("\nPlease press the \"enter\" key to start.")
input()               # start the design.
turtle.hideturtle()   # hide the turtle.      
turtle.circle(50)     # design the first 50 pixels radius circle.
turtle.penup()        # pen up. 
turtle.forward(125)   # move forward 125 pixels.
turtle.pendown()      # pen down.
turtle.circle(50)     # design the 2nd 50 pixels radius circle.
turtle.penup()        # pen up.
turtle.backward(250)  # move the turtle 250 pixels to the left of the 1st circle. 
turtle.pendown()      # pen down.
turtle.circle(50)     # design the 3rd 50 pixels radius circle.
turtle.penup()        # pen up.
turtle.forward(62.5)  # move forward 62.5 pixels.
turtle.left(90)       # turn the turtle 90 degrees pointing in a northern direction.
turtle.forward(35.5)  # move 35.5 pixels up.
turtle.left(90)       # turn the turtle 90 degrees west.
turtle.pendown()      # pen down.
turtle.circle(50)     # design the 4th 50 pixels radius circle.
turtle.penup()        # pen up.
turtle.backward(125)  # move 125 pixels pointing to the East.
turtle.pendown()      # pen down.
turtle.circle(50)     # design the 5th 50 pixels radius circle.
print("\nThank you! please close the graphic window or the command line window.") # display a message to close graphic window.
turtle.done()         #close the graphic window.




