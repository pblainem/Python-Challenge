# Import CSV file
import os
import pandas as pd
file_one = os.path.join('raw_data', 'election_data_1.csv')
file_one_df = pd.read_csv(file_one, encoding = 'ISO-8859-1')
print(file_one_df.head())

# Total # of votes
total_rows = file_one_df['Voter ID'].count()
print(str(total_rows))
# RowCount - 1

# Create a dictionary or an array w/ the name of each candidate
# Loop through each row, counting each vote by adding one to that candidate's count


# Percentage of vote each candidate received = their count over total


# Winner = candidate with most votes



# Export to txt file


# Print to terminal


#pandas.pydata.org