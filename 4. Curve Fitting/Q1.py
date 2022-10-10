import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
from sklearn.linear_model import LinearRegression
from scipy.io import loadmat

# linear function ----------------------------------------------------------
# create input X and ideal value Y
X_dummy = np.linspace(-20, 20, 40)
intercept, slope = 15, 0.8
Ylinear = 15 + 0.8*X_dummy
print("Y =", intercept, "+", slope, "* X")
# noise that mostly range from -2 and 2
# using Guassian random to better reflect real life cases
noise = np.random.normal(0, 2, Ylinear.size)
Ylinear_noise = Ylinear + noise
plt.plot(X_dummy, Ylinear)
plt.scatter(X_dummy, Ylinear_noise)
plt.show()

# curve fitting using linear regression
# model Y = intercept_ + coef_*X
X1 = X_dummy.reshape(len(X_dummy), 1)
reg1 = LinearRegression().fit(X1, Ylinear_noise)
print("Best fit function y =", reg1.intercept_, "+", reg1.coef_, "* X")
best_fit1 = reg1.intercept_ + reg1.coef_*X_dummy
plt.plot(X_dummy, Ylinear, X_dummy, best_fit1)
plt.scatter(X1, Ylinear_noise)
plt.show()


# quadratic function --------------------------------------------------------
a0, a1, a2 = 6, 0.8, 0.3
Yquad = a0 + a1*X_dummy + a2*X_dummy**2
print("\n\nY =", a0, "+", a1, "* X +", a2, "* X^2")
# noise that mostly range from -2 and 2
noise2 = np.random.normal(0, 10, Yquad.size)
Yquad_noise = Yquad + noise2
plt.plot(X_dummy, Yquad)
plt.scatter(X_dummy, Yquad_noise)
plt.show()

# curve fitting using linear regression
# model Y = intercept_ + coef_[0]*X + coef_[1]*X*X
X2 = np.empty((len(X_dummy), 2))
X2[:, 0] = X_dummy
X2[:, 1] = X_dummy**2
print(X2)
reg2 = LinearRegression().fit(X2, Yquad_noise)
print("Best fit function Y = ", reg2.intercept_, "+",
      reg2.coef_[0], "* X +", reg2.coef_[1], "* X^2")
best_fit2 = reg2.intercept_ + reg2.coef_[0]*X2[:, 0] + reg2.coef_[1]*X2[:, 1]
plt.plot(X_dummy, Yquad, X_dummy, best_fit2)
plt.scatter(X_dummy, Yquad_noise)
plt.show()


# load data from mat file -----------------------------------------------------------
data = loadmat("./4. Curve Fitting/Homework 4/data.mat", squeeze_me=True)
X = data['x']
X_array = np.asarray(X)
Y = data['y']
plt.scatter(X, Y)
plt.show()
print("Looking at the data, a cubic polynomial would work best.")

# curve fitting using linear regression
# model Y = intercept_ + coef_[0]*X + coef_[1]*X**2 + coef_[2]*X**3
X3 = np.empty((len(X), 3))
X3[:, 0] = X
X3[:, 1] = X**2
X3[:, 2] = X**3
print(X3)
reg3 = LinearRegression().fit(X3, Y)
print("Best fit function Y = ", reg3.intercept_, "+", reg3.coef_[0], "* X +", reg3.coef_[1], "* X^2 +", reg3.coef_[2], "* X^3")
best_fit3 = reg3.intercept_ + reg3.coef_[0]*X3[:, 0] + reg3.coef_[1]*X3[:, 1] + reg3.coef_[2]*X3[:, 2]
plt.plot(X, best_fit3)
plt.scatter(X, Y)
plt.show()
