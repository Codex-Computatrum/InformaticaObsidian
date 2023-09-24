---
author: Simone Parente, Mario Penna
tags:
  - definition/property
---
Siano $A$ un insieme, $\rho$ una relazione di equivalenza definita su $A$ e siano $a,b \in A$.
Allora:
$$2)\ [a] = [b] \iff a \rho b$$
DIM: (relazione sufficiente)
$$[a] = [b] \implies a \rho b$$
quindi:
$\forall \in A,\ a\in [a]$ ; $[a] = [b]$ $\implies a \in [b] = \{ x \in A (x \rho b) \} \implies a \rho b$

DIM: (relazione necessaria)
$$a \rho b \implies [a] = [b]$$
$[a] = [b] \iff [a] \subseteq [b] \land [b] \subseteq [a]$
- $[a] = [b] \iff \forall x \in [a], \ x\in [b]$
	$x \in [a] \implies x \rho a$
	$per\ ipotesi \implies a \rho b$
	$\implies \forall x \in [a], x \in [b] \implies [a] \subseteq [b]$
- $[b] \subseteq [a] \iff \forall x \in [a], x \in [b]$
	$x \in [b] \implies x \rho b$
	$per \ ipotesi \implies a \rho b$
	$Simmetria: a\rho b \implies b \rho a  \ || \ Transitività: x\rho b \land b \rho a \implies x \rho a$
	$\implies \forall x\in [b], x \in [a]$