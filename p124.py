#searching

import numpy as np
a = np.array([6, 7, 8, 9])
print(a)

print("Sorting Elements", np.searchsorted(a, 7))
print("Sorting Elements", np.searchsorted(a, 7, side='right'))