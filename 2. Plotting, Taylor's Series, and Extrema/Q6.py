import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
# r, h
# V = pi * r^2 * h = 1.5
# -> h = 1.5/(pi * r^2)

# A = 2pi*r*h + 2pi*r^2
# -> A = 2pi*r*(1.5/(pi * r^2)) + 2pi*r^2

r0 = np.linspace(-1, 1, 100)
A = (2*1.5/r0) + 2*np.pi*r0**2
plt.plot(r0, A)
plt.show()


def function(var):
    return 2*1.5 / var + 2*np.pi*var**2


r = op.minimize(function, 0.5)
print(r)
print("r = 0.62035063")
print("h = ", 1.5 / (np.pi * 0.62035063**2))

# A' = -3/r^2 + 4pi*r
# A'' = 6 / r^3 + 4pi
var = 0.62035063
print("A' = ", -3 / var**2 + 4 * np.pi * var, "-> this point is an extrema.")
print("A'' = ", 6 / var**3 + 4 * np.pi, "> 0 -> this point is an minima")
