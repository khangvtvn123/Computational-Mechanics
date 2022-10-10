import numpy as np

# (a) Print a, b, ab
print("(a)")
# 4x3 matrix a and 3x2 matrix b
a = np.array([[1, -2, 3], [-4, 5, -6], [-1, 2, -3], [4, -5, 6]])
print("a = \n", a)
b = np.array([[1, -3], [-4, 5], [7, 9]])
print("b = \n", b)
print("ab = \n", np.dot(a, b))

# (b) Is it possible to do the multiplication aa^T? Why or why not?
print("\n(b)")
aT = a.transpose()
print("a^T = \n", aT)
print("aa^T = \n", np.dot(a, aT))
print("This is possible because a^T have the shape of (3, 4). The number of row ")
print("of matrix a is the same as the number of column of the matrix a^T, which ")
print("is the requirement of matrix mulplication.")

# (c) Show that (ab)^T = b^T a^T
print("\n(c)")
# (ab)^T
print("(ab)^T = \n", np.dot(a, b).transpose())
# b^T a^T
print("b^T a^T = \n", np.dot(b.transpose(), a.transpose()))
print("--> (ab)^T = b^T a^T")

# (d) Create two square matrices of equal size and show that (cd)^-1 = d^-1 c^-1
print("\n(d)")
c = np.array([[-1, -2, -3], [-15, 16, 17], [24, -23, 22]])
d = np.array([[55, -1, 12], [95, -6, -5], [512, 4, 49]])
print("c = \n", c)
print("d = \n", d)
# (cd)^-1
cd = np.dot(c, d)
cdI = np.linalg.inv(cd)
print("(cd)^-1 = \n", cdI)
# d^-1 c^-1
dI = np.linalg.inv(d)
cI = np.linalg.inv(c)
dIcI = np.dot(dI, cI)
print("d^-1 c^-1 = \n", dIcI)
print("--> (cd)^-1 = d^-1 c^-1")

# (e) Show that (c^-1)^T = (c^T)^-1
print("\n(e)")
# (c^-1)^T
print("(c^-1)^T = \n", cI.transpose())
# (c^T)^-1
cT = c.transpose()
cTI = np.linalg.inv(cT)
print("(c^T)^-1 = \n", cTI)
print("--> (c^-1)^T = (c^T)^-1")
