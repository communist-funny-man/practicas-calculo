# bisection algorithm
import numpy as np
i=1
a=(np.pi/2)
b= np.pi
# function definition
def f(x):
    return np.sin(x)-x/2
for i in range(900):
    x=(a+b)/2
    if (f(a)*f(b)<0):
        b=x
else:
    a=x
print('SOLUTION: ',x)
    
