#Program, williamPrudencio_lab3-16.py, 02/03/19

''' This program will ask the user to enter a year, it
will then test if the inputted year is indeed a leap year.
The program will return a message letting the user know if
the year that they entered is a leap year or not. '''

#VARIABLES------------------------------------------

yearEntered, leapYear, febDays = 0, False, 28

#REQUEST USER INPUT---------------------------------

yearEntered = int(input("Please enter a year: "))

#PERFORM TESTING------------------------------------

#Check for leap year---------------
if yearEntered % 100 == 0 and yearEntered % 400 == 0:
    leapYear = True 
elif yearEntered % 100 != 0 and yearEntered % 4 == 0:
    leapYear = True
else:
    leapYear = False

#Days in february------------------

if leapYear == True:
    febDays = 29

#DISPLAY RESULTS--------------------------------------
print("In",yearEntered, "February has", febDays, "days.")
    

    