#statistical Function
#average

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.mean(a)
w = np.array([4, 3, 2, 1])
print("Average Function ::", np.average(a, weights=w))