# Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca su interi $T$ e due valori $k_{1}, k_{2} \in N$,
# cancelli da $T$ le chiavi $k$ comprese tra $k_{1}$ e $k_{2}$ $(k_{1}\leq k \leq k_{2})$. Tale algoritmo dovrà essere efficiente e non far uso né di
# variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.
#
#
# Algoritmo Ricorsivo
def Algo(T, k1, k2):
    if T != NULL:
        T -> sx = Algo(T -> sx, k1, k2)
        T -> dx = Algo(T -> dx, k1, k2)
        if T -> key >= k1 AND T -> key <= k2:
            T = RimuoviNodo(T)
    return T


def RimuoviNodo(T):
    if T -> sx == NULL:
        SkipRight(T)
    elif T -> dx == NULL:
        SkipLeft(T)
    else:
        T -> key = Get & DeleteMin(T -> dx, T)
        return T


def SkipRight(T):
    tmp = T -> dx
    Deallocate(T)
    return tmp


def SkipLeft(T):
    tmp = T -> sx
    Deallocate(T)
    return tmp


def Get&DeleteMin(T, P):
    if T -> sx == NULL:
        key = T -> key
        SwapChild(P, T, T -> dx)
        return key
    else:
        return Get & DeleteMin(T -> sx, T)


def SwapChild(P, T, R):
    if P -> sx == T:
        P -> sx = R
    else:
        P -> dx = R
    Deallocate(T)

# Algoritmo Iterativo
def AlgoIterative(T ,k1, k2):
    cT = T, stT = NULL; last = NULL; start = True
    while start or stT != NULL:
        if start:
            ret = NULL
            if cT != NULL:
                push(cT, stT); cT = cT -> sx
            start = False
            last = cT
            ret = cT
        else: #start = False
            cT = top(stT)
            if last == cT -> sx: # torno dalla chiamata a riga 9
                cT -> sx = ret
                if cT -> dx != NULL: # devo fare la chiamata a riga 10
                    cT = cT -> dx # ho gia cT sullo stack, non faccio il push
                    start = True # riscendo nell'albero di rircorsione
                else: # ignoro la riga 10
                    if cT -> key >= k1 && cT -> key <= k2:
                        cT = RimuoviNodo(cT)
                    ret = cT
                    pop(stT)
                    last = cT
            else: # ritorno da chiamata a riga 10
                cT -> dx = ret
                if cT -> key >= k1 && cT -> key <= k2:
                    cT = RimuoviNodo(cT)
                ret = cT
                pop(stT)
                last = cT
    return ret


