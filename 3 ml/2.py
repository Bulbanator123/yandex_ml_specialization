import numpy as np


def minmax_scale(arr):
    xmin = arr.min(axis=0)
    xmax = arr.max(axis=0)
    
    xdel = np.array([(el == 0) * 1 + el for el in list(xmax - xmin)])


    return (arr - xmin) / xdel


X = np.array([[1, 1, 1]])
print(minmax_scale(X))