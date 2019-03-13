#Program, williamPrudencio_lab7-4.py, 02/27/19

''' This program will ask the user how many numbers they would 
like to generate, the specified amount will then be generated using 
a random number generator. The program will then display the smallest 
and largest numbers in the list, as well as the total and the average 
of the numbers in the list. '''

def main(): #define the main function ---------------------------------------- 
    #find out how many numbers to generate
    numsToGenerate = int(input('How many numbers would you like to generate: '))
    
    numList = numGenerator(numsToGenerate) #create the list of random numbers
    numTotal = numListTotal(numList) #get total of the list of random numbers
    numAverage = numListAverage(numTotal, numsToGenerate) # get the average 
    sortSmall = sortBySmall(numList) #sort by smallest to biggest 
    sortBig = sortByBig(numList) #sort by biggest to smallest 
    
    #print the results 
    print("\nThe list of random numbers is:\n", numList)
    print("\nThe list sorted by smallest to largest:\n", sortSmall)
    print("\nThe list sorted by biggest to smallest:\n", sortBig)
    print("\nThe total of the random numbers list is: ", numTotal)
    print("\nThe avarage of the random average list is: ", numAverage)
    
    
def numGenerator(numsToGenerate): #define the number generator fuction---------    
    import random #import the random number generator
    numList = [] #create the list of random numbers 
    
    #add the random numbers to the list
    for i in range(numsToGenerate):
        nums = int(random.randrange(1, 101)) 
        numList.append(nums) 
    return numList

def numListTotal(numList): #define numListTotal to calculale total---------------
    total = 0
    for number in numList:
        total += number
    return total   

def numListAverage(numListTotal, numsToGenerate):#average finder function---------
    return numListTotal / numsToGenerate


def sortBySmall(numList):#function to sort from smallest to biggest---------------
    smallNum = numList.copy()#Copy the list to avoid it being replaced
    
    for i in range(len(smallNum)): #loop for sorting the list
        for j in range(i + 1, len(smallNum)):
            if smallNum[i] > smallNum[j]: #test for smaller number
                smallNum[i], smallNum[j] = smallNum[j], smallNum[i]   
                
    return smallNum

def sortByBig(numList):#function to sort from biggest to smallest---------------
    bigNum = numList.copy()#Copy the list to avoid it being replaced
    
    for i in range(len(bigNum)): #loop for sorting the list
        for j in range(i + 1, len(bigNum)):
            if bigNum[i] < bigNum[j]: #test for bigger number
                bigNum[i], bigNum[j] = bigNum[j], bigNum[i]   
                
    return bigNum

main() #call the main function to run the program    
