import numpy as np

a = np.logspace(1.0, 2.0)
print(a)

a = np.logspace(1.0, 2.0, num=10)
print(a)

a = np.logspace(1.0, 2.0, num=10, base=2)
print(a)
