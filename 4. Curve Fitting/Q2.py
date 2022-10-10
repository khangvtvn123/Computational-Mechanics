import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

# load data
tensile = np.loadtxt("./4. Curve Fitting/Homework 4/stressstrain.csv", delimiter=",")
strain = tensile[:, 0]
stress = tensile[:, 1]
plt.scatter(strain, stress, s=2)
plt.show()


# curve fitting  -----------------------------------------------------------
def stress_function(strain, K, n):
    return K * strain**n
pars, cov = op.curve_fit(f=stress_function, xdata=strain, ydata=stress, p0=[0, 0], bounds=(-np.inf, np.inf))
print('K = ', pars[0])
print('n = ', pars[1])

plt.scatter(strain, stress, s=2)
plt.plot(strain, stress_function(strain, pars[0], pars[1]), color='red')
plt.show()
