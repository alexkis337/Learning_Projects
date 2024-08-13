import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression


x, y = make_regression(n_samples=50, n_features=1, noise=10, n_informative=1, random_state=11)


print(x)
print(y)

# plot the data
plt.scatter(range(len(x)), x)
plt.show()