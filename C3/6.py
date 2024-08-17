import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal([61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74,
74.5, 76, 76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87])
plt.hist(x, bins=range(40,110,5), )
plt.title('Cherry tree heights',loc='left')
plt.title('SREYAS SATHEESH\nMCA 2023-2025', loc='right')
plt.xlabel('Height (in inches)')
plt.ylabel('Frequency')
plt.savefig("./Outputs/6.png")

plt.show()