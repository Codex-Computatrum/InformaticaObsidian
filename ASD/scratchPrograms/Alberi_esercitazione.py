def Search(T, k): # Ricerca dell'elemento k 
    if T == NULL:
        return NULL
    else:
        if T->key > k:
            return Search(T->sx,k)
        else if T->key < k:
            return Search(T->dx, k)
        else: 
            return T

def Inserimento(T, k):
    if T == NULL:
        BuildNode(k)
    else: 
        if T->key > k:
            return Inserimento(T->sx, k)
        else if T->key < k:
            return Inserimento(T->dx, k)
        return T

def Cancellazione(T,  k):
    if T == NULL:
        return NULL
    else:
        if T->key > k:
            return Cancellazione(T->sx , k)
        else if T ->key < k:
            return Cancellazione(T->dx, k)
        else:
            DeleteNode(k)

def DeleteNode(T):
    if T->sx == NULL:
        SkipLeft(T)
    else if T->dx == NULL:
        SkipRight(T)
    else:
        Get&DeleteMin(T)
        return T

def Get&DeleteMin(T):
    if T-> sx == NULL:
        d = T->key
        r = T->dx
        Deallocate(T)
        return(d,r)
    else:
        (d,r) = Get&DeleteMin(T->sx)
        T->sx = r
        return (d,r)

def SkipLeft(T):
    tmp = T->sx
    Deallocate(T)
    return tmp

def Minimo(T):
    if T->sx == NULL:
        return T
    else:
        return Minimo(T->sx)

def Massimo(T):
    if T->dx == NULL:
        return T
    else:
        return Massimo(T->dx)


def Successore(T, k, s):
    if T == NULL:
        return s
    else:
        if T->key > k:
            return Successore(T->sx, k, s)
        else T->key < k:
            return Successore(T->dx, k , s)


