#read in csv
import os
import csv

#Declare constants

ELECTION_DATA_PATH = os.path.join( "Resources", "election_data.csv")
vote_count = 0
unique_candidate_names = []
CC_Stockham_votes = 0
D_DeGette_votes = 0
RA_Doane_votes = 0
winner = 0

# change directory to the correct folder (from Python to PyBank)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open and read csv
with open(ELECTION_DATA_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # store the header 
    csv_header = next(csv_file)
    #print(csv_header) - was check to ascertain header was stored

#Display (print) the analysis
#reads through each row after the header
    for row in csv_reader:  
#1 sum of the votes (last line)
        vote_count = vote_count + 1  
#2 list of candidates (unique names in column 2)
        candidate_name = row[2]
        if candidate_name not in unique_candidate_names:
            unique_candidate_names.append(candidate_name)
#3 total number of votes for a candidate, which is the sum of the rows for a given name
        if (candidate_name == "Charles Casper Stockham"):
            CC_Stockham_votes = CC_Stockham_votes + 1
        if (candidate_name == "Diana DeGette"):
            D_DeGette_votes = D_DeGette_votes +1
        if (candidate_name == "Raymon Anthony Doane"):
            RA_Doane_votes = RA_Doane_votes +1
#4 % of the vote for a candidate, sum of the rows for a given name divided by sum of rows (#1)
CC_Stockham_perc = (CC_Stockham_votes/vote_count) * 100
D_DeGette_perc = (D_DeGette_votes/vote_count) * 100
RA_Doane_perc = (RA_Doane_votes/vote_count) * 100
#5 declare the winner, which is the candidate with the greatest number of rows/votes
if (CC_Stockham_perc > D_DeGette_perc and CC_Stockham_perc > RA_Doane_perc):
    winner = ("Charles Casper Stockham")
if (D_DeGette_perc > CC_Stockham_perc and D_DeGette_perc > RA_Doane_perc):
    winner = ("Diana Degette")
if (RA_Doane_perc > CC_Stockham_perc and RA_Doane_perc > D_DeGette_perc):
    winner = ("Raymon Anthony Doan")

#print(vote_count) #total number of votes
#print(unique_candidate_names) #is the list of candidates that received votes - verification

#print commands to produce the example output
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------------")
print(f"Charles Casper Stockham:  {CC_Stockham_perc}%  ({CC_Stockham_votes})")
print(f"Diana Degette:  {D_DeGette_perc}%  ({D_DeGette_votes})")
print(f"Raymon Anthony Doan:  {RA_Doane_perc}%  ({RA_Doane_votes})")
print("-------------------------------")
print(f"Winner:  {winner}")
print("-------------------------------")

#export a new csv file
#writing out the text file of the Financial Analysis
lines = ["Election Results", 
             "---------------------------------------", 
             "Total Votes:  " + str(vote_count),
             "---------------------------------------",
             "Charles Casper Stockham:  " + str(CC_Stockham_perc) +"%  (" + str(CC_Stockham_votes) + ")",
             "Diana Degette:  " + str(D_DeGette_perc) +"%  (" + str(D_DeGette_votes) + ")",
             "Raymon Anthony Doan:  " + str(RA_Doane_perc) +"%  (" + str(RA_Doane_votes) + ")",
             "---------------------------------------",
             "Winner:  " + str(winner),
             "---------------------------------------"]
#Specify the file to write to
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")