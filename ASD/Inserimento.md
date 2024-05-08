---
author: Lorenzo Tecchia
tags:
  - operation
  - dataStructure/abr
  - to-do/implementation
---
È importante che la struttura di [[Albero binario di ricerca|BST]] persista anche dopo l’inserimento.  
Per semplicità non considereremo anche il caso dei duplicati; dato che se ci fossero, basterebbe tener traccia di quanti valori duplicati ci sono con un contatore nel nodo in questione.

```python
def Insert(T, k):
	if T = NULL:
		return BuildNode(k)
	else
		if T -> key > k:
			T -> sx = Insert(T -> sx, k)
		else if T -> key < k:
			T -> dx = Insert(T -> dx, k)
		return T	
```
^InsertABR

$BuildNode(d)\rightarrow$ Crea un nuovo nodo con dato $d$
Va a sx o a dx a seconda se il dato è maggiore o minore del nodo alla ricorsione corrente, fino ad arrivare ad un nodo `NULL` dove verrà inserito il nuovo nodo.
![[Pasted image 20230830084407.png]]
Nell’esempio sopra, aggiungo $3$ nell’albero colorato in nero.  
Se il nodo è `NULL`, lo inserisco, altrimenti controllo se ciò che voglio inserire è maggiore o minore del dato corrente.

Scorro ricorsivamente a destra se il dato è maggiore, altrimenti a sinistra; finché non trovo un nodo null dove inserirò il dato.

>[!note]
> L’inserimento fatto in questo modo potrebbe sbilanciare l’albero.  
> Esistono metodi per inserire e mantenere l’albero bilanciato; è più costoso ma ne giovano tutti gli altri algoritmi. 

---
## Implementazione in C
```C
```