def TopologicalOrdering(G):
    ge = EnteringDegree(G)      # Per ogni nodo all'interno del grafo calcola il grado entrate
    Q = InitQueue(G, ge)        # inizializza la coda con i gradi entrati
    while !empty(Q):            # itera finquando la coda non è vuota
        (Q,v) = Head&Dequeue(Q) # prende il primo valore uscente della coda
        for w  in Adj[v]:       # itera sugli adiacenti a v, facendo una BFS
            ge(w) = ge(w) - 1   # diminuisce il valore del grado
            if ge(w) == 0:      
                Q = Enqueue(Q, w) 
        p = Append(p,v)         # aggiunge alla lista il nodo v 
    return p

def EnteringDegree(G):
    for v in V:             
        ge = 0                  # da come nr. di gradi entrati 0 a tutti i nodi
    for v in V:
        for w in Adj[w]:        # per tutti i nodi uscenti da v 
            ge(w) = g(w) + 1    # aggiunge 1 al loro grado entrate
    return ge

def InitQueue(G, ge):
    for v in V:
        if ge(v) == 0:
            Q = Enqueue(Q, v)
    return Q

def TopologicalOrdering_1(G):
    c = Init(G)
    for v in V:
        if c(v) == bn:
            s = DFSTopologicalOrdering(G,S,v,c)
    return S

def DFSTopologicalOrdering(G, S, v, c):
    c(v) = gr
    for w in Adj[v]:
        if c(w) == bn:
            S = DFSTopologicalOrdering(G, S, w, c)
    c(v) = nr
    S = Push(S, v)
    return S
