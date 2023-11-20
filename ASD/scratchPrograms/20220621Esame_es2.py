def Algo(T, k1, k2):
    L = init()
    if T == NULL:
        return NULL
    else:
        if T->key > k2:
            return Algo(T->sx, k1, k2)
        else if T->key < k1:
            return Algo(T->dx, k1, k2)
        else:
            L.append(T->key)
    return L
        
def AlgoRecursive(T, k1, k2):
    start = True
    last = NULL
    stT = NULL
    cT = T
    while start or stT != NULL:
        if start:
            L = init()
            if cT == NULL:
                return NULL
            else:
                if cT->key > k2:
                    push(cT, stT); cT = cT->sx
                else if cT->key < k1:
                    push(cT, stT); cT = cT -> dx
                else:
                    L.append(T->key)
            start = False
            last = cT
        else: # start = NULL
            cT = top(sT)
            if cT -> key > k2:
                pop(stT)
                last = cT
            else if cT->key < k2:
                pop(stT)
                last = cT
            else:
                L.append(T->key)
    return L
