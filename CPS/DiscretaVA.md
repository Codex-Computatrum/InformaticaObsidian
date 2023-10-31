---
author: Lorenzo Tecchia
tags: [definition, probability, aleatoryVariable]
---
Si dice **discreta** una [[variabile aleatoria]] che può assumere una quantità finita o numerabile di valori.

Se $X$ è una **variabile aleatoria discreta**, la sua _funzione di massa di probabilità_ o _funzione di massa_ di definisce nel modo seguente: $$p(a) = \mathbb{P}(X=a)$$ ^a918c6

Siccome $X$ deve assumere dei valori $x_{1},x_{2}, \dots$ necessariamente la funzione di massa di probabilità deve soddisfare la seguente equazione:$$\sum^{\infty}_{i=1}p(x_{i})= 1$$

Per una variabile aleatoria discreta, la funzione di ripartizione $F$ può essere espressa in funzione della funzione di massa di probabilità, tramite$F(a) = \sum_{x \leq a}p(x)$ dove si intende che la serie è limitata ai soli valori possibili di $X$ minori o uguali ad $a$. Si noti che la $F$ che ne risulta è na funzione a gradini, e più precisamente, se $x_{1}< x_{2} < \dots$ sono i valori possibili di $X$, allora $F$ è costante su ciascuno degli intervalli $[x_{i-1}, x_{i})$ e in $x_{i}$ fa un salto di ampiezza $p(x_{i})$

>[!important]
> ![[Distribuzione]]

