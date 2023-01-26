# matmul

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 1]])
b = np.array([2, 4])

print(a)
print(b)

print(np.matmul(a,b))

"""
1*2=2  + 2*4=8      10
3*2=6  + 4*4=16     22
5*2=10 + 1*4=4      14
"""