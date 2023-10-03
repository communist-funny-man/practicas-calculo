import numpy as np

# Working with lists
# This is a Python list
L=[1,2,3,4,5]
# To access the elements we use [], like in C++
# Printing the list
for i in range(0,len(L)):
    print('Element ',i,': ',L[i])

# If we multiply a list by 2, this is creating
# a list with two copies of L
L2=2*L
print('List L2: ',L2)

# Working with numerical arrays
# We can create arrays with floating point values
# in Numpy
x=np.array([1,2,3,4,5])
# Now x is a numerical array
# We can perform math operations with this
# numerical arrays. We can apply functions
# to arrays, and the operations are performed element by element
print('Double of the elements: ',2*x)
print('Sine of the elements: ',np.sin(x))

# We can create special arrays
# Example: Array of 3 equally spaced points in the interval [a,b]
a=0
b=1
x=np.linspace(a,b,3)
print('With linspace: ',x)

# Also we can use arrange, but in this case we give
# the space between the poins as the argument
# Be careful because it stops before the last point
size=0.5
x=np.arange(start=a,stop=b+size,step=0.5)
print('With arange: ',x)

