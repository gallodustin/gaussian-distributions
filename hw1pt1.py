import numpy as np
import matplotlib.pyplot as plt

# Draw 100 items x=[x_1,x_2]^T from a 2-dimensional Gaussian distribution
# N(mu,Sigma) with mean mu=(0,0)^T and identity covariance matrix Sigma=I, i.e.
# p(x)=(1/2pi)exp(-||x||^2/2), and make a scatter plot (x_1 vs. x_2).

# mean vector and covariance matrix
mu = np.array([0, 0])
Sigma = np.array([[1, 0], [0, 1]])

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