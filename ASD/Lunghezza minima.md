---
author: Lorenzo Tecchia
tags:
  - algorithm
  - to-do/implementation
---
Calcola il [[Path|percorso]] minimo da $v$ ad $u$. 
Restituisce uno [[stack]] di vertici che rappresentano il percorso.

```python
def MinimalPath(G, v, u):
	(c, -, p) = DistanceBFS(G, v)
	if c(u) = nr:
		return BuildMinimalPath(EmptyStack, p, v, u)
	return EmptyStack
```

- La funzione _[[Calcolo delle distanze|DistanceBFS]]_ colorerà di **nero** tutti i percorsi attraversati da $v$, questo servirà a capire se c’è un percorso da $v$ a $u$, ovvero $(v, u) \in Reach(G)$.
- Inoltre, la funzione _DistanceBFS_ imposta anche i predecessori di ogni nodo e, per come è strutturata la funzione, seguendo a ritroso i predecessori, si ricava il ***percorso minimo***.
Viene impostato il predecessore di un vertice $v$ nel momento in cui questo viene ***scoperto***, ma un vertice viene ***scoperto*** quando il predecessore visita i suoi adiacenti.  
Se il vertice $v$ ha più padri, allora $v$ si troverà nella lista di adiacenza di più vertici. Ma $v$ sarà ***scoperto la prima volta*** dal vertice che ci arriva prima. Chi arriverà dopo, troverà il vertice $v$ già colorato.
Di conseguenza, se si segue il percorso dei predecessori a ritroso, si ricava il percorso minimo.
- Se $u$ è colorato di **nero**, allora vuol dire che $v$ raggiunge $u (\text{ovvero} (v, u) ∈ Reach(G))$ ed è quindi possibile costruire il percorso
- Se $(v, u) \notin Reach(G)$ allora restituisce uno **stack** vuoto, dato che non è possibile costruire il percorso minimo.

```python
def BuildMinimalPath(Sπ, p, v, u):
	(Sπ) = Push(Sπ, u)
	if u != v:
		Sπ = BuildMinimalPath(Sπ, p, v, p(u))
	return Sπ
```

- $S_{\pi}\;\;$ Stack di vertici raffiguranti il percorso
- $p\;\;\;\;$ Vettore dei predecessori

Dato che il percorso viene costruito partendo dall’ultimo vertice e procedendo a ritroso, questi vengono inseriti in uno **stack**. Cosi facendo, quando si leggerà lo **stack**, lo si leggerà partendo dal primo vertice del percorso.

La ricorsione avviene sul parametro $u$ sostituito con il suo predecessore $p(u)$ 
La ricorsione termina quando il predecessore è il vertice iniziale.