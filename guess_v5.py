#Mikayla Grace and Kyle Bodge
#CS 021 lab
#This program is designed to be a guessing game.  The computer picks a random number between 1 and 100, and the user gets 5 tries to guess the number.

print("This program is a guessing game.  The computer picks a random number between 1 and 100, and the user gets 5 tries to guess the number.")

LOW=1
HIGH=100
again ="y"
MAX_TRIES=5

while again == "y" or again=="Y":
    counter=1
    import random
    number = random.randint(LOW,HIGH)
    guess = int(input("Guess an integer between 1 and 100."))
    while number!=guess and counter<5:
        if guess<1 or guess>100:
            print("Invalid input.")
            guess=int(input("Guess an integer between 1 and 100."))
        elif number<guess:
            print("Your guess was too high.  Please guess again.")
            counter+=1
            guess=int(input("Guess a different integer between 1 and 100."))
        elif number>guess:
            print("Your guess was too low.  Please guess again.")
            counter+=1
            guess=int(input("Guess a different integer between 1 and 100."))
    if number==guess:
        print("Congrats, you won!  Your guess was correct.  It took you",counter,"tries.")
    else:
        print("You lose.  You have used all 5 of your tries.  The answer was",number)
    again = input("Do you want to play again? (Y/N)")

        
