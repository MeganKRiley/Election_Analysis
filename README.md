# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has asked for an election audit to be completed for a recent local congressional election.

## Resources
Data Source: election_results.csv
Software: Python 3.7.6, Visual Studio Code 1.60.2

## Election Analysis

- There were **369,711** votes cast in this congressional election
```
    for row in reader:
        total_votes = total_votes + 1
```

- The full list of counties in this precinct and their voter turnout
    - **Jefferson**: 10.5% of the votes with 38,855 total votes
    - **Denver**: 82.8% of the votes with 306,055 total votes
    - **Arapahoe**: 6.7% of the votes with 24,801 total votes

- The county with the largest number of votes was:
    - **Denver, which accounted for 82.8% of the votes with 306,055 total votes**
```
        if (cvotes > highest_turnout_count) and (countyvote_percentage > highest_turnout_percentage):
            highest_turnout_count = cvotes
            highest_turnout_county = county_name
            highest_turnout_percentage = countyvote_percentage    
```

- The full list of candidates and their results
    - **Charles Casper Stockham** 23.0% of the votes with 85,213 total votes
    - **Diana Degette** 73.8% of the votes with 272,892 total votes
    - **Raymon Anthony Doane** 3.1% of the votes with 11,606 total votes
```
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
```        

- The winner of the election was: 
    - **Diana Degette, who received 73.8% of the votes and 272,892 total votes**      

### Summary
This python script has the capability to be used for any election.  The script does not have any hard rules based on candidate names or county names, it's just referencing specific rows of joined data, meaning that there are very few modifications that would need to be made to make it work for other elections.  As you can see in the below code, file_to_load and file_to_save create a path to very specific resources, so the first thing that would need to be done to make this work for a different election would be to change those paths to match the current data we want run. This would allow the script to load the correct data in the functions, and output results into the desired location.  The file_to_load is the document that lists the raw results.  It will be important to review this file, and clean if necessary. There are currently two variables in the script that reference the file_to_load document, they are candidate_name and county_name.  It's important to double check which row these appear on the document because the script references them based on which row they appear in.  The data will either need to be modified to match the code or the code will need to be updated to reflect the document.  Once these fields match the script should be ready to run. There are countless items that can be added to the script to perform other desired functions, but to just run for the current results, these two changes will make the script usable for any election. 

```
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
```
candidate_name = row[2]
county_name = row[1]
```
