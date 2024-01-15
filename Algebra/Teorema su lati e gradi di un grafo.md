---
author: Simone Parente
tags:
  - algebra/grafi
  - notReviewed
---
Sia $G=(V,L,f)$ un [[Multigrafo semplice|multigrafo finito]], allora:
$$\sum^{}_{v \in V}deg(v)=2|L|$$
### Dimostrazione
Si può dimostrare per induzione oppure alternativamente prendo:
Sia $t$ il numero di estremi dei lati del grafo. Allora $t=2|L|$, visto che ogni lato ha due estremi. Allo stesso tempo, ogni vertice $v$ è estremo di $deg(v)$ lati, dunque $\sum^{}_{v \in V}deg(v)=2|L|$.