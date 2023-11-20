def Algoritmo(A, l, r):
    cL = l; cR = r
    stL = stR = stK = NULL
    start = True
    last = NULL
    ret = 0
    while start or stL != NULL:
        z = 0
        if start:
            s = cR - cL + 1
            if s <= 3:
                z += S(A, cL, cR)
                return z
            else:
                cK = s / 3
                push(cL, stL); push(cR, stR); push(cK, stK)
                cR -= ck; 
            last = cL
            start = False
        else: # start == False
            cL = top(stL); cR = top(cR)
            h = s /2
            if s > 3:
                pop(stL); pop(stR); pop(stK)
                ret = z
                last = cL
                if last > cL:
                    if last - cL == h:
                        push(cL, stL); push(cR, stR)
                        cL += h; cR -= h
                        start = True
                    push(cL, stL); push(cR, stR); push(cK, stK)
                    cL += cK
                    start = True
                else:
                    pop(stL); pop(stK); pop(stR)
                    ret += z; last = cL
                    if last - cL == cK:
                        pop(stL);pop(stR);pop(stK)
                        last = cL; ret -= z
    return ret
