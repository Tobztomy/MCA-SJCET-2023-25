print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
import numpy as np;
X = np.array([[1, 2],
              [3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2* Y
print(result)