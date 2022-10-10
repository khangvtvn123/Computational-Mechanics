import numpy as np

A = np.array([[   2,   0.7, -3.5,    7, -0.5],
              [-1.2, 2.7*3,    0,   -3, -2.5],
              [   1,     1,   -1,   -1,    1],
              [ 2.9,     0,    0,    0,  7.5],
              [   0,     0,  1.8, -2.7, -5.5]])
B = np.array([[2], [-17], [5], [0], [-11]])
print("Coefficient Matrix  A = \n", A)
print("Result matrix B = \n", B)
AI = np.linalg.inv(A)
X = np.dot(AI, B)
print("X = A^-1 B = \n", X)
# substitute X back to the original functions
print("Substitute x back to the original functions: ")
f = [0, 0, 0, 0, 0]
for i in range(5):
    for x in range(5):
        f[i] += A[i][x] * X[x]

for i in range(5):
    print(A[i][0], "*", X[0][0], "+", A[i][1], "*", X[1][0], "+", A[i][2], "*", X[2]
          [0], "+", A[i][3], "*", X[3][0], "+", A[i][4], "*", X[4][0], "=", f[i][0])

print("The end result match the initial system of equations.")
