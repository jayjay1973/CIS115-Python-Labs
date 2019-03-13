#Program, williamPrudencio_lab6-8.py, 02/23/19

''' This program will read the numbers generated onto randomNumber.txt in the 
previous lab assignment lab6-7. It will display all the numbers that were read
from the file and add them together to get a sum total. It will also keep and 
display a count of how many number were read from the file. '''

#define the main function --------------------------------------
def main():
    file_object = open("randomNumber.txt", "r")   #open the file
    fileReader(file_object) # Send the file to the file reader function
    file_object.close() #Close the file

#define the file reader function -------------------------------
def fileReader(file_object):
    #Begin counter and sum of numbers read
    counter = 0
    total = 0
   
    print("\nNumbers on file: \n") 
    for line in file_object: #Read the lines 
        line = int(line.rstrip("\n"))
        print(line) #print the lines
        #increase counter and total
        counter += 1
        total += line
    
    #print the counter and total
    print("\nNumbers read from file: ", counter)
    print("Sum of numbers read from file: ", total)
    print("Average of numbers read from file: ", total/counter)
        
#call the main function to run progarm -------------------------
main()