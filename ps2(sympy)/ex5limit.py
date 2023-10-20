import sympy as sp
x=sp.S('X')
f=(3*x**2-2)/(4*x**2+1)
sp.plot(f)
#horizontal asintote computation
print('limit at infinity',sp.limit(f,x,'+oo'))
print('limit at infinity',sp.limit(f,x,'-oo'))
#two horizontal asintotes exist at 3/4 on both sides of the limit
rightasint = sp.limit(f,x,'+oo')
leftasint = sp.limit(f,x,'-oo')
sp.plot(f,rightasint) # you can plot many functions

# slant asintotes are impossible as a horizontal asintote exists