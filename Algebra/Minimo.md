Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]] e  $a \in S$ e [[confrontabile]] con tutti gli elementi di $S$:

$$a = min(S) \iff \forall x \in S (a \leq x)$$ ^fad11a
- In $(\mathbb{N}, \leq)$, $min(\mathbb{N})= 0$ ^45dc88
- In $(\mathbb{N}, |)$, $min(\mathbb{N})= 1$, visto che 1 divide tutti i numeri naturali
- $(\mathbb{Z}, \leq)$, $min(\mathbb{Z})= \nexists$

## Teorema di unicità del minimo
Sia $(S, \leq)$ un insieme ordinato, $min(S)$, se esiste, è unico.
### Dimostrazione
Supponiamo per assurdo che $a=min(S) \land b=min(S)$
$$a = min(S) \iff \forall x \in S (a \leq x)$$
$$b=min(S) \iff \forall x \in S (b \leq x)$$
$$\implies a \leq b \; \; \land \; \; b \leq a \iff a = b$$
