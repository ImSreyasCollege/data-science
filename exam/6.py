# Multi line plot 

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

affordable = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
super_luxury = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]

plt.plot(months, affordable, color="pink", label="Affordable", marker="o", linestyle="-")
plt.plot(months, luxury, color="yellow", label="Luxury", marker="s", linestyle="--")
plt.plot(months, super_luxury, color="blue", label="Super Luxury", marker="^", linestyle="-.")

plt.grid(True, color="blue", linestyle=":", alpha=0.7)
plt.legend(loc="upper right")

plt.title("Sales data")
plt.xlabel("Month of year", fontsize=18) # labelpad : for padding
plt.ylabel("Sales of segment")

plt.show()