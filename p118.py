import numpy as np
a = np.array([[30, 40, 70], [80, 20, 20], [50, 90, 10]])
print("Inputted Array")
print(a)

print("Applying ArgMax() ::", np.argmax(a))
print("Applying ArgMin() ::", np.argmin(a))

print("Applying ArgMax() Axix = 0 ::", np.argmax(a, axis=0))
print("Applying ArgMax() Axix = 1 ::", np.argmax(a, axis=1))

print("Applying ArgMin() Axix = 0 ::", np.argmin(a, axis=0))
print("Applying ArgMin() Axix = 1 ::", np.argmin(a, axis=1))

