import os
import csv

# Create path to the file that we are using the data from
election_csv = os.path.join('Resources', 'election_data.csv')

votes = []

# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Reads through file and separates values by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Makes the first row of the file the header
    header = next(csvreader)

    for row in csvreader:

        votes.append(row[2])

total_votes = len(votes)

candidates = []
[candidates.append(x) for x in votes if x not in candidates]

first_candidate_votes = 0
second_candidate_votes = 0
third_candidate_votes = 0
fourth_candidate_votes = 0

for vote in votes:

    if vote == candidates[0]:

        first_candidate_votes += 1

    elif vote == candidates[1]:

        second_candidate_votes += 1

    elif vote == candidates[2]:

        third_candidate_votes += 1

    else:

        fourth_candidate_votes += 1

first_candidate_percent = (first_candidate_votes / total_votes) * 100
second_candidate_percent = (second_candidate_votes / total_votes) * 100
third_candidate_percent = (third_candidate_votes / total_votes) * 100
fourth_candidate_percent = (fourth_candidate_votes / total_votes) * 100

candidate_votes_list = [first_candidate_votes, second_candidate_votes, third_candidate_votes, fourth_candidate_votes]

votes_max = max(candidate_votes_list)

votes_max_location = candidate_votes_list.index(votes_max)

votes_max_candidate = candidates[votes_max_location]

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"{candidates[0]}: {round(first_candidate_percent, 3)}% ({first_candidate_votes})")
print(f"{candidates[1]}: {round(second_candidate_percent, 3)}% ({second_candidate_votes})")
print(f"{candidates[2]}: {round(third_candidate_percent, 3)}% ({third_candidate_votes})")
print(f"{candidates[3]}: {round(fourth_candidate_percent, 3)}% ({fourth_candidate_votes})")
print("-----------------------")
print(f"Winner: {votes_max_candidate}")
print("-----------------------")