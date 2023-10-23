# Solve x**2-3=0 to compute the decimal places of sqrt(3)
# This kind of algorithms is what is implemented in your calculators
# for computing sqrt(3), for example

import numpy as np

# Define function
def f(x):
    return x**2-3

# Define derivative
def df(x):
    return 2*x

maxit=1000

x=2  # Starting poing (initial guess)
for i in range(maxit):
    x=x-f(x)/df(x)
    if(np.abs(f(x))<1e-15):
        print('Iterations: ',i)
        break
    
print('Approximation of sqrt(3): ',x)
print('Value of sqrt(3) in your calculator or math library: ',np.sqrt(3))
print('THE SAME!')