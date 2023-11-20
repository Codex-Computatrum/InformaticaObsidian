def DFS(G):
    (c,p) = Init(G)
    t = 0
    for v in V:
        if c(v) == bn:
            (c,p,d,f) = DFSVisit(G,v,c,p,d,f,t)
    return (c,p,d,f)

def DFSVisit(G, v):
    c(v) = gr
    t++
    for w in Adj[v]:

        
