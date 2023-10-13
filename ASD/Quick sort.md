---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Quick sort è un [[algoritmo]] che impiega, nel caso peggiore, $\Theta(n^2)$.
Mediamente però, impiega $\Theta(n\log(n))$ con costanti moltiplicative molto basse.

Nel quick sort, il [[dividi et impera]] agisce in questo modo:
- **Dividi**: 
	- partiziona l'array $A[p \dots r ]$ in due sotto-array $A[p\dots q-1]$ e $A[q\dots r]$ in modo tale che che $A[p \dots q-1]\leq A[q]\leq A[q+1\dots r]$
	- Ogni elemento del primo sotto-array è minore o uguale di $A[q]$ che a sua volta è minore o uguale di tutti gli elementi del secondo sotto-array.
	- I due sotto-array saranno disordinati, ma intanto si ha la proprietà  che gli elementi del primo sono minori o uguali agli elementi del secondo.
- **Impera**: si chiama ricorsivamente QuickSort
- **Combina**: non occorre ordinare i due sotto-array essendo già ordinati tra di loro

![[Pasted image 20230828193954.png]]
$x$ sarà il pivot (perno) intorno al quale verrà partizionato l’array $A[p\dots r]$  
Essendo $i$ incrementato all’interno di un `repeat until` (quindi almeno una volta viene incrementato), allora partirà da $p − 1$ e non da $p$. Stesso discorso per $j$.

---
## Proprietà partition
1. $p \leq q < r$
2. $\forall p \leq i \leq q$    $\forall q+1 \leq j \leq r$,   $A[i] \leq A[j]$ 
---
## [[Analisi asintotica|Analisi]]
>[!important] 
> Per sviluppare una nozione chiara del caso medio di Quicksort, dobbiamo fare un'ipotesi su quanto frequentemente prevediamo di incontrare i vari input


![[appuntiIngenito (dragged) 3.pdf]]

---
## Implementazione in C
```C
// da implementare
```