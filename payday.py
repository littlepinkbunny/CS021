#Mikayla Grace
#CS 021

print("This program is designed to tell the user their total pay and to write this information to a text file.")

#define main and make the empty lists that we will add to. Set the running total to 0 to be used laeter.
def main():
    userNames=[]
    hoursWorked=[]
    hourlyPay=[]
    total = 0
    outfile = open('payroll.txt','w')
    answer ='y'
    #start a while loop based on user input because we don't know the number of users
    while answer=='y' or answer == 'Y':
    #use try/except to handle ValueError and get the user inputs
        try:
            name = str(input("What is the name of the user?"))
            hours = float(input("How many hours did this person work?"))
            pay = float(input("What is this person's hourly pay?"))
            userNames.append(name)
            hoursWorked.append(hours)
            hourlyPay.append(pay)
            answer = input("Would you like to add another user? y/n")
        except ValueError:
            name = str(input("Value error.  Please input the user's data again. What is the name of the user?"))
            hours = float(input("How many hours did this person work?"))
            pay = float(input("What is this person's hourly pay?"))
            userNames.append(name)
            hoursWorked.append(hours)
            hourlyPay.append(pay)
            answer = input("Would you like to add another user? y/n")
    #go through the lists and do the calculations. write the results to the file
    for i in range(0,len(userNames)):
        totalPay = format(float(hoursWorked[i]*hourlyPay[i]),'0.2f')
        total+=float(totalPay)
        outfile.write("User: "+userNames[i]+" Hours Worked: "+str(hoursWorked[i])+" Hourly Pay: "+str(hourlyPay[i])+" Total Pay: "+str(totalPay)+"\n")
    average = format(total/len(userNames),'0.2f')
    outfile.write("Total pay for all users: $"+str(format(total,'0.2f'))+'\n')
    outfile.write("Total average paycheck is: $"+str(average))
    outfile.close()
main()
