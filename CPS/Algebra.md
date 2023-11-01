---
author: Lorenzo Tecchia
tags: [definition, probability]
---
 Sia $\Huge a$ una famiglia di sottoinsiemi di $\Omega$. Si dice che $\Huge a$ è un’***algebra*** se e solo se:
- $a_{1}\;\;\;\Omega \in \Huge a$
- $a_{2}\;\;\;A \in \Huge a$ e $A^{c} \in \Huge a$
- $a_{3}\;\;\;A_1,A_{2}\in \Huge a$ e $A_{1}\cup A_{2}\in \Huge a$
>[!important] L'intersezione su un'algebra è un operazione chiusa
> Sia $\Huge a$ un'algebra. Siano $A_{1}, A_{2} \in \Huge a$. Allora $A_{1}\cap A_{2} \in \Huge a$
> ##### dimostrazione
> Possiamo portare $A_{1} \cap A_{2}$ in questa forma grazie alle leggi di De Morgan $$A_{1} \cap A_{2} = (A_{1}^c \cup A_{2}^c)$$
> $A_{1}^{c} \in \Huge a$ per $a_2$. Stessa cosa per $A_{2}^c$. Dunque $A_{1}^{c} \cup A_{2}^{c}\in \Huge a$ per $a_2$.
> 
> Dalla proposizione possiamo generalizzare e possiamo certamente dire: sia $\Huge a$ un'algebra, sia $n \in \mathbb{N}: n\geq 2$ e siano $A_1,A_{2},\dots, A_{n}\in \Huge a$, allora:$$\bigcap_{i=1}^{n}A_{i}=\left(\bigcup_{i=1}^{n}A_{i}^{c}\right)^{c}\in \Huge a$$
