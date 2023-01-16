#PTP Function

import numpy as np
i = [[15, 18, 16, 63, 44], [19, 4, 29, 5, 20], [24, 4, 54, 6, 4]]

print("Inputted Array ", i)
print("The Range Of Array When The Axix = NO")
print(np.ptp(i))
print("The Range Of Array When The Axix = 0")
print(np.ptp(i, axis=0))
print("The Range Of Array When The Axix = 1")
print(np.ptp(i, axis=1))
