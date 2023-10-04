import numpy as np

def f(x):
    return np.sin(x)-x/2 ## why?
## Reason: it is the function

a=np.pi/2
b=np.pi
maxit=100 ## MAXIMUM ITERATIONS
for i in range(maxit):
    x=(a+b)/2
    if (f(a)*f(x)<0): ## selects one of the
        b=x
    else:
        a=x
print('Solution: ',x)
print(f(x))
