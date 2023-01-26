#copy

import numpy as np
a = np.array([1, 2, 3, 4, 5])
x = a.copy()
a[0] = 42
print(a)
print(x)