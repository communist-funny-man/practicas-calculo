import sympy as sp
x=sp.S('x') #symbolic variable defined
f=(sp.Abs(2*x-1)-sp.Abs(2*x+1))/x #symbolic function given by expression
f.subs(x,1)
#compute values of the symbolic function with subs
#substitutes x by 1
print(f)
#left sided limit of function f
print('left sided limit is', sp.limit(f,x,0,dir='-'))
print('Right sided limit is',sp.limit(f,x,0,dir='+'))
sp.plot(f)
g=x**2
sp.plot(f,g,ylim=[-5,1],xlim=[-5,5])
