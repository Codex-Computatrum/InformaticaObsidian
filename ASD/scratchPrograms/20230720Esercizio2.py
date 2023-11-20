def Algo(G, A, k, v, w): # tale che esiste un un insieme Z sottoinsieme dell'insieme dei vertici
                      # che soddisfano tale condizione: z in Z solo se tutti i percorsi 
                      # semplici in G che partono da v e terminano in w non passano per z
    Z = init()        # inizializzo una qualsiasi struttura dati 
    DFS(G)            # vado a compiere una dfs su G mettendo ad ogni vertice del grafo tempo
                      # tempo di scoperta e tempo di fine scoperta
    for(i = 0, i <= k, i++): # itero sui vertici 
        if A[i].d > v.d && A[i].f < w.f: # se si verifica questa condizione per il teorema dela struttura a parentesi il vertice è discendente di v e w sarà suo discendente
            pass
        else:
            Z.append(A[i]) # se la condizione di discendenza non si verifica allora il veritice è esterno alla "discendenza" v-w 
    return Z # infine ritorno Z

# la struttura dati grafo presenta flag di scoperta e fine scoperta, assieme ai flag p: parent e a quello di c: color per il corretto funzionamento della DFS
# la DFS ha andamento di tempo lineare su |E| + |V|
def DFS(G):
    c = Init(G)
    t = 0
    for v in V:
        if c(v) == bn:
            (c,p,d,f, t) = DFSVisit(G, v,c,p,d,f,t)
    return (c,p,d,f)

def DFSVisit(G,v,c,p,d,f,t):
    c(v) = gr
    d(v) = t
    t++
    for w in Adj[v]:
        if c(w) == bn:
            p(w) = v
            (c,p,d,f,t) = DFSVisit(G,w,c, p, t, d, f, t)
    c(v) = nr
    f(v) = t
    t++
    return (c,p,d,f, t)
