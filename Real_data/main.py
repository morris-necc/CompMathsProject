import os
import sys
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

max = 0
while(max<=0):
    max = int(input("How many people do you want to send the survey to: "))
    if(max<=0):
        print("You must input a number greater than 0!")
x = np.random.randint(1, max)  # randomized sample size
anime_num_list = np.random.randint(200, 576, size=10000) #changed to this from 1-1001 due to it generating a large std and an unrealistic mean

print(f"The survey is sent to {max} people")
print(f"This is the number of people who answered: {x}")

mean = np.mean(anime_num_list)
std = np.std(anime_num_list)

new_data = sp.stats.norm(mean, std).rvs(x) #generates float (try find a way to make it genereate int instead if possible)
domain = np.linspace(np.min(new_data), np.max(new_data))

mean = np.mean(new_data)
std = np.std(new_data)
median = np.median(new_data)
mode = stats.mode(new_data).mode[0]
var = np.var(new_data)


print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}") #because new data consists of float, mode is most likely float
print(f"Standard deviation = {std}")
print(f"Variance = {var}")
print(f"Skew = {stats.skew(new_data)}")


n, bins, patches = plt.hist(new_data, bins= 20, edgecolor='red') #histogram for the total list answer
plt.xlabel("Number of anime")
plt.ylabel("Frequency")
plt.title("Anime")
plt.show()



#inferential statistics
# print(stats.zscore(anime_num_list))
# plt.hist(stats.zscore(anime_num_list), bins = 20)
anime_num = int(input("How many anime that you watch: "))
zscore = (anime_num - mean)/std
print(zscore)

plt.plot(domain, norm.pdf(domain, mean, std), label='$\mathcal{N}$ ' + f'$( \mu \\approx {round(mean)} , \sigma \\approx {round(std)} )$')
n, bins, patches = plt.hist(new_data, bins= 20, edgecolor='red', density = True) #histogram for the total list answer
plt.xlabel("Number of anime")
plt.ylabel("Frequency")
plt.title("Density Histogram")
plt.legend()
plt.show()



# anime_time = int(input("how many list for the time: "))


