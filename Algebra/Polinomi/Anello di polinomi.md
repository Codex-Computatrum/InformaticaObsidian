---
author: Simone Parente
tags:
  - algebra/polinomi
  - notReviewed
---
>[!warning] Attenzione
>I polinomi non sono funzioni, possono essere considerati tali solo nei [[campo|campi]] infiniti.

Sia $A$ un [[Anello Commutativo Unitario|anello commutativo unitario]], chiameremo $A_{[x]}$ un <span style="color:#00ff00"><b>anello di polinomi</b></span> a coefficienti in $A$ per una indeterminata $x$, quindi $A_{[x]}$ è un [[Anello Commutativo Unitario|anello commutativo unitario]] tale che:
1. $A$ sia un sottoanello unitario di $A_{[x]}$ $(1_{A_{[x]}}=1_A)$ (le unità dell'anello dei polinomi e dell'anello commutativo coincidono)
2. $x \in A_{[x]}$
3. $(\forall f \in A_{[x]})(\textcolor{#FF2052}{\exists !} (a_i)_{i \in \mathbb{N}}) \in A^{\mathbb{N}})(\exists n \in \mathbb{N}: (f=a_0+a_1x+a_2x^2+\ldots + a_nx_n) \land (\forall i \in \mathbb{N}(i>n(a_i=0_A))))$
 >[!warning] Attenzione
 >- $(a_i)_{\in \mathbb{N}}$ indica una successione di coefficienti in $f$
 >- $a_0=a_0 \cdot x^0=a_0 \cdot 1$

>[!info] 
 Per ogni $A$ è possibile trovare un anello di polinomi con le tre proprietà richieste:
 >$A_{[x]}$ esiste sempre, ed a meno di isomorfismi, è unico.

>[!example] Esempio
Se $A=\mathbb{Z}$, per $x=\sqrt{2}$, <span style="color:#ff2052">esiste più di una successione</span> con stesso risultato:
>- $0+0 \cdot (\sqrt{2})+1 \cdot (\sqrt{2})^2 = 2$
>- $2+0 \cdot (\sqrt{2})=2$

Siano:
$$f=\sum^{n}_{i=0}a_ix^i$$
$$f=\sum^{m}_{i=0}b_ix^i$$
e sia $n \geq m$, 
- $\forall i \in \{0,\ldots,m\} \; a_i=b_i$
- $\forall i \in \{m+1,\ldots, n\} \; a_i=0_A$
$\implies$ non esiste un unico modo per scrivere un polinomio, una volta scritti i coefficienti non nulli, è possibile aggiungere infiniti coefficienti nulli, in questo modo si ottengono diverse scritture dello stesso polinomio.
### Polinomi costanti
>Gli elementi di $A$ si dicono <span style="color:#00ff00"><b>polinomi costanti</b></span>, uno di questi è proprio lo zero dell'anello, è anche detto polinomio nullo.
>$0_A=0_{A_{[x]}}$
