from matplotlib import pyplot as plt
import numpy as np

fig, a = plt.subplots(2, 2)
x = np.arange(1, 5)
a[0][0].plot(x, x*x)
a[0][0].set_title("Squre")

a[0][1].plot(x, np.sqrt(x))
a[0][1].set_title("Squre Root")

a[1][0].plot(x, np.exp(x))
a[1][0].set_title("Exp")

a[1][1].plot(x, np.log(x))
a[1][1].set_title("log")

plt.show()

