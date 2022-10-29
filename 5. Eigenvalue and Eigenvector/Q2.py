from math import sqrt
import numpy as np

print("A*u = lamda*u")
print("Matrix A = \t[-k/m_1\tk/m_2\t0\t]")
print("\t\t[k/m_2\t-2k/m_2\tk/m_2\t]")
print("\t\t[0\tk_m_1\t-k/m_1\t]")
print("Column eigenvector u = [A_1   A_2   A_3]")
print("Eigenvalue lamda = w^2")

# find eigen value and eigen vector
k = 1.8e2
m1 = 35.45 * 1.6605 * 10e-27
m2 = 9.01 * 1.6605 * 10e-27
A = np.array([[-k/m1, k/m1, 0], [k/m2, -2*k/m2, k/m2], [0, k/m1, -k/m1]])
print(A)
lamda, u = np.linalg.eig(A)

print("\n")
for i in range (len(lamda)):
    print("w = ", sqrt(-lamda[i]))
    print("Corresponding eigenvector u = ", u[i])