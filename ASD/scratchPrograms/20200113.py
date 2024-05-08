# Algoritmo ricorsivo
def Algo(T , k1, k2, P):
    ret = 0
    if T != NULL:
        if T -> k < k1:
            ret = Algo(T -> dx, k1, k2, T)
        elif T -> key > k2:
            ret = Algo(T -> dx, k1, k2, T)
        else:
            ret = Algo(T -> dx, k1, k2, T)
            ret = ret || Algo(T -> sx, k1, k2, T)
            if !ret:
                if P -> sx != NULL:
                    P -> sx = CancellaRoot(T)
                else:
                    P -> dx = CancellaRoot(T)
    return ret


# ALgoritmo Iterativo
def Algo(T , k1, k2, P):
    cP = P; cT = T; stT = stP = stRet = NULL
    last = NULL; start = True
    while start or stT != NULL:
        if start:
            if cT != NULL:
                ret = 0; acc = 0
                push(cT, stT); push(cP, stP); cP = cT
                if cT -> k < k1:
                    cT = cT -> dx
                elif cT  -> k > k2:
                    cT = cT -> sx
                else:
                    cT = cT -> dx
            start = False
            last = cT
            acc = ret
        else: # start = False
            cT = top(stT); cP = top(stP)
            if cT -> k < k1:
                ret = acc
                last = cT
            elif cT -> k > k2:
                ret = acc
                last = cT
            else:
                if last = cT -> dx: # sto tornando da riga 10
                    if cT -> sx == NULL: # non devo fare una parte di riga 11
                        ret = ret 
                        if !ret:
                            if cP -> sx != NULL:
                                cP -> sx = CancellaRoot(cT)
                            else:
                                cP -> dx = CancellaRoot(cT)
                        pop(stT); pop(stP)
                        last = cT
                    else: # devo fare la chiamata ricorsiva a riga 11
                        cP = cT; cT = cT -> sx
                        start = True
                else: # sto tornando dalla chiamamta ricorsiva  a riga 11
                    ret = ret || acc
                    if !ret:
                        if cP -> sx != NULL:
                            cP -> sx = CancellaRoot(cT)
                        else:
                            cP -> dx = CancellaRoot(cT)
                    pop(stT); pop(stP)
                    last = cT
            pop(stT); pop(stP)
            last = cT
        acc = ret
    return acc
