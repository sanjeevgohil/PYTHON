#stastical function

import numpy as np
a = [[14, 17, 12, 33, 44], [15, 6, 27, 8, 19], [23, 2, 54, 1, 4]]
print(a)

print("Median of Array Axix = NONE ::", np.median(a))
print("Median of Array Axix = 0 ::", np.median(a, axis=0))
print("Median of Array Axix = 1 ::", np.median(a, axis=1))