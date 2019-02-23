#Program, williamPrudencio_lab3-8.py, 01/30/19

''' This program will calculate the number of hot dog and hot dog buns packages 
needed for a cookout with minimum left overs. The calculation is based on the 
user inputed information of how many people will be attending and the amount 
of hot dogs they will each be given. '''

#CONSTANTS-----------------------------------------

H_DOGS_PER_PACKAGE, H_DOG_BUNS_PER_PACKAGE = 10, 8 #Number of hot dogs and hot dog buns per package

#VARIABLES TO BE USED---------------------------
numRequiredHotDogs, numRequiredHotDogBuns = 0, 0 #Required number of hot dogs and hot dog buns 
leftOverHotDogs, leftOverHotDogBuns = 0, 0 #Hot dogs and Hot dog buns that will be left over
peopleAttending = 0         #Store the number of people attending the cookout
hotDogsPerPerson = 0        #Store the number of hot dogs that each person gets

#GET USER INPUT-----------------------------------------------------------

#Find out how many people will be attending
peopleAttending = int(input("How many people will attend the cookout: "))

#Find out how many hot dogs each person will get
hotDogsPerPerson = int(input("How many hot dogs will each person get: "))

#This will give us the total hot dogs and hot dog buns needed for the cookout
totalHotDogs = peopleAttending * hotDogsPerPerson
   
numRequiredHotDogs = int(totalHotDogs /H_DOGS_PER_PACKAGE)
numRequiredHotDogBuns = int(totalHotDogs /H_DOG_BUNS_PER_PACKAGE)

'''Turning the above results into an interger allows for the below testing
to work. If the totalHotDogs is divisible without any remainders then it makes 
no difference, however, if not divisible and there is a remainder then it will
be dropped allowing for the if statement to run and adding an extra package
as necessary so that no people are left without a hot dog.'''
 
#CALCULATE RESULTS-------------------------------------------------------

if totalHotDogs > numRequiredHotDogs * H_DOGS_PER_PACKAGE:
   numRequiredHotDogs = numRequiredHotDogs + 1

if totalHotDogs > numRequiredHotDogBuns * H_DOG_BUNS_PER_PACKAGE:
   numRequiredHotDogBuns = numRequiredHotDogBuns + 1

#-------------------------------------------------------------------------
 
#Calculate the left overs    
leftOverHotDogs = (numRequiredHotDogs * H_DOGS_PER_PACKAGE) - totalHotDogs      
leftOverHotDogBuns = (numRequiredHotDogBuns * H_DOG_BUNS_PER_PACKAGE) - totalHotDogs

#DISPLAY RESULTS---------------------------------------------------------
print("\n")
print ("The minimun number of packages of hot dogs required is: ", numRequiredHotDogs)
print ("The minimum number of packages of hot dog buns required is: ", numRequiredHotDogBuns)
print  ("The number of hot dogs that will be left over is: ", leftOverHotDogs)
print  ("The number of hot dog buns that will be left over is: ", leftOverHotDogBuns)