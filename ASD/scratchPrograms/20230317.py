def Algo(T, k):
    if T!= NULL:
        l = Algo(T -> sx, k)
        r = Algo(T -> dx, k)
        max = MAX{l, r}
        if max == -1:
            if T -> key % k == 0:
                return 0
            return -1
        else:
            return max + 1
    else
        return -1

## Algoritmo Iterativo
def AlgoIterative(T, k):
    cT = T; stT = NULL; last = NULL
    start = True
    while start or stT != NULL:
        if start:
            ret = NULL
            if cT != NULL:
                push(cT, stT); cT = cT -> sx
            else:
                ret = -1
                last = cT
                start = False
        else: ## start = False
            cT = top(stT)
            if last == cT -> sx: # torno da riga 3
                l = ret
                r = -1
                if cT -> dx != NULL: # devo fare la chiamata a riga 4
                    cT = cT -> dx; start = False
                else:
                    last = cT
                    ret = -1
            else: # torno da riga 4
                r = ret
                max = MAX{l,r}
                if max == -1:
                    if cT -> key % k == 0:
                        ret = 0
                    ret = -1
                else:
                    ret = max + 1
            pop(stT)
            last = cT
    return ret
