# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w") 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Counties in the Election Header
     txt_file.write("Counties in the Election\n")

     # Create Divider between header and text
     txt_file.write("--------------------------\n")

     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")

# 1. Initialize a total vote counter. 
total_votes = 0

# Open the election results and read the file
candidate_options = []
     
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)   

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count. 
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

    # Print the candidate list.
    print(candidate_options)