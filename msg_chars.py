#Mikayla Grace
#CS 021
#This program will count the number of character in a user-inputted message.

#define main and create the empty lists
def main():
    letter = []
    freq = []
#get the user input
    msg = input("Please input a message.")
#for each character, check if it's already in the list and add to the letter's corresponding freq
#if it's not in the list, add it and add a frequency corresponding to the new letter
    for ch in msg:
        if ch.upper() in letter:
            freq[letter.index(ch.upper())]+=1
        else:
            letter.append(ch.upper())
            freq.append(1)
#print the lists
    print("Letter\tFreq")

    for ch in letter:
        print(ch.upper(),"\t",freq[letter.index(ch)])    

#call main 
main()
