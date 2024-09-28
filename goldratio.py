def goldCut(f, l, r, eps=1e-4):
    tau = (math.sqrt(5)-1)/2
    print(tau)

    L = r-l
    x1 = l+(1-tau)*L
    x2 = l+tau*L
    fx1 = f(x1)
    fx2 = f(x2)
    
    iterNum = 0
    funcNum = 2  

    xVal = [x1, x2]
    yVal = [fx1, fx2]
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
            xVal.append(x1)
            yVal.append(fx1)
        else:
            l = x1
            x1 = x2
            fx1 = fx2
            L = r-l
            x2 = l+tau*L
            fx2 = f(x2)
            funcNum += 1
            xVal.append(x2)
            yVal.append(fx2)

    xm = (l+r)/2
    xVal.append(xm)
    yVal.append(f(xm))
    return xm, f(xm), iterNum, funcNum, xVal, yVal