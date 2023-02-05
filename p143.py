import numpy as np
import matplotlib.pyplot as plt
fig, a = plt.subplots(1, 3)
x = np.arange(1, 5)
a[0].plot(x, np.exp(x))
a[0].plot(x, x*2)
a[0].set_title("Normal Scale")
a[0].set_xlabel("X Axis")

a[1].set_ylabel("Y Axis")
a[1].set_xlabel("X Axis")
a[0].xaxis.labelpad = 10
a[1].yaxis.labelpad = 2

a[1].plot(x, np.exp(x))
a[1].plot(x, x**2)
a[1].set_yscale("Log")
a[1].set_title("Logarithmic Scale(y)")
plt.show()