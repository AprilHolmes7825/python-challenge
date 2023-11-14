import csv
import os

bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
#bank_csv = "PyBank/Resources/budget_data.csv"
#PyBank\Resources\budget_data.csv

#Lists to store data
date = []
profit_loss =[]
change = []

#to store output
output = []

with open(bank_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #challenge requirements say to read and store contents of header row, but it's never used?
    #skip header
    header = next(csvfile)

    for row in csvreader:
        #don't calculate change for first data row, but add change for every row
        if len(profit_loss) > 0:
            last_profit_loss = profit_loss[len(profit_loss)-1]
            change.append(int(row[1]) - int(last_profit_loss))
        else:
            change.append(0)

        #add date
        date.append(str(row[0]))

        #add profit/loss
        profit_loss.append(int(row[1]))

#find greatest increase
greatest_increase = max(change)

#find greatest decrease
greatest_decrease = min(change)

#build output lines
output.append("Financial Analysis")
output.append("")
output.append("----------------------------")
output.append("")
output.append("Total Months: " + str(len(date)))
output.append("")
output.append("Total: $" + str(sum(profit_loss)))
output.append("")
output.append(f"Average Change ${(sum(change)/(len(change)-1)):.2f}")
output.append("")
output.append("Greatest Increase in Profits: " + date[change.index(greatest_increase)] + " ($" + str(greatest_increase) + ")")
output.append("")
output.append("Greatest Decrease in Profits: " + date[change.index(greatest_decrease)] + " ($" + str(greatest_decrease) + ")")
output.append("")
output.append("")
output.append("")

# Specify the file to write to
#output_path = os.path.join("..", "analysis", "output.csv")
output_path = "PyBank/analysis/output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as export:
    for row in output:
        export.write('{}\n'.format(row))
        print(row)
