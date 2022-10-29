import numpy as np
from math import acos

A = np.array([[40, 20, -18], [20, 28, 12], [-18, 12, 4]])
pri_stress, normal = np.linalg.eig(A)

print("Origianl principal stress: ", pri_stress)
print("Original normal: \n", normal)

# sor the pri_stress
for i in range (len(pri_stress)-1):
    for j in range (len(pri_stress) - 1 - i):
        if (pri_stress[j] > pri_stress[j+1]):
            pri_stress[j], pri_stress[j+1] = pri_stress[j+1], pri_stress[j]
            normal[:, [j, j+1]] = normal[:, [j+1, j]]

print("Sorted principal stress: ", pri_stress)
print("Sorted normal: \n", normal)

print()
print("The angles that the normal to the principal plane which has the maximum principal stress makes with the:")
print("x axis: \t", acos(normal[0, 2] / np.linalg.norm(normal[:, 2])))
print("y axis: \t", acos(normal[1, 2] / np.linalg.norm(normal[:, 2])))
print("z axis: \t", acos(normal[2, 2] / np.linalg.norm(normal[:, 2])))

print("The angles that the normal to the principal plane which has the minimum principal stress makes with the:")
print("x axis: \t", acos(normal[0, 0] / np.linalg.norm(normal[:, 0])))
print("y axis: \t", acos(normal[1, 0] / np.linalg.norm(normal[:, 0])))
print("z axis: \t", acos(normal[2, 0] / np.linalg.norm(normal[:, 0])))