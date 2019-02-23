#Program, williamPrudencio_lab4-16.py, 02/09/19

''' This program draws a turtle graphic based on a loop
with a specified number of squares from the user. '''

#Number of squares the user would like to draw
numSquares = int(input("Enter the number of squares to draw: "))

import turtle

j = 0 #Counter for counting the quares
moveF = 100 #Amount to move turtle foward
moveL = 90 #Amount to move turtle left

#Compare counter to numSquares to begin loop
while j < numSquares:
    #Loop that will draw the square(s)
    for i in range (4):
        turtle.left(moveL)
        turtle.forward(moveF)
    #--------------------------------   
    j = j + 1 #Increase the value of j
    moveF = moveF + 10 #Increase moveF(bigger square next iteration)

#Stop turtle
turtle.done()