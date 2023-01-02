import numpy as np
a = b"Sanjeev Gohil"
print(type(a))

n = np.frombuffer(a, dtype="S1")
print(n)
print(type(n))

n1 = np.frombuffer(a, dtype="i1")
print(n1)
print(type(n1))

n2 = np.frombuffer(a, dtype="b1")
print(n2)
print(type(n2))

n3 = np.frombuffer(a, dtype="C1")
print(n3)
print(type(n3))

n4 = np.frombuffer(a, dtype="f1")
print(n4)
print(type(n4))

n5 = np.frombuffer(a, dtype="u1")
print(n5)
print(type(n5))