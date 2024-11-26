import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


x, y = make_regression(n_samples=50, n_features=1, noise=10, n_informative=1, random_state=11)
model = LinearRegression()
print(x, y)


model.fit(x, y)

coef = model.coef_
intercept = model.intercept_
print(coef, intercept)


# plot regression line
plt.scatter(x, y)
plt.plot(x, coef*x + intercept, color='red')

print(model.predict([x[0]]))  # predict y for x=0.5

plt.show()