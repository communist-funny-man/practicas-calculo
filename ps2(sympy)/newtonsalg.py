import numpy as np
def f(x):
    return x**2-3
def df(x):
    return 2*x
maxit = 10
x = 2
for i in range(maxit):
    x=x-f(x)/df(x)
print(x)