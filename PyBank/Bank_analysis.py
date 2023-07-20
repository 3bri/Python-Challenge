#read in csv
import os
import csv
#Declare constants
BUDGET_DATA_PATH = os.path.join( "Resources", "budget_data.csv")

month_count = 0
total_profit = 0
previous_profit = 1088983  # is the value of the first entry so row 1 - row 1 equals zero and doesn't alter the sum of differences
change = 0
monthly_change = []
greatest_increase = 0
smallest_increase = 0
greatest_date = 1
smallest_date = 1


# change directory to the correct folder (from Python to PyBank)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open and read csv
with open(BUDGET_DATA_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # store the header 
    csv_header = next(csv_file)

#Display (print) the analysis
#1 number of months which is the number of rows
    for row in csv_reader:
        month_count = month_count + 1
        current_month = row[0]
        current_profit = int(row[1])
        total_profit += current_profit #keeps adding the values
        change = (current_profit) - (previous_profit)    #calculation of monthly change 
        monthly_change.append(change)  #creation of the list of monthly changes

        sum_of_monthly_change = sum(monthly_change)
        #could be done by len, regardless differences have one less row than entries so reduce the denominator
        average_monthly_change = sum_of_monthly_change / month_count - 1    

        #calculating greatest and smallest changes
        if change > greatest_increase:
            greatest_increase = change
            greatest_date = row[0]
        elif change < smallest_increase:
            smallest_increase = change
            smallest_date = row[0]

        #setup for next iteration
        previous_profit = current_profit
        
#change print commands to match the output
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {month_count}")
#2 sum of column 2
print(f"Total: ${total_profit}")
#3 monthly changes and the average of the monthly changes
print(f"Average Change: ${average_monthly_change}")
#4 the greatest monthly change
print(f"Greatest Increase in Profits: {greatest_date}  ${greatest_increase}")
#5 the smallest monthly change
print(f"Greatest Decrease in Profits: {smallest_date}  ${smallest_increase}")

#writing out the text file of the Financial Analysis
lines = ["Financial Analysis", 
             "---------------------------------------", 
             "Total Months:  " + str(month_count),
             "Total:  $" + str(total_profit),
             "Average Change:  $" + str(average_monthly_change),
             "Greatest Increase in Profits:  " + str(greatest_date) + "  ($" + str(greatest_increase) + ")",
             "Greatest Decrease in Profits:  " + str(smallest_date) + "  ($" + str(smallest_increase) + ")"]
#Specify the file to write to
output_path = os.path.join("Analysis", "bank_analysis.txt")
with open(output_path, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")