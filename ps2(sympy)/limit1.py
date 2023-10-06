import sympy as sp
x=sp.S('x') #symbolic variable defined
#compute values of the symbolic function with subs
#substitutes x by 1
sp.Subs(x,1)
f=(sp.Abs(2*x-1)-sp.Abs(2*x+1))/x #symbolic function given by expression
print(f)
