import numpy as np

def calculate_inception_score(p_yx: np.ndarray, epsilon): 
    q = np.mean(p_yx, axis=0)
    sumpyx = np.sum(p_yx * np.log((p_yx + epsilon) / (q + epsilon)), axis=1)
    return np.round(np.exp(np.mean(sumpyx)), 3)

p_yx = np.array([
    [1.0, 0.0, 0.0], 
    [0.0, 1.0, 0.0], 
    [1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0],
])
print(calculate_inception_score(p_yx, epsilon=1e-16))