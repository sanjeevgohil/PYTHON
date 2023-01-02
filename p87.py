import numpy as np
l1 = range(5)
it = iter(l1)
a = np.fromiter(it, dtype=float)
print(a)
print(type(a))