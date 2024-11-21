# Bar plot (Mode of transport)

import matplotlib.pyplot as plt

x = ["Walking", "Cycling", "Car", "Bus", "Train"]
y = [29, 15, 35, 18, 3]

plt.title("Transport")
plt.xlabel("Mode of transport")
plt.ylabel("Frequency")

plt.bar(x, y, width=0.1, color="green")
plt.show()