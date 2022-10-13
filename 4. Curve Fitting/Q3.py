import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op


# load data -----------------------------------------------------------
keeling_nh = np.loadtxt("./4. Curve Fitting/Homework 4/Keeling-NH.csv", delimiter=",")
year = keeling_nh[:, 3]
co2 = keeling_nh[:, 4]
plt.title("Original Data")
plt.scatter(year, co2, s=3)
plt.show()
print("There are some negative values, which should not exist.")


# remove negative data ---------------------------------------------------
year_c_general = year
co2_c_general = co2
i = 0
while (i < len(co2_c_general)):
    if (co2_c_general[i] < 0):
        year_c_general = np.delete(year_c_general, i)
        co2_c_general = np.delete(co2_c_general, i)
    else:
        i += 1
# plot corrected data at different time periods --------------------------
plt.title("Corrected Data\nFrom 1958 to present")
plt.ylim(300, 450)
plt.scatter(year_c_general, co2_c_general, s=3)
plt.show()
# from 2015 to 2020
year_c_seasonal = year_c_general
co2_c_seasonal = co2_c_general
i = 0
while (i < len(year_c_seasonal)):
    if (year_c_seasonal[i] < 2015 or year_c_seasonal[i] > 2020):
        year_c_seasonal = np.delete(year_c_seasonal, i)
        co2_c_seasonal = np.delete(co2_c_seasonal, i)
    else:
        i += 1
plt.title("Corrected Data\nFrom 2015 to 2020")
plt.xlim(2015, 2020)
plt.ylim(380, 420)
plt.scatter(year_c_seasonal, co2_c_seasonal, s=3)
plt.show()


# curve fitting with different model ------------------------------------
# from 1958 to present
def model1(x, a0, a1):
    return a0 + a1*x

def model2(x, a0, a1, a2):
    return a0 + a1*x + a2*x**2

def model3(x, a0, a1, a2, a3, a4):
    return a0 + a1*x + a2*x**2 + a3*np.sin(a4 - x)

pars1_general, cov1_general = op.curve_fit(f=model1, xdata=year_c_general, ydata=co2_c_general, p0=[0, 0], bounds=(-np.inf, np.inf))
print("Model_1 =", pars1_general[0], "+", pars1_general[1], "x")

pars2_general, cov2_general = op.curve_fit(f=model2, xdata=year_c_general, ydata=co2_c_general, p0=[0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_2 =", pars2_general[0], "+", pars2_general[1], "* x +", pars2_general[2], "*x**2")

pars3_general, cov3_general = op.curve_fit(f=model3, xdata=year_c_general, ydata=co2_c_general, p0=[0, 0, 0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_3 =",  pars3_general[0], "+", pars3_general[1], "*x +", pars3_general[2], "*x**2 +", pars3_general[3], "* sin(", pars3_general[4], "- x )")

plt.scatter(year_c_general, co2_c_general, s=2)
plt.plot(year_c_general, model1(year_c_general, pars1_general[0], pars1_general[1]), color = "red", label = "model_1")
plt.plot(year_c_general, model2(year_c_general, pars2_general[0], pars2_general[1], pars2_general[2]), color = "purple", label = "model_2")
plt.plot(year_c_general, model3(year_c_general, pars3_general[0], pars3_general[1], pars3_general[2], pars3_general[3], pars3_general[4]), color = "green", label = "model_3")
plt.legend(loc='upper left', fontsize='large')
plt.title('Corrected Data\nFrom 1958 to present')
plt.show()

# from 2015 to 2020
pars1_seasonal, cov1_seasonal = op.curve_fit(f=model1, xdata=year_c_seasonal, ydata=co2_c_seasonal, p0=[0, 0], bounds=(-np.inf, np.inf))
print("Model_1 =", pars1_seasonal[0], "+", pars1_seasonal[1], "x")

pars2_seasonal, cov2_seasonal = op.curve_fit(f=model2, xdata=year_c_seasonal, ydata=co2_c_seasonal, p0=[0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_2 =", pars2_seasonal[0], "+", pars2_seasonal[1], "* x +", pars2_seasonal[2], "*x**2")

pars3_seasonal, cov3_seasonal = op.curve_fit(f=model3, xdata=year_c_seasonal, ydata=co2_c_seasonal, p0=[0, 0, 0, 0, 0], bounds=(-np.inf, np.inf))
print("Model_3 =",  pars3_seasonal[0], "+", pars3_seasonal[1], "*x +", pars3_seasonal[2], "*x**2 +", pars3_seasonal[3], "* sin(", pars3_seasonal[4], "- x )")

plt.scatter(year_c_seasonal, co2_c_seasonal, s=2)
plt.plot(year_c_seasonal, model1(year_c_seasonal, pars1_seasonal[0], pars1_seasonal[1]), color = "red", label = "model_1")
plt.plot(year_c_seasonal, model2(year_c_seasonal, pars2_seasonal[0], pars2_seasonal[1], pars2_seasonal[2]), color = "purple", label = "model_2")
plt.plot(year_c_seasonal, model3(year_c_seasonal, pars3_seasonal[0], pars3_seasonal[1], pars3_seasonal[2], pars3_seasonal[3], pars3_seasonal[4]), color = "green", label = "model_3")
plt.legend(loc='upper left', fontsize='large')
plt.title('Corrected Data\nFrom 2015 to 2020')
plt.show()


# predict future value -----------------------------------------------------------------------------
print("It is hard to tell which model best fit the the seasonal data due to its limited input.")
print("We would use Model_2 and Model_3 from the corrected data form 1957 to 2021 to predict the future, since they visually best fit the data.")
future = np.linspace(2023, 2027, (2027 - 2023) * 12)
plt.plot(future, model2(future, pars2_seasonal[0], pars2_seasonal[1], pars2_seasonal[2]), label = "model_2")
plt.plot(future, model3(future, pars3_seasonal[0], pars3_seasonal[1], pars3_seasonal[2], pars3_seasonal[3], pars3_seasonal[4]), label = "model_3")
plt.legend(loc='upper left', fontsize='large')
plt.title("Future prediction\nFrom 2023 to 2027")
plt.show()
