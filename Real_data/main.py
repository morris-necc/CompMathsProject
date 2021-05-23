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
def get_column(purpose, frequency_enabled = False):
    while True:
        column = input("Enter which column "+ purpose +": ")
        if column not in columns:
            if frequency_enabled and column == "frequency":
                break
            print("That is not a valid column!")
        else:
            break
    return column

def get_graph_type():
    while True:
        print("============GRAPH MENU============")
        print("1. Histogram")
        print("2. Bar Graph")
        print("3. Scatter plot")
        print("4. Back")
        choice = int(input("Enter your choice(1-4): ")) #don't forget to do a check for data type (rn it crashes if you input string)
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

def visualize_bar(x, y, data):
    #show just the first 1000 unique values
    over_limit = False
    uniques = data[x].unique().tolist()
    if len(uniques) >= 100: #too many uniques
        print("There are too many unique values! X-axis shortened to 100 values to reduce crashes")
        over_limit = True
    if y == "frequency":
        frequency_count = data[x].value_counts()[:101] if over_limit else data[x].value_counts()
        uniques = frequency_count.index.tolist()
        plt.bar(uniques, frequency_count)
        plt.xlabel(x)
        plt.ylabel("Frequency")
        plt.show()
    else:
        if type(data[y][0]) == str:
            print("You cannot create a bar graph using non-numeric y-values")
        else:
            #how do you deal with duplicate x-values e.g. 2 people from india having a different number of animes_completed
            if(len(uniques) != len(data)):
                print("There are duplicate values that may conflict with each other")
            else:
                temp_data = data.sort_values(by=[y], ascending=False)
                y_values = temp_data[y][:101] if over_limit else temp_data[y]
                x_values = temp_data[x][:101] if over_limit else temp_data[x]
                plt.bar(x_values, y_values)
                plt.xlabel(x)
                plt.ylabel(y)
                plt.show()

def visualize_scatter(x, y, data):
    #both x and y have to be numbers
    if type(data[x][0]) == str or type(data[y][0]) == str:
        print(type(data[x][0]))
        print(type(data[y][0]))
        print("You can't create a scatter plot with non-numerical values")
    else:
        plt.scatter(data[x], data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

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
        if graph_type == 1: #hist
            column = get_column("to make into a histogram")
            visualize_hist(column, data)
        elif graph_type == 2: #bar
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis(you can write 'frequency')", True)
            visualize_bar(x, y, data)
        elif graph_type == 3: #scatter
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis")
            visualize_scatter(x, y, data)
    elif choice == 3:
        #inferential statistics part
        #idea to compare
        #check p-value
        #check manually (loop through the list, make a new list where every value is True/False, then check percentage of True)
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
