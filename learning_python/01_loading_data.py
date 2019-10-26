

#the question I wrote down for this task is:
#How tdo I load bike share data from the following sources,
#.csv
#.xlsx
#website

#I found a nice dataset of capital bikeshare data with weather and holiday patterns, so I'll start with that.
#also I forgot to mention that I'm going to learn everything in Python 3 because 2 will be unmaintained come 2020..
#unzip the dataset, I found a nice explaination here: https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/#targetText=To%20unzip%20it%20first%20create,()%20on%20that%20object%20i.e.&targetText=It%20will%20extract%20all%20the%20files%20in%20zip%20at%20current,it%20will%20overwrite%20those%20files.
import os
from zipfile import ZipFile

try:
    # Change the current working Directory
    os.chdir("C:/Users/dpatterson/code/Impact_of_weather_on_ridership/learning_python/data")
    print("Directory changed")
except OSError:
    print("Can't change the Current Working Directory")

#write a file: https://www.geeksforgeeks.org/reading-writing-text-files-python/
try:
    file = open("testfile.txt", "w")
    text = "Learning Python Using Bikeshare Data. 10-24-2019"
    file.write(text)
    print("text recorded. Hooray.")
except:
    print("what happened?!")

try:
    contents = os.listdir() # returns list
    print(contents)
    print("Perfecto.")
except OSError:
    print("Error bud..")

#awesome, now lots write the dataset to the folder

def main():
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('C:/Users/dpatterson/Downloads/Bike-Sharing-Dataset.zip') as zipObj:
       # Extract all the contents of zip file in different directory
       os.chdir("C:/Users/dpatterson/code/Impact_of_weather_on_ridership/learning_python/data")
       zipObj.extractall()

       print('Extract single file from ZIP')


if __name__ == '__main__':
   main()

try:
    contents = os.listdir() # returns list
    print(contents)
    print("Perfecto.")
except OSError:
    print("Error bud..")



#let use csv.reader(csvfile, dialect='excel', **fmtparams) to read csvs
#https://docs.python.org/3.5/library/csv.html#csv.reader

import csv
with open('day.csv', newline='') as csvfile:
     days = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in days:
         print(', '.join(row))

with open('hours.csv', newline='') as openhours:
     hours = csv.reader(openhours, delimiter=' ', quotechar='|')
     for row in hours:
         print(', '.join(row))

#but this doesn't seem to be helpful.... pandas?

import pandas as pd
days = pd.read_csv("day.csv")
print(days) #that was much easier...
hours = pd.read_csv("hour.csv")
#onto the next one

##### read x;sx, but to read we need to write
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
try:
    with pd.ExcelWriter('bikeshare_data.xlsx') as writer:
        days.to_excel(writer, sheet_name='days')
        hours.to_excel(writer, sheet_name='hours')
    print('written')
except:
    print('Something is missing')

try:
    contents = os.listdir() # returns list
    print(contents)
    print("Perfecto.")
except OSError:
    print("Error bud..")


xl = pd.ExcelFile('bikeshare_data.xlsx')
print(xl.sheet_names)
days = xl.parse('days')
hours = xl.parse('hours')
#Hooray


#############Get from website
hours = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/hour.csv')
days = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/day.csv')
#cool, simple but cool. I know real life problems will be more difficult, but this is all I need for confidence right now.
# likely going to be issues later on with json data needing to be flattened, and extracted specific tables from html sites... o well


#
