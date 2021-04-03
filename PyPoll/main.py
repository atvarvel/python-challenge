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

candidates = []
[candidates.append(x) for x in votes if x not in candidates]
