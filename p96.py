import numpy as np

a = np.arange(0, 60, 5)
print(a)

a = a.reshape(3, 4)
print("Original Array", a)

print("Transpose of The original array is:")
b = a.T
print(b)

for i in np.nditer(b):
    print(i)