# This program design 100 nested squares.
# Import the turtle module  .
import turtle

# Assign a name to the turtle, set the speed and the 1st square sides.
mame = turtle.Turtle()
mame.speed(10)
side = 10


# Set the turtle head west and hide the turtle head.
mame.setheading(180)
mame.hideturtle()

# Start the design with a loop.
for square in range (100):
    mame.forward(side)          
    mame.right(90)             
    mame.forward(side)
    mame.right(90)
    mame.forward(side)
    mame.right(90)
    mame.forward(side)
    mame.right(90)

    # Set the turtle back to the start of the 1st square.
    mame.goto(0, 0)

    # Increment the sides of the next square.
    side += 2


turtle.done()


     
   
    
    
  
   


       
        

    

    
