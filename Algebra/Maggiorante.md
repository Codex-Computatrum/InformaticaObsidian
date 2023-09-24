---
author: Simone Parente, Mario Penna
tags:
  - definition/property
  - example
---
Sia $(S, \leq)$ un [[Insieme Ordinato|insieme ordinato]] e sia $X \subseteq S$
$$a \text{ è un maggiorante di X} \iff \forall h \in X(a \geq h)$$ ^4a8b90
### Esempio 1
$$S= (\mathbb{N}, |)\; \; \; X = \{3,5\} \subseteq S$$
$$b \in \mathbb{N} \text{ è un maggiorante di X} \iff \forall h \in X (h|b) \iff \text{vale per tutti i multipli di 15}$$
### Esempio 2
$$S = (\forall (a,b), (c,d) \in (\mathbb{N} \times \mathbb{N})) ((a,b) \sigma (c,d)) \iff (a,b) = (c,d) \lor (a \cdot b \leq c \cdot d)$$
$$S = (\mathbb{N} \times \mathbb{N}, \sigma), \; \; X= \{(0,1),(1,0),(3,2)\}$$
$$(a,b) \in \mathbb{N} \times \mathbb{N} \iff ((0,1)\sigma (a,b) \land (1,0) \sigma (a,b) \land (3,2) \sigma (a,b))$$
Abbiamo quindi 2 casi:
1. $\max(X) = (3,2)$ e sarà anche un [[Maggiorante#^4a8b90|maggiorante]].
2. Poniamo $(a,b) \notin X \iff (a\cdot b) > (1\cdot 0), (0 \cdot 1), (3 \cdot 6))$
   Quindi $(a,b)$ sarà un maggiorante di $X \iff a \cdot b >5$.