import random
#
import matplotlib
import matplotlib.pyplot as plt


def func(x):
    inp = x
    arr_x = []
    arr_y = []
    i = 0
    while x != 1:
        if x % 2 == 1:
            x = x * 3 + 1
        else:
            x = x / 2
        i += 1
        arr_x.append(i)
        arr_y.append(x)

    plt.figure()
    plt.plot(arr_x, arr_y)
    plt.legend([f'(x={inp})'])
    plt.show()

func(random.randint(1,10000))


