---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure
  - operation
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C
### Funzionamento

```python
def DFVPost(X, F, a):
	if x != NULL:
		a = DFVPost(x.sx, F, a)
		a = DFVPost(x.dx, F, a)
		a = F(x.dato, a)
	return a
```
^DFV-PostOrder

- $x$ è il nodo della radice di un albero (quindi anche i sotto-alberi)
- $F$ è una funzione che restituisce un valore $F: D \times A \rightarrow A$
- $a$ valore iniziale dell'accumulatore
---
![[Pasted image 20230829154704.png]]
![[Pasted image 20230829154720.png]]

---
## Implementazione in C
```C
```