import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

# A = 10 * 14
# V = h * (14 - 2h) * (10 - 2h) = (14h - 2hh) * (10 - 2h) = 140h - 48hh + 4hhh
# V' = 140 - 96h + 12hh
#V'' = -96 + 24h
h = np.linspace(-5, 5, 100)
V = 140*h - 48*h*h + 4*h*h*h
plt.plot(h, V)
plt.show()

def Vinverse(var):
  V = 140*var - 48*var*var + 4*var*var*var
  return 1/V

hmaxV = op.minimize(Vinverse, 1.8)
print(hmaxV)
print("At h = 1.92 in, the volume is at maximum.")

#prove
print("V' = ", 140 - 96*1.91826666 + 12*1.91826666*1.91826666, "-> this point is an extrema.")
print("V'' = ", -96 + 24*1.91826666, "< 0 -> this point is an maxima.")