def RicercaAlberobinario(T, k):
    if T = NULL 
        return NULL
    else:
        if T-key < k:
            return RicercaAlberobinario(T->dx, k)
        else if T-> key > k:
            return RicercaAlberobinario(T->sx, k)
        else
            return T
            
def CancellazioneAlberoBinario(T, k):
    if T == NULL 
        return  NULL
    
    if T->key > dato:
        T->sx = CancellazioneAlberoBinario(T->sx, k)
    else if T->key < dato:
        T->sx = CancellazioneAlberoBinario(T->sx, k)
    else:
        return DeleteNode(T)
    return T

def DeleteNode(T):
    if T->sx == NULL:
        return SkipRight(T)
    else if T->dx = NULL:
        return SkipLeft(T)
    else:
        T->key = Get&DeleteMin(T->dx)
        return T

def Get&DeleteMin(T):
    if T->sx == NULL:
        d = T->key
        r = T-> dx
        Deallocate(T)
        return (d,r)
    else:
        (d, r) = Get&DeleteMin(T->sx)
        return (d, r)

def SkipLeft(T):
    tmp = T->sx
    Deallocate(T)
    return tmp

def SkipRight(T):
    tmp = T-> dx
    Deallocate(T)
    return tmp

def InsertAlberoBinario(T, k):
    if T == NULL:
        return BuildNode(k)
    else:
        if T->key > k:
            return InsertAlberoBinario(T->dx)
        else if T->key < k:
            return InsertAlberoBinario(T->sx)
        return T

def RicercaSuccessore(T, k):
    if T = NULL:
        return T
    else:
        if T->key <= dato:
            return RicercaSuccessore(T->dx, k)
        else:
            s = RicercaSuccessore(T->sx, k)
            if s = NULL:
                return T
            else
                return s

