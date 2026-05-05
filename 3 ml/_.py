import numpy as np

# x = np.array([[2, 0, 2, 2], 
#               [5, 3, 3, 5], 
#               [0, 3, 1, 2], 
#               [2, 8, 7, 6], 
#               [7, 1, 3, 2]])


# y = np.array([1, 2, 3, 5, 8])

# w = np.array([-1, 1, 1, -1, 1])
# w_ = w[1:]

# y_ = -1 + np.dot(x, w_)
# print((y-y_))
# print(np.sum((y - y_)**2))



x = np.array(
             [[1, 1, 9, 6, 3],
              [1, 3, 1, 9, 6],
              [1, 6, 3, 1, 9],
              [1, 9, 6, 3, 1],
              [1, 1, 0, 1, 0]])

y = np.array([2, 1, 3, -1, 1])

l = 1

x_1 = np.transpose(x)
print(x_1)
x_1_x = np.linalg.inv(np.dot(x_1, x) + l*l*np.eye(5, 5))
print(np.dot(x_1, x))
x_1_y = np.dot(x_1, y)
print(x_1_y)    ,
print(np.dot(x_1_x, x_1_y))