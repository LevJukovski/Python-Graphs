#Imports:
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

#Reading data from the file:
data = pd.read_csv("Demographics of China.csv")

#Taking specific data from specific rows, crating labels:
pop_percent_in_1955 = data.iloc[-1]["Country's Share of World Pop"]
pie_1955 = [100 - pop_percent_in_1955, pop_percent_in_1955]
pop_percent_in_2020 = data.iloc[0]["Country's Share of World Pop"]
pie_2020 = [100 - pop_percent_in_2020, pop_percent_in_2020]
place = ["Rest of the world", "China"]

#Creating multiple windows, defining and adjusting the plots:
plt.figure(1)
plt.title("China's share of world's population in 1955", fontsize=20)
explode = [0, 0.1]
plt.pie(pie_1955, labels=place, autopct="%.2f%%", explode=explode)
plt.tight_layout()

plt.figure(2)
plt.title("China's share of world's population in 2020", fontsize=20)
explode = [0, 0.1]
plt.pie(pie_2020, labels=place, autopct="%.2f%%", explode=explode)
plt.tight_layout()

#Opening the windows:
plt.show()