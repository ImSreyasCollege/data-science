import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

affordable = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
super_luxury = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]

plt.scatter(months, affordable, color="pink")
plt.scatter(months, luxury, color="yellow")
plt.scatter(months, super_luxury, color="blue")
plt.title("Sales data")
plt.xlabel("Month of year", fontsize=18)
plt.ylabel("Sales of segment")
plt.tight_layout()
plt.show()