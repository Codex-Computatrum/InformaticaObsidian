def Algo(T):
    cT = T; start = True
    last = NULL; stT = st_sx = NULL
    ret = -1
    while start or stT != NULL:
        if start:
            if cT != NULL:
                push(cT, stT)
                cT = cT -> sx
            else:
                start = False
                last = cT
        else:
            cT = top(cT)
            if last != cT -> dx and cT->dx != NULL:
                sx = ret
                push(sx, st_sx)
                cT = cT -> dx
                start = True
            else if last != cT -> dx:
                sx = ret
                dx = -1
                h = 1 + max(sx, dx)
                ret = h
                last = cT
                start = False
                pop(stT)
            else:
                dx = ret
                sx = Top(st_sx)
                h = 1 + max(sx, dx)
                ret = h
                last = cT
                start = False
                pop(stT)
                pop(st_sx)
    return ret
