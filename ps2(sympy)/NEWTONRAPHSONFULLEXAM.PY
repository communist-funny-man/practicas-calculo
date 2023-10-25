import numpy as np
import sympy as sp

x = sp.symbols('x', real=True) # define la variable simbólica x

f_expr = x**3+2*x-2
f_der_expr = sp.diff(f_expr,x)

f = sp.lambdify(x,f_expr)
f_der = sp.lambdify(x,f_der_expr)

N_max = 10
tol = 1.e-9
x0 = 2.

x_aprox = np.zeros(N_max)
x_aprox[0] = x0

for k in range(1,N_max):
    if f_der(x_aprox[k-1]) < 1.e-14: break

    x_aprox[k] = x_aprox[k-1] - f(x_aprox[k-1])/f_der(x_aprox[k-1])

    if ( (k > 0) and (np.abs(x_aprox[k]-x_aprox[k-1]) / np.abs(x_aprox[k]) < tol) ): break

print('Número de iteraciones realizadas: ', k) 
print('Aproximación de la raíz: ', x_aprox[k])