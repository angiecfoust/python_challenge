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
    print ("")

    #net total amount of profit_losses over the entire period
    total = 0
    csvfile.seek(1)
    next(csvreader)

    for row in csvreader:
        total = (total + int(row[1])) 
        date_yr.append(row[0]) 
        profit_loss.append(int(row[1]))

    print (f"Total: ${total}")
    print("")

    #changes in profit/losses over the entire period and average of those changes
    #create list of months (date_yr) and list of pofit/loss
    

    csvfile.seek(1)
    next(csvreader)

    for i in range (1, len(csvfile.readlines())): #this loop Amanda helped with
        change = profit_loss[i] - profit_loss[i-1]
        changes.append(change)
            
    average = sum(changes)/(months - 1)
    max_inc = max(changes)
    max_date = ([changes.index(max_inc)][0]) #this is not working, only includes an index number
    max_dec = min(changes)
    dec_date = ([changes.index(max_dec)][0]) #this is not working, only includes an index number

print (f"Average Change: ${average:.2f}") #tip from Amanda (2f) put in readme
print("")
print (f"Greatest Increase in Profits: ${max_inc} {max_date}") 
print("")
print (f"Greatest Decrease in Profits: ${max_dec} {dec_date}") 
print("")

#write results to a text file
file = open(os.path.join("analysis", "analysis.txt"), "w")
file.write("\nFinancial Analysis")
file.write("\n_________________________")
file.write("\n ")
file.write(f"\nTotal Months {months}")
file.write("\n ")
file.write(f"\nTotal: $ {total}")
file.write("\n ")
file.write(f"\nAverage Change: ${average:.2f}")
file.write("\n ")
file.write(f"\nGreatest Increase in Profits: ${max_inc} {max_date}")
file.write("\n ")
file.write(f"\nGreatest Decrease in Profits: ${max_dec} {dec_date}")
file.write("\n ")
file.write("\n_________________________")
