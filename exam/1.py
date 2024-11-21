# Value depreciation plot 

import matplotlib.pyplot as plt

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]

# plt.figure(figsize=(10, 6))
plt.plot(years, car_values, linestyle="dashdot", color="red", marker="*", markersize=20, markerfacecolor="green")
plt.title("value depreciation", loc="left")
plt.xlabel("years")
plt.ylabel("car values")
plt.show()