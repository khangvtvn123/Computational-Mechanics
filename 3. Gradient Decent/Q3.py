import numpy as np 
import matplotlib.pyplot as plt 
import scipy.optimize as op

# 3. f(x, y) = (x - 1)**2 + y**2
# fx = 2**(x - 1) = 0 -> x = 1
# fy = 2**y -> y = 0
# the expected answer is [1 0]
print("f(x, y) = (x - 1)**2 + y**2")

X = np.outer(np.linspace(-5, 5, 100), np.ones(100))
Y = X.copy().T # transpose
Z = (X - 1)**2 + Y**2
 
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Creating color map
my_cmap = plt.get_cmap('coolwarm')
 
# Creating plot
surf = ax.plot_surface(X, Y, Z, cmap = my_cmap, edgecolor ='none')
 
fig.colorbar(surf, ax = ax, shrink = 0.5, aspect = 10)
 
# show plot
plt.show()

def f3(x, y):
  return (x - 1)**2 + y**2

def gradMinimize3(a, initialGuess):  
  tol = 10e-6 # approximate zero
  n = 0
  N = 1e6
  finalGuess = np.zeros(2)
  stepRec = np.zeros([2, 100])
  while True:
    finalGuess[0] = initialGuess[0] - a*(2*(initialGuess[0] - 1))
    finalGuess[1] = initialGuess[1] - a*(2*initialGuess[1])
    stepRec[0][n] = finalGuess[0]
    stepRec[1][n] = finalGuess[1]
    # check if the gradient is approximately zero
    if (np.linalg.norm(finalGuess - initialGuess) < tol):
      return finalGuess, stepRec
    else:
      initialGuess[0] = finalGuess[0]
      initialGuess[1] = finalGuess[1]
    # prevent infinite loop
    if (n > N):
      print("The function is not converge with alpha = ", a)
      break
    else:
      n += 1
min, stepRec = gradMinimize3(0.1, [-5, 5])
print("Using gradient decent, we found the minima at [", round(min[0]), ", ", round(min[1]), "]")
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Creating color map
my_cmap = plt.get_cmap('coolwarm')

# Creating plot
ax.view_init (-90 ,90) # change view to directly above
ax.plot_surface(X, Y, Z, cmap = my_cmap, edgecolor ='none')
ax.scatter3D(stepRec[0], stepRec[1], f3(stepRec[0], stepRec[1]), color = "green")
fig.colorbar(surf, ax = ax, shrink = 0.5, aspect = 10)
 
# show plot
plt.show()