### Requirements
# 1. Input the data
# 2. Split the Flight Details field to form:
#    1. Date 
#    2. Flight Number
#    3. From
#    4. To
#    5. Class
#    6. Price
# 3. Convert the following data fields to the correct data types:
#      1. Date to a date format
#      2. Price to a decimal value
# 4. Change the Flow Card field to Yes / No values instead of 1 / 0
# 5. Create two tables, one for Flow Card holders and one for non-Flow Card holders
# 6. Output the data sets
# 7. Output
#    Both outputs have the same data structure:

# 9 data fields:
# Date
# Flight Number
# From
# To
# Class
# Price
# Flow Card?
# Bags Checked
# Meal Type

import pandas as pd

df = pd.read_csv(r"C:\Users\ALVIN KAYI\Desktop\python_data_analysis\projects\Prep Air's Flow Card\Data\PD 2024 Wk 1 Input.csv")
df

df.info()

# Split the Flight Details field to form:
#    1. Date 
#    2. Flight Number
#    3. From
#    4. To
#    5. Class
#    6. Price

df.head()

df['Flight Details'] = df['Flight Details'].astype(pd.StringDtype())

df.dtypes

# Assuming df['Flight Details'] contains strings that you want to split by '//'
# and you want to extract the first part.

# Split the string by '//'
split_strings = df['Flight Details'].str.split('//')

# Access the first part of each split result
df['Date'] = split_strings.str[0]

# Display the 'Date' column
df['Date']



df.head()

columns = ['Date ', 'Flight Number','From','To','Class','Price','Flow Card?','Bags Checked','Meal Type']
table = pd.DataFrame(columns=columns)

table

table['Date']= df['Flight Details'].str.split('//').str[0]
table['Flight Number'] = df['Flight Details'].str.split('//').str[1]
table['Class'] = df['Flight Details'].str.split('//').str[3]
table['Price'] = df['Flight Details'].str.split('//').str[4]

place = df['Flight Details'].str.split('//').str[2]
table['From'] = place.str.split('-').str[0]
table['To'] = place.str.split('-').str[1]

table['Date']= df['Flight Details'].str.split('//').str[0]

table.drop(table.columns[0], axis=1, inplace=True)

table

# fill the rest of the table
table['Flow Card?'] = df['Flow Card?']
table['Bags Checked'] = df['Bags Checked']
table['Meal Type'] = df['Meal Type']
table

# Convert the following data fields to the correct data types:
#      1. Date to a date format
#      2. Price to a decimal value

table['Date'] = pd.to_datetime(table['Date'])

table['Price'] = pd.to_numeric(table['Price'],errors='coerce')
table['Price'].dtypes


## Change the Flow Card field to Yes / No values instead of 1 / 0

change = {
    1:'Yes',
    0:'No'
}
table['Flow Card?'] = table['Flow Card?'].map(change)

table['Flow Card?']

## Create two tables, one for Flow Card holders and one for non-Flow Card holders

# flow card holders
flow_card_holders = table[table['Flow Card?'] == 'Yes']
flow_card_holders.reset_index(drop = True,inplace=True)

#non_flowcard_holders
non_flow_card_holders = table[table['Flow Card?'] == 'No']
non_flow_card_holders.reset_index(drop = True,inplace=True)
non_flow_card_holders























































