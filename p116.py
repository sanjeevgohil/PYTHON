# Sorting

import numpy as np

dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([('Raj', 21), ('Anil', 25), ('Aman', 17), ('Ravi', 27)], dtype=dt)
print("Original Array ::")
print(a)
print("Ordering Name", np.sort(a, order='name'))