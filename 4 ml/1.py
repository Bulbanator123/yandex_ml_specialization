import numpy as np


def gradient_descent(func, start_point, gamma, epsilon, steps):
    delta_x = 1e-9
    start_point = np.atleast_1d(np.array(start_point, dtype=float))
    result = [start_point.copy()]

    def numerical_gradient(func, x):

        gradient = np.zeros_like(x)

        for i in range(len(x)):
            x_plus_delta = x.copy()
            x_plus_delta[i] += delta_x
            gradient[i] = ((func(x_plus_delta)) - func(x)) / delta_x
            
        return gradient
    
    if steps == 0:
        while True:
            new_start_point = start_point - gamma * numerical_gradient(func, start_point)
            result.append(new_start_point.copy())

            if abs(func(new_start_point) - func(start_point)) < epsilon:
                break

            start_point = new_start_point
    else:
        for _ in range(steps):
            start_point = start_point - gamma * numerical_gradient(func, start_point)
            result.append(start_point.copy())

    return np.round(result, 3)

def f1(v):
    x, y = v
    return (x - 2)**2 + (y + 3)**2

history1 = gradient_descent(f1, start_point=[0, 0], gamma=0.1, steps=5, epsilon=0)
print("Тест 1 — история градиентного спуска:\n", history1)