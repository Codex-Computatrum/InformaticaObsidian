def Acyclic(G):
    c = Init(G)
    for v in V:
        if c(v) == bn:
            acyclic = DFSAcyclic(G, v)
            if !acyclic:
                return False
    return True

def DFSAcyclic(G, v):
    c(v) = gr
    for v in Adj[v]:
        if c(v) == bn:
            DFSAcyclic(G, w)
            if !acyclic:
                c(v) = nr
                return False
        else if c(w) == gr:
            return False
    c(v) = nr
    return True

