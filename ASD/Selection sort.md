---
author: Lorenzo Tecchia
tags: [algorithm, to-do]
---
>[!todo] 
>- [ ] Implementazione in C

Il ***selection sort*** è un [[Algoritmo|algoritmo]] di [[ordinamento]] che opera in place. 

Consiste nel selezionare di volta in volta il minimo valore presente nella sequenza $A[i \dots n]$ e lo si sposta nella $i$-esima posizione. 

Così facendo si viene a creare una sotto-sequenza ordinata da $0$ a $i-1$, trovato il valore minimo lo si sposta all'$i$-esima posizione, e così via.

```python
def SelectionSort(A, n):
	for i = n-1 in range(1):
		m = Max(A, i)
		Swap(A, i, n)
```

```python
def Max(A, i):
	m = 0
	for j = 1 in range(i):
		if A[m] < A[j]:
			m = j
```

---
#### [[Analisi asintotica|Analisi]]
La funzione _Max_ impiega $\Theta(i)$, dato che le istruzioni all'interno del $for$ sono tutte costanti, si ottiene quindi:
$$\sum^{i}_{j=1}1=i$$
La funzione _Max_ viene eseguita $n-1$ volte, nel $for$ della funzione _SelectionSort_.
Il tutto impiega:
$$\sum^{n-1}_{i}\Theta(i) = \sum^{n-1}_{i=1}= \frac{n(n+1)}{2} \rightarrow \Theta(n^{2})$$

---
## Implementazione in C
```C
```