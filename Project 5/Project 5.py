#Imports:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Reading data from the file:
data = pd.read_csv("Insurance.csv")

#Extracting the needed information:
data = data.loc[(data["smoker"] == "no")]
age = np.array([data.iloc[:]["age"]]).reshape(-1,1)
charges = np.array([data.iloc[:]["charges"]]).reshape(-1,1)

model = LinearRegression()
model.fit(age, charges)


#Creating a window and making the graph:
plt.scatter(age, charges)
plt.plot(np.linspace(18, 64, 100).reshape(-1, 1), model.predict(np.linspace(18, 64, 100).reshape(-1, 1)), "r")
plt.suptitle('Yearly insurance charges for non smokers (18-64):', fontsize=30)
plt.xlabel('Age', fontsize=20, color="black")
plt.ylabel('Charges', fontsize=20, color="black")
plt.ylim(0, 40000)

#Opening the windows:
plt.show()

#Printing the wanted information:
for age in np.linspace(18, 64, 47):
    print(f"Yearly price prediction for a non smoker {int(age)} year old: {int(model.predict(np.array([age]).reshape(-1,1)))}$")
