---
author: Simone Parente
tags:
  - algebra/strutture/proprietà
---
>[!failure] Attenzione
>- I [[Dominio di integrità|domini di integrità]], ad esempio $(\mathbb{R}, +, \cdot)$, non ammettono divisori dello zero, ciò vuol dire che l'operazione $\cdot$, effettuata tra due elementi $a,b \in \mathbb{R} \setminus \{0\}$ non potrà mai dare $0$ come risultato.
>- La definizione seguente è data su un anello <u>commutativo</u> unitario, per anelli <u>non commutativi</u>:
>	- Un divisore dello zero è tale se è un divisore sinistro <u>o</u> un divisore destro dello zero.
>	- Un elemento $a$ di un anello $S$ è [[Elementi cancellabili|cancellabile]] $\iff$ non è un divisore dello zero.
^attenzione

Generalizzando
>[!summary] Definizione
>Sia $(S,\cdot, \star)$ un [[Anello Commutativo Unitario|anello commutativo unitario]], un divisore dello zero è un elemento $x$ non nullo tale che $\exists x,z \in S \setminus \{0\}: x \star z = z \star x = 0$

>[!example] Esempio
>Siamo nell'anello commutativo unitario $(\mathbb{Z}_8,+,\cdot)$.
>$\mathbb{Z}_8=\{0,1,2,3,4,5,6,7\}$, la tabella moltiplicativa è la seguente:
>
| $\cdot$ | $0$ | $1$ | $2$                  | $3$ | $4$                  | $5$ | $6$                  | $7$ |
| ------- | --- | --- | -------------------- | --- | -------------------- | --- | -------------------- | --- |
| $0$     | $0$ | $0$ | $0$                  | $0$ | $0$                  | $0$ | $0$                  | $0$ |
| $1$     | $0$ | $1$ | $2$                  | $3$ | $4$                  | $5$ | $6$                  | $7$ |
| $2$     | $0$ | $2$ | $4$                  | $6$ | $\textcolor{red}{0}$ | $2$ | $4$                  | $6$ |
| $3$     | $0$ | $3$ | $6$                  | $1$ | $4$                  | $7$ | $2$                  | $5$ |
| $4$     | $0$ | $4$ | $\textcolor{red}{0}$ | $4$  | $\textcolor{red}{0}$ | $4$   | $\textcolor{red}{0}$ | $4$    |
| $5$     | $0$ | $5$ | $2$                     | $7$    | $4$                     | $4$    | $1$                     | $3$    |
| $6$     | $0$ | $6$ | $4$                     | $2$    | $\textcolor{red}{0}$                     | $1$    | $4$                     | $2$    |
| $7$     | $0$ | $7$ | $6$                     | $5$    | $4$                     | $3$    | $2$                     | $1$    |
>Di conseguenza $2,4,6$ sono dei divisori dello 0.

