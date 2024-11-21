# Subplot (sales of drinks and food)

import matplotlib.pyplot as plt

days = ["mon", "tues", "wed", "thu", "fri"]
drinks = [300, 450, 150, 400, 650]
food = [400, 500, 350, 300, 500]

plt.subplot(211)
plt.plot(days, drinks, linestyle="dotted", color="cyan", marker="H", markerfacecolor="magenta", markeredgecolor="black", label="drinks")
plt.xlabel("Days of week")
plt.ylabel("Sale of Drinks")
plt.title("Sales data1", loc="right")
plt.grid(True, linestyle="dotted", color="blue")

plt.subplot(212)
plt.plot(days, food, linestyle="dashed", color="yellow", marker="D", markerfacecolor="green", markeredgecolor="red", label="food")
plt.xlabel("Days of week")
plt.ylabel("Sale of Food")
plt.title("Sales data2", loc="center")
plt.grid(True, linestyle="dotted", color="blue")

plt.tight_layout()
plt.show()