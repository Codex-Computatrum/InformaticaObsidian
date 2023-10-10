---
tags:
  - Combinatoria
---

Nelle <span style="color:#ffbe0a">disposizioni semplici</span> l'ordine è importante e NON ammette ripetizioni.
$$D_{n,k} = \frac{n!}{(n-k)!}$$
dove: $\forall n,k \in \mathbb{N} \ (k\leq n)$

### Esempio Tris
In una gara di $9$ cavalli bisogna scommettere per indovinare il podio, quante possibili giocate ci sono?
$$D_{9,3}=\frac{9!}{(9-3)!}$$
Questo esempio è riconducibile al [[Principio di Enumerazione]] perché non è altro che la moltiplicazione di tutti i possibili simboli, però poiché non abbiamo ripetizioni, il primo posto ha $9$ possibili scelte, il secondo ne ha $9 - 1$ possibili scelte, perché un elemento è già stato usato per il primo posto.