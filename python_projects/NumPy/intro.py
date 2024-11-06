import numpy as np


movie_rt = np.array([[63.0, 54.0, 70.0, 50.0],
                     [94.0, 85.0, 89.0, 95.0],
                     [64.0, 90.0, 73.0, 85.0]])

print(movie_rt)
print(movie_rt[2])
print(type(movie_rt[movie_rt > 80]))

for row in movie_rt:
    print(row)
    print(int(row[0]))

test_arr = np.genfromtxt('sample_data.csv', delimiter=',')
for col in range(len(test_arr)):
    print(test_arr[col])