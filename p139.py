import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 10)
y = np.sin(x)

print(x)
print(y)

plt.plot(x, y, "-r")
plt.show()