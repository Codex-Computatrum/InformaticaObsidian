---
tags:
  - definition
  - to-do/implementation
  - algorithm/graph/search
  - graph
author: Lorenzo Tecchia
aliases:
  - DFS
  - dfs
---
![[Pasted image 20230908170349.png]]
- Inizialmente tutti i nodi vengono colorati di **bianco**.
- Supponiamo che la visita parta dal nodo $b$, questo viene scoperto e quindi colorato di **grigio**.
    Successivamente esplora la stella uscente.
- Supponiamo che il nodo $b$ visiti prima il nodo $e$, questo viene scoperto e quindi colorato di **grigio**.
- Il controllo passa al nodo $e$ il quale farà la stessa cosa, ovvero esplorare la stella uscente. In questo caso è presente solo $f$ come adiacente.
- Viene ripetuto il procedimento finché il nodo corrente non ha più nodi da esplorare.  
    In questo caso si procede fino al nodo $a$ il quale tenta di visitare $b$ che però è già stato scoperto.
- Il nodo $a$ quindi termina la sua visita e viene colorato di **nero**.  
    Passa il controllo al chiamante, in questo caso $c$ il quale a sua volta non ha altro da visitare, termina la visita e viene colorato di **nero**.  
    E così via fino ad arrivare a $b$ che ha da visitare ancora $d$.
- Il nodo $d$ tenta di visitare $f$ ma che è già stato visitato, termina la sua visita, viene colorato di **nero** e passa il controllo a $b$.
- Anche $b$ ha terminato e viene colorato di **nero**.
- Non essendoci più nodi da visitare, l’[[algoritmo]] termina.
## Funzionamento dell'algoritmo

```python
def DFS(G):
	(c,p) = Init(G)
	t = 0
	for v in V:
		if c(v) = bn:
			(c, p, d, f, t) = DFSVisit(G, v, c, p ,d, f, t)
	return (c, p, d, f)
```
^DFS

- La funzione $\textbf{DFS}$ esegue la visita su tutti i nodi bianchi del [[grafo]].
- La funzione di visita $\textbf{DFSVisit}$ partirà da un certo nodo e scorrerà fino in fondo, colorando i nodi che incontra.
- Di conseguenza, il $for each$ in $\textbf{DFS}$ non visiterà nuovamente i nodi già visitati da qualche altro nodo durante la visita $\textbf{DFSVisit}$
 
```python
def DFSVisit(G, v, c, p, d, f, t):
	(c(v), d(v), t) = (gr, t, t+1)
	for w in Adj[v]:
		if c(w) = bn:
			p(w) = v   # imposto il predecessore di w
			(c, p, d, f, t) = DFSVisit(G, w, c, p, d, f, t)
	(c(v), f(v), t) = (nr, t, t+1)
	return (c, p, d, f, t)
```
^DFS-Visit

- La funzione $\textbf{DFSVisit}$ esegue la vera e propria visita.
- Dato un nodo, $\textbf{DFSVisit}$ ha il compito di scendere, e quindi effettuare la visita, fin tanto che può; ossia finché arriva ad un nodo che non ha archi uscenti.

>[!note] 
> - $t\;\;$ Tempo, è un intero che rappresenta il momento in cui un nodo inizia o finisce la visita
> - $d\;\;$ Vettore del tempo di inizio visita 
> - $f\;\;$ Vettore del tempo di fine visita
> - $c\;\;$ Vettore dei colori
> - $p\;\;$ Vettore dei predecessori

$d, f, t$ sono solo utili a dimostrare il teorema della [[Teorema della struttura a parentesi|struttura a parentesi]] delle $DFS$, non servono per la visita in profondità.
- Ho scoperto il nodo $v$ quindi lo coloro di **grigio**, imposto il tempo di inizio visita con $t$, poi incremento $t$.
- Il nodo corrente $v$ visita la stella uscente.
	- Se il nodo adiacente $w$ non è stato ancora scoperto, ovvero è **bianco**, allora prima di passare al nodo adiacente successivo, scende a visitare $w$.
- Terminata la visita dei suoi adiacenti, $v$ termina il suo lavoro: viene colorato di **nero** e viene impostato il tempo di fine visita  
>[!note]
> Viene assegnato $t$ come tempo di fine visita, ma le chiamate ricorsive l’avranno incrementato, quindi **non è lo stesso di prima**

## Implementazione
```C
// da implementare
```
