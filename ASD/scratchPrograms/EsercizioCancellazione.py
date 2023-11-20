def Canc(T, k , p):
    start = True; last = NULL
    stT = stP = NULL; cT = T; cP = p
    while start or ct != NULL:
        if start:
            x = 0
            if cT != NULL:
                if cT -> key > k:
                    push(cT, stT); push(cP, stT)
                    cP = cT; cT = cT -> sx
                else if cT -> key < k:
                    push(cT, stT); push(cP, stT)
                    cP = cT; cT = cT -> dx
                else:
                    if cP != NULL:
                        if cT = cP -> sx:
                            cP -> sx = CancellaRoot(T)
                        else:
                            cP -> dx = CancellaRoot(T)
            else:
                start = False
                last = cT
                ret = x
        else:
            cT = top(stT); cP = top(stP)
            if cT -> key != NULL:
                if cT -> key > k and last != cP -> dx:
                    x = 1 + ret
                    pop(stT); pop(stP)
                    last = cT
                else if cT -> key < k and last != cP -> sx:
                    x = 1 + ret
                    pop(stT); pop(stP)
                    last = cT
                else:
                    if cP != NULL:
                        if cT = cP -> sx:
                            cP -> sx = CancellaRoot(T)
                        else:
                            cP -> dx = CancellaRoot(T)
    return x
