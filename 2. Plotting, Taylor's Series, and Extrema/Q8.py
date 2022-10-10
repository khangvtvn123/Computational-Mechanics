import scipy.optimize as op

# V = x*y*z = 1000 -> z = 1000/xy
# A = 2*(xz + xy + yz)
# With z = 1000/xy
# -> A = 2*(xy + 1000/x + 1000/y)
# -> dA/dx = 2(y - 1000/x^2)
#    dA/dy = 2(x - 1000/y^2)


def gradientA(var):
    (x, y) = var
    Ax = 2 * (y - (1000/x/x))
    Ay = 2 * (x - (1000/y/y))
    return [Ax, Ay]


r = op.fsolve(gradientA, [1, 1])
print("The value of (x, y):", r)
print("z = 1000 / ", r[0], " / ", r[1], " = ", 1000/r[0]/r[1])
