import sympy as sp
import numpy as np
t=sp.S('t')
f=(t**1+1)/t-2
rasin = sp.plot(sp.limit(f,t,'+oo'))
lasin = sp.plot(sp.limit(f,t,'-oo'))
m=sp.limit

##get the code from the M. Teams folder
