import numpy as np


def mse(n1, n2):
    return (1 / len(n1)) * np.sum((n2 - n1)**2)

def mae(n1, n2):
    return (1 / len(n1)) * np.sum(abs(n2 - n1))

def rmse(n1, n2):
    return np.sqrt(mse(n1, n2))


n1 = np.array(list(map(float, input().split())))
n2 = np.array(list(map(float, input().split())))
print(n1, n2)
print(f"MSE: {mse(n1, n2):.2f}", f"MAE: {mae(n1, n2):.2f}", f"RMSE: {rmse(n1, n2):.2f}", sep="\n")