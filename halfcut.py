def halfCut(f, l, r, eps=1e-4):
    iterNum = 0
    funcNum = 0

    xm = (l+r)/2
    fxm = f(xm)
    funcNum+=1

    xVal = [xm]
    yVal = [fxm]
    while(r-l) > eps:
        iterNum += 1
        L = r-l

        x1 = l+L/4
        x2 = r-L/4

        fx1 = f(x1)
        fx2 = f(x2)
        
        funcNum += 2

        if fx1 < fxm:
            r = xm
            xm = x1
            fxm = fx1
            xVal.append(x1)
            yVal.append(fx1)

        elif fx2 < fxm:
            l = xm
            xm = x2 
            fxm = fx2
            xVal.append(x2)
            yVal.append(fx2)

        else:
            l = x1
            r = x2
            xVal.append(xm)
            yVal.append(fxm)

    xm = (l+r)/2
    xVal.append(xm)
    yVal.append(f(xm))
    return xm, f(xm), iterNum, funcNum, xVal, yVal