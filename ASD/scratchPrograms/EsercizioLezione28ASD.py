def QuickSortIterative(A, p, r):
    start = True; last = NULL
    cP = p; cR = r;stR = stQ = NULL
    while start or stQ != NULL:
        if start:
            if cP < cR:
                q = Partiziona(A, p, r)
                push(cR, stR); push(q, stR)
                cR = q 
            else:
                start = False
                last = cR
        else:
            cR = top(cR); q = top(stQ)
            if last != cR:
                push(cR, stR); push(q, stQ)
                cP = q + 1
                start = True
            else:
                last = cR
                pop(stR); pop(stQ)
                

