# Algoritmo Iterativo
def Algo(T , k1, k2, L):
    if T != NULL:
        L = Algo(T -> sx, k1, k2, L)
        if T -> key >= k1 && T -> key <= k2:
            L = InserisciInTesta(T -> key, L)
        L = Algo(T -> dx, k1, k2, L)
    return L

# Algoritmo Iterativo
def AlgoIterativ(T , k1, k2, L):
    cT = T; cL = L
    stT = NULL; last = NULL; start = True
    while start or stT != NULL:
        if start:
            if cT != NULL:
            ret = NULL
                push(cT, stT); cT = cT -> sx
            start = False
            last = cT
            ret = cL
        else: # start = False
            cT = top(stT)
            if last == cT -> sx: # sto ritornando da sx
                cL = ret
                if cT -> key >= k1 && cT -> key <= k2:
                    cL = InserisciInTesta(cT -> key, cL)
                if cT -> dx != NULL: # devo fare la chiamata a riga 7
                    cT = cT -> dx
                    start = True # così riscendo nelle chiamate ricorsive
                pops(stT); last = cT
                ret = cL
            else: # torno da chiamata a riga 7
                cL = ret
                pop(stT); last = cT
                ret = L
    return ret
