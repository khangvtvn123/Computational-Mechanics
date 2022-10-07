import numpy as np 
import matplotlib.pyplot as plt 
import scipy.optimize as op
from scipy.misc import derivative

# 1. f(x) = x^2 + 3x - 30
print("f(x) = x^2 + 3x - 30")
# plot the function
X = np.linspace(-10, 10, 100)
Y = X**2 + 3*X - 30
plt.plot(X, Y)
plt.show()

# find min using op.minimize
def f1(x):
  return x**2 + 3*x - 30
min1 = op.minimize(f1, -1.5)
print("Minima:\n", min1)
# gradient decent function
def gradMinimize2(a, initialGuess, function):
  tol = 10e-6 # approximation of zero
  n = 0
  gradf = np.zeros(10000) # dynamic is better
  while True:
    finalGuess = initialGuess - a*derivative(function, initialGuess)
    gradf[n] = finalGuess
    
    # check if the gradient is approximately zero
    if (abs(finalGuess - initialGuess) < tol):
      return finalGuess, gradf
    else:
        initialGuess = finalGuess

    # prevent infinite loop
    if (n > 10e6):
      print("The function is not converge with alpha = ", a)
      break
    else:
      n += 1
min2, gradDecent = gradMinimize2(0.1, 10, f1)
plt.plot(X, Y)
plt.scatter(gradDecent, f1(gradDecent))
plt.show()
print("Using gradient decent, we found the minima to be ", min2)

#-----------------------------------------------------------------------------
# 2. 
print("\n2. y = f(x) = x**2 − 10*x + 12")
def f2(x):
  return x**2 - 10*x + 12
X = np.linspace(0, 10, 100)
Y = f2(X)
plt.plot(X, Y)
plt.show()

# square the function so that x-intersect points would become minimum point
YSquare = Y**2
plt.plot(X, YSquare)
def f2Square(x):
  return (x**2 - 10*x + 12)**2

print("Using gradient decent, we have:")
# find roots
min, gradDecent = gradMinimize2(0.005, 6.5, f2Square)
plt.scatter(gradDecent, f2Square(gradDecent))
print("root1 = ", min)
min, gradDecent = gradMinimize2(0.005, 4, f2Square)
plt.scatter(gradDecent, f2Square(gradDecent))
print("root2 = ", min)
plt.show()