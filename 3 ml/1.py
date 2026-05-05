import numpy as np


def onehot_encoding(arr):
    un = np.unique(arr)
    n = len(np.unique(arr))
    m = {}
    i = 0

    for el in un:
        m[el] = i
        i += 1

    res = np.zeros((len(arr), len(un)), int)
    for i in range(len(arr)):
        res[i][m[arr[i]]] = 1
    
    return res


x = np.array([3, 2, 2, 1])
print(onehot_encoding(x))
