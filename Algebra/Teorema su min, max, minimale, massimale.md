---
author: Simone Parente, Mario Penna
tags:
  - theorem
  - example
---
Sia $(S, \leq)$ un [[Insieme Ordinato|insieme ordinato]], un [[Minimo|minimo]] (o un [[Massimo|massimo]]) è sempre un [[Minimale|minimale]] (o un [[Massimale|massimale]]), ed è sempre l'unico [[Minimale|minimale]] (o [[Massimale|massimale]]).
$$a = \min(S) \implies a \text{ unico minimale}$$
### Dimostrazione (minimo e minimale)
$a = \min(S)$, per assurdo $\exists b \in S: b \text{ è un minimale} \land b \neq a$.

$$b \text{ è un minimale} \iff \nexists \; x \in S(x < b)$$ ^0133da

$$a = \min(S) \iff \forall x \in S (a \leq x)$$
$$\implies a \leq b \land b \neq a \implies a<b$$
Ma $a<b$ è assurdo perché $b$ è un minimale e per la [[Teorema su min, max, minimale, massimale#^0133da|prima definizione]], questo è assurdo.

---
Per la dimostrazione (massimo e massimale) basta ragionare allo stesso modo, dicendo che $a$ è il [[Massimo|massimo]] e $b$ un [[Massimale|massimale]].