#open and read csv file in pybank resources folder
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #print(csvreader) #I think this an be removed for the final project

    csv_header=next(csvreader)
    #print(f"CSV Header: {csv_header}") #can remove this for the final project, just prints header row

    #for row in csvreader: #can remove this for final project
        #print(row) #can remove this for final project; lines 14-15 just print the csv file rows

#total number of months included in dataset
print ("Financial Analysis")
print ("______________________________")

months = len(csvpath)
print ("Total Months: ", months) #this is returning 25- what the heck?!



#net total amount of profit/losses over the entire period
print ("Total: ")

#changes in profit/losses over the entire period and average of those changes
print ("Average Change: ")

#greatest increase in profits (date and amount) over entire period
print ("Greatest Increase in Profits: ")

#greatest decrease in profits (date and amount) over entire period
print ("Greatest Decrease in Profits: ")