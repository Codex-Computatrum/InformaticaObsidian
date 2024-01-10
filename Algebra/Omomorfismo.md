---
author: Simone Parente
tags:
  - algebra/basics
---
Un omomorfismo è una [[Algebra/Funzione|funzione]] tra due [[Struttura algebrica|strutture algebriche]] dello stesso tipo che conserva le operazioni in esse definite.
### Esempio su gruppi
Siano $(G, \cdot)$ e $(H,\star)$ due [[Gruppo|gruppi]], un esempio di omomorfismo è l'applicazione:
$$f: G \to H$$
$$\text{definita come } \forall a,b \in G , f(a\cdot b)=f(a) \star f(b)$$
### Esempio sull'anello dei polinomi
Siano $A$ e $A[x]$ due [[Anello Commutativo Unitario|anelli commutativi unitari]].
Per ogni $f=\sum\limits^{n}_{i=0}a_ix^i \in A[x]$ poniamo $f(c)=\sum\limits^{n}_{i=0} a_ic^i$, l'applicazione
$$f \in A[x] \mapsto f(c) \in A$$
è un omomorfismo, detto **omomorfismo di sostituzione**. ^sostituzione