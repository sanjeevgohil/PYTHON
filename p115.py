# Sorting

import numpy as np
a = np.array([[3, 7], [9, 1]])

print("Input Array ::", a)
print("Sort Array ::")
print(np.sort(a))
print("Sort Array Axis=0 ::")
print(np.sort(a, axis=0))
print("Sort Array Axis=1 ::")
print(np.sort(a, axis=1))
