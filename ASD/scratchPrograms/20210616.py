# Si definisca un albero orientato come un grafo orinetato con le seguenti proprieta`: (i) esiste un unico 
# vertice s (detto radice) che raggiunge ogni altro vertice tramite un qualche percorso orientato; (ii) 
# se un qualsiasi vertice v e` raggiungibile da un arbitrario vertice u, allora esiste un solo 
# percorso orientato da u a v. Una foresta oriantata e`, allora, un grafo orientato formato 
# da uno o piu` alberi orientati tra loro non connessi Si scriva un algoritmo che, in tempo lineare 
# sulla dimensione del grafo orientato G = (V, E) fornito in ingresso, verifichi se G e` una foresta orientata oppure no.

# Una foresta è un grafo aciclico
def Algo(G):
    acyclic = Acyclic(G)
    if acyclic:
        return True
    return False


def Acyclic(G):
    Init(G, color)
    for v in V:
        if color[v] == B:
            acyclic = DFS_Acyclic(G, v)
            if !acyclic:
                return False
    return True

def DFS_Acyclic(G, v):
    color[v] == G
    for w in Adj[v]:
        if color[w] == B:
            acyclic = DFS_Acyclic(G, w)
            if !acyclic:
                color[v] = N
                return False
        elif color[w] == G:
            return False
    color[v] = N
    return True
