import numpy as np
import matplotlib.pyplot as plt
import math

print("y = sin(x) + cos(x)")

# a
print("\n(a)")
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x) + np.cos(x)
plt.plot(x, y1)
plt.show()

# b
print("\n(b)")
x0 = 0
y2 = np.sin(x0) + np.cos(x0) + ((x - x0)**1 / math.factorial(1)) * (np.cos(x0) - np.sin(x0))
y3 = y2 + ((x - x0)**2 / math.factorial(2)) * (-np.sin(x0) - np.cos(x0))
y4 = y3 + ((x - x0)**3 / math.factorial(3)) * (-np.cos(x0) + np.sin(x0))
y5 = y4 + ((x - x0)**4 / math.factorial(4)) * (np.sin(x0) + np.cos(x0))
y6 = y5 + ((x - x0)**5 / math.factorial(5)) * (np.cos(x0) - np.sin(x0))

plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6)
plt.show()

# c
print("\n(c)")
x0 = np.pi/4
y2 = np.sin(x0) + np.cos(x0) + ((x - x0)**1 / math.factorial(1)) * (np.cos(x0) - np.sin(x0))
y3 = y2 + ((x - x0)**2 / math.factorial(2)) * (-np.sin(x0) - np.cos(x0))
y4 = y3 + ((x - x0)**3 / math.factorial(3)) * (-np.cos(x0) + np.sin(x0))
y5 = y4 + ((x - x0)**4 / math.factorial(4)) * (np.sin(x0) + np.cos(x0))
y6 = y5 + ((x - x0)**5 / math.factorial(5)) * (np.cos(x0) - np.sin(x0))

plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6)
plt.show()