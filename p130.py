# Dot function
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])

print("Dot Function")
print(np.dot(a, b))

"""
1 2         11 12
3 4         13 14 

1*11=11
2*13=26 37
1*12=12
2*14=28 40

3*11=33
4*13=52 85
3*12=36
4*14=56 92
"""
