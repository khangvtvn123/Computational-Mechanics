import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

# a
print("(a)")
x = np.linspace(-6 * np.pi, 6 * np.pi, 100)
y = x**3 * np.cos(x)
zero = [0] * 100
plt.plot(x, y)
# for cos(x) = 0 -> x = +/- [pi/2, 3pi/2, 5pi/2, 7pi/2, 9pi/2, 11pi/2]
# for x^3 = 0 -> x = 0
guesses = [-np.pi/2, 3 * -np.pi/2, 5 * -np.pi/2, 7 * -np.pi/2, 9 * -np.pi/2, 11 * -np.pi/2,
           0, np.pi/2, 3 * np.pi/2, 5 * np.pi/2, 7 * np.pi/2, 9 * np.pi/2, 11 * np.pi/2]
plt.plot(guesses, [0] * 13, marker="o")
plt.show()

# b
print("\n(b)")


def function(x):
    return x**3 * np.cos(x)


roots = op.fsolve(function, guesses)
print("Roots of the function: \n", roots)
