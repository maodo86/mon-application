import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, lambdify       # librarie pour les symboles et calcul avec des valeurs exactes
#init_printing()           ## formatte la sortie selon l ’interface
print("Résolution équation de la forme a.x**3 + b.x**2 + c.x + d = 0")
response=input("Voulez-vous resoudre une équation (Y/N) : ?")
if response=='Y' or 'y':
    j=complex(0,1)
    x = symbols('x')

    a=float(input("Valeur de a :"))
    b=float(input("Valeur de b :"))
    c=float(input("Valeur de c :"))
    d=float(input("Valeur de d :"))
    a_2=b/a
    a_1=c/a
    a_0=d/a
    q=(3*a_1-a_2**2)/9
    r=(9*a_1*a_2 - 27*a_0 - 2*a_2**3)/54
    P=q**3+r**2
#expression de f(x)y
    expf = a*x**3 +b*x**2 +c*x+d
    f = lambdify(x, expf,"numpy")
#tracé de la  courbe  de f 
    xmin, xmax, ymin, ymax = -10, 10, -50, 50
    plt.axis([xmin, xmax, ymin, ymax])
    t = np.linspace(xmin, xmax, 500)
    y = f(t)
    plt.axhline(color='blue')
    plt.axvline(color='blue')
    plt.grid(True)
    plt.plot(t, y, linestyle='-', linewidth=2, color='red', label=r'$y=f(x)$')
    plt.legend(loc='upper left')

    if P>=0:
        s=(r+P**0.5)**0.5
        t=(r-P**0.5)**0.5
        alpha=-1/3*a_2+(s+t)
        beta=-1/3*a_2-1/2*(s+t)+1/2*j*3**0.5*(s-t)
        gamma=-1/3*a_2-1/2*(s+t)-1/2*j*3**0.5*(s-t)
        gamma1=round(gamma.real,2)+round(gamma.imag,2)*1j
        beta1=round(beta.real,2)+round(beta.imag,2)*1j
        alpha1=round(alpha.real,2)+round(alpha.imag,2)*1j
    else:
        theta=acos(r/(-q**3)**0.5)
        alpha=2*(-q)**0.5*cos(theta/3)-1/3*a_2
        beta=2*(-q)**0.5*cos((theta+2*pi)/3)-1/3*a_2
        gamma=2*(-q)**0.5*cos((theta+4*pi)/3)-1/3*a_2
        gamma1=round(gamma.real,2)+round(gamma.imag,2)*1j
        beta1=round(beta.real,2)+round(beta.imag,2)*1j
        alpha1=round(alpha.real,2)+round(alpha.imag,2)*1j    
    racines=(alpha1,beta1,gamma1)
    print(f"la valeur de P est: {d}")
    print(f"les racines sont : {racines}")