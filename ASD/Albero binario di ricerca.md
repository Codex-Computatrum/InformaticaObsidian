---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure/abr
  - to-do/implementation
aliases:
  - bst
  - BST
  - abr
  - ABR
---
>[!todo] 
>- [ ] Implementazione in C

Un ***BST*** (***Binary Search [[Tree]]***) è una particolare [[Struttura dati|struttura dati]] che permette di effettuare in modo efficiente operazioni come:
- [[ricerca]]
- [[inserimento]]
- [[cancellazione]]
- [[Minimo-massimo|ricerca del massimo/minimo]]
- [[Successore|ricerca del successore]] 
- $\dots$
È organizzato in un [[albero binario]]; ogni nodo, oltre agli attributi per i dati contiene gli attributi $dx$ e $sx$ che puntano rispettivamente la figlio destro e al figlio sinistro.

$$\forall x \in T, \;\;\forall y \in T_{x.sx},\;\; \forall z \in T_{x.dx}\;\;\longrightarrow \;\; y.dato < x.dato \leq z.dato$$
>[!note] 
>Di base un ***BST*** viene letto [[Order-in|in-order]]

---
## Implementazione in C
```C
// da implementare
```
