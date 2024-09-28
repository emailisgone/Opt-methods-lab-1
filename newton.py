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

    xVal = [xi]
    yVal = [fSk(xi)]
    
    while iterNum < maxIter:
        fIsv_xi = fIsvSk(xi)
        fIsv2_xi = fIsv2Sk(xi)
        funcNum += 2
        
        if abs(fIsv2_xi) < eps:  
            break
        
        xiNext = xi-fIsv_xi/fIsv2_xi
        iterNum += 1

        xVal.append(xiNext)
        yVal.append(fSk(xiNext))
        
        if abs(xiNext-xi) < eps:  
            break
        
        xi = xiNext
    
    return xi, fSk(xi), iterNum, funcNum, xVal, yVal

x = sp.symbols('x')
fSym = ((x**2-5)**2)/7-1