#searching

import numpy as np
arr = [1, 2, 3, 3, 3, 4, 5, 6, 6]

print("Array {}".format(arr))
print("Left Most index = {}".format((np.searchsorted(arr, 3, side="Left"))))
print("Right Most index = {}".format((np.searchsorted(arr, 3, side="Right"))))