# fit a straight line to the economic data
# Good Example of Curve Fitting from : https://machinelearningmastery.com/curve-fitting-with-python/
#
# Column data headings
# - GNP.deflator: GNP implicit price deflator (1954=100)
# - GNP: Gross National Product.
# - Unemployed: number of unemployed.
# - Armed.Forces: number of people in the armed forces.
# - Population: ‘noninstitutionalized’ population ≥ 14 years of age.
# - Year: the year (time).
# - Employed: number of people employed.
#
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# define the true objective function
# This function using linear function
def objective_linear(x, a, b):
	return a * x + b

def objective_polynomial(x, a, b, c, d, e, f):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

# load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe = read_csv(url, header=None)
print(dataframe)
data = dataframe.values

# choose the input and output variables
# using Population for input and Employed as output
# x=Population Size
# y=Employed
x, y = data[:, 4], data[:, -1]

# curve fit
popt, _ = curve_fit(objective_linear, x, y)


# summarize the parameter values
a, b = popt
print('y = %.5f * x + %.5f' % (a, b))

# plot input vs output
plt.scatter(x, y)

# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective_linear(x_line, a, b)

# create a line plot for the mapping function
plt.plot(x_line, y_line, '--', color='red', label="linear")

######################################
#now try the same with a poloynomial curve fitting objective
######################################
# curve fit
# Based on x & y already known from training data
# x=Population Size
# y=Employed
popt, _ = curve_fit(objective_polynomial, x, y)

# summarize the parameter values
a, b, c, d, e, f = popt
#print('y = %.5f * x + %.5f' % (a, b))

# plot input vs output
#pyplot.scatter(x, y)

# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective_polynomial(x_line, a, b, c, d, e, f)

# create a line plot for the mapping function
plt.plot(x_line, y_line, '--', color='green', label="Polynomial")
plt.ylabel("Employed")
plt.xlabel("Population Size")
plt.legend(loc="upper left")
plt.show()