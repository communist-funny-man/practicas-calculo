import numpy as np
import matplotlib.pyplot as plt

def DivDiffCoef(x,y):
    n=len(x)
    print('Number of points: ', n)
    # Create the matrix
    D=np.zeros([n,n])
    
    # Storing the y values in the first column of D
    D[:,0]=y
    
    # Loop in colums j=1,....,n-1
    for j in range(1,n):
        for i in range(0,n-j):
            D[i,j]=(D[i+1,j-1]-D[i,j-1])/(x[i+j]-x[i])
    
    # We return only the first row
    # This means taking all the elements of the first row
    return D[0,:]
    
    
# The arguments are
# D: the vector of coefficients of the Newton expression of the Lagr. int. pol.
# xi, they are the x values of the interpolation
# x, the point where I am computing the valur of the interp. pol
def LagrangePol(D,xi,x):
    n=len(xi)
    val=0 # Accumulator for the sum
    prod=1 # Accumulator for the products
    for i in range(n):
        val=val+D[i]*prod
        prod=prod*(x-xi[i])
    return val
        


# Create numerical values of the interpolation points
xi=np.array([-2,0,1,3])
yi=np.array([-16,0,-1,9])

# Call the function
NewtonCoeffs=DivDiffCoef(xi,yi)
print('Newton Coeffs: ',NewtonCoeffs)


# Plot the Lagrange polynomial and the interpolation points
plt.plot(xi,yi,'ro')
x=np.linspace(-2,3)
plt.plot(x,LagrangePol(NewtonCoeffs,xi,x),'b-')

# Point where I want to approximate the value of the unknown function
x=2
print('Approximation of the value at x=2: ',LagrangePol(NewtonCoeffs,xi,x))
