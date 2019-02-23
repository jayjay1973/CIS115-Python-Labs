# Program, williamPrudencio_lab4-13.py, 02/09/19

'''This programs predicts the population size based on the
following information that the user inputs: The starting number of
organisms, the average daily increase and the number of days to
multiply.'''

# VARIABLES--------------------------------------------------

startingPopulation, dailyIncrease, daysToMultiply = 1, 0, 0


#Main loop for keeping the program runnig 
while startingPopulation != 0:
    
    #Find the starting population--------------------------------------
    startingPopulation = int(input("\nStarting number of organisms: "))
    #If starting population is 0, stop the program
    if startingPopulation == 0:
        break
    #------------------------------------------------------------------
    #Find the average daily increase and the number of days to multiply
    dailyIncrease = float(input("Average daily increase(.3 is 30%): "))
    daysToMultiply = int(input("Number of days to multiply: "))
    
    #Print the table heading, use ; for separate statements same line
    print("\nDay \t Population"); print("---------------------------")
    
    #Loop for calculating the population------------------------------- 
    for number in range(1, daysToMultiply + 1):
        print(number, "\t", startingPopulation)
        startingPopulation += startingPopulation * dailyIncrease    





