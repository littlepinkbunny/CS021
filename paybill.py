#Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.
# Mikayla Z Grace
# CS 021
# The program "Paybill" is designed to help you figure out the total cost of your meal including tip and tax.
 
# Get total cost of meal.
Cost_of_Meal = float(input("Cost of meal?"))
# Calculate tax.  Food tax is 9% in the state of Vermont.
TAX = 0.09*Cost_of_Meal
# Calculate tip. Tip is conventionally 20% after tax.
TIP = 0.2*TAX
# Calculate the total cost of the meal using these three numeric values.
Total_Cost = float(Cost_of_Meal+TAX+TIP,"0.2d")
# Display total to user.
print("Your total meal cost, including tax and tip, is"," ","$",Total_Cost,sep="")


