def Count(A, p, r, k):
    start = True; last = NULL
    cP = p; cR = r; stX = stQ = stR = NULL
    ret = NULL
    while start or stQ != NULL:
        if start:
            x = 0
            if cP <= cR:
                q = (cP + cR) / 2
                if A[q] == k:
                    x = 1
                push(x, stX); push(q, stQ); push(cR, stR)
                cR = q - 1
            else:
                ret = x
                start = False
                last = cR
        else:
            cR = Top(stR); q = top(stQ); x = top(stX)
            if cR != last:
                x = x + ret
                push(cR, stR); push(x, stX); push(q, stQ)
                cP = q + 1; start = True
            else:
                x = x + ret
                pop(stR);pop(stX);pop(stQ)
                ret = x
                last = cR
    return ret  
