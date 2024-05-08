---
author: Lorenzo Tecchia
tags:
  - operation/graph
  - algorithm
  - to-do/implementation
aliases:
  - CFC
  - scc
---
Dato un [[grafo]] [[orientato]] [[Cycle|ciclico]], si richiede di identificare le componenti fortemente connesse e un loro [[Ordinamento Topologico|ordine topologico]].

Ricordiamo la definizione di Componenti fortemente connesse:
![[Strongly connected components]]

---
>[!note]- Nota sui grafi connessi
> Per verificare che un grafo sia connesso, possiamo effettuare una [[Depth First Search|DFS]] (o una [[Breadth First Search|BFS]]) e verificare che nell'array dei predecessori non vi esistano due vertici con predecessori a `NULL`.

In questo esempio sono cerchiate le componenti fortemente connesse.
![[Pasted image 20230910163001.png]]
Così com’è non è possibile calcolare le componenti fortemente connesse, dato che non sappiamo da dove parta la visita.
Se ad esempio la visita in [[profondità]] partisse da c, troverebbe anche altre componenti:
- $b,d,e,f$
- $n$
- $g,h,i$
- $j,k,l,m$ 
e la includerebbe nella sua , formando quindi un'unica componente, il che è sbagliato

Bisogna quindi seguire tre step:
1. Eseguire una prima $\textbf{DFS}$ per ottenere in uno stack l'ordine inverso di visita dei nodi
2. Calcolare il grafo trasposto $G^T$ di $G$
3. Eseguire una $\textbf{DFS}$ leggermente modificata su $G^T$ e sullo [[stack]] $S$ restituito dalla prima $\textbf{DFS}$.

La prima $\textbf{DFS}$ restituisce anche uno stack $S$ con i vertici ordinati in modo decrescente per tempo di fine visita, ovvero dall’ultimo che finisce al primo che finisce.

La visita in $G^T$ viene fatta sui vertici nello stack $S$ (dalla $\textbf{DFS}$ di prima)
![[Pasted image 20230910163336.png]]
- Parte da $a$ ma non ci sono archi uscenti, quindi termina la sua visita.
- Continua con $o$ ma non ci sono archi uscenti, quindi termina la sua visita.
- Continua con $c$ ma non ci sono archi uscenti, quindi termina la sua visita.
- Continua con $j$ c'è un arco uscente quindi scende in $m$:
	- $m$ scende in $l$
	- $l$ prova a visitare $j$ ma è stato già scoperto; visita $k$
	- $k$ prova a visitare $j$ ma  è stato già scoperto.
	- ***Le viste terminano***
- E così via per tutti gli altri nodi

Se non avessimo trasposto il grafo, nella prima visita, il nodo $a$ avrebbe trovato $b$ e $c$ come archi uscenti e il risultato sarebbe stato sbagliato.

## Algoritmi
>[!important] 
>$$G=<V,E>\;\;\;G^{T}=<V,E^{-1}>$$


```Python
def DFS1(G):
	c = Init(G) # c is for color
	StackRET = NULL
	for v in V:
		if c(v) == bn:
			StackRET = DFS1_Visit(G, v, StackRET)
	return StackRET
```
^DFS-Stack

```python
def DFS1_Visit(G, v, Stack):
	c(v) = gr
	for w in Adj[v]:
		if c(w) == bn:
			Stack = DFS1_Visit(G, w, Stack)
	c(v) = nr
	Push(v, Stack)
	return Stack
```
^DFS-Visit-Stack

```python 
def Transpose(G):
	VGt = VG
	for v in VG:
		for w in Adj[v]:
			EGt = Insert(EGt, (w,v))
	return (VGt, EGt)
```
^Transpose

- I vertici rimangono gli stessi, quindi faccio una semplice copia.
- Gli archi sono rappresentati dagli adiacenti di un vertice, in questo caso da $v$ a $w$.
- Basterà quindi inserire nell’insieme degli archi del grafo trasposto $E_{G^{T}}$ , l’arco che va da $w$ a $v$.

### Strongly [[Connected]] Component
Il vettore ***scc*** contiene il vertice rappresentante della componente alla quale l’$i$-esimo vertice partecipa.

Ad esempio, la componente $j, k, l, m$ ha come rappresentate $j$ solo perché compare prima nell’ordinamento topologico, ma ognuno di questi vertici sarebbe potuto esserlo.
- $scc(j):j\;\;\;\;\;j$ si trova nella componente con rappresentante $j$
- $scc(k):j\;\;\;\;\;k$ si trova nella componente con rappresentante $j$
- $scc(l):j\;\;\;\;\;l$ si trova nella componente con rappresentante $j$
- $scc(m):j\;\;\;\;\;m$ si trova nella componente con rappresentante $j$

```python
def DFS_SCC(G, S):
	(c,scc) = Init(G)
	while isNotEmpty(S):
		(S,v) = TopAndPop(S)
		if c(v) == B:
			(c,scc) = DFS_SCC_Visit(G,c,scc,v,v)
	return scc
```
^DFS-SCC

- $Init$ imposta i colori dei vertici a bianco e dichiara un vettore $scc$
- Scorre i vertici dello stack, ovvero i vertici dell’ordinamento topologico ordinati in ordine inverso sul tempo di fine visita, ed esegue una $\textbf{DFS}$ su di essi.
```python
def DFS_SCC_Visit(G, c, scc, v, w)
	(c(w), scc(w)) = (gr , v)
	for z in Adj[w]:
		if c(z) == B:
			(c,scc) = DFS_SCC_Visit(G, c, scc, v, z)
	c(w) = N
	return (c, scc)
```
^DFS-SCC-Visit

- Il parametro $v$ è il vertice rappresentante della componente.
- Il parametro $w$ è il vertice attuale.
- Lo scopo è quello di scendere in profondità impostando la componente rappresentante di ogni vertice della componente, ovvero $scc(w) \leftarrow v$ 

## Implementazione
```C
// da implementare
```
