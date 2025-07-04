import matplotlib.pyplot as plt
import numpy as np
month = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
AS = np.array([173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131])
LS = np.array([189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161])
SLS = np.array([185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110])

plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments')

plt.title('Sales Data')
plt.title('SJC23MCA-2059 : TOBIN K TOMY\nBatch : MCA 2023-25\n', loc='right')

plt.scatter(month, AS, label='Affordable Segment', color='pink')
plt.scatter(month, LS, label='Luxury Segment', color='yellow')
plt.scatter(month, SLS, label='Super Luxury Segment', color='blue')

plt.show()