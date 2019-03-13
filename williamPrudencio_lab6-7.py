#Program, williamPrudencio_lab6-7.py, 02/23/19

''' This program will write a user specified number of random 
numbers ranging from 1-500 that will be written to a file. '''

#Define the main function -----------------------------------------
def main():
    #get the quantity of randoms numbers to generate
    numsToGenerate = int(input("How many random numbers should the file hold: "))
    #send quantity to the number generator function
    numGenerator(numsToGenerate)

#define the number generator function-------------------------------
def numGenerator(numsToGenerate):
    
    import random #import the random number generator
    
    #create the file to output random numbers to
    file_object = open("randomNumber.txt", "w")    
    
    #generate and write the random numbers
    for i in range(numsToGenerate):
        nums = str(random.randrange(1, 501))
        file_object.write(nums + "\n")
      
    #Close the file
    file_object.close()    

#call the main function to run the program-------------------------    
main()     
        
        