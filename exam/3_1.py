# Subplot (sales of drinks and food)

import matplotlib.pyplot as plt

days = ["mon", "tues", "wed", "thu", "fri"]
drinks = [300, 450, 150, 400, 650]
food = [400, 500, 350, 300, 500]

fig, axs = plt.subplots(2, 1, figsize=(8, 8))

axs[0].plot(days, drinks, linestyle="dotted", color="cyan", marker="H", markerfacecolor="magenta", markeredgecolor="black", label="drinks")
axs[0].set_xlabel("Days of week")
axs[0].set_ylabel("Sale of Drinks")
axs[0].set_title("Sales data1", loc="right")
axs[0].grid(True, linestyle="dotted", color="blue")

axs[1].plot(days, food, linestyle="dashed", color="yellow", marker="D", markerfacecolor="green", markeredgecolor="red", label="food")
axs[1].set_xlabel("Days of week")
axs[1].set_ylabel("Sale of Food")
axs[1].set_title("Sales data2", loc="center")
axs[1].grid(True, linestyle="dotted", color="blue")

plt.tight_layout()
plt.show()