#The data we need to retrieve from the file Resources/election_results.csv
# 1. The total number of votes cast
# 2. A complete lst of candidates who received votes
# 3. The total number of votes that each candidate received
# 4. The % of votes that each candidate won
# 5. The winner of the election based on popular vote.

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Declare list for Candidate Options
candidate_options = []

# Create a(n empty) dictionary to hold candidate names and votes
candidate_votes = {}

# Winning Candidate and Wnning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes+= 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # Calculate % of votes that each candidate received
    # Use a for-loop to iterate through the candidate_options
    for candidate_name in candidate_votes:
        # Retrieve the votes of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the % of votes
        vote_percentage = float(votes)/float(total_votes) * 100
        # Print the candidate name and the percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine if vote count is greater than winning_count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote %
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print out the Winning Candidate, vote count, and % vote to the terminal
    winning_candidate_summary = (
        f'--------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'--------------------------')
    print(winning_candidate_summary)
            

#Using the open() function with the "w" mode we will write data to the file
# with open(file_to_save,"w") as txt_file:
 #   txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 3. Print the Total Votes
#print(total_votes)

#print the candidate vote dictionary
#print(candidate_votes)
