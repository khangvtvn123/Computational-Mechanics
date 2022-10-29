import numpy as np

A = np.array([[1,2,3,4,5], [2,4,7,1,2], [3,7,8,5,6], [4,1,5,8,10], [5,2,6,10,3]])
print("A = \n", A)
lamda, u = np.linalg.eig(A)
print("Matrix A's eigen values: ", lamda)
print("Matrix A's eigen vectors: \n", u)

# show A*u = lamda*u
for i in range (len(lamda)):
    print("A * u_", i, "=\t\t", np.dot(A, u[:, i]))
    print("lamda_", i, "* u_", i, "=\t", np.dot(lamda[i], u[:, i]))

# show lamda of inverse A = 1 / lamda
A_inv = np.linalg.inv(A)
print("\nA^-1 = \n", A_inv)
lamda_inv, u_inv = np.linalg.eig(A_inv)
print("Eigenvalues of inverse A = \t", lamda_inv)
print("(Eigenvalue of A)^-1 = \t\t", 1/lamda)