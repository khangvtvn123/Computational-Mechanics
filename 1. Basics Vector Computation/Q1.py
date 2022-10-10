import numpy as np

# Initialize vector
A = np.array([2, -3, 7])
B = np.array([-4, 1, 0])
C = np.array([5, -1, 9])
D = np.array([0, 0, 2])

# Find
# (a) vec(A) . vec(B) and vec(C) . vec(D)
print("(a)")
print("\tvec(A) . vec(B) = ", np.dot(A, B))
print("\tvec(C) . vec(D) = ", np.dot(C, D))

# (b) The angles which vec(A) X vec(B) makes with the x, y, z axes
print("\n(b)")
# vec(A) X vec(B)
AcrossB = np.cross(A, B)
print("\tvec(A) X vec(B)", AcrossB)
# Angle AcrossB makes with the x, y, z, axes
angleX = np.arccos(np.dot(AcrossB, [
                   1, 0, 0]) / (np.linalg.norm(AcrossB) * np.linalg.norm([1, 0, 0]))) * 180 / np.pi
angleY = np.arccos(np.dot(AcrossB, [
                   0, 1, 0]) / (np.linalg.norm(AcrossB) * np.linalg.norm([0, 1, 0]))) * 180 / np.pi
angleZ = np.arccos(np.dot(AcrossB, [
                   0, 0, 1]) / (np.linalg.norm(AcrossB) * np.linalg.norm([0, 0, 1]))) * 180 / np.pi
print("\tAngle with X = ", angleX)
print("\tAngle with Y = ", angleY)
print("\tAngle with Z = ", angleZ)

# (c) Unit vector in the direction of vec(B) X vec(D)
print("\n(c)")
# vec(B) X vec(D)
BcrossD = np.cross(B, D)
# Devide by its magnitude to find the unit vector
BcrossDunit = np.array([BcrossD[0] / np.linalg.norm(BcrossD), BcrossD[1] /
                       np.linalg.norm(BcrossD), BcrossD[2] / np.linalg.norm(BcrossD)])
print("\tvec(B) X vec(D) = ", BcrossD)
print("\tUnit vector of vec(B) X vec(D) = ", BcrossDunit)

# (d) The vector with the largest magnitude
print("\n(d)")
# Calculate the magnitude of all vectors
magA = np.linalg.norm(A)
magB = np.linalg.norm(B)
magC = np.linalg.norm(C)
magD = np.linalg.norm(D)
print("\tMagnitude of vec(A) = ", magA)
print("\tMagnitude of vec(B) = ", magB)
print("\tMagnitude of vec(C) = ", magC)
print("\tMagnitude of vec(D) = ", magD)
# Compare the magnitude of vectors to find the largest
nameMax = "A"
magMax = magA
if magB > magMax:
    nameMax = "B"
    magMax = magB
if magC > magMax:
    nameMax = "C"
    magMax = magC
if magD > magMax:
    nameMax = "D"
    magMax = magD
print("\tThe vector with the largest magnitude is ",
      nameMax, ". Its magnitude is ", magMax, ".")
