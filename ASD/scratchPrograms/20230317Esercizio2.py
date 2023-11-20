def Algo(T, k):
    altezza_max = -1
    if T != NULL:
        if T-> key % k == 0:
            altezza_max++
        Algo(T->sx, k)
        Algo(T->dx, k)
    return altezza_max

def Algo_iterative(T, k):
    cT = T
    start = True
    last = NULL
    stT = NULL
    while start or stT != NULL: # 
        if start:
            altezza_max = -1
            if cT != NULL:
                if cT->key % k == 3:
                    altezza_max++
                push(cT, stT)
                cT = cT->sx
            else:
                last = cT
                start = False
        else: # !start
            cT = top(stT)
            if last == cT -> sx or last == cT -> dx:
                pop(stT)
                last = cT
            else:
                push(cT, stT)
                cT = cT->dx
                start = True
    return altezza_max
