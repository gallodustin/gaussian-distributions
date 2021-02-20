import numpy as np
import matplotlib.pyplot as plt

# Make a scatter plot by drawing 100 items from N(mu + (1,-1)^T, 2Sigma).

# mean vector and covariance matrix
mu = np.array([1, -1])
Sigma = np.array([[2, 0], [0, 2]])

# generate 100 sample points
x = np.empty(100)
y = np.empty(100)
for i in range (100):
    val = np.random.multivariate_normal(mu, Sigma)
    x[i] = val[0]
    y[i] = val[1]

# plot
plt.scatter(x, y)
plt.show