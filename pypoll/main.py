import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)


#total number of votes cast
    rows = list(csvreader)
    totalvotes = len(rows)
    #start printing results
    print ("Election Results")
    print ("")
    print ("-------------------------")
    print ("")
    print (f"Total Votes: {totalvotes}")
    print ("")
    print ("-------------------------")

    csvfile.seek(1)
    next(csvreader)

    
    candidates = []
    votes = []
    for i in range(totalvotes):
        candidate = rows[i][2]
        votes.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)

    #votes will be length of votes list for that candidate (i.e. number of occurrences)
    
    csvfile.seek(1)
    next(csvreader)

    cand_votes = []
    percentages = []

    for j in range (totalvotes):
        name = candidates[j]
        cand_votes.append(votes.count(name))
        percentage = cand_votes[j]/totalvotes
        percentages.append(percentage)

    csvfile.seek(1)
    next(csvreader)

    #print list each voter name, give % of votes, and give total votes
    for k in range(totalvotes):
        print(f"{candidates[k]}: {percentages[k]}%: ({cand_votes[k]:,})")
        print("")
        print ("-------------------------")
        print("")

#the winner of the election based on popular vote
    winner = cand_votes.index(max(votes))

    print (f"Winner: {winner}")
    print ("")
    print ("-------------------------")