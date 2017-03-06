#Mikayla Grace and Kyle Bodge
#CS 021
#This program is designed to give the output from the quadratic formula when the user inputs values for a,b, and c.

print("This program is designed to give the output from the quadratic formula when the user inputs values for a,b, and c.  The variables are the coefficients in the equation ax^2+bx+c=0")

#We are using a function that is stored in the math module:
import math

#Get values for a,b, and c.
a = float(input("Please input a value for A."))
b = float(input("Please input a value for B."))
c = float(input("Please input a value for C."))

#The quadratic formula is defined as
#x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a) and x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a), where x_1 and x_2 are solutions.

if (b**2-4*a*c)<0:
    print("There are no real roots.")
elif (b**2-4*a*c)==0:
    print("There is only one root which is",(-b)/(2*a))
else:
    x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("One solution to the formula is",format(x_1,'0.1f'))
    print("The second solution to the formula is",format(x_2,'0.1f'))
