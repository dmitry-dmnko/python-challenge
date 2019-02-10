import os
import csv

election_csv = os.path.join("/Users/dmytrodmytrenko/Documents/Git/python-challenge/PyPoll", "election_data.csv")

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    
    total_row = 0
    khan = 0
    correy = 0
    li = 0
    tooley = 0

    print("Election Results")
    print("---------------------")
    for row in csvreader:
        total_row += 1
        if row[2] == 'Khan':
            khan += 1
        elif row[2] == 'Correy':
            correy += 1
        elif row[2] == 'Li':
            li += 1
        elif row[2] == "O'Tooley":
            tooley += 1
    
    if max(khan, correy, li, tooley) == khan:
        winner = 'Khan'
    elif max(khan, correy, li, tooley) == correy:
        winner = 'Correy'
    elif max(khan, correy, li, tooley) == li:
        winner = 'Li'
    elif max(khan, correy, li, tooley) == tooley:
        winner = "O'Tooley"

    print(f"Total Votes: {total_row}")
    print("---------------------")
    print(f"Khan: {round((khan/total_row)*100,3)}% {khan}")
    print(f"Correy: {round((correy/total_row)*100,3)}% {correy}")
    print(f"Li: {round((li/total_row)*100,3)}% {li}")
    print(f"O'Tooley: {round((tooley/total_row)*100,3)}% {tooley}")
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")

with open("election_results.txt", "w") as file:
    file.write(f"Total Votes: {total_row} \n \
--------------------\n \
Khan: {round((khan/total_row)*100,3)}% {khan} \n \
Correy: {round((correy/total_row)*100,3)}% {correy} \n \
Li: {round((li/total_row)*100,3)}% {li} \n \
O'Tooley: {round((tooley/total_row)*100,3)}% {tooley} \n \
--------------------\n \
Winner: {winner} \n \
--------------------")
    file.close()