"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.
2. Aprašykite tikslo funkciją f(x) = (x2-5)2/b-7.
3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^(-4) bei Niutono metodu nuo x_0 = 5 kol žingsnio ilgis didesnis už 10^(-4).
4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.
5. Vizualizuokite tikslo funkciją ir bandymo taškus.
"""
import math
from datetime import datetime
import sympy as sp
print(f"{datetime.now()}")

def f(x):
    return ((x**2-5)**2)/7-1

def g(x):
    return (100-x)**2

def halfCut(f, l, r, eps=1e-4):
    iterNum = 0
    funcNum = 0

    while(r-l) > eps:
        iterNum += 1
        xm = (l+r)/2
        L = r-l

        x1 = l+L/4
        x2 = r-L/4

        fx1 = f(x1)
        fx2 = f(x2)
        fxm = f(xm)
        funcNum += 3

        if fx1 < fxm:
            r = xm
            xm = x1  
        elif fx2 < fxm:
            l = xm
            xm = x2 
        else:
            l = x1
            r = x2

    xm = (l+r)/2
    return xm, f(xm), iterNum, funcNum

result = halfCut(f, 0, 10)
print("Interval div. Minimum point:", result[0])
print("Interval div. Function value at minimum:", result[1])
print("Interval div. Iterations:", result[2])
print("Interval div. Functions invoked:", result[3])


def goldCut(f, l, r, eps=1e-4):
    tau = (math.sqrt(5)-1)/2
    
    L = r-l
    x1 = l+(1-tau)*L
    x2 = l+tau*L
    fx1 = f(x1)
    fx2 = f(x2)
    
    iterNum = 0
    funcNum = 2  
    
    while(r-l) > eps:
        iterNum += 1
        if fx1<fx2:
            r = x2
            x2 = x1
            fx2 = fx1
            L = r-l
            x1 = l+(1-tau)*L
            fx1 = f(x1)
            funcNum += 1
        else:
            l = x1
            x1 = x2
            fx1 = fx2
            L = r-l
            x2 = l+tau*L
            fx2 = f(x2)
            funcNum += 1

    xm = (l+r)/2
    return xm, f(xm), iterNum, funcNum


result2 = goldCut(f, 0, 10)
print("Gold cut Minimum point:", result2[0])
print("Gold cut Function value at minimum:", result2[1])
print("Gold cut Iterations:", result2[2])
print("Gold cut Functions invoked:", result2[3])

def newton(fSym, x0, eps=1e-4, maxIter=100):
    x = sp.symbols('x')
    
    fIsv = sp.diff(fSym, x)
    fIsv2 = sp.diff(fIsv, x)
    
    fSk = sp.lambdify(x, fSym)
    fIsvSk = sp.lambdify(x, fIsv)
    fIsv2Sk = sp.lambdify(x, fIsv2)
    
    xi = x0
    iterNum = 0
    funcNum = 0
    
    while iterNum < maxIter:
        fIsv_xi = fIsvSk(xi)
        fIsv2_xi = fIsv2Sk(xi)
        funcNum += 2
        
        if abs(fIsv2_xi) < eps:  
            break
        
        xiNext = xi-fIsv_xi/fIsv2_xi
        iterNum += 1
        
        if abs(xiNext-xi) < eps:  
            break
        
        xi = xiNext
    
    return xi, fSk(xi), iterNum, funcNum

x = sp.symbols('x')
fSym = ((x**2-5)**2)/7-1

x0 = 5
result3 = newton(fSym, x0)

print("Newton Minimum point:", result3[0])
print("Newton Function value at minimum:", result3[1])
print("Newton Iterations:", result3[2])
print("Newton Functions invoked:", result3[3])
