import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    tot_votes = len(csvfile.readlines())

    print ("Election Results")
    print ("")
    print ("-------------------------")
    print ("")
    print (f"Total Votes: {tot_votes}")
    print ("")
    print ("-------------------------")

    csvfile.seek(1)
    next(csvreader)

    #create a list of candidates- this is working! (now through if/else)
    candidates = []
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        else:
            candidate = row[2]
    
    csvfile.seek(1)
    next(csvreader)

    #create a list of votes and count per candidate in candidate list- this is working! (now through votes.append)
    votes = []

    for row in csvreader:
        votes.append(row[2])

    #print: candidate name, percentage of votes, then vote count in ()
        #candidate name will be candidates[0], candidates[1], and candidates[2]
        #percentage will be ((votes.count(candidates[0])) / (tot_votes)) * 100)
        #vote count will be (votes.count(candidates[0]))
    candidate1 = candidates[0]
    candidate2 = candidates[1]
    candidate3 = candidates[2]

    votes1 = votes.count(candidates[0])
    votes2 = votes.count(candidates[1])
    votes3 = votes.count(candidates[2])

    percent1 = (votes1 / tot_votes) * 100
    percent2 = (votes2 / tot_votes) * 100
    percent3 = (votes3 / tot_votes) * 100

    print("")
    print(f"{candidate1}: {percent1:2f}% ({votes1})")
    print("")
    print(f"{candidate2}: {percent2:2f}% ({votes2})")
    print("")
    print(f"{candidate3}: {percent3:2f}% ({votes3})")
    print("")
    print ("-------------------------")
    print("")
    print(f"Winner: {candidate2}")
    print("")
    print ("-------------------------")

#write results to txt file
file = open(os.path.join("analysis", "analysis.text"), "w")
file.write("\nElection Results")
file.write("\n-------------------------")
file.write("\n ")
file.write(f"\nTotal Votes: {tot_votes}")
file.write("\n ")
file.write("\n-------------------------")
file.write("\n ")
file.write(f"\n{candidate1}: {percent1:2f}% ({votes1})")
file.write("\n ")
file.write(f"\n{candidate2}: {percent2:2f}% ({votes2})")
file.write("\n ")
file.write(f"\n{candidate3}: {percent3:2f}% ({votes3})")
file.write("\n ")
file.write("\n-------------------------")
file.write("\n ")
file.write(f"\nWinner: {candidate2}")
file.write("\n-------------------------")
file.write("\n ")