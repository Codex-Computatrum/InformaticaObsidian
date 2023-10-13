---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure
  - operation
  - to-do/implementation
---
>[!todo] 
>- [ ] [[Visita in ampiezza]] generalizzata

---
## Alberi binari 
Per la [[visita in ampiezza]] c'è bisogno di una [[struttura dati]] accessori: la [[coda]].

- Estraggo il nodo in testa, lo utilizzo, poi accodo i figli nel caso li abbia.
	- Verrà inizialmente accodata la radice fuori dal $repeat \dots until$ 
### Implementazione dell'[[algoritmo]]
![[Pasted image 20230829172608.png]]
- $Q$ è la coda, struttura d'appoggio
- $Enqueue$ inserisce la radice $x$ in $EmptyQueue$ 
- $EmptyQueue$ è una generica coda vuota

Dato che l’algoritmo non sfrutta la struttura dell’albero, ma quella della coda, conviene farlo iterativo.

Lo scorrimento in ampiezza scorre tutti i nodi, quindi non può fare meglio di: $n \rightarrow \Omega(n)$
Un nodo, una volta visitato, non verrà più visitato, quindi non può fare peggio di: $n \rightarrow O(n)$ 

## Implementazione
```C
// da implementare
```
