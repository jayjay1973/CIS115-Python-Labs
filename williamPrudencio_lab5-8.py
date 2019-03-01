#Program, williamPrudencio_lab5-8.py, 02/16/19

'''Given the following informarion: area coverrage is 750 sqft per gallon and 8 hours of labor to cover said area
and hourly charge for the company is $35.00 . This program will ask the user to input sqft area to be painted
and the cost of paint per gallon to calculate and display the following: The number of gallons required, the 
hours of labor required, the cost of the paint, the cost of the labor and the total cost of the paint job.
'''

#CONSTANT_VARIABLES---------------------------------------------

HOURLY_RATE = 35.00  #Hourly rate charged by the company
SQFT_PER_GALLON = 750.00 #Square feet covered per gallon
HOURS_PER_GALLON = 8.00 #Hours to use a gallon or cover 750sqft

def main():
    #Get user input
    wallArea = float(input("Enter the square feet of wall space to be painted: "))
    gallonCost = float(input("Enter the cost of the paint per gallon: "))
    
    calc1 = numReqGal(wallArea) #Number of gallons required
    calc2 = reqLaborHours(calc1) #Labor hours required
    calc3 = paintCost(calc1, gallonCost) #Cost of the paint
    calc4 = laborCost(calc2) #Cost of the labor
    calc5 = totalCost(calc3, calc4) #Total cost of the job 
    
    showResults(calc1, calc2, calc3, calc4, calc5) #Display the results
    
#Number of gallons required    
def numReqGal(wallArea): 
    calc1 = wallArea / SQFT_PER_GALLON
    return calc1

#Labor hours required
def reqLaborHours(calc1):
    calc2 = calc1 * HOURS_PER_GALLON
    return calc2

#Cost of the paint
def paintCost(calc1, gallonCost):
    calc3 = calc1 * gallonCost
    return calc3

#Cost of the labor
def laborCost(calc2):
    calc4 = HOURLY_RATE * calc2
    return calc4

#Total cost of the job 
def totalCost(calc3, calc4):
    calc5 = calc3 + calc4
    return calc5

#Display the results
def showResults(calc1, calc2, calc3, calc4, calc5):
    print("\nNumber of gallons required: ", format(calc1,".2f"))
    print("Hours of labor required: ", format(calc2, ".2f"))
    print("Cost of the paint: $", format(calc3, ".2f"))
    print("Labor charges: $", format(calc4, ".2f"))
    print("Total cost of the paint job: $", format(calc5, ".2f"))

#Call the main function
main()