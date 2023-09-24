---
author: Simone Parente, Mario Penna
tags:
  - definition/property
  - theorem
  - example
  - to-do
---
Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]] e  $a \in S$ e [[Elemento Confrontabile|confrontabile]] con tutti gli elementi di $S$:

$$a = min(S) \iff \forall x \in S (a \leq x)$$ ^fad11a
### Esempi
- In $(\mathbb{N}, \leq)$, $min(\mathbb{N})= 0$ ^45dc88
- In $(\mathbb{N}, |)$, $min(\mathbb{N})= 1$, visto che 1 divide tutti i numeri naturali
- $(\mathbb{Z}, \leq)$, $min(\mathbb{Z})= \nexists$
### Esempio
$$S = (\forall (a,b), (c,d) \in \mathbb{N} \times \mathbb{N}) ((a,b) \sigma (c,d)) \iff (a,b) = (c,d) \lor (a \cdot b \leq c \cdot d)$$
$$(e,f)=\min(S) \in \mathbb{N} \times \mathbb{N}\iff \forall (x,y) \in S ((e,f) \sigma (x,y)) \iff (e,f)=(x,y) \lor e \cdot f < x \cdot y$$
In particolare, $\forall x,y \in S (x=0 \lor y=0) \implies (x,y) \text{ è un minimale per S} \iff \text{ esistono } \inf \text{ minimali} \implies \text{ non esiste nessun minimo}$
## Teorema di unicità del minimo
Sia $(S, \leq)$ un insieme ordinato, $min(S)$, se esiste, è unico.
### Dimostrazione
Supponiamo per assurdo che $a=min(S) \land b=min(S)$
$$a = min(S) \iff \forall x \in S (a \leq x)$$
$$b=min(S) \iff \forall x \in S (b \leq x)$$
$$\implies a \leq b \; \; \land \; \; b \leq a \iff a = b$$
