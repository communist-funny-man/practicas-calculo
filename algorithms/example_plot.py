# Example of plotting functions

import numpy as np
import matplotlib.pylab as plt

# Generate a vector of x coordinates
x=np.linspace(0,2*np.pi)
# Compute the images by the function
y=np.sin(x)

plt.plot(x,y)

plt.show()

