---
author: Simone Parente
tags:
  - algebra/polinomi
  - notReviewed
---
Siano $A$ e $B$ [[Anello Commutativo Unitario|anelli commutativi unitari]], definisco $\theta$ omomorfismo di anelli unitari da $A$ a $B$, cioè $\theta(1_A)=1_B$.
$A_{[x]}$ è un [[Anello di polinomi|anello di polinomi]] su $A$ con indeterminata $x$.
Allora: $\forall c \in B, \exists ! \; \theta_\star \text{ omomorfismo di anelli unitari } A_{[x]} \to B \text{ tale che }(\theta_\star)_A=\theta \; \text{  e  }\; \theta_\star(x)=c$.
$$\theta_\star:\sum^{n}_{i=0}a_ix^i \in A_{[x]} \mapsto \sum^{n}_{i=0} \theta(a_i)c^i \in B$$
$$\sum^{n}_{i=0}a_ix^i=\sum^{n}_{i=0}\theta_\star(a_i)\theta_\star(x^i)=\sum^{n}_{i=0}\theta_\star(a)(\theta_\star(x))^i=\sum^{n}_{i=0}\theta_\star(a)\theta_\star c^i$$
