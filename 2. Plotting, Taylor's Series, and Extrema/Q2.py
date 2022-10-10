import numpy as np
import matplotlib.pyplot as plt

# Creating dataset
x = np.outer(np.linspace(-np.pi, np.pi, 100), np.ones(100))
y = x.copy().T  # transpose
z = (np.sin(x * y) + np.cos(x * y))

# Creating figure
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


# Creating color map
my_cmap = plt.get_cmap('coolwarm')

# Creating plot
surf = ax.plot_surface(x, y, z, cmap=my_cmap, edgecolor='none')

ax.set_zlim(-5, 5)

fig.colorbar(surf, ax=ax,
             shrink=0.5, aspect=10)

ax.set_title('Surface plot')

# show plot
plt.show()
