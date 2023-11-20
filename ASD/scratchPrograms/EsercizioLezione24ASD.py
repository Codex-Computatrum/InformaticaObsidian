def Algo(T):
    cT = T
    last = NULL
    start = True
    stT = NULL
    while start or stT != NULL:
        if start:
            if cT != NULL:
                push(cT, stT); cT = cT -> sx
            else: 
                start = False
                last = cT
        else:
            cT = top(stT)
            if last != cT -> dx && cT->dx != NULL:
                push(cT , stT)
                cT = cT -> dx
                start = True
            else:
                Print(cT -> key)
                last = cT
                pop(stT)

