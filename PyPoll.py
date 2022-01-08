#The data we need to retrieve from the file Resources/election_results.csv
# 1. The total number of votes cast
# 2. A complete lst of candidates who received votes
# 3. The total number of votes that each candidate received
# 4. The % of votes that each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indrect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    #print each row in the CSV file
   # for row in file_reader:
    #    print(row)

#Using the open() function with the "w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
