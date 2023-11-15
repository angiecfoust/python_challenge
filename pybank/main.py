#open and read csv file in pybank resources folder
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#lists to store data
date_yr = []
profit_loss = []


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    #total number of months included in dataset
    months = len(csvfile.readlines()) #keep this out of the for loop
    
    #net total amount of profit_losses over the entire period
    total = 0
    csvfile.seek(1)
    next(csvreader)

    for row in csvreader:
        total = (total + int(row[1])) 

        
    #changes in profit/losses over the entire period and average of those changes
    #find difference between current row and previous row, starting with row 3 (including header)
        date_yr.append(row[0]) #this is working and creating a list of all the months
        profit_loss = 0 #starting here it's not working- maybe need an if/then?
        date_yr[1] = 0
        profit_loss = ((date_yr[1]) - (date_yr[1]-1))
        profit_loss.append(row[1])

        
    #store those in a list called profit_loss
    #find average of profit_loss list
        #print(profit_loss)
    #greatest increase in profits (date and amount) over entire period
    #max of profit_loss list


    #greatest decrease in profits (date and amount) over entire period
    #min of profit_loss list

print(date_yr)
print(profit_loss)




#print results
print ("Financial Analysis")

print ("______________________________")

print ("Total Months: ", months) 

print ("Total: ", "$",(total))

print ("Average Change: $")

print ("Greatest Increase in Profits: ") #include month and in () $amount

print ("Greatest Decrease in Profits: ") #include month and in () $amount