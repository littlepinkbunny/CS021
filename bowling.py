#Mikayla Grace
#CS 021
#This program will print how each faculty member did based on their bowling score.

def main():
    print("This program will print how each faculty member did based on their bowling score.")
    try:
        infile = open('bowlingscores.txt','r')
        outfile = open('bowlingstats.txt','w')
#we need it to start reading the file
        name = infile.readline()
        score = ' '
#we want it to keep reading until the end of the file
        while name!='':
            try: score = int(infile.readline())
            except ValueError: break
#we want it to write the name, score, and assign an assessment to the score (perfect, not too shabby, or needs practice)
            if isinstance(score,int):
                if score==300:
                    outfile.write(name+str(score)+": Perfect\n")
                    name = infile.readline()
                elif score > 200:
                    outfile.write(name+str(score)+": Not too shabby.\n")
                    name = infile.readline()
                elif score < 200:
                    outfile.write(name+str(score)+": Needs practice.\n")
                    name = infile.readline()
            else:
                print(score)
                name = infile.readline()
        infile.close
        outfile.close
#we don't want it to crash so we add the "except" clause        
    except IOError:
        print("An error occurred while trying to read the file",file_name)

main()
