#program, williamPrudencio_lab2-15part2.py, 01/26/19

'''
This program will use Turtle Graphics to draw the second shape 
shown on page 107 of the "Starting Out With Python" book.
'''

import turtle;

#Change the fill color to orange------------
turtle.fillcolor("orange")

#Begin filling the shape with color----------
turtle.begin_fill()

#Move turtle using x & y coordinates to make the design
turtle.goto(200, 0)
turtle.goto(0, 200)
turtle.goto(-200, 0)
turtle.goto(200, 0)

#Stop filling the shape with color----------
turtle.end_fill()

#Continue moving turtle to finish the design-------------
turtle.goto(0, 400)
turtle.goto(-200, 0)

#Hide turtle 
turtle.hideturtle()

#Close turtle----------------------------
turtle.done()