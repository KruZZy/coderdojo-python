import matplotlib.pyplot as plt
import numpy as np

f = np.arange(0, 10000)

plt.plot(f, f, 'r', f, f**2, 'g')
plt.show()
