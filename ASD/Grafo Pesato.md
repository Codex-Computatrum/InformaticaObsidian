---
author: Giulia Gargiulo
tags:
  - algorithm
  - definition
  - dataStructure
  - operation/graph
  - graph
---
Un ***grafo pesato*** è un [[grafo]] $G =(V, E, w)$, dove  $w: E\rightarrow \mathbb{R}$ è una funzione che associa un numero reale chiamato peso ad ogni arco.
Sia $π=v_1v_2\dots v_{k-1}v_k$ un [[Path|percorso]] in G, allora il peso di questo percorso è uguale a: $$w(π)=\sum_{i=1}^{k-1}\limits w(v_i,v_{i+1})$$

Definiamo il peso del percorso minimo da $u$  a $v$: 
$$\delta(u, v) = \begin{cases}\min \{w(p): u \rightarrow v\} & \text { se esiste un percorso da u a v}\\ \infty & \text { altrimenti }\end{cases} $$

Un percorso minimo da $u$ a $v$ è un qualsiasi percorso con peso $w(p)=\delta(u, v)$

>[!important] 
> L'obiettivo degli algoritmi seguenti è quello di, dato un grafo $G =(V, E, w)$, trovare il percorso minimo da un vertice sorgente $s\in V$ ad un qualsiasi vertice $v\in V$.

###  Lemma 
Dato un grafo pesato ed orientato $G =(V, E, w)$ e sia  $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$ in G,  $\forall \ 1 \leq i  \leq j  \leq k$,  $π_{ij} =v_iv_{i+1}\dots v_j$ è il sotto-percorso  da $v_i$ a $v_j$. 
Allora $π_{ij}$ è un percorso minimo da $v_i$ a $v_j$.
>[!note] 
> Ogni sotto-percorso di un percorso minimo è a sua volta un percorso minimo.

---
### Archi a peso negativo
Se un grafo $G = (V, E, w)$ contiene archi a peso negativo ma non contiene cicli a peso negativo raggiungibili da $s$, allora $\forall \ v \in V$, il peso del percorso minimo rimane ben definito.

Invece, se il grafo contiene cicli a peso negativo raggiungibili da $s$, non è possibile definire un percorso minimo, perchè possiamo trovare sempre un percorso a peso minore seguendo il precedente percorso minimo e passando per un ciclo negativo.
Quindi, se nel grafo è presente un ciclo a peso negativo raggiungibile da $s$, definiamo $\delta(s, v) = -\infty$.

>[!note] 
> Un percorso minimo non può contenere nemmeno cicli positivi, perchè togliendo un ciclo da un percorso minimo, trovo un altro percorso minimo.

---
### Inizializzazione delle stime

Gli algoritmi che risolvono il problema del percorso minimo usano la tecnica di rilassamento degli archi. Per ogni vertice $v \in V$, viene conservato un attributo, $d[v]$, che indica il limite superiore del peso del percorso minimo da $s$ a $v$, cioè la sua stima.

```python
def Init(G, s):
	for v in V
		d[v]= ∞
		Pred[v] = NULL	
	d[s] = 0	
```
^Init-GrafoPesato

- La stima del vertice sorgente viene inizializzata a 0, mentre per ogni vertice $v\in V$, viene inizializzata a $\infty$.
- Il vettore $Pred[v]$ contiene il predecessore di $v$ nel percorso minimo.
---
### Operazione di rilassamento
L'operazione di rilassamento di un arco $(u, v)\in E$ consiste nel verificare se si può migliorare il cammino minimo per $v$ trovato fino a quel momento passando per $u$, e in questo caso, nell'aggiornare $d[v]$ e $Pred[v]$. Altrimenti, il valore di $d[v]$ resta invariato.

```python
def Relax(u, v, w):
	if d[v] > d[u] + w(u, v):
		d[v] = d[u] + w(u, v)   # aggiorno la stima
		Pred[v] = u
```
^Relax

- Viene eseguita in tempo costante

![[Pasted image 20231127100941.png|500]]
>[!example]-
> - Nel caso (a), $d[v]\geq d[u] + w(u, v)$, quindi con l'operazione di rilassamento il valore di $d[v]$ decresce.
> - Nel caso (b), $d[v] \leq d[u] + w(u, v)$ prima di rilassare l'arco, quindi l'operazione di rilassamento lascia d[v] invariato.

---

