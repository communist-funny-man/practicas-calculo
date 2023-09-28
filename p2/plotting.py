import numpy as np
import matplotlib.pyplot as plt

arr = np.array([1,2,3,4,5,6])


sn = (np.pi/2)
x = np.linspace(0,sn,10)
y = np.sin(sn)
plt.plot(x,y)
plt.show()