def Algo(A, p, r, L):
    start = True; last = NULL
    cP = p; cR = r; cL = L
    stL_1 = stR = stP = NULL
    while start or stR != NULL:
        if start:
            x = cL
            if cP <= cR:
                q = (cP + cR) / 2
                L_1 = AllocaNodo()
                L_1 -> key = A[q]
                push(cR, stR); push(L_1, stL_1); push(cP, stP)
                if A[q] % 2 == 0:
                    cP = q + 1
                else:
                    cP = q - 1
            else:
                ret = x
                start = False
                last = cR
        else:
            cR = top(stR);L_1 = top(stL_1);cP = top(stP)
            q = (cP + cR) / 2
            if A[q] % 2 == 0:
                if last != cR:
                    x = ret
                    last = cR
                    pop(stR);pop(stP);pop(stL_1)
                else:
                    L_1 -> next = ret
                    cR = q - 1
                    cL = L_1
                    start = True
            else:
                if last != cR:
                    cP = q + 1
                    cL = L_1
                    start = True
                else:
                    x = ret
                    last = cR
                    pop(stR);pop(stP);pop(stL_1)
    return x
