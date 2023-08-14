#Programmed by XKMR on GitHub
#
#   Copyright 2023 XKMR
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# -----------------
#this is a script for simulating a object with a direction that can move in said direction.
#define time for delays
from time import sleep

#Function to Turn in a given direction
def turn(directionToTurn, currentDirection):
    '''
    turnes the object by 90 degrees clockwise or counterclockwise

            Parameters:
                    directionToTurn (str): `CW` or `CC`
                    currentDirection (str): `up` , `down` , `left` , `right`

            Returns:
                    newDirection (str): `up` , `down` , `left` , `right`
    '''
    if(directionToTurn != "CC" and directionToTurn != "CW"):
        return "ERROR: invalid direction to turn"
    if(currentDirection != "up" and currentDirection != "down" and currentDirection != "left" and currentDirection != "right"):
        return "ERROR: invalid current direction"
    newDirection = "up"
    if(directionToTurn == "CC"):
        if(currentDirection == "up"):
            newDirection = "left"
        elif(currentDirection == "down"):
            newDirection = "right"
        elif(currentDirection == "left"):
            newDirection = "down"
        elif(currentDirection == "right"):
            newDirection = "up"

    if(directionToTurn == "CW"):
        if(currentDirection == "up"):
            newDirection = "right"
        elif(currentDirection == "down"):
            newDirection = "left"
        elif(currentDirection == "left"):
            newDirection = "up"
        elif(currentDirection == "right"):
            newDirection = "down"
    return newDirection
#Function to move a given number of steps
def forward(x, y, currentDirection, numbersOfSteps):
    '''
    moves object in the direction that it is facing

            Parameters:
                    x                (int): position of said object on the X axis
                    y                (int): position of said object on the Y axis
                    currentDirection (str): `up` , `down` , `left` , `right`
                    numberOfSteps    (int): number of steps that should be taken
            Returns:
                    x, y (tuple): The new X, Y for the object
    '''
    if(currentDirection == "up"):
        y = y + numbersOfSteps
    elif(currentDirection == "down"):
        y = y - numbersOfSteps
    elif(currentDirection == "left"):
        x = x - numbersOfSteps
    elif(currentDirection == "right"):
        x = x + numbersOfSteps
    return x, y
#defining currentX, currentY and the default currentDirection
currentX = 0
currentY = 0
currentDirection = "up"
#smiplified function for turning
def smturn(directionToTurn):   
    '''
    simplifies the turn command by removing the need for inputing the `currentDirection`
    requires the `turn()` function to work, requires a variable named `currentDirection` to work

            Parameters:
                    directionToTurn (str): `left` , `right`
            Returns:
                    0
    '''
    global currentDirection
    if(directionToTurn == "right"):
        CCorCW = "CW"
    elif(directionToTurn == "left"):
        CCorCW = "CC"
    else:
        return('ERROR: direction to turn must be "left" or "right"')
    currentDirection = turn(CCorCW, currentDirection)
    return 0
#simplified function for moving
def smforward(numberOfSteps):
    '''
    simplifies the turn command by removing the need for inputing anything other than the amount
    of steps that is going to be taken.

            Parameters:
                    numberOfSteps (int): number of steps to be taken
            Returns:
                    0
    '''
    global currentX
    global currentY
    x,y = forward(currentX, currentY, currentDirection, numberOfSteps)
    currentX = x
    currentY = y
    return 0

def displayCurrentPlace(localX, localY, currentDirection):
    '''
    makes a 20x20 "screen" that will display the place and direction of the object.
    note that this needs some improvements
                
            Parameters:
                    localX (int):           position of said object on the X axis
                    localY (int):           position of said object on the Y axis
                    currentDirection (str): `up` , `down` , `left` , `right`
            Returns:
                    output (str): output "screen" each line of "pixels" seperated by a newline character
    '''
    localY = localY - (2*localY)
    drawX = 0
    drawY = 0
    output = ""
    character = ""
    if(currentDirection == "up"):
        character = "▲"
    elif(currentDirection == "down"):
        character = "▼"
    elif(currentDirection == "left"):
        character = "◄"
    elif(currentDirection == "right"):
        character = "►"


    while(True):
        if(drawX == 19):
            if(drawY == 19):
                if(localX == drawX and localY == drawY):
                    if(drawX == 19):
                        output += character
                else:
                    if(drawX != 19):
                        output += "□"
                        drawX = drawX + 1
                break
            output += "\n"
            drawY = drawY + 1
            drawX = 0
        else:
            if(localX == drawX and localY == drawY):
                output += character
            else:
                output += "□"
            drawX = drawX + 1
    return output

