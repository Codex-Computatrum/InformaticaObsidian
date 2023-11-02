def Algorithm(T,k):
    last = NUll
    start = True
    cT = T; cA = a
    stT = stA = NULL
    while stT != NULL or start:
        ret = NULL
        if start:
            cA = NULL
            if cT != NULL:
                if cT ->key < k:
                    push(cT, stT); push(cA, stA)
                    cT = cT -> dx
                else if cT->key > k:
                    push(cT, stT); push(cA, stA)
                    cT = cT -> sx
                else:
                   push(cT, stT)
                   cT = cT -> dx
            else:
                last = cT; start = False
        else:
            cT = top(stT)
            if cT->key < k:
                
