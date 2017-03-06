#Mikayla Grace
#CS 021
#This program is a game in which the user inputs a certain number of each type of coins in an attempt to achieve a sum of $1.00.  The program will tell the user if their combination of coins is a “winning” combination, meaning that their coins sum to $1.00.

#Assign values to coins.
PENNYVAL = 0.01
NICKELVAL = 0.05
DIMEVAL = 0.10
QUARTERVAL = 0.25

#Get guesses for number of each coin.
penny = int(input(“Guess number of pennies.”))
nickel = int(input(“Guess number of nickels.”))
dime = int(input(“Guess number of dimes.”))
quarter = int(input(“Guess number of quarters.”))

#Total the value of the change inputted by the user.
total = penny*0.01 + nickel*0.05 + dime*0.10 + quarter*0.25
if total = 1.00:
	print(“Congratulations, you won! Your total is equal to $1.00!”)
elif total > 1.00:
	print(“Sorry, you lost.  Your total is,”$”+(total-1.00),”over $1.00.”)
else:
	print(“Sorry, you lost.  Your total is, “$”+(1.00-total),”less than $1.00.”)
