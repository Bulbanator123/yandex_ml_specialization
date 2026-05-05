import numpy as np


def mse(n1, n2):
    return np.mean((n2 - n1)**2)


def rsq(n1, n2):
    n3 = np.mean(n1)
    return 1 - mse(n1, n2) / mse(n3, n1)


n1 = np.array(list(map(float, input().split())))
n2 = np.array(list(map(float, input().split())))
print(f"R2: {rsq(n1, n2):.2f}", sep="\n")