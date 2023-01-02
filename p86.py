import numpy as np
a = b"Sanjeev Gohil"
print(type(a))

n = np.frombuffer(a, dtype="S1")
print(n)
print(type(n))

n1 = np.frombuffer(a, dtype="S1", count=4)
print(n1)
print(type(n1))

n2 = np.frombuffer(a, dtype="S1", count=4, offset=4)
print(n2)
print(type(n2))
