import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return x**2


def func_derivative(x):
    return 2*x


x = np.linspace(-20, 20, 200)
y = func(x)
learning_rate = 0.1

# plot rnd point
plt.figure(figsize=(16,6))
plt.plot(x, y, 'r', label='y=x^2')

# HERE WE CALCULATE GRADIENT DESCENT STEP BY STEP
start_point = 10
plt.plot(start_point, func(start_point), '-*b', label='start point')

# calc gradient and move against it
grad = func_derivative(start_point)
print(grad)

next_point = start_point - learning_rate * grad
plt.plot([start_point, next_point], func(np.array([start_point, next_point])), '-*b', label='next point')

curr_point = next_point
grad = func_derivative(curr_point)

plt.plot([curr_point, curr_point - learning_rate * grad],
         func(np.array([curr_point, curr_point - learning_rate * grad])), '-*g', label='next point')
plt.show()


# # HERE WE CALCULATE GRADIENT DESCENT IN A LOOP
#
# start_point = 10
# # learning_rate = 0.1
# next_point = start_point
#
# x = [start_point]
#
# plt.plot(x, func(np.array(x)), '-Db', label='start point')
# plt.axvline(x)
#
# n = 20
#
# for i in range(n):
#     curr_point = next_point
#     next_point = curr_point - learning_rate * func_derivative(curr_point)
#     x.append(next_point)
#
#     print(f'Iteration {i}: x={next_point}, y={func(next_point)}')
#
# x_grad = np.array(x)
# plt.plot(x_grad, func(x_grad), '-', '+g', label='next point')
# plt.legend()
# plt.show()
