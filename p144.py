import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

x = np.arange(0, 20, 0.2)

a = np.sin(x)
b = np.cos(x)

ax.plot(a, color='green')
ax.plot(b, color='yellow')
plt.xlim([25, 50])
plt.ylim([0, 1])

plt.show()


