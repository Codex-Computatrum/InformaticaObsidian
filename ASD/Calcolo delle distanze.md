---
author: Lorenzo Tecchia
tags:
  - algorithm
  - operation/graph
  - to-do/implementation
---
## Funzionamento
![[Pasted image 20230908145019.png|600]]
![[Pasted image 20230908145032.png|500]]
- Imposta il colore di tutti i nodi del grafo a **bianco**
-  Imposta le distanze a **infinito** 
-  Imposta i predecessori a `NULL` ($\bot\;\; bottom$)

>[!important] 
> - $c\;\;$ Vettore dei colori: $\forall u \in V, c(u)=\text{colore}$
> - $d\;\;$ Vettore delle distanze: $\forall u \in V, d(u)=\text{numero}$ ovvero la distanza dal vertice di partenza $v$ a $u$
> - $p\;\;$ Vettore dei predecessori: $\forall u \in V, p(u)=\text{predecessore}$

---
## Complessità
Un vertice può non entrare in [[coda]], ma se entra lo farà una sola volta (data la colorazione).
Nel caso peggiore entrano tutti vertici.

Il $for each$ si traduce nella somma del numero di [[Adjacent|adiacenti]] di $u$, questo $\forall u \in V$ . Non stiamo facendo altro che contare gli archi $|E|= \sum_{u \in V}\Theta(|Adj[u]|) = |E|$

Le istruzioni nel $while$ sono in $\Theta(1)$; come detto prima, nel caso peggiore entrano tutti i vertici, quindi il while si traduce nella $\sum_{u \in V}\Theta(1) = V$

Nel totale avremo:$$\sum\limits_{u\in V}(\Theta(1) + \Theta(|Adj[u]|))= |V|+|E|=|G|$$
## Implementazione
```C
// da implementare
```
