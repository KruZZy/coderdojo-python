import matplotlib.pyplot as plt
import numpy as np

f = np.arange(0, 11)

plt.plot(f, f, 'r', f, 2 ** f, 'g')
plt.show()
