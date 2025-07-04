import matplotlib.pyplot as plt
import numpy as np
mode_transport = np.array(['Walking', 'Cycling', 'Car', 'Bus', 'Train'])
feq = np.array([29, 15, 35, 18, 3])
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('SJC23MCA-2059 : TOBIN K TOMY\nBatch : MCA 2023-25', loc='right')
plt.bar(mode_transport, feq, width=0.1, color='green')
plt.show()