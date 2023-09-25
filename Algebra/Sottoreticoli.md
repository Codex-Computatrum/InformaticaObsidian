---
author: Simone Parente
tags:
  - definition/property
---

Sia $(S, \leq)$ un [[Reticolo|reticolo]] e $H \subseteq S$ $(H \neq \emptyset)$.
$$H \text{ è un sottoreticolo di S} \iff \forall x,y \in H((x \lor y) \in H) \land ((x \land y) \in H))$$
Cioè se $\inf(S) = \inf(H) \land \sup(S)=\sup(H)$

## Esempio
Sia $S=\{a,b,c,d,e,f\}$ e $H=\{a,c,d,f\}$.
Il relativo [[Diagrammi di Hasse|diagramma di Hasse]] sarà:

```start-multi-column
ID: ID_ig11
Number of Columns: 2
Largest Column: standard
```

![[hasse_sottoret.jpg|150]]

--- column-end ---

$c \land d \in S = b = \inf\{c,d\} \in S$

$c \land d \in H = a = \inf\{c,d\} \in H$

Quindi $H$ non è sottoreticolo di $S$, perché hanno [[Estremo superiore|sup]] comune ma [[Estremo inferiore|inf]] diversi.

--- end-multi-column

