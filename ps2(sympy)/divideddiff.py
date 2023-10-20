import numpy as np

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
            D[i,j]=(D[i+1,j-1]-D[i,j-1,])/(x[i+j]-x[i])
    
    # We return only the first row
    return D[0,:]
# The arguments are
# D: the vector of coefficients of the Newton expression of the Lagr. int. pol.
# xi are the values of the interpolation points needed for the product
# x is the point where I am computing the value of the interpolation polynomial.
def LagrangePol(D,x):
    n = len(xi)
    val = 0 # Accumulator for the sum
    prod = 1 #accumulator for the products

    for i in range(n):
        sum = sum+D[i]*prod
        prod*(x-xi[i])

    


# Create numerical values of the interpolation points
xi=np.array([-2,0,1,3])
yi=np.array([-16,0,-1,9])

# Call the function
NewtonCoeffs=DivDiffCoef(xi,yi)
print('Newton Coeffs: ',NewtonCoeffs)
x=2
print('Approximation of the value at x=2',LagrangePol(NewtonCoeffs,xi))