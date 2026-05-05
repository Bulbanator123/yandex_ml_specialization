import numpy as np

def calculate(p, c):
    calc = np.ceil(np.dot(c, p))
    calc = calc.astype(int)
    print("Молоко, литры:", calc[0])
    print("Яйца, штуки:", calc[1])
    print("Мука, кг:", calc[2])




products = np.array([
    [0.1, 2, 0.05],
    [0.2, 1, 0.2],
    [0.5, 3, 0.3]])

cook = [10, 32, 8]

calculate(products, cook)