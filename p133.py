# Matmul

import numpy as np
a = [[1, 0], [0, 1]]
b = [[-8, 4], [2, 5]]

print(a)
print(b)

print(np.matmul(a, b))

"""
1*-8=-8 -8
0*-8=0
0*2=0
1*2=2    2   

1*4=4   4   
0*5=0
0*4=0
1*5=5   5

"""