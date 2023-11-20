---
author: Lorenzo Tecchia
tags:
  - operation
  - dataStructure/abr
  - to-do/implementation
---
 Se il nodo da cancellare non **ha figli**, si elimina il nodo stesso
- Se il nodo $x$ da eliminare **ha un solo figlio**, basta collegare il figlio di $x$ al padre di $x$
	- ![[Pasted image 20230830085528.png]]
- Se il nodo $x$ da eliminare **ha entrambi i figli**, ci sono due possibili modi per eliminare il nodo:
	- Sposto il **MAX del ramo sinistro**
		- Il MAX del ramo sinistro può avere al massimo il figlio destro che è più piccolo. Se avesse anche il figlio destro, non sarebbe il massimo
	- Sposto il **MIN del ramo destro**
		- Il Min del ramo destro può avere al massimo il figlio sinistro che è più grande. Se avesse anche il figlio sinistro, non sarebbe il massimo
#### Esempio
![[Pasted image 20230830090150.png]]
In questo caso è stato spostato il **MIN del ramo destro** dovendo eliminare il nodo con dato $10$.

---
>[!important] 
>Prima di definire il metodo $Delete(x,d)\rightarrow$ il metodo per cancellare il nodo con dato $d$.
>Bisogna trovare il [[Minimo-Massimo|minimo]] (o il massimo) quindi definire tale funzione per gli [[Albero binario di ricerca|BST]]

---
## $\textbf{Delete}$
Questa è la funzione che verrà chiamata per eliminare il nodo contente il dato $d$.
- Cerca il nodo
- Se trovato, chiama la funzione $DeleteNode$
	- Se il nodo ha un solo figlio, verrà fatto [[Minimo-Massimo#$ textbf{SkipRight}$|SkipRight]] se non ha il sinistro, [[Minimo-Massimo#$ textbf{SkipLeft}$|SkipLeft]] se non ha il destro
	- Altrimenti posso eliminarlo in due modi possibili:
		1. ceco il MAX del ramo sinistro
		2. cerco il MIN del ramo destro
	- In questo caso si procede con il MIN 
- Sia $Skip$ che [[Minimo-Massimo#$Get &DeleteMIN$|Get&Delete]] restituiscono un nodo a $DeleteNode$  
- La funzione $DeleteNode$ restituirà un nodo che sarà restituito alla chiamata ricorsiva di $Delete$. Questo verrà inserito al posto del nodo da eliminare

```python 
def Delete(x, d)
	if x = NULL:  # dato non trovato
		return NULL
	# cerco il nodo che contiene il dato
	if d > x.dato:
		x.dx = Delete(x.dx, d)
	else if d < x.dato:
		x.sx = Delete(x.sx, d)
	else   # nodo trovato  
		return DeleteNode(x)
	return x
```

```python
def DeleteNode(x):
	if x.sx = NULL:
		return SkipRight(x)
	else if x.dx = NULL:
		return SkipLeft(x)
	else
		x.dato = GetAndDeleteMin(x.dx, x)
		return x
```

[[Minimo-Massimo#^get-delete-min|Get&DeleteMin]]

---
## Implementazione in C
```C
```