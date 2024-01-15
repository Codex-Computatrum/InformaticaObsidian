---
author: Simone Parente
tags:
  - algebra/polinomi/teorema
  - notReviewed
---
>[!info] 
>Sia $A$ un [[Anello Commutativo Unitario|anello commutativo unitario]] e siano $f \in A[x]$ e $c \in A$, allora $f(c)$ è il [[Teorema divisione tra polinomi#^intro|resto della divisione]] di $f$ per $x-c$.

>[!quote] Dimostrazione
>È sicuramente possibile effettuare la divisione di $f$ per $x-c$ , questo perché $x-c$ è un [[Polinomio monico|polinomio monico]] e quindi il suo coefficiente direttore è invertibile ($1_A \in\mathcal{U}(A)$) , quindi è possibile applicare  per il [[Teorema divisione tra polinomi#^th|teorema della divisione tra polinomi]].
>Effettuando la divisione otteniamo $(q,r) \in A[x]$ tali che $f=(x-c)q+r$ e, inoltre, $\nu r < \nu(x-c)=1$. Se $\nu (x-c)=1$ e $\nu(r) < 1$, allora $r$ avrà grado 0, quindi sarà un polinomio costante, applicando l'[[Omomorfismo#^sostituzione|omomorfismo di sostituzione]] otteniamo:
>$$f(c)=((x-c)q+r)c=\textcolor{blue}{(c-c)q(c)}+r(c)=\textcolor{blue}{0_A}+r$$
>$\text{cioè che } f(c)=r$. $\square$
