# Program - williamPrudencio_lab2-6.py 01/22/19

'''
This program will ask the user to input their purchase ammount, the program will then
calculate and display the purchase amount, state tax, county tax, total tax, and the total
amount of the purchase.
'''

#-------VARIABLES TO BE USED-----------

purchaseAmount, stateTax, countyTax, totalTax, totalAmount = 0.0, 0.0, 0.0, 0.0, 0.0 ;

#-------Constants-----------------------------

STATE_TAX_RATE = 0.05;
COUNTY_TAX_RATE = 0.025;

#GET USER INPUT(purchaseAmount)-------

purchaseAmount = float( input("Please enter the amount of your purchase: ") );

#----------------CALCULATIONS----------------------------

#calculate the state tax------------------
stateTax = purchaseAmount * STATE_TAX_RATE;

#calculate the county tax----------------
countyTax = purchaseAmount * COUNTY_TAX_RATE;

#calculate the total tax------------------
totalTax = stateTax + countyTax;

#calculate the total amount------------- 
totalAmount = purchaseAmount + totalTax;

#-----------DISPLAY RESULTS---------------------
print("Purchase amount: ", format(purchaseAmount, ".2f") );
print("State tax: " , format(stateTax, ".2f") );
print("County tax: ", format(countyTax, ".2f") );
print("Total tax: ", format(totalTax, ".2f") );
print("Total amount: ", format(totalAmount, ".2f") );