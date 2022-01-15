# Election-Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election:

### Tasks
1. Calculate the total number of votes cast.
2. Compile a complete list of candidates who received votes.
3. Determine the the total number of votes that each candidate received.
4. Calculate the percentage of votes that each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the voter turnout for each of the three counties in the dataset.
7. Determine the percentage of votes from each county out of the total count.
8. Determine the county with the highest turnout.

## Resources
+ Data Source: [election_results.csv](Resources/election_results.csv)
+ Software: Python 3.9.7, Visual Studio Code 1.63.2


## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- Denver County had the largest voter turnout with 82.8% of the vote (306,055 votes).
  - Jefferson County had 10.5% of the vote (38,855 votes).
  - Arapahoe County had 6.7% of the vote (24,801 votes).
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was Diana DeGette with 73.8% of the vote (272,892 votes).

### Results
The results of the election audit can be viewed here: [election_analysis.txt](analysis/election_analysis.txt)

## Process
To analyze the results of the election I wrote a script to read the raw data which was held in a CSV file called [election_results.csv](Resources/election_results.csv). I created a variable to hold the total votes, an empty list to hold the candidate names, an empty dictionary to hold candidate votes, an empty list to hold the county names, and an empty dictionary to hold the county votes. The following code block illustrates this.

```python
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}
```

I then initialized empty variables to track the winning candidate's name, vote count, and vote percentage and likewise the winning county's name, vote count, and percentage of votes. These variables will be assigned a value and used to print the results. The following code block illustrates this.

```python
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0
```

Next, I opened the CSV file to read, and using a for statement, iterated through each row of the file. For each row, I added to the total vote count, then checked to see if the candidate name was in the list of candidate names (and if not, I appended the candidate name to the list of candidates) and likewise checked to see if the county name was yet in the list of counties (and if not, I appended the county name to the list of counties). During this iteration I also added +1 to the vote count for each candidate and for each county. The following code block illustrates this part of the code.

```python
# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
  ```
  
  In the next block of code, I opened the text file that had been created to hold the results of the election audit, [election_analysis.txt](analysis/election_analysis.txt), and printed the total votes to the terminal and to the output text file. 
  
  ```python
  # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
 ```
 
 The next step is two for-loops, one to loop through the counties in the county votes dictionary to determine which county had the highest voter turnout (and to print the results to the output text file and the terminal):
 
 ```python
  # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        count_votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        count_votes_percentage = float(count_votes)/float(total_votes) *100
        county_results = (f'{county_name}: {count_votes_percentage:.1f}% ({count_votes:,})')
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(f'{county_results}\n')
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (count_votes > winning_county_votes) and (count_votes_percentage > winning_county_percentage):
            winning_county = county_name
            winning_county_percentage = count_votes_percentage
            winning_county_votes = count_votes

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f'\n-------------------------\n'
        f'Largest County Turnout: {winning_county}\n'
        f'-------------------------\n'
    )
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
 ```
 
 And another for loop to similarly loop through the candidate votes dictionary to see which candidate won the most votes, and to print the results to the terminal and to the output text file:
 
 ```python
 # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
 ```
 
 All of the code can be viewed in one file at [PyPoll_challenge.py](PyPoll_challenge.py)

## Election Audit Summary
Because of the way this code was written it is capable of analyzing elections of any size with any number of candidates, total voters, and counties. Rather than retrieving the candidates' and counties' names with user input, the code uses a simple if-statement and the append function to create a list of candidates and users. The code is also efficient, looping through the data in the CSV file only one time, making it a good option for even larger datasets. 

### Gubernatorial Elections
This code could be copied and tweaked slightly (replacing "counties" with "states") to analyze, for example, the gubernatorial elections held every 2-4 years ( depending on the state). Instead of creating a county list and county vote dictionary, the code could be tweaked to create a state list and state dictionary to determine which states had elections and which states had the highest voter turnout. In this case we would also need to create a dictionary of candidates for each state. Or, if the analysis were to be done at the state level, the code could be used as-is to determine the winner of the election for Governor within that state and to analyze the turnout per county.

### School Board Example
Another way this code could be modified slightly and be very useful is in analyzing the elections for school board. Similar to the above, we would want to replace "counties" with "schools" to determine which schools in the district had the highest voter turnout. If we wanted to analyze multiple districts at once, we would need to add a dictionary of lists of candidates associated with each school district. But, with minimal modifications, the code is useful for analyzing a school board election with one seat up for election in one school district. If there are multiple seats available in that election, as is common with school boards, then we could add a variable(s) such second_place_winner and third_place_winner to use in the final for-loop to determine all of the candidates who have won a seat on the school board.
