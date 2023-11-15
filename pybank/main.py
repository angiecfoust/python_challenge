#open and read csv file in pybank resources folder
import os
import csv
from tkinter.tix import ROW
csvpath = os.path.join('Resources', 'budget_data.csv')

#set up to store data?
#months = []
#row = 0

#open file and set up reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#define/exclude header
    csv_header = next(csvreader)

 #count total number of months   
    months = len(csvfile.readlines())

    for row in csvreader: 
        print(row) #can remove this for final project; lines 14-15 just print the csv file rows
        print (row[1]) #I think this is testing what row you start on

    
        

#net total amount of profit/losses over the entire period
    
        total = sum(int(row[1]))
       # total += int(row[1]) #this is only returning the first row value
        #profit_loss = (total + int(row[1]))   #this is the first thing I tried and it's returning first row value

        

#changes in profit/losses over the entire period and average of those changes


#greatest increase in profits (date and amount) over entire period


#greatest decrease in profits (date and amount) over entire period

#print it all
print("Financial Analysis")
print("______________________________")
print("Total Months: ", (months)) 

print("Total: ", total) #this section is not working- it is just showing 0
        #print (row[1]) #this is just testing what row you end on?- and it is ending on the correct row
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")
