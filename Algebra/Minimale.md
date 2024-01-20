---
author: Simone Parente, Mario Penna
tags:
  - algebra/reticoli
---
>[!danger] Attenzione
>Un elemento minimale **in un reticolo** è necessariamente minimo. Di conseguenza i reticoli finiti sono limitati, cioè hanno minimo e massimo, ma questo non è sempre vero per reticoli infiniti.

Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]]:
$$c \in S \text{ è un minimale} \iff \nexists x \in S (x <c)$$ ^12dc8b

A differenza del [[Minimo|minimo]]: ^86cb4a
- Non è detto che un minimale sia unico, possono esisterne di diversi.
- Non è necessario che sia [[Elemento Confrontabile|confrontabile]] con tutti gli elementi. 
## Teorema
Sia $(S, \leq)$ un [[Insieme ordinato|insieme ordinato]]: un [[Minimo|minimo]] è sempre un minimale ed è l'unico minimale. $\cancel{\impliedby}$
$$a = min(S) \implies a \text{ unico minimale}$$
### Dimostrazione
Sia $a = min(S)$, supponiamo _**per assurdo**_ che $\exists b \in S: b$ è un [[Minimale#^12dc8b|minimale]] e che $b \neq a$.

$$b \; \text{minimale} \iff \nexists x \in S (x < b)$$ ^f8fa47

$$a = min(S) \iff \forall x \in S (a \leq x)$$

$$\implies a \leq b \land b \neq a \implies a < b$$
Ma $b$ non può essere minore di $a$ per [[Minimale#^f8fa47|definizione di minimale]].