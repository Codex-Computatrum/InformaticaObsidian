---
author: Simone Parente, Mario Penna
tags:
  - definition
  - theorem
---
Sia data $\forall n \in \mathbb{N} (n \leq n_0)$ una proposizione $P(n)$ .
Se sono soddisfatte le seguenti condizioni:
1. $P(n_0)$ è vera <span style="color:red">BASE INDUTTIVA</span>
2. $\forall n>n_0 (P(n-1) \implies P(n))$  <span style="color:red">PASSO INDUTTIVO</span>

Allora $P(n)$ risulta vera $\forall n\leq n_0$

Esempi:
![[Somma Di Gauss]]

![[Somma Primi numeri naturali dispari]]


## Tutorato
### Notazione
In questa parte $\mathbb{N}_m=\{ n \in \mathbb{N}| m \leq n \} = \{m,m+1,m+2,\ldots\}$
### Principio di induzione (I forma)
$$(\forall X \in P(\mathbb{N}) \setminus \{0\})((\forall n)(n \in X \implies n+1 \in X) \implies (X = \mathbb{N}_{\min X}))=\{n \in \mathbb{N}: n \geq \min X\}$$^ipotesi
#### Dimostrazione
$X \in (P(\mathbb{N}) \setminus  \{\emptyset\})$, dato che $\mathbb{N}$ è [[Insieme ben ordinato|ben ordinato]]. 
Sia $\mathbb{N}_{\min(X)}=\{n \in \mathbb{N} | n \geq \min(X)\}$, $X \subseteq \min(X)$, se $x \in X$, $x \geq \min(X)$
$$\implies (x \in \mathbb{N}) \land (x \geq \min(X)) \implies x \in \mathbb{N}_{\min X}$$
Supponiamo <span style="color:#ff0000">per assurdo</span> che $(X \subset \mathbb{N}_{\min X})$, cioè $(\exists x \in X \,|\, x \notin \mathbb{N}_{\min X})$ , questo implica $\mathbb{N}_{\min X} \setminus X \neq \emptyset$.
Sia $n=min(\mathbb{N}_{\min X} \setminus X )$, in particolare $n \in (\mathbb{N}_{\min X} \setminus X)$ cioè $((n \in \mathbb{N}_{\min X}) \land (n \notin X))$ 
$$\implies (n \geq m) \land (n \neq m) \text{ questo perché }x \notin X, (m=\min(X) \in X)$$
$$\implies n > m \implies n-1 \geq m$$
Per ipotesi $n-1 < n$, $n=\min(\mathbb{N}_m \setminus X)$. Di conseguenza $(n-1 \notin (\mathbb{N}_{m} \setminus X))$, quindi $n-1 \in X$
A questo punto sappiamo che $n-1 \in X$, per [[Principio di Induzione#^ipotesi|ipotesi]] $(n-1)+1=n \in X$, che va contro la tesi, visto che $n=min(\mathbb{N}_{\min X} \setminus X )$, ciò implica che $n \in (\mathbb{N}_{\min X} \setminus X)$, ma essendo anche un elemento di $\mathbb{N}_{\min X}$, $n \notin X$.  $\square$
