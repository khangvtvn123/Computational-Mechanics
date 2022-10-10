import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

# a
print("(a)")
print("v(r) \t\t= sin(r) + r^2 + 1")
print("dv/dr \t\t= cos(r) + 2r")
print("d^2v/dr^2 \t= -sin(r) + 2")
print("d^3v/dr^3 \t= -cos(r)")

# b
print("\n(b)")
r = np.linspace(-np.pi, np.pi, 100)
v = np.sin(r) + r**2 + 1
plt.plot(r, v)
plt.show()

# c
print("\n(c)")
print("Through visual inspection of the plot, v is minimum at r = -0.5")

# d
print("\n(d)")
# plot the derivative of v
w = np.cos(r) + 2*r
plt.plot(r, w)
plt.show()
# find root of w


def function(root):
    return np.cos(root) + 2*root


root = op.fsolve(function, 1000000)
print("w = 0 at r = ", root[0])
print("This result is relatively close to the expected value stated in part c.")
