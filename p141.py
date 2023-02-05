import numpy as np
from matplotlib import pyplot as plt
fig, a = plt.subplots(1, 3)
x = np.arange(1, 5)

a[0].plot(x, x*x, 'g', lw=2)
a[0].grid(True)
a[0].set_title("Default Grid")

a[1].plot(x, np.sqrt(x), 'r')
a[1].grid(color='b', ls="--", lw=0.25)
a[1].set_title("Custom Grid")

a[2].plot(x, x)
a[2].set_title("No Grid")

plt.show()
