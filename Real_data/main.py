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
    #Let's users choose between several graph types, returns an integer
    while True:
        print("============GRAPH MENU============")
        print("1. Histogram")
        print("2. Bar Graph")
        print("3. Scatter plot")
        print("4. Back")
        choice = int(input("Enter your choice(1-4): "))
        if choice < 1 or choice > 4:
            print("That is not a valid choice!")
        else:
            break
    return choice

def visualize_hist(column, data):
    #Creates a histogram based on a column the user has specified
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
    #Creates a bar graph based on the columns the user has specified
    #Shows just the first 100 unique values
    over_limit = False
    uniques = data[x].unique().tolist()
    if len(uniques) >= 100: 
        #Shortens x-axis if there are too many unique values
        print("There are too many unique values! X-axis shortened to 100 values to reduce crashes")
        over_limit = True
    if y == "frequency":
        #Plots a bar graph based on frequency as the y-axis
        frequency_count = data[x].value_counts()[:101] if over_limit else data[x].value_counts()
        uniques = frequency_count.index.tolist()
        plt.bar(uniques, frequency_count)
        plt.xlabel(x)
        plt.ylabel("Frequency")
        plt.show()
    else:
        #If the user inputs a column for y, checks if the data is string
        if type(data[y][0]) == str:
            print("You cannot create a bar graph using non-numeric y-values")
        else:
            #Deals with duplicate x-values e.g. 2 people from india having a different number of animes_completed
            if(len(uniques) != len(data)):
                print("There are duplicate values that may conflict with each other")
            else:
                #plots the bar graph using user-specified x and y data
                temp_data = data.sort_values(by=[y], ascending=False)
                y_values = temp_data[y][:101] if over_limit else temp_data[y]
                x_values = temp_data[x][:101] if over_limit else temp_data[x]
                plt.bar(x_values, y_values)
                plt.xlabel(x)
                plt.ylabel(y)
                plt.show()

def correlation_strength(x, y, r):
    #Returns an association description based on the pearson correlation coefficient
    if 0.1 <= abs(r) < 0.3:
        description = "small "
    elif 0.3 <= abs(r) < 0.5:
        description = "medium "
    elif 0.5 <= abs(r) <= 1:
        description = "large "
    description += "positive" if r > 0 else "negative"
    return f"{x} and {y} have a {description} association"

def visualize_scatter(x, y, data, pearson):
    #creates a scatter plot, with an optional pearson boolean to display the correlation between x and y
    if type(data[x][0]) == str or type(data[y][0]) == str:
        #both x and y have to be numbers
        print(type(data[x][0]))
        print(type(data[y][0]))
        print("You can't create a scatter plot with non-numerical values")
    else:
        #if x and y are numbers, create scatter plot
        plt.scatter(data[x], data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        if(pearson):
            #Tells the user the pearson coefficient between the 2 columns based on the pearson coefficient
            r, _ = stats.pearsonr(data[x], data[y])
            plt.title('Pearson Correlation Coefficient $r=$'+np.array2string(r))
            print(correlation_strength(x, y, r))
        plt.show()

while not quit:
    #Main menu
    print("============MAIN MENU============")
    print("Column names: ", end="")
    for column in columns[:-1]:
        print(column, end=", ")
    print(columns[-1])
    print("1. Describe column")
    print("2. Generate Graph")
    print("3. Pearson's Correlation Coefficient")
    print("4. Quit")
    while True:
        #Repeats until user enters a choice between 1 to 4
        choice = int(input("Enter your choice here: "))
        if choice < 1 or choice > 4:
            print("That is not a valid choice!")
        else:
            break
    if choice == 1:
        #Prints description of specified column based on scipy's describe() function
        column = get_column("to describe")
        print("============DESCRIPTION============")
        description = data[column].describe()
        print(description, end="\n\n")
    elif choice == 2:
        #graph type is returned to the variable graph_type
        graph_type = get_graph_type()
        if graph_type == 1: #histogram
            column = get_column("to make into a histogram")
            visualize_hist(column, data)
        elif graph_type == 2: #bar
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis(you can write 'frequency')", True)
            visualize_bar(x, y, data)
        elif graph_type == 3: #scatter
            x = get_column("to be used as the x-axis")
            y = get_column("to be used as the y-axis")
            visualize_scatter(x, y, data, False) #No pearson correlation
    elif choice == 3:
        #Generate a scatter graph with a pearson correlation value
        x = get_column("to be used as the x-axis for comparison")
        y = get_column("to be used as the y-axis for comparison")
        visualize_scatter(x, y, data, True) #With pearson correlation
        pass
    else:
        quit = True