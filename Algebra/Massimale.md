---
author: Simone Parente, Mario Penna
tags:
  - definition/property
  - theorem
  - to-do
---
Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]]:

$$d \in S \text{ è un massimale} \iff \nexists x \in S (x > d)$$ ^c13a1a
## Teorema
Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]]: un [[Massimo|massimo]] è sempre un massimale ed è l'unico massimale. $\cancel{\impliedby}$
$$a = max(S) \implies a \text{ unico massimale}$$
### Dimostrazione
Sia $a = max(S)$, supponiamo _**per assurdo**_ che $\exists b \in S: b$ è un [[Massimale#^c13a1a|massimale]] e che $b \neq a$.

$$b \; \text{massimale} \iff \nexists x \in S (x > b)$$ ^f8fa47

$$a = max(S) \iff \forall x \in S (a \geq x)$$

$$\implies a \geq b \land b \neq a \implies a > b$$
Ma $a$ non può essere maggiore di $b$ per [[massimale#^f8fa47|definizione di massimale]].