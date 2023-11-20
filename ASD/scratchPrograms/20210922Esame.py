# L'algoritmo deve verificare che il grafo in questione contenga un ciclo: che quindi dati due # indici esiste un path da uno all'altro e viceversa. E che i colori dei due debbano essere
# diversi, in questo caso uno rosso e uno verde. Ma tutti gli algoritmi di DFS  che abbiamo
# visto sono in realta possibili con solo due colori. Che in questo caso possono essere rosso
# e verde. Partendo da un vertice v e un finendo nello stesso vertice v possiamo fermarci al
# vertice esattamente precedente u sapendo che al penultimo passo non avendo completato il 
# ciclo fino a v, quest ultimo non avrà lo stesso colore del suo predecessore.
# Dato che stiamo usando una versione modificata della dfs nell'utilizzo di controlli e non nel# reale funzionamento delle cose,  la complessità sarebbe $\Theta(|V|+ |E|)$

def Algo(G, color[red, green]):
    if !Acycliclic(G, color[red, green]):
        return True
    else:
        return False


def Acycliclic(G, color[red, green]):
    c = Init(G, color[0]) # colori vengono inizializzati tutti a rosso 
    for v in V:
        if c(v) == color[0]:
            acyclic = DFSAcyclicModified(G,color[red, green], v)
            if !(acyclic):
                return False
    return True

def DFSAcyclicModified(G,color[red, green], v):
    for w in Adj[v]:
        if w == v:
            return False
        else if c(w) == color[1]:
            return True
        else:
            c(w) = color[1]
            acyclic = DFSAcyclicModified(G, w)
    return True
