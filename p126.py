#copy and view

import numpy as np
a = np.arange(6).reshape(3, 2)
print(a)
print("Create view of A:", a.view())
print("Create Copy of A:", a.copy())