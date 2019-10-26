

import csv
import pandas as import pd


hours = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/hour.csv')
days = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/day.csv')

hours.head()
days.head()

#Questions
#How can I access specific data within my data set?
season = days['season']
season = season.assign(hires = 1)
season.head()

season = days[['season', 'yr']] #double brackets if selecting multiple columns
season = season.assign(hires = 1)
season.head()

#Rows
season = days[1:6]

#Describe what 0-based indexing is. #first row in 0, not 1. slice from -1 to grab all in slice
#Note: Let’s remind ourselves that Python uses 0-based indexing. This means that the first element in an object is located at position 0
# This is different from other tools like R and Matlab that index elements within objects starting at 1.

#to create a refrence using '='. This does not create a fresh new object, instead creates a refrence to it... importantly
#if something is deleted from all_days, it's actually being deleted from days...
all_days = days
seasons = all_days[0:3]

#to create a new object we use the copy method
true_copy_days = days.copy()
seasons = true_copy_days[1:3]

#Manipulate and extract data using column headings and index locations.
#Employ slicing to select sets of data from a DataFrame.
#rows and columns
#loc is primarily label based indexing. Integers may be used but they are interpreted as a label.
#iloc is primarily integer based indexing
#https://www.ritchieng.com/'pandas-selecting-multiple-rows-and-columns/
#Employ label and integer-based indexing to select ranges of data in a dataframe.
season = days.loc[[0,1,4,6], ['season', 'yr']]
season = days.loc[[0,1,4,6], 'season']
season = days.loc[[0, 10, 600], :] # in this case ':' stands for all and can be used in place of rows or columns
season = days.iloc[:, 3] #this is more akin to R in that it uses numbers to index columns as in thier relative position left to right


#Reassign values within subsets of a DataFrame.

Create a copy of a DataFrame.
#Query / select a subset of data using a set of criteria using the following operators: =, !=, >, <, >=, <=.
season = days[days.yr > 1]
season = days[(days.yr > 1) & (days.workingday == 1)] #notice the use of ==, and parenthasis to seperate and statments
#pretty straight forward, in the future time will be valueable to extract

#Locate subsets of data using masks.
#A mask can be useful to locate where a particular subset of values exist or don’t exist - for example, NaN, or “Not a Number” values. To understand masks, we also need to understand BOOLEAN objects in Python.
#Describe BOOLEAN objects in Python and manipulate data using BOOLEANs.
#Boolean values include True or False. For example,
# Set x to 5
x = 5
# What does the code below return?
x > 5
# How about this?
x == 5
#this could be more nueancy that, but gets the point across.

#null
pd.isnull(days)
nulls = days[pd.isnull(days['season'])]['yr']
print(nulls)#non
#will need to learn to omit nas, or dedect spikes
