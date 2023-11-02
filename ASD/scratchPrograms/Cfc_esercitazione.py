# CFC:
# 1. Ordinamento Topologico
# 2. Transposizione del grafo
# 3. DFS modificata

def TopologicalOrdering(G):
    ge = EnterDegree(G)
    Q = InitQueue(G, ge)
    while !empty(Q):
        (Q, v) = Head&Dequeue(Q)
        for w in Adj[v]:
            ge(w) = ge(w) - 1
            if ge(w) == 0:
                Q = Enqueue(Q, w)
        p = Append(p, v)
    return p

def EnterDegree(G):
    for v in V:
        ge(v) = 0
    for v in V:
        for w in Adj[v]:
            ge(w) = ge(w) + 1
    return ge

def InitQueue(G, ge):
    for v in V:
        if ge(v) == 0:
            Q = Enqueue(Q, v)
    return Q
