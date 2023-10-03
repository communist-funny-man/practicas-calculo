# Compute the sum of the Euler series
# Sum (1/i**2), with i between 1 an n
# You can see the series at 
# https://es.wikipedia.org/wiki/Leonhard_Euler

import numpy as np

# Variable for storing the sum (accumulator)
sum=0
# Number of terms to add
# If you increase the number of terms,
# this sum approaches to the exact value
# computed by Euler: pi**2/6
n=100
for i in range(1,n+1):
    sum+=1/i**2

print('The sum of the series is: ',sum)
print('The exact value of the sum is: ',np.pi**2/6)