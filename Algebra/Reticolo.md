---
author: Simone Parente
tags:
  - definition/property/structure
---

Sia $(S, \leq)$ un [[Insieme Ordinato|insieme ordinato]].

$$(S, \leq) \text{ è un reticolo} \iff \forall x,y \in S (\exists \inf\{x,y\} \land \exists \sup\{x,y\})$$ ^703fff

Cioè se ogni sottoinsieme di $S$ con [[Cardinalità di un insieme|cardinalità 2]] ammette [[Estremo superiore|estremo superiore]] e [[Estremo inferiore|estremo inferiore]]. ^3d12bf
### Esempio
$(P(S),\subseteq)$ è un reticolo?
Per essere un reticolo deve valere che $\forall X,Y \in P(S) (\exists F=\inf\{X,Y\} \land \exists K=\sup\{X,Y\})$.
Troviamo quindi un insieme che rispetti queste condizioni: 
$$F=\inf\{X,Y\} \iff$$
1. $F \subseteq X \land F \subseteq Y$
2. $\forall T \in P(S), (T \subseteq X \land T \subseteq Y) \implies  T \subseteq F$
$F$ sarà quindi uguale a $X \cap Y$, che è il più grande insieme contenuto sia in $X$ che in $Y$
Facciamo lo stesso ora per il $\sup$
$$K=\sup\{X,Y\} \iff$$
1. $X \subseteq K \land Y \subseteq K$
2. $\forall T \in S, X \subseteq T \land Y \subseteq T \implies K \subseteq T$
L'insieme $K$ che rispetta queste condizioni è $K=X \cup Y$.

Di conseguenza $(P(S), \subseteq)$ <span style="color:#4ddb00">è un reticolo</span>.