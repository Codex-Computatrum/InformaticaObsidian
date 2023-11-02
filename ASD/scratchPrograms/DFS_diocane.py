def DFS(G):
    c = Init(G)
    t = 0
    for v in G.V:
        if c(v) == bn:
            (c,p,d,f,t) = DFSVisit(G,v,c,p,d,f,t)
    return (c,p,d,f)

def DFSVisit(G,v,c,p,d,f,t):
    c(v) = gr
    d(v) = t
    t++
    for w in Adj[v]:
        if c(w) == bn:
            p(w) = v
            (c,p,d,f,t) = DFSVisit(G,w,c,p,d,f,t)
    c(v) = nr
    f(v) = t
    t++
    return (c,p,d,f,t)
