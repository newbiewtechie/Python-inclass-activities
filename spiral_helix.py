import turtle
import math

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
spiral = turtle.Turtle()
spiral.speed(0)   # Fastest drawing speed
spiral.color("cyan")
spiral.pensize(2)

# Draw the spiral helix
for i in range(100):
    spiral.forward(math.sqrt(i) * 10)  # Move forward with increasing distance
    spiral.left(45)                    # Turn left
    spiral.forward(math.sqrt(i) * 10)  # Move again
    spiral.left(45)

# Hide turtle and finish
spiral.hideturtle()
turtle.done()