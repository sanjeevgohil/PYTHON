import numpy as np

a = np.array([100, 200, 13, 0, 400, 500, 0])
print(a)
print(np.argsort(a))

"""
0   1   2  3 4   5   6
100 200 13 0 400 500 0
3   4   2  0 5   6   1 

0 0 13 100 200 400 500
3 6 2   0   1   4   5

"""

