---
author: Simone Parente
tags:
  - prolog
---

Una sostituzione è un insieme finito di coppie:
$$\theta= \{\textcolor{lime}{X_1}=\textcolor{cyan}{t_1},\ldots, \textcolor{lime}{X_n}=\textcolor{cyan}{t_n}\}$$
Dove:
- le $\textcolor{lime}{X_i}$ sono le <span style="color:lime">variabili</span> e sono tutte **diverse tra loro**.
- i $\textcolor{cyan}{t_i}$ sono  <span style="color:cyan">termini</span>.
- Nessuna delle  $\textcolor{lime}{X_i}$ compare nei $\textcolor{cyan}{t_i}$
Sia $E$ un'espressione, cioè:
- un termine
- un fatto
- una query
- oppure una regola
l'applicazione di $\theta$ ad $E$, denotata con $E \theta$, **sostituisce** tutte le occorrenze della variabili $\textcolor{lime}{X_i}$ in $E$ con i corrispettivi termini $\textcolor{cyan}{t_i}$.

## Esempio
Sia $E_1 = sum(A,B,C)$ e $E_2 = sum(X,0,X)$.
Esempi di **sostituzioni** sono: ^32cd6b
- $\theta_0 =\{ A=0,\; B=0,\; C=0,\; X=0\}$ ^33a9bf
- $\theta_1=\{A=X,\; B=0,\; C=X\}$ ^2694eb
- $\theta_2=\{A=1,\; B=0,\; C=1,\; X=1\}$ ^02a195