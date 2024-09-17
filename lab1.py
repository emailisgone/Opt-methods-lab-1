"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.
2. Aprašykite tikslo funkciją f(x) = (x2-5)2/b-7.
3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^(-4) bei Niutono metodu nuo x_0 = 5 kol žingsnio ilgis didesnis už 10^(-4).
4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.
5. Vizualizuokite tikslo funkciją ir bandymo taškus.
"""
import math
from datetime import datetime
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

        f_xm = f(xm)
        f_x1 = f(x1)
        f_x2 = f(x2)
        funcNum += 3

        if f_x1 < f_xm:
            r = xm
            xm = x1  
        elif f_x2 < f_xm:
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


def golden_section_method(f, l, r, eps=1e-4):
    tau = (math.sqrt(5)-1)/2
    
    L = r-l
    x1 = l+(1-tau)*L
    x2 = l+tau*L
    f_x1 = f(x1)
    f_x2 = f(x2)
    
    iterNum = 0
    funcNum = 2  
    
    while(r-l) > eps:
        iterNum += 1
        if f_x1<f_x2:
            r = x2
            x2 = x1
            f_x2 = f_x1
            L = r - l
            x1 = l+(1-tau)*L
            f_x1 = f(x1)
            funcNum += 1
        else:
            l = x1
            x1 = x2
            f_x1 = f_x2
            L = r-l
            x2 = l+tau*L
            f_x2 = f(x2)
            funcNum += 1

    xm = (l+r)/2
    return xm, f(xm), iterNum, funcNum


result2 = golden_section_method(f, 0, 10)
print("Gold cut Minimum point:", result2[0])
print("Gold cut Function value at minimum:", result2[1])
print("Gold cut Iterations:", result2[2])
print("Gold cut Functions invoked:", result2[3])

def isv(f, x, h=1e-4):
    return (f(x+h)-f(x-h))/(2*h)

def isv_2(f, x, h=1e-4):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

def newtons_method(f, x0, eps=1e-4, max_iter=100):
    xi = x0
    iterNum = 0
    funcNum = 0
    
    while iterNum < max_iter:
        fIsv_xi = isv(f, xi)
        fIsv2_xi = isv_2(f, xi)
        funcNum += 5

        if abs(fIsv2_xi) < eps:  
            break
        
        xiNext = xi - fIsv_xi/fIsv2_xi
        iterNum += 1
        
        if abs(xiNext - xi) < eps:
            break
        
        xi = xiNext

    return xi, f(xi), iterNum, funcNum

x0 = 5
result3 = newtons_method(f, 5)

print("Newton Minimum point:", result3[0])
print("Newton Function value at minimum:", result2[1])
print("Newton Iterations:", result3[2])
print("Newton Functions invoked:", result2[3])