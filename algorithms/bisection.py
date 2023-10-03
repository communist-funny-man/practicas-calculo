import numpy as np

def f(x):
    return np.sin(x)-x/2

a=np.pi/2
b=np.pi
maxit=100
for i in range(maxit):
    x=(a+b)/2
    if (f(a)*f(x)<0):
        b=x
    else:
        a=x
print('Solution: ',x)
print(f(x))
