#open and read csv file in pybank resources folder
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#lists to store data
date_yr = []
profit_loss = []
changes = []

#set up printed results
print ("Financial Analysis")
print ("")
print ("______________________________")
print ("")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    #total number of months included in dataset
    months = len(csvfile.readlines()) #keep this out of the for loop
    
    print (f"Total Months: {months}") 

    #net total amount of profit_losses over the entire period
    total = 0
    csvfile.seek(1)
    next(csvreader)

    for row in csvreader:
        total = (total + int(row[1])) 

    print (f"Total: ${total}")  

    #changes in profit/losses over the entire period and average of those changes
    #create list of months (date_yr) and list of pofit/loss
    date_yr.append(row[0]) 
    profit_loss.append(int(row[1]))

    
    for i in range (1, len(csvfile.readlines())):
        
        change = profit_loss[i] - profit_loss[i-1]
        changes.append(change)

        average = (sum(changes)/len(changes))
        max_inc = max(changes)
        max_date = months[changes.index(max_inc) + 1]
        max_dec = min(changes)
        dec_date = months[changes.index(max_dec) +1]

    print (f"Average Change: ${average:.2f}")
    print (f"Greatest Increase in Profits: {max_inc} {max_date}") #include month and in () $amount
    print (f"Greatest Decrease in Profits: {max_dec} {dec_date}") #include month and in () $amount