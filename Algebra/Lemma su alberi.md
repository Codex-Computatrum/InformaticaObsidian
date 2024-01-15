---
author: Simone Parente
tags:
  - algebra/grafi/alberi
  - notReviewed
---
Sia $T=(V,L)$  un albero, $v \in V$, $(deg(v)=1) \implies v \text{ è una foglia}$; sia $l \in L$, tale che $v$ è un estremo di $l$. Allora $T'=(V \setminus \{v\}, L \setminus \{l\})$ è ancora un albero.
### Dimostrazione
$\forall a,b \in T', a \neq v \land b \neq v \implies \text{ il cammino da } a \text{ a } b \text{ non è } l$, perché ogni vertice in un cammino ha grado $\geq 2$  se non è un estremo.