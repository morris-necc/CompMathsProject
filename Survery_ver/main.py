import os
import sys
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

#import dataset
file_name = "users_cleaned.csv"
file_dir = os.path.join(sys.path[0], file_name)
data = pd.read_csv(file_dir, delimiter = ',')
columns = list(data.columns)

#initialize variable
quit = False

#menu functions
def get_column(purpose):
    while True:
        column = input("\n\nEnter which column "+ purpose +": ")
        if column not in columns:
            print("That is not a valid column!")
        else:
            break
    return column

def get_graph_type():
    while True:
        print("============GRAPH MENU============")
        print("1. Histogram")
        print("2. Bar Graph")
        print("3. Line Graph")
        print("4. Scatter plot")
        choice = int(input("Enter your choice(1-4):")) #don't forget to do a check for data type (rn it crashes if you input string)
        if choice < 1 or choice > 4:
            print("That is not a valid choice!")
        else:
            break
    return choice

def visualize_hist(column, data):
    column_data = data[column]
    if(type(column_data[0]) == str):
        print("You cannot create a histogram from this column!")
    else:
        bins = int(input("How many bins do you want: "))
        n, bins, patches = plt.hist(column_data, bins=bins, edgecolor='black') #histogram for the total list answer
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

def visualize_bar(column, data):
    pass

def visualize_line(x, y, data):
    pass

def visualize_scatter(x, y, data):
    pass

while not quit:
    print("============MAIN MENU============")
    print("Column names: ", end="")
    for column in columns[:-1]:
        print(column, end=", ")
    print(columns[-1])
    print("1. Describe column")
    print("2. Generate Graph")
    print("3. Compare new value")
    print("4. Quit")
    while True:
        choice = int(input("Enter your choice here: "))
        if choice < 1 or choice > 4:
            print("That is not a valid choice!")
        else:
            break
    if choice == 1:
        column = get_column("to describe")
        print("============DESCRIPTION============")
        description = data[column].describe()
        print(description, end="\n\n")
    elif choice == 2:
        graph_type = get_graph_type()
        if graph_type == 1:
            column = get_column("to make into a histogram")
            visualize_hist(column, data)
        elif graph_type == 2:
            column = get_column("to make into a bar graph")
            visualize_bar(column, data)
        elif graph_type == 3:
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis")
            visualize_line(x, y, data)
        else:
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis")
            visualize_scatter(x, y, data)
    elif choice == 3:
        pass
    else:
        quit = True


#inferential statistics
# anime_num = int(input("How many anime that you watch: "))
# zscore = (anime_num - mean)/std
# print(zscore)
    
#check data type of column
# column_data = data[column]
# if string bar graph
# if numbers histogram
