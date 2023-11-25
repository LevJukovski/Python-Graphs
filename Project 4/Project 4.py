#Imports:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Style of plots:
style.use("bmh")

#Making x values:
mu, sigma = 78.25, 10
x = mu + sigma * np.random.randn(10000)

#Creating a window, defining and adjusting the plot:
plt.hist(x, 1000, facecolor="blue", density=True)
plt.xlabel("Weights", fontsize=20, color="black")
plt.ylabel("Percentage of employees", fontsize=20, color="black")
plt.suptitle("Acme corporation-\nWeight of employees:", fontsize=25, color="black")
plt.text(40, 0.043, "avg. = 78.25 Kg\nstd. = 10 Kg")
plt.tight_layout()
plt.grid(True)

#Opening the window:
plt.show()
