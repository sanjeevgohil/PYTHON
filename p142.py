import matplotlib.pyplot as plt
import numpy as np
a1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
a2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3)
a3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)

x = np.arange(1, 20)
a1.plot(x, np.exp(x))
a1.set_title("Exp")

a2.plot(x, np.log(x))
a2.set_title("Log")

a3.plot(x, x*x)
a3.set_title("Squre")

plt.show()