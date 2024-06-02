# Prep-Air-s-Flow-Card

### Context
At Preppin' Data we use a number of (mock) companies to look at the challenges they have with their data. For January, we're going to focus on our own airline, Prep Air. The airline has introduced a new loyalty card called the Flow Card. We need to clean up a number of data sets to determine how well the card is doing. 

The first task is setting some context for later weeks by understanding how popular the Flow Card is. Our stakeholder would like two data sets about our passengers. One data set for card users and one data set for those who don't use the card. 
Input
There is one input file. You can download it from here [Prep Air's Flow Card Data](https://drive.google.com/file/d/1STVYZvXzfGMuEq9Yq3yYOmCDCFq4iB0Z/view)



### Requirements
Input the data
Split the Flight Details field to form:
   1. Date 
   2. Flight Number
   3. From
   4. To
   5. Class
   6. Price
### Convert the following data fields to the correct data types:
 1. Date to a date format
 2. Price to a decimal value
Change the Flow Card field to Yes / No values instead of 1 / 0
Create two tables, one for Flow Card holders and one for non-Flow Card holders
Output the data sets
Output
Both outputs have the same data structure:

9 data fields:
Date
Flight Number
From
To
Class
Price
Flow Card?
Bags Checked
Meal Type

