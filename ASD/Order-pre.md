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
def DFVPre(X, F, a):
	if x != NULL:
		a = F(x.dato, a)
		a = DFVPre(x.sx, F, a)
		a = DFVPre(x.dx, F, a)
	return a
```

- $x$ è il nodo della radice di un albero (quindi anche i sotto-alberi)
- $F$ è una funzione che restituisce un valore $F: D \times A \rightarrow A$
- $a$ valore iniziale dell'accumulatore
---
![[Pasted image 20230829144830.png]]
![[Pasted image 20230829144852.png]]

---
## Implementazione in C
```C
```