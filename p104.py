#Statistical Function
#axix=0 is column
#axix=1 is row

import numpy as np

i = [[15, 18, 16, 63, 44], [19, 4, 29, 5, 20], [24, 4, 54, 6, 4]]
print("Inputted Array")
print("Array Max Value is :", np.amax(i))
print("Array Min Value is :", np.amin(i))

print("Array Max Axis = 0", np.amax(i, axis=0))
print("Array Max Axis = 1", np.amax(i, axis=1))

print("Array Min Axis = 0", np.amin(i, axis=0))
print("Array Min Axis = 1", np.amin(i, axis=1))