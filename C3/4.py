import matplotlib.pyplot as plt
import numpy as np
month =np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
AS = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
LS = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
SLS = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.plot(month,AS, label='Affordable', color='pink',linestyle='--')
plt.plot(month,LS, label='Luxury', color='yellow',linestyle='-.')
plt.plot(month,SLS, label='Super Luxury', color='blue',linestyle=':')
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments')
plt.title('Sales Data')
plt.title('SREYAS SATHEESH\nMCA 2023-2025', loc='right')

plt.savefig("./Outputs/4.png")
plt.show()