### Proprietà del percorso minimo e del rilassamento
#### Corollario 1
Dato un grafo pesato $G =(V, E, w)$ e sia  $π=v_{1}v_{2}\dots v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$ , allora  $\delta(v_1, v_k)\leq\delta(v_1, v_{k-1})+w(v_{k-1}, v_k)$

#### Lemma 2
Dato un grafo pesato $G =(V, E, w)$ e $s \in V$. Per ogni arco $(u, v)\in E$ vale che:
$\delta(s, v)\leq\delta(s, u)+w(u, v)$.

#### Lemma 3
Dato un grafo pesato $G =(V, E, w)$ e  un arco $(u, v) \in E$, immediatamente dopo l'esecuzione di $Relax(u, v, w)$ varrà che: $d[v]\leq d[u]+ w(u, v)$.

#### Lemma 4
Dato un grafo pesato $G =(V, E, w)$ e posti $d[v]= \infty$,  $\forall v \in V \setminus \{s\}$ e $d[s] = 0$ lungo una qualsiasi sequenza di operazioni di rilassamento vale sempre: $d[v]\geq \delta(s, v), \ \forall v \in V$
##### Dimostrazione
Dimostrazione per ***induzione*** sul ***numero delle operazioni di rilassamento*** $i$:

***Caso base:*** 
 Se $i =0$, è ovvio, perché non viene eseguita nessuna operazione di rilassamento, e dopo l'inizializzazione vale: $d[v]=\infty$, quindi  $d[v]\geq \delta(s, v)\ \forall \ v\in V\setminus\{s\}$ e $d[s]=0\geq\delta(s,s)$;  in particolare $\delta(s,s)=-\infty$ se $s$ fa parte di un ciclo a peso negativo, altrimenti $\delta(s,s)=0.$

***Caso induttivo:***
 Se $i >0$, prima della $i-esima$ operazione vale ,per ipotesi induttiva, che: $\forall v \in V, \ d[v]\geq\delta(s, v)$. Consideriamo un arco $(x, y)\in E$, su cui eseguo $Relax(x, y, w)$; poiché l'operazione di rilassamento modifica soltanto $d[y]$, sicuramente $\forall \ v \in V \setminus\{y\}$ vale: $d[v]\geq\delta(s, v)$:
      1. Se prima dell'operazione di rilassamento $d[y]\leq d[x]+w(x,y)$, $Relax(x, y, w)$ non modifica niente, quindi vale $d[y]\geq\delta(s, y)$.
      2. Se prima dell'operazione di rilassamento $d[y]> d[x] + w(x,y)$ allora $Relax(x, y, w)$ rilassa l'arco: $d[y]=d[x]+w(x,y)$. Quindi dal Lemma 2:
	   $d[x]\geq \delta(s,x)$, e di conseguenza $d[x] +w(x,y)\geq \delta(s,x)+w(x,y)\geq \delta(s,y)$.

#### Corollario 2
Siano $s,v \in V$ e sia $s$ la sorgente. Se $v$ è raggiungibile da $s$, in ogni momento lungo una sequenza arbitraria di rilassamenti vale: $d[v]=\delta(s, v)$. Consideriamo le stime iniziali: $d[s]=0,\ d[v]=\infty$.
Di conseguenza, se $v$ non è raggiungibile da $s$, allora $\delta(s, v)=\infty$ e $d[v]\geq\delta(s, v),\ \forall v \in V$

#### Lemma 5
Dato un grafo pesato $G =(V, E, w)$ e sia $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$, inizializzando $d[s]= 0,\ d[v]=\infty$. Presa un'arbitraria sequenza di rilassamento che contiene $Relax(v_{k-1},v_k,w)$, se prima dell'esecuzione di $Relax$ $d[v_{k-1}]=\delta(s, v_{k-1})$, allora dopo l'esecuzione di $Relax$ vale: $d[v_k]=\delta(s, v_k)$.

---
### Algoritmo di Dijkstra
L' [[algoritmo]] di ***Dijkstra*** risolve il problema dei cammini minimi con sorgente singola su un grafo orientato e pesato $G =(V, E, w)$, nel caso in cui tutti i pesi degli archi siano non negativi. Assumiamo quindi che $w(u, v)\geq 0, \ \forall \ (u,v)\in E$.

