import csv
import os

#election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")
election_csv = "PyPoll/Resources/election_data.csv"

#Lists to store data
ballot_id = []
ballot_county =[]
ballot_candidate = []

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
        ballot_id.append(str(row[0]))
        ballot_county.append(str(row[1]))
        ballot_candidate.append(str(row[2]))

#find greatest increase
greatest_increase = max(ballot_candidate)

#find greatest decrease
greatest_decrease = min(ballot_candidate)

#build output lines
output.append("Election Results")
output.append("")
output.append("----------------------------")
output.append("")
output.append("Total Votes: " + str(len(ballot_id)))
output.append("----------------------------")




output.append("")
output.append("Total: $" + str(sum(ballot_county)))
output.append("")
output.append(f"Average Change ${(sum(ballot_candidate)/(len(ballot_candidate)-1)):.2f}")
output.append("")
output.append("Greatest Increase in Profits: " + ballot_id[ballot_candidate.index(greatest_increase)] + " ($" + str(greatest_increase) + ")")
output.append("")
output.append("Greatest Decrease in Profits: " + ballot_id[ballot_candidate.index(greatest_decrease)] + " ($" + str(greatest_decrease) + ")")
output.append("")
output.append("")
output.append("")

# Specify the file to write to
#output_path = os.path.join("..", "analysis", "output.csv")
output_path = "PyPoll/analysis/output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as export:
    for row in output:
        export.write('{}\n'.format(row))
        print(row)
