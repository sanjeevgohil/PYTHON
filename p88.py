import numpy as np
it = iter(a*a for a in range(6))
a = np.fromiter(it, dtype=float, count=3)
print(a)
print(type(a))