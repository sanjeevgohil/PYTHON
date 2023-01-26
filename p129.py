# Matrix Library

import numpy.matlib as m1
print("Empty Array is ", m1.empty((3, 3)))
print("Zero Array is ", m1.zeros((3, 3)))
print("One Array is ", m1.ones((3, 3)))
print("random Array is ", m1.rand((3, 3)))

print("Eye Function")
print(m1.eye(n=4, M=4, k=0))

print("Indentify Function")
print(m1.eye(n=4, dtype=int))
