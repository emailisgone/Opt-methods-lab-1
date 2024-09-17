"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.
2. Aprašykite tikslo funkciją f(x) = (x2-5)2/b-7.
3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^(-4) bei Niutono metodu nuo x_0 = 5 kol žingsnio ilgis didesnis už 10^(-4).
4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.
5. Vizualizuokite tikslo funkciją ir bandymo taškus.
"""

def f(x):
    return ((x**2-5)**2)/7-1

def g(x):    
    return (100-x)**2

"""def dalPus(l, r, eps):
    while (r-l) >= eps:
        x_m = (l+r)/2
        L = r - l
        
        x_1 = l+L/4
        x_2 = r-L/4

        if f(x_1) < f(x_m):
            r = x_m
            x_m = x_1
        elif f(x_2) < f(x_m):
            l = x_m
            x_m = x_2
        else:
            l = x_1
            r = x_2

        if (r-l)<eps:
            break
    
    return x_m"""
