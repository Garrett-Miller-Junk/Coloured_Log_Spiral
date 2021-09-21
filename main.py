"""
Basic Code Using Turtle Library (just for fun)

Haven't used turtle before so I decided to try it out.

Stuff that I can add;
-make it faster
-print final image once done

Garrett Miller-Junk
"""

# import the turtle library
import turtle

# initializes the screen
screen = turtle.Screen()

# declares the size of the screen
screen.setup(1000, 1000)

# background colour of screen
screen.bgcolor("black")

# creates a turtle to draw on the screen
marker = turtle.Turtle()

# how fast the turtle will move
marker.speed(100)

# creates a tuple to store the RGB values as floats from 0.00-1.00 (I only go up to 0.99)
RGB = (0.99, 0.00, 0.00)

# creates a list from the tuple
RBG_list = list(RGB)

# just made relatively large for loop so that it would go through a lot of iteration, but eventually stop
for i in range(3000):
    # make a list out of the tuple
    RGB_list = list(RGB)

    # increase the amount of red (if possible) if it is not at its max and if there is currently no green.
    if (RGB_list[0] < 0.99) and (RGB_list[1] <= 0.00):
        RGB_list[0] += 0.01
    # if there is still red left and green is at its max value, decrease the amount of red
    elif (RGB_list[0] > 0.00) and (RGB_list[1] >= 0.99):
        RGB_list[0] -= 0.01

    # do the same process to increase green (now with respect to blue) and blue (with respect to red)
    if (RGB_list[1] < 0.99) and (RGB_list[2] <= 0.00):
        RGB_list[1] += 0.01
    elif (RGB_list[1] > 0.00) and (RGB_list[2] >= 0.99):
        RGB_list[1] -= 0.01
    if (RGB_list[2] < 0.99) and (RGB_list[0] <= 0.00):
        RGB_list[2] += 0.01
    elif (RGB_list[2] > 0.00) and (RGB_list[0] >= 0.99):
        RGB_list[2] -= 0.01

    #turn the new list into a touple and make that the new RGB touple
    RGB = tuple(RGB_list)

    #moves forward the marker a small amount (chose this a i^2 base so that the spiral would get larger and larger, but start small)
    marker.forward((i / 200) * (i / 5000))

    #turn right by 1 degree
    marker.right(1)

    #change the colour to the new touple
    marker.color(RGB)
