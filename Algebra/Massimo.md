---
author: Simone Parente, Mario Penna
tags:
  - definition/property
  - theorem
  - example
  - to-do
---
Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]] e  $a \in S$ e [[Elemento Confrontabile|confrontabile]] con tutti gli elementi di $S$:

$$b = max(S) \iff \forall x \in S (b\geq x)$$ ^3e0315
### Esempi
- In $(\mathbb{N}, \leq)$, $max(\mathbb{N})= \nexists$
- In $(\mathbb{N}, |)$, $max(\mathbb{N})= 0$, visto che 0 è diviso da tutti i numeri naturali
- $(\mathbb{Z}, \leq)$, $max(\mathbb{Z})= \nexists$
### Esempio
### Esempio 2
$$S = (\forall (a,b), (c,d) \in \mathbb{N} \times \mathbb{N}) ((a,b) \sigma (c,d)) \iff (a,b) = (c,d) \lor (a \cdot b \leq c \cdot d)$$
$$\forall (a,b) \in S \exists (a, b+1) \lor (a+1,b): (a,b)\sigma (a,b+1)$$
$$(a \cdot b+1 > a \cdot b) \forall a,b \in \mathbb{N} \implies S \text{ non ammette massimali} \implies \nexists \max(S)$$
## Teorema di unicità del massimo
Sia $(S, \leq)$ un insieme ordinato, $max(S)$, se esiste, è unico.
### Dimostrazione
Supponiamo per assurdo che $a=max(S) \land b=max(S)$
$$a = max(S) \iff \forall x \in S (x \leq a)$$
$$b=max(S) \iff \forall x \in S (x \leq b)$$
$$\implies a \leq b \; \; \land \; \; b \leq a \iff a = b$$
