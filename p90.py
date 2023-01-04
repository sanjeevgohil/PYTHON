import numpy as np

a = np.linspace(10, 20)
print(a)

a = np.linspace(10, 20, 5, endpoint=False)
print(a)

a = np.linspace(10, 20, 5, retstep=True)
print(a)

a = np.linspace(10, 20, 5, endpoint=False, dtype=int)
print(a)
