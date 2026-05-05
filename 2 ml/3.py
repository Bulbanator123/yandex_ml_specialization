import pandas as pd
import numpy as np


def ed(r1, r2):
    return np.sqrt(np.sum((r1 - r2) ** 2))


def knn(data, n, k):
    t = data[n]
    d = sorted([(ed(t, data[i]), data[i]) for i in range(len(data)) if i != n], key=lambda x: x[0])
    neighbors = [it[1] for it in d[:k]]
    return neighbors


data = pd.read_csv("penguins.csv")
data = data.dropna()
features = np.array(data[["bill_length_mm", "bill_depth_mm"]])

n = int(input())
k = int(input())

neighbors = knn(features, n, k)

print(*neighbors, sep="\n")
