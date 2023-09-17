Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]] e  $a \in S$ e [[confrontabile]] con tutti gli elementi di $S$:

$$b = max(S) \iff \forall x \in S (b\geq x)$$ ^3e0315
### Esempi
- In $(\mathbb{N}, \leq)$, $max(\mathbb{N})= \nexists$
- In $(\mathbb{N}, |)$, $max(\mathbb{N})= 0$, visto che 0 è diviso da tutti i numeri naturali
- $(\mathbb{Z}, \leq)$, $max(\mathbb{Z})= \nexists$
## Teorema di unicità del massimo
Sia $(S, \leq)$ un insieme ordinato, $max(S)$, se esiste, è unico.
### Dimostrazione
Supponiamo per assurdo che $a=max(S) \land b=max(S)$
$$a = max(S) \iff \forall x \in S (x \leq a)$$
$$b=max(S) \iff \forall x \in S (x \leq b)$$
$$\implies a \leq b \; \; \land \; \; b \leq a \iff a = b$$
