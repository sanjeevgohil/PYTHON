import numpy as np

a = np.arange(0, 60, 5)
print(a)

a = a.reshape(3, 4)
print(a)

for i in np.nditer(a):
    print(i)