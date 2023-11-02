def BFS(G):
    c = Init(G)
    Q = Enque(Q,v)
    c(v) = bn
    while !empty(Q):
        (Q, v) = Head&Dequeue(Q)
        for w in Adj(v):
            if c(w) == bn:
                (Q, c(w)) = (Enqueue(Q,u), gr)
        c(v) = nr

def Init(G):
    for v in V:
        c(v) = bn

