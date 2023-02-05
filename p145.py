import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, math.pi * 2, 0.05)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
y = np.sin(x)
ax.plot(x, y)
ax.set_xlabel("Angel")
ax.set_title("Sine")
ax.set_xticks([0, 2, 4, 6])
ax.set_xticklabels(['Zero', 'Two', 'Four', 'Six'])
ax.set_yticks([1, 0, 2])
ax.set_yticklabels(['One', 'Zero', 'Two'])

plt.show()
