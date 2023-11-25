#Imports:
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

#Style of plots:
style.use("ggplot")

#Reading data from the file:
data = pd.read_excel("Used Car Prices In Poland (January 2022).xlsx", engine="openpyxl")

#Creating Series:
car_price_by_year = data.groupby("year")["price"].mean()
car_price_by_province = data.groupby("province")["price"].mean()
car_price_by_province = car_price_by_province.drop("(", axis=0)

#Converting Series to dataframes:
car_price_by_year = car_price_by_year.to_frame()
car_price_by_year.reset_index(level=0, inplace=True)
car_price_by_year = car_price_by_year[28:]

car_price_by_province = car_price_by_province.to_frame()
car_price_by_province.reset_index(level=0, inplace=True)

#Making x and y axes:
x1 = list(car_price_by_year.year)
y1 = list(car_price_by_year.price)
x2 = list(car_price_by_province.province)
for i, p in enumerate(x2):
    short_province = p[:4] + "."
    x2[i] = short_province
y2 = list(car_price_by_province.price)

#Creating multiple windows, defining and adjusting the plots:
plt.figure(1)
plt.scatter(x1, y1, c="black", marker=".", s=50)
plt.plot(x1, y1, c="black")
plt.title("Average price of used cars by the car's year of production (2022)\nData includes cars produced between 1997 - 2022", fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Price', fontsize=20)
plt.ylim(0, 225000)
plt.grid(axis="x")

plt.figure(2)
plt.bar(x2, y2, width=0.6, color="blue")
plt.title('Average price of used cars by province (2022)\nData includes cars from all polish provinces', fontsize=20)
plt.xlabel('Province', fontsize=20)
plt.ylabel('Price', fontsize=20)
plt.ylim(0, 120000)
plt.grid(axis="x")

#Opening the windows:
plt.show()