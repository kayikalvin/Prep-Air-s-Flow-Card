# Prep-Air-s-Flow-Card

January 03, 2024
Created by: Carl Allchin

Welcome to a New Year of Preppin' Data challenges. For anyone new to the challenges then let us give you an overview how the weekly challenge works. 
Each Wednesday the Preppin' crew (Jenny, myself or a guest contributor) drop a data set(s) that requires some reshaping and/or cleaning to get it ready for analysis. 
You can use any tool or language you want to do the reshaping (we build the challenges in Tableau Prep but love seeing different tools being learnt / tried).
Share your solution on LinkedIn, Twitter/X, GitHub or the Tableau Forums
Fill out our tracker so you can monitor your progress and involvement
The following Tuesday we will post a written solution in Tableau Prep (thanks Tom) and a video walkthrough too (thanks Jenny)
As with each January for the last few years, we'll set a number of challenges aimed at beginners. This is a great way to learn a number of fundamental data preparation skills or a chance to learn a new tool — New Year's resolution anyone? So on to this year's challenges!
Context
At Preppin' Data we use a number of (mock) companies to look at the challenges they have with their data. For January, we're going to focus on our own airline, Prep Air. The airline has introduced a new loyalty card called the Flow Card. We need to clean up a number of data sets to determine how well the card is doing. 

The first task is setting some context for later weeks by understanding how popular the Flow Card is. Our stakeholder would like two data sets about our passengers. One data set for card users and one data set for those who don't use the card. 
Input
There is one input file. You can download it from here.


Requirements
Input the data
Split the Flight Details field to form:
Date 
Flight Number
From
To
Class
Price
Convert the following data fields to the correct data types:
Date to a date format
Price to a decimal value
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

Output 1

Rows: 1883 (1884 including the header)

Output 2


Rows: 1895 (1896 including the header)

You can download the output from here.

After you finish the challenge make sure to fill in the participation tracker, then share your solution on Twitter using #PreppinData and tagging @Datajedininja, @JennyMartinDS14 & @TomProwse1
