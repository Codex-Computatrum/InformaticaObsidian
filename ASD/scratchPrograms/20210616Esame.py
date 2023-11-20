# L'algoritmo è per trovare l'aciclicità su un grafo orientato. Ma un grafo orientato aciclo
# è una foresta orientata. La complessità è O(|G|)

def Acyclic(G):
    c = Init(G)
    for v in V:
        if c(w) == bn:
            acyclic = DFSAcyclic(G, v)
            if !(acyclic):
                return False
    return True

def DFSAcyclic(G, v):
    c(v) = gr
    for w in Adj[w]:
        if c(w) == bn:
            acyclic = DFSAcyclic(G, w)
            if !(acyclic):
                c(v) = nr
                return False
        else if c(w) == gr:
            return False
    c(v) = nr
    return True

