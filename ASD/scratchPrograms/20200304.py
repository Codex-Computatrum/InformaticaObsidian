k# Algoritmo Ricorsivo
def Algo(T, h, k):
    ret = 0
    if T != NULL & & h > 0:
        if T -> key < k:
            ret = Algo(T -> dx, h - 2, k)
        else:
            if T -> key % 2 == 0:
                ret = 1
            x = ret + Algo(T -> sx, h/2, k)
            ret = x + Algo(T -> dx, h - 1, k)
    return ret

# Algoritmo iterativo


def Algo(T, h, k):
    cT = T
    cH = h
    start = True
    stT = stH = stRet = NULL
    last = NULL
    while start or stT != NULL:
        if start:
            ret = 0
            acc = 0
            if cT != NULL & & cH > 0:
                if cT -> key < k:
                    push(cT, stT)
                    push(cH, stH)
                    cT = cT -> dx
                    cH = cH - 2
                else:
                    if cT -> key % 2 == 0:
                        ret = 1
                    push(cT, stT)
                    push(cH, stH)
                    cT = ctT -> sx
                    cH = cH / 2
            acc = ret
            start = False
            last = cT
        else:  # start = False
            cT = top(stT)
            cH = top(stH)
            if cT -> key < k:
                pop(stT)
                pop(stH)
                ret = acc
                last = cT
            else:
                if cT -> key % 2 == 0:
                    ret = 1
                if last == cT -> sx:  # torno dalla chiamata a riga 10
                    if cT -> dx == NULL:  # chaiamata a riga 11 da non fare
                        x = ret + acc
                        last = cT
                        acc = ret
                        pop(stT)
                        pop(stH)
                    else:  # chiamata a riga 11 da fare
                        push(ret, stRet)
                        # push(cT, stT); push(cH, stH)
                        cT = cT -> dx
                        cH = cH - 1
                        start = True
                else:  # torno dalla chiamata 11
                    ret = top & pop(stRet)
                    ret = x + acc
                    last = cT
                    acc = ret
                    pop(stT)
                    pop(stH)
    return acc
