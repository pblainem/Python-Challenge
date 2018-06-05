# Import CSV file
import os
import pandas as pd
file_one = os.path.join('raw_data', 'election_data_1.csv')
file_one_df = pd.read_csv(file_one, encoding = 'ISO-8859-1')

# Total # of votes
total_rows = file_one_df['Voter ID'].count()

# Count how many votes each candidate received
canVotes = file_one_df['Candidate'].value_counts()

# Percentage of vote each candidate received = their count over total
canVotesPerc = canVotes / total_rows *100
canVotes_df = canVotes.to_frame()
canVotes2_df = canVotesPerc.to_frame()
canVotes2_df['Total Votes'] = canVotes_df

canVotes2_df = canVotes2_df.rename(columns={'Candidate': 'Percent'})



Winner = canVotes2_df['Percent'].idxmax()

canVotes2_df['Percent'] = canVotes2_df['Percent'].map('{:,.1f}%'.format)
canVotes2_df['Total Votes'] = canVotes2_df['Total Votes'].map('({:.0f})'.format)


# Print to terminal
outp = "\n\nElection Results \n-------------------------"
outp = outp + "\nTotal Votes: " + str(total_rows)
outp = outp + "\n-------------------------\n"
outp = outp + str(canVotes2_df)
outp = outp + "\n-------------------------\nWinner: " + Winner
print(outp)


# Export to txt file
output_file_path = os.path.join('outputFile', 'output.txt')

text_file = open(output_file_path, "w")
text_file.write(outp)
text_file.close()
