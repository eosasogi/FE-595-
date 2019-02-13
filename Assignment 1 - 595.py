import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,2*np.pi,0.1)
sin = np.sin(time)
cos = np.cos(time)
tan = np.tan(time)

plt.plot(time, sin, time, cos, time, tan)
plt.show()
