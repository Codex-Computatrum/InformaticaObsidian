def HgtAVL(T):
    return (x = NULL ? -1 : T.ht)

def UpdateHgtAVL(T):
    h_l = HgtAVL(T->sx)
    h_r = HgtAVL(T->dx)
    T.ht = max{h_l, h_r}

def AVLInsert(T, k):
    if T == NULL:
        return BuildNodeAVL(d)
    else:
        if T->key > k:
            T->sx = AVLInsert(T->sx, d)
            T = LBalanceAVL(x)
        else if T->key < k:
            T->dx = AVLInsert(T->dx)
            T = RBalanceAVL(T)
    return T

def AVLDelete(T, k):
    if x != NULL:
        if T->key > k:
            T->sx = AVLDelete(T->sx, k)
            T = RBalanceAVL(T)
        else if T->key < k:
            T->dx = AVLDelete(T->dx,k)
            T = LBalanceAVL(T)
        else:
            T = DeleteNodeAVL(T)
    return T


