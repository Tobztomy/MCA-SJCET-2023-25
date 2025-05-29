print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
import numpy as np
A = np.array([[5, 27, 32], [14, 53, 62],[67, 88, 19]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt
print("Original Matrix A : ")
print(A)
print("Singular Values : ")
print(S)
print("Reconstructed Matrix A_hat : ")
print(A_hat)