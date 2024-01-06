---
author: Simone Parente
tags:
  - algebra/polinomi
  - notReviewed
---
>[!info]
>Siano $A$ un [[Anello Commutativo Unitario|anello commutativo unitario]] e $f,g \in A[x]$, allora

>[!tip] Proposizioni
>1. Se in $A[x]$, $f$ divide $g$, ogni [[Radice di un polinomio|radice]] di $f$ in $A$ è [[Radice di un polinomio|radice]] di $g$
>2. Se in $A[x]$, $f$ e $g$ sono [[Polinomi associati|associati]], $f$ e $g$ hanno le stesse radici in $A$
>3. Se $A$ è un [[Dominio di integrità|dominio di integrità]], allora le [[Radice di un polinomio|radici]] di $fg$ sono tutti e soli gli elementi di $A$ che sono [[Radice di un polinomio|radici]] di $f$ o di $g$

>[!quote] Dimostrazione 1.
>Se $f|_{A[x]}g$ esiste $h \in A[x]$ tale che $g=fh$. Allora applicando l'omomorfismo di sostituzione ($g \in A[x] \mapsto g(c) \in A$), abbiamo $g(c)=f(c)h(c)=0_Ah(c)=0_A$, quindi $c$ è [[Radice di un polinomio|radice]] di $f$. Se non è chiaro il motivo, vedi [[Divisibilità tra polinomi]].

>[!quote] Dimostrazione 2.
>Segue da 1., se $f$ e $g$ sono [[Polinomi associati|associati]], allora $f$ divide $g$, quindi le [[Radice di un polinomio|radici]] di $f$ sono radici di $g$ e viceversa.

>[!quote] Dimostrazione 3.
>Per 1., segue che gli elementi di $A$ che sono radici di $f$ o di $g$ sono anche radici di $fg$. Viceversa, se $c$ è una radice in $A$ di $fg$, allora $0_A=(fg)(c)=f(c)g(c), questo perché $A[x]$ è un [[Dominio di integrità|dominio di integrità]], quindi $c$ è una radice di uno tra $f$ e $g$.

