#Program, williamPrudencio_lab5-23.py, 02/16/19

''' This program will use turtle graphics to display a snowman.
There will be five different functions used to accomplish this 
task. '''

def main():
    #draw the base
    drawBase(0, 0, 100 , "white")
    #draw the mid section
    drawMidSection(0, 175, 75, "white")
    #Draw the left arm
    drawArms(-75, 175, -115, 185, "black")
    drawArms(-115, 185, -130, 230, "black")
    drawArms(-130, 230, -140, 235, "black")
    drawArms(-130, 230, -125, 245, "black")
    #draw the right arm
    drawArms(75, 175, 140, 185, "black")
    drawArms(140, 185, 145, 195, "black")
    drawArms(140, 185, 150, 175, "black")
    #draw the head
    drawHead(0, 300, 50 , "white")
    drawHead(-25, 305, 5 , "black")
    drawHead(25, 305, 5 , "black")
    drawArms(-30, 280, 30, 280, "black")
    #draw the hat
    drawHat(-35, 320, 70, "black")
    drawHat(-50, 320, 20, "black")
    drawHat(-70, 320, 20, "black")
    drawHat(30, 320, 20, "black")
    drawHat(50, 320, 20, "black")

#draw the base of the snow man
def drawBase(x, y, radius, color):
    turtle.penup()              #Raise pen
    turtle.goto(x, y - radius)  #Position turtle
    turtle.fillcolor(color)     #Set fill color
    turtle.pendown()            #Lower pen
    turtle.begin_fill()         #Start filling
    turtle.circle(radius)       #Draw circle
    turtle.end_fill()           #End filling

#draw the mid section of the snowman    
def drawMidSection(x, y, radius, color):
    turtle.penup()              #Raise pen
    turtle.goto(x, y - radius)  #Position turtle
    turtle.fillcolor(color)     #Set fill color
    turtle.pendown()            #Lower pen
    turtle.begin_fill()         #Start filling
    turtle.circle(radius)       #Draw circle
    turtle.end_fill()           #End filling    

#draw the arms
def drawArms(startX, startY, endX, endY, color):
    turtle.penup()              #Raise pen
    turtle.goto(startX, startY) #Move to start
    turtle.pendown()            #Lower pen
    turtle.pencolor(color)      #Set pen color
    turtle.goto(endX, endY)     #Move to end, draw line
    
#draw the head
def drawHead(x, y, radius, color):
    turtle.penup()              #Raise pen
    turtle.goto(x, y - radius)  #Position turtle
    turtle.fillcolor(color)     #Set fill color
    turtle.pendown()            #Lower pen
    turtle.begin_fill()         #Start filling
    turtle.circle(radius)       #Draw circle
    turtle.end_fill()           #End filling   

#draw the hat
def drawHat(x, y, width, color):
    turtle.penup()              #Raise pen
    turtle.goto(x, y)           #Position turtle
    turtle.fillcolor(color)     #Set fill color
    turtle.pendown()            #Lower pen
    turtle.begin_fill()         #Start filling
    for count in range(4):      #Draw square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()           #End filling

import turtle

main()

turtle.done()