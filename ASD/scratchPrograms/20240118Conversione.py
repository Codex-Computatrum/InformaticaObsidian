
# Algoritmo Ricorsivo
def Algo(T, l1, l2):
    if T != NULL:
        s = Algo(T -> sx, l1 - 1, l2 - 1)
        s = s + Algo(T -> dx , l1 - 1, l2 - 2)
        if l1 > 0 OR l2 < 0:
            s = s + T -> key
        return s
    return 0

# Algorimto Iterativo
def AlogIterative(T , l1, l2):
    cL1 = l1; cL2 = l2; cT = T
    start = True; last = NULL;
    stT = stL1 = stL2 = NULL
    while start or stT != empty:
        if start:
            if cT != NULL:
                push(cT, stT); push(cL1, stL1); push(cL2, stL2)
                cT = cT -> sx; cL1 = cL1 - 1; cL2 = cL2 - 1
            last = cT
            start = False
            ret = 0
        else: # start = False
            cT = top(stT); cL1 = top(stL1); cL2 = top(stL2)
            if last = cT -> sx: # sto tornando dalla prima chiamata ricorsiva
                    s = ret
                if cT -> dx == NULL: # chaiamata ricorsiva a riga 6 da non eseguire
                    if cL1 > 0 OR cL2 < 0:
                        s = s + cT -> key
                    ret = s
                    last = cT
                    pop(sT); pop(stL1); pop(stL2)
                else: # chiamata a riga 6 da fare 
                    push(cT, stT); push(cL1, stL1); push(cL2, stL2)
                    cT = cT -> dx; cL1 = cL1 - 1; cL2 = cL2 - 1
                    start = True
            else: # sto tornando da riga 6
                s = s + ret
                if cL1 > 0 OR cL2 < 0:
                    s = s + cT -> key
                ret = s
                last = cT
                pop(sT); pop(stL1); pop(stL2)
    return ret
