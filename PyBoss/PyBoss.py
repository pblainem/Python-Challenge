# Import CSV file
import os
import pandas as pd
file_one = os.path.join('raw_data', 'employee_data1.csv')
file_one_df = pd.read_csv(file_one, encoding = 'ISO-8859-1')
print(file_one_df.head())
# Turn the Name column into 2 columns, using ' ' as a delimeter
# Create column 'First Name' containing the first word
# Create a column 'Last Name' containing the second word
file_one_df[['First Name','Last Name']] = file_one_df['Name'].str.split(' ',expand=True)
# Drop the name column
file_one_df = file_one_df.drop(['Name'], axis=1)

# Turn month, day and year into 3 columns, using '-' as a delimter
file_one_df[['Year','Month', 'Day']] = file_one_df['DOB'].str.split('-',expand=True)
# Create a new column out of the 3 columns in the order month, day, year in the format:
# file_one_df = file_one_df.drop(['DOB'], axis=1)


# 'mm/dd/yyyy'
file_one_df['DOB'] = file_one_df['Month'] +"/" + file_one_df['Day'] + "/" + file_one_df['Year']
# drop other columns
file_one_df = file_one_df.drop(['Month'], axis=1)
file_one_df = file_one_df.drop(['Day'], axis=1)
file_one_df = file_one_df.drop(['Year'], axis=1)


# Turn SSN into 3 columns, using '-' as a delimiter
# Overwrite the first 2 columns with "***" and "**" respectively
# Combine again into one column with "-" in between each
# Really you don't need the first 2 columns

file_one_df['SSN'] = "***-**-" + file_one_df['SSN'].str[7:]


# Convert the states to their abbreviations
# Can I import a CSV, to basically be used as a dictionary, to look up the state abbreviations
# Loop through each row, converting the state to its abbreviation 

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

file_one_df['State'] = file_one_df['State'].replace(us_state_abbrev)

print(file_one_df.head())
