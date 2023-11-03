import sympy as sp
x = sp.S('X')

f=sp.log(1+x)
#center of taylor polynomial
a = 0
#Degree
n=2
#compute first derivative of f
fa = f.subs(x,a)
df = sp.diff(f,x)
dfa = df.subs(x,a)
d2f = sp.diff(f,x,2)
d2fa = d2f.subs(x,a)
# obtain the polynomail
P2 = fa+dfa*(x-a)+d2fa/sp.factorial(2)*(x-a)**2

print(P2)


## AUTOMATIZATION FUNCTION DEFINITION
def TaylorPolynomial(f,n,a):
        P =0
        for i in range(n+1):
            #i-th derivative of the function
            dif = sp.diff(f,x,i)
            P = P+dif.subs(dif,a)/sp.factorial(i)*(x-a)**i
return P

#computing the MCLAURIN POLYNOMIAL AUTOMATIZED
P2 = TaylorPolynomial(f,2,0)
print(P2)