import numpy as np


def snake(m, n):
    a = np.arange(1, m * n + 1).reshape(m, n)
    for i in range(1, m, 2):
        a[i] = np.flip(a[i])
    return a


print(snake(3, 4))