L'algoritmo conserva un insieme S, che contiene i vertici il cui peso di cammino minimo è già stato determinato, cioè, per tutti i vertici $v\in S$, vale: $d[v]= \delta(s, v)$. L'algoritmo seleziona ripetutamente il vertice $u\in V\setminus S$ con la minima stima di cammino minimo, inserisce $u$ in $S$, e rilassa tutti gli archi uscenti da $u$.

Inoltre, usa una [[Code a priorità|coda a priorità]] $Q$, che contiene tutti i vertici in $V\setminus S$, usando come chiave i rispettivi valori delle stime d.

```python
def Dijkstra(G, s):
	Init(G, s)
	S = ø
	Q = V 
	while Q != ø:
		u = Extract_Min(Q)
		S = S ∪ {u}
		Q = Q - {u}
		for v in Adj[u]:
			Relax(u, v, w)
```
^Dijkstra

- La riga $4$ inizializza la coda a priorità $Q$ con tutti i vertici in $V$.
- Ogni volta che viene eseguito il ciclo $while$ delle righe $5-10$, un vertice $u$ , con la minima stima tra i vertici di $Q$, viene estratto da $Q = V-S$  e  inserito in $S$. 
- Le righe $9-10$, rilassano ogni arco uscente da $u$ e se il cammino minimo per $v$ può essere migliorato passando per $u$, aggiornano la stima $d[v]$ e il predecessore $Pred[v]$.
- Dopo la riga $4$, nessun vertice viene inserito in $Q$, infatti ogni vertice che esce da $Q$ viene inserito in $S$ esattamente una volta, quindi il ciclo $while$ viene eseguito $|V|$ volte.

#### Analisi
Poiché l'algoritmo sceglie sempre il vertice in $Q$ "più vicino" da inserire in $S$, diciamo che esso utilizza una strategia [[greedy]].

Ogni operazione di $Extract\_Min$ richiede tempo $O(V)$, e ci sono $|V|$ operazioni di questo tipo, quindi il tempo totale richiesto da $Extract\_Min$ è $O(V^2)$.

Ogni vertice $v\in V$  viene inserito in $S$ esattamente una volta e ogni arco in $Adj[v]$ viene esaminato nel ciclo $for$ esattamente una volta. 
Poiché ogni lista di adiacenza contiene $|E|$ archi, il ciclo $for$ viene eseguito $|E|$ volte, ognuna delle quali richiede tempo $O(1)$.

Quindi il tempo totale di esecuzione dell'algoritmo è di $O(V^{2}+ E)= O(V^2)$.

---
### Algoritmo di Bellman-Ford

L'algoritmo di Bellman-Ford risolve il problema dei percorsi minimi con sorgente singola nel caso in cui i pesi degli archi possono essere negativi.

Dato un grafo pesato $G=(V,E,w)$ con sorgente $s$, l'algoritmo restituisce un ***valore booleano*** che indica se esiste oppure no un ciclo a peso negativo raggiungibile dalla sorgente. In caso affermativo, l'algoritmo indica che non esiste nessuna soluzione, altrimenti calcola i percorsi minimi e i loro pesi.

Anche questo algoritmo utilizza la tecnica del rilassamento degli archi, diminuendo progressivamente la stima $d[v],\ \forall \ v \in V$, fino a raggiungere il reale peso del percorso minimo $\delta(s,v)$. L'algoritmo restituisce $True$ solo se non esiste un ciclo a peso negativo raggiungibile dalla sorgente.

```python
def Bellman_Ford(G, s):
	Init(G, s)
	for i == 1 in range (|V|-1):
		for (u, v) in E:
			Relax(u, v, w)
	for (u, v) in E:
		if d[v] > d[v] + w(u, v):
			return False
	return True
```
^Bellman-Ford

- Ogni volta che viene eseguito il ciclo $for$ delle righe $3-5$, ogni arco viene rilassato una volta.
- Le righe $6-9$ controllano l'esistenza di cicli a peso negativo e restituiscono il valore booleano appropriato.
#### Analisi
Ogni esecuzione di $Init$ richiede tempo $\Theta(V)$, ogni iterazione del ciclo $for$  alle righe $3-5$ richiede tempo $O(E)$, mentre il ciclo for alle righe $6-9$ richiede anch'esso tempo $O(E)$, quindi il tempo totale di esecuzione dell'algoritmo è $O(VE)$, mentre nel caso peggiore sarà $O(V^3)$.
