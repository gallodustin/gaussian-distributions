import numpy as np
import matplotlib.pyplot as plt

# Make a scatter plot by drawing 100 items from a mixture distribution
# 0.3N((1,0)^T, (1 & 0.2 \\ 0.2 & 1)) + 0.7N((-1,0)^T,(1 & -0.2 \\ -0.2 & 1)).

# mean vector and covariance matrix
mu1 = np.array([1, 0])
Sigma1 = np.array([[1, 0.2], [0.2, 1]])
mu2 = np.array([-1, 0])
Sigma2 = np.array([[1, -0.2], [-0.2, 1]])

# generate 100 sample points
x = np.empty(100)
y = np.empty(100)
for i in range (100):
    val1 = np.random.multivariate_normal(mu1, Sigma1)
    val2 = np.random.multivariate_normal(mu2, Sigma2)
    x[i] = (0.3 * val1[0]) + (0.7 * val2[0])
    y[i] = (0.3 * val1[1]) + (0.7 * val2[1])

# plot
plt.scatter(x, y)
plt.show