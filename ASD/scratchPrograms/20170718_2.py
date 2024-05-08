def Algo(T, h):
    ret = - 1
    s = 0; d = 0
    if T != NULL:
        if T -> sx != NULL:
            s = Algo(T -> sx, h + 1)
        if T -> dx != NULL:
            d = Algo(T -> dx, h + 1)
        if s == 0 && d == 0:
            ret = h
        else:
            ret = s + d
    return ret

def AlgoIterative(T, h):
   # ho bisogno di stack per T e h
   # faccio backtracking grazie a T
    cT = T; cH = h
    stT = stH = NULL; start = True
    last = NULL
    while start or stT != NULL:
        if start:
            acc = NULL; ret = -1
            s = 0; d = 0
            if cT != NULL:
                if cT -> sx != NULL:
                    push(cT, stT); push(cH, stH)
                    cT = cT -> sx; cH = cH + 1
            else:
                last = cT
                start = False
                acc = ret
        else: #start == False
            cT = top(stT); cH = top(stH)
            if last == cT -> sx: # sto torndando da riga 6
                s = acc
                if cT -> dx != NULL:
                    start = True
                    cT = cT -> dx; cH = cH + 1
                else:
                    if s == 0 && d == 0:
                        ret = cH
                    else:
                        ret = s + d
            else: # sto tornando da riga 8
                d = acc
                if s == 0 && d == 0:
                    ret = h
                else:
                    ret = s +  d
            pop(stT);pop(stH)
            last = cT
            acc = ret
    return acc


                    


