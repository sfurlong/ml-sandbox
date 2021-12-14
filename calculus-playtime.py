import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import derivative

# Define parabola
def func(x):
    return x**2

# method to return its derivative
def deriv(x):
    return derivative(func, x)

# Define tangent line
# y = m*(x - x1) + y1
def line(x, x1, y1):
    d = deriv(x1)
    ret = d * (x -x1) + y1
    return ret


# Define x data range for parabola
x = np.linspace(-5,5,100)

# Choose point to plot tangent line
x1 = -3
y1 = func(x1)


# Define x data range for tangent line
xrange = np.linspace(x1-1, x1+1, 10)

# Plot the figure
plt.figure()
plt.plot(x, func(x))
plt.scatter(x1, y1, color='C1', s=50)
plt.plot(xrange, line(xrange, x1, y1), 'C1--', linewidth = 2)

plt.show()