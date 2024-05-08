def Algo(T):
    ret = 0
    if T != NULL:
        if T -> sx == T -> dx == NULL:
            ret = T -> key
        else:
            x = Algo(T -> sx)
            y = Algo(T -> dx)
            ret = x T -> key y
    return ret


def AlgoIterative(T):
    start = True; last = NULL; stT = NULL; cT = T
    while start || stT != NULL:
        if start:
            ret = 0
            acc = 0
            if cT != NULL:
                if cT -> sx == cT -> dx == NULL:
                    ret = cT -> key
                else:
                    push(cT, stT);
                    cT = cT -> sx
            start = False
            last = cT
        else: # start = False risalgo nell'albero di ricorsione
            cT = top(stT)
            if last == cT -> sx: # sto tornando da chiamata a riga 7
                x = acc
                if cT -> dx != NULL: # chiamata a riga 8 da fare
                    cT = cT -> dx
                    start = True # devo riscendere nell'albero di ricorsione
                else: # chiamata a riga 8 da ignoarare
                    acc = ret
                    pop(stT)
                    last = cT
            else: # sto tornando da chiamata a riga 8
                y = acc
                ret = x( T -> key) y 
                acc = ret
                pop(stT)
                last = cT
    return acc







