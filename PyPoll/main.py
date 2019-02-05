import os
import csv

election_csv = os.path.join("/Users/dmytrodmytrenko/Documents/Git/python-challenge/PyPoll", "election_data.csv")

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    
    print("Election Results")
    print("---------------------")
    row_count = sum(1 for row in csvreader)
    print(f"Total Votes: {row_count}")
    print("---------------------")