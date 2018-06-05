# Import CSV file
import os
import pandas as pd
file_one = os.path.join('raw_data', 'employee_data1.csv')
file_one_df = pd.read_csv(file_one, encoding = 'ISO-8859-1')
print(file_one_df.head())
# Turn the Name column into 2 columns, using ' ' as a delimeter
file_one_df[['First Name','Last Name']] = file_one_df['Name'].str.split(' ',expand=True)
# Drop the name column
file_one_df = file_one_df.drop(['Name'], axis=1)

# Turn month, day and year into 3 columns, using '-' as a delimter
file_one_df[['Year','Month', 'Day']] = file_one_df['DOB'].str.split('-',expand=True)
# 'mm/dd/yyyy'
file_one_df['DOB'] = file_one_df['Month'] +"/" + file_one_df['Day'] + "/" + file_one_df['Year']
# drop other columns
file_one_df = file_one_df.drop(['Month'], axis=1)
file_one_df = file_one_df.drop(['Day'], axis=1)
file_one_df = file_one_df.drop(['Year'], axis=1)

# Overwrite SSN column
file_one_df['SSN'] = "***-**-" + file_one_df['SSN'].str[7:]


# Replace the states with their abbreviations using dictionary
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

#Print to Console
print(file_one_df.head())
