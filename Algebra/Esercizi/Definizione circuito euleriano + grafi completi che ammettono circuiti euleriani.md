---
author: Simone Parente
tags:
  - algebra/grafi/cammini
  - algebra/esercizi/corretti
Esame: 16/01/2023
---
Dare la definizione di circuito euleriano e determinare tutti e soli i numeri interi positivi $n$ tali che il grafo completo $K_n$ su $n$ vertici possieda circuiti euleriani.
### Soluzione
Un circuito o cammino euleriano è un cammino che attraversa tutti i vertici di un grafo una ed una sola volta.
Dato che $G$ è un grafo completo, esso avrà $L=P_2(V)$, di conseguenza sarà connesso e avrà $|L|=\binom{n}{2}$.
Un grafo possiede circuiti euleriani se una di queste condizioni è soddisfatta:
- Ogni vertice ha grado pari.
- Il grafo ha 0 o 2 vertici con grado dispari.

Ogni grafo completo con numero di vertici dispari ammette circuiti euleriani (ogni vertice ha grado $|V|-1$), ogni grafo completo con $2$ vertici ammette circuiti euleriani.