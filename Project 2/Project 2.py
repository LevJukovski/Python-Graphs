#Imports:
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

#Style of plots:
style.use("fivethirtyeight")

#Reading data from the files
data1 = pd.read_csv("One star michelin restaurants.csv")
data2 = pd.read_csv("Two stars michelin restaurants.csv")
data3 = pd.read_csv("Three stars michelin restaurants.csv")

#Merging data1, data2, and data3 into "data":
pre_data = pd.merge(data1, data2, on="name", how="outer")
data = pd.merge(pre_data, data3, on="name", how="outer")
data.set_index("name", inplace=True)
data["cuisine"] = data["cuisine"].replace(["French contemporary"],"Fr. con")

#Creating Series:
cuisine_eastern = data.groupby("cuisine")["longitude"].max()
cuisine_eastern.sort_values(axis=0, inplace=True)
cuisine_western = data.groupby("cuisine")["longitude"].min()
cuisine_western.sort_values(axis=0, inplace=True)

#Converting Series to dataframes:
cuisine_eastern = cuisine_eastern.to_frame()
cuisine_eastern.reset_index(level=0, inplace=True)

cuisine_western = cuisine_western.to_frame()
cuisine_western.reset_index(level=0, inplace=True)

#Making x and y axes:
x1 = list(cuisine_eastern.cuisine)
for i, c in enumerate(x1):
    short_cuisine = c[:6] + "."
    x1[i] = short_cuisine
y1 = list(cuisine_eastern.longitude)
for i, c in enumerate(y1):
    short_longitude = str(c)[:6] + "     "
    y1[i] = short_longitude
x2 = list(cuisine_western.cuisine)
for i, c in enumerate(x2):
    short_cuisine = c[:6] + "."
    x2[i] = short_cuisine
y2 = list(cuisine_western.longitude)
for i, c in enumerate(y2):
    short_longitude = str(c)[:6] + "     "
    y2[i] = short_longitude

#Creating multiple windows, defining and adjusting the plots:
def add_value_label(x,y):
    for i in range(1, len(x)+1):
        plt.text(i,y[i-1],y[i-1],  ha="right")

plt.figure(1)
plt.scatter(x1, y1, c="black", marker=".", s=50)
add_value_label(x1,y1)
plt.suptitle("Longitude of easternmost Michelin restaurant by cuisine type:\n(Relevant for 2019)", fontsize=30)
plt.xlabel('Cuisine', fontsize=20, color="black")
plt.ylabel('Longitude', fontsize=20, color="black")

plt.figure(2)
plt.scatter(x2, y2, c="black", marker=".", s=50)
add_value_label(x2, y2)
plt.suptitle('Longitude of westernmost Michelin restaurant by cuisine type:\n(Relevant for 2019)', fontsize=30)
plt.xlabel('Cuisine', fontsize=20, color="black")
plt.ylabel('Longitude', fontsize=20, color="black")

#Opening the windows:
plt.show()