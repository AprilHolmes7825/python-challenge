import csv
import os

#election_csv = os.path.join("...", "Resources", "election_data.csv")
election_csv = "PyPoll/Resources/election_data.csv"

ballots = []
candidates = []

#to store output
output = []

with open(election_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #challenge requirements say to read and store contents of header row, but it's never used?
    #skip header
    header = next(csvfile)

    for row in csvreader:
        #add ballot_id
        ballots.append({"id": row[0],
                        "county": row[1],
                        "candidate": row[2]})
        
        #if new candiate, add to candidates lilst
        if candidates.count(str(row[2])) == 0:
            candidates.append(str(row[2]))

#build output lines
output.append("Election Results")
output.append("")
output.append("----------------------------")
output.append("")
#output.append("Total Votes: " + str(len(ballot_id)))
output.append("Total Votes: " + str(len(ballots)))
output.append("----------------------------")
output.append("")

#Summarize candidates and determine winner
winner = ""
winner_votes = 0


for candidate in candidates:
    num_votes = 0
    percentage = 0
    #tally number of votes per candidate
    for ballot in ballots:
        if ballot["candidate"] == candidate:
            num_votes += 1
    
    #check against current winner
    if num_votes > winner_votes:
        winner = candidate
        winner_votes = num_votes

    percentage = num_votes/len(ballots) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({str(num_votes)})")
    output.append("")

output.append("----------------------------")
output.append("")
output.append("Winner: " + winner)
output.append("")
output.append("----------------------------")

# Specify the file to write to
#output_path = os.path.join("..", "analysis", "output.csv")
output_path = "PyPoll/analysis/output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as export:
    for row in output:
        export.write('{}\n'.format(row))
        print(row)
