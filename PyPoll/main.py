import os
import csv

csv_path = "/Users/hatkiet/Bootcamp/Module 3 Challenge/Submitted/PyPoll/Resources/election_data.csv"

# Initialize dictionaries to store candidate's name, number of votes, and percentages
Candidate_Votes = {}
Candidate_Percentage = {}

# Initialize the value of total votes
Total_Votes = 0

# Read the CSV file from csv_path
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip the header row

    # Iterate through rows of data after the header
    for row in csvreader:
        Total_Votes += 1
        Candidate = row[2]

        # Check if candidate is already in the dictionary
        if Candidate in Candidate_Votes:
            Candidate_Votes[Candidate] += 1
        else:
            Candidate_Votes[Candidate] = 1

    # Calculate and store candidate's percentage
    for Candidate in Candidate_Votes:
        Candidate_Percentage[Candidate] = round((Candidate_Votes[Candidate]/Total_Votes)*100,3)
        #print(round(Candidate_Percentage[Candidate], 3))

    # Find the winner. Find in the candidate_votes dictionary that has the maximum associated value (vote count)
    Winner = max(Candidate_Votes, key=Candidate_Votes.get) 
    #print(Winner)

    # Write the Summary table to a output file
    output_file = "/Users/hatkiet/Bootcamp/Module 3 Challenge/Submitted/PyPoll/Analysis/result.txt"
    with open(output_file, "w") as resultfile:
        resultfile.write("\nElection Results\n")
        resultfile.write("\n-------------------------\n")
        resultfile.write(f"Total Votes: {Total_Votes}\n")
        resultfile.write("\n-------------------------\n")
        for Candidate in Candidate_Votes:
            resultfile.write(f"{Candidate}: {Candidate_Percentage[Candidate]}% ({Candidate_Votes[Candidate]})\n")
        resultfile.write("\n-------------------------\n")
        resultfile.write(f"Winner: {Winner}")
        resultfile.write("\n-------------------------\n")