import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op


# load data -----------------------------------------------------------
keeling_nh = np.loadtxt(
    "./4. Curve Fitting/Homework 4/Keeling-NH.csv", delimiter=",")
year = keeling_nh[:, 3]
co2 = keeling_nh[:, 4]
plt.title("Original Data")
plt.scatter(year, co2, s=3)
plt.show()
print("There are some negative values, which should not exist.")


# remove negative data ---------------------------------------------------
year_c = year
co2_c = co2
i = 0
while (i < len(co2_c)):
    if (co2_c[i] < 0):
        year_c = np.delete(year_c, i)
        co2_c = np.delete(co2_c, i)
    else:
        i += 1
# plot corrected data at different time periods --------------------------
plt.title("Corrected Data\nFrom 1958 to present")
plt.ylim(300, 450)
plt.scatter(year_c, co2_c, s=3)
plt.show()
plt.title("Corrected Data\nFrom 2015 to 2020")
plt.xlim(2015, 2020)
plt.ylim(380, 420)
plt.scatter(year_c, co2_c, s=3)
plt.show()


# curve fitting with different model ------------------------------------
def model1(x, a0, a1):
    return a0 + a1*x
pars1, cov1 = op.curve_fit(f=model1, xdata=year_c, ydata=co2_c, p0=[0, 0], bounds=(-np.inf, np.inf))
print("Model_1 =", pars1[0], "+", pars1[1], "x")

def model2(x, a0, a1, a2):
    return a0 + a1*x + a2*x**2
pars2, cov2 = op.curve_fit(f=model2, xdata=year_c, ydata=co2_c, p0=[0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_2 =", pars2[0], "+", pars2[1], "* x +", pars2[2], "*x**2")

def model3(x, a0, a1, a2, a3, a4):
    return a0 + a1*x + a2*x**2 + a3*np.sin(a4 - x)
pars3, cov3 = op.curve_fit(f=model3, xdata=year_c, ydata=co2_c, p0=[0, 0, 0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_3 =",  pars3[0], "+", pars3[1], "*x +", pars3[2], "*x**2 +", pars3[3], "* sin(", pars3[4], "- x )")

plt.scatter(year_c, co2_c, s=2)
plt.plot(year_c, model1(year_c, pars1[0], pars1[1]), color = "red", label = "model_1")
plt.plot(year_c, model2(year_c, pars2[0], pars2[1], pars2[2]), color = "purple", label = "model_2")
plt.plot(year_c, model3(year_c, pars3[0], pars3[1], pars3[2], pars3[3], pars3[4]), color = "green", label = "model_3")
legend = plt.legend(loc='upper left', fontsize='large')
plt.show()