---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Insertion sort è un [[algoritmo]]  di [[ordinamento]] abbastanza efficiente per l'ordinamento di array di piccole dimensioni.

#### Pseudo codice
![[Pasted image 20230826171202.png]]
---
#### Correttezza
----
#### [[Analisi asintotica|Analisi]] dell'algoritmo iterativo
$$\sum^{n}_{i=1}T_{insert}(A,i) = \sum^{n}_{i=1}\Theta (k^{A}_{i}) = \Theta(\sum^{n}_{i=1}k^{A}_{i})$$
- Se $k^{A}_{i} = i$ (_caso peggiore_)
	$$\sum^{n}_{i=1}i = \frac{n(n+1)}{2} \rightarrow \Theta(n^{2})$$
	`Esempio: 10 9 8 7 6 5 4 3 2 1 0`

- Se $k^{A}_{i} = 1$ (_caso migliore_)
	$$\sum^{n}_{i=1}1 = n \rightarrow \Theta(n)$$
	`Esempio: 0 1 2 3 4 5 6 7 8 9 10`
#### [[Analisi asintotica|Analisi]] dell'algoritmo ricorsivo
![[appuntiIngenito (dragged) 2.pdf]]

---
## Implementazione in C
```C
// da implementare
```