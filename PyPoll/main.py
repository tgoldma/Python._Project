import os
import csv

csvpath = os.path.join("election_data.csv")
myList = list(csv.reader(open('election_data.csv')))

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    votes = 0
    candidates = {}
    winner = ''
    winningvotes = 0
    
    csv_header = next(csvreader)
    for row in csvreader:
        votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] = candidates[row[2]]+1

    for c in candidates:
        percentage = round((candidates[c]/votes)*100,3)
        if candidates[c]>winningvotes:
            winningvotes = candidates[c]
            winner = c
    
output_file = os.path.join("output.txt")
with open(output_file, 'w') as textfile:
	    print("Election Results")
	    textfile.write("Election Results \n")
	    print("-------------------------")
	    textfile.write("------------------------- \n")
	    print(f"Total Votes: {str(votes)}")
	    textfile.write(f"Total Votes: {str(votes)}"+"\n")
	    print("-------------------------")
	    textfile.write("------------------------- \n")
	    for c in candidates:
	        percentage = round((candidates[c]/votes)*100,3)
	        print(f"{c}: {str(percentage)}% ({str(candidates[c])})")
	        textfile.write(f"{c}: {str(percentage)}% ({str(candidates[c])}) \n")
	        if candidates[c] > winningvotes:
	            winningvotes = candidates[c]
	            winner = c
	    print("-------------------------")
	    textfile.write("-------------------------"+"\n")
	    print(f"Winner: {winner}")
	    textfile.write(f"Winner: {winner} \n")
	    print("-------------------------")
	    textfile.write("-------------------------"+"\n")