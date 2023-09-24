---
author: Simone Parente
tags:
  - definition/property
---

Sia $(S, \leq)$ un reticolo e $(S, \lor,\land)$ la [[Struttura algebrica associata a un reticolo|struttura associata]], allora valgono:
1. $\land$ e $\lor$ sono [[Associatività|associative]].
2.  $\land$ e $\lor$ sono [[Commutatività|commutative]].
3. $\forall x,y \in S, x \lor (x \land y) = x = x \land (x \lor y)$. (vale la legge dell'[[Assorbimento|assorbimento]])
---
Viceversa se $(S, \overline{\lor}, \overline{\land})$ è una struttura algebrica che verifica 1. 2. 3. allora la [[Classificazione di relazioni binarie|relazione binaria]] $\rho: \forall x,y \in S (x \rho y \iff x=x \overline{\land} y)$ è una [[Relazioni d'ordine|relazione d'ordine]] e $(S, \rho)$ è un [[Reticolo|reticolo]] in cui 
1. $x \overline{\land} y = \inf\{x,y\}$
2. $x \overline{\lor} y = \sup\{x,y\}$
