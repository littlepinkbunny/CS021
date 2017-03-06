#Mikayla Grace
#CS 021

print("This program is a guessing game where you will guess the number of jelly beans in a jar based on the jar's height and radius.")

#import the needed functions and define 2 global constants
import random
import math
MIN=1
MAX=10

#define main and get the comp. to randomly generate the height and radius, and call the functions
def main():
    print("The jar's dimensions are:")
    height = random.randint(MIN,MAX)
    print("The height of the jar is",height,"inches.")
    radius = random.randint(MIN,MAX)
    print("The radius of the jar is",radius,"inches.")
    volume = computeVolume(height,radius)
    beans = computeBeans(volume)
    guess = int(input("Guess the number of jelly beans in the jar based on the dimensions given above."))
    classifyGuess(beans,guess)
    print("You guessed that there are",guess,"beans in the jar.")
    print("The actual number of beans in the jar is",beans)

#compute the volume using the equation for volume
def computeVolume(height,radius):
    volume = math.pi*height*radius**2
    return volume

#compute the number of beans based on the parameters given about bean volume and air volume
def computeBeans(volume):
    beans = volume*0.8//0.47
    return beans

#using the user's guess given in main, classify it as too high, too low, or acceptable and print the result
def classifyGuess(beans,guess):
    if guess>(beans*1.1):
        print("Sorry, your guess is too high")
    elif guess<(beans*0.9):
        print("Sorry, your guess is too low.")
    else:
        print("Congrats, your guess is within the acceptable range!")

main()
