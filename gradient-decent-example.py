#############################################
# Linear Regression using Gradient Descent.
# from blog post: https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931
# Code at Git: https://github.com/chasinginfinity/ml-from-scratch/tree/master/02%20Linear%20Regression%20using%20Gradient%20Descent
#############################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
#plt.show()
print("X: ", X)
print("Y: ", Y)

# Building the model
m = 0
b = 0
L = 0.0001  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X))  # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m * X + b  # The current predicted value of Y
    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_b = (-2 / n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    b = b - L * D_b  # Update c
    print("iter: ", i, " m: ", m, " b: ", b)
    plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='blue') # predicted

print(m, b)

# Making predictions
Y_pred2 = m*X + b
print("m: ", m)
print("c: ", b)

plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()