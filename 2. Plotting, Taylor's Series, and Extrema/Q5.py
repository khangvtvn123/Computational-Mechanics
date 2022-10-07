import scipy.optimize as op

# y = -2x - 4
# y = x^2 - 4
print("y = -2*x - 4")
print("y = x**2 - 4")

def fun(var):
    x = var[0]
    y = var[1]

    eq1 = -2 * x - 4 - y
    eq2 = x**2 - 4 - y
    return [eq1, eq2]
print("Solutions (x, y): ")
results = op.fsolve(fun,[10, 10])
print(results, " ~= [0, -4]")
results = op.fsolve(fun,[-5, 2])
print(results, " ~= [-2, 0]")