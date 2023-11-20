def Algo(A, i, j, x):
    cI = i; cJ = j; cX = x
    stI = stJ = stY = NULL
    start = True
    last = NULL
    accumulatore = NULL
    while start or stY != NULL:
        if start:
            if cJ - cI >= 1:
                y = rand() % 2
                if cX == 1:
                    push(cI, stI); push(cJ, stJ); push(cX, stY)
                    cI = (cI + cJ) / 2; cX = y
                    if ret % 2 == 0:
                        cJ = (cJ + cI) / 2; cX = 1 -y
                else: 
                    push(cI, stI); push(cJ, stJ); push(cX, stY)
                    cJ = (cJ + cI) / 2; cX = 1 -y
                    if ret % 2 == 1:
                        cI = (cI + cJ) / 2 + 1; cX = 1 - y
            else:
                ret = A[i]
                start = False
                last = cX
        else:
            cX = top(stX)
            if cX = 1 && last == cX:
                ret = accumulatore
                if ret  % 2 == 0:
                    accumulatore = ret
            else:
                accumulatore = ret
                if ret % 2 == 1:
                    accumulatore += ret
    return accumulatore
