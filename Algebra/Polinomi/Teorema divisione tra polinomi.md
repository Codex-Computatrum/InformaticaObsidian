---
author: Simone Parente
tags:
  - algebra/polinomi/teorema
  - notReviewed
---
>[!info] Introduzione
>Siano $f,g$ due polinomi su un [[Anello Commutativo Unitario|anello commutativo unitario]], con $g \neq 0_A$, diciamo che nell'anello $A_{[x]}$ è possibile effettuare la divisione di $f$ (detto dividendo) per $g$ (detto divisore) $\iff \exists q,r \in A_{[x]}: (f=gq+r) \land (\nu r < \nu g)$, ($q$ è il quoziente, $r$ è il resto della divisione). $\iff$ è possibile scrivere $f$ come moltiplicazione di un certo quoziente $q$ per il polinomio $g$, sommando il resto $r$ al risultato. ^intro

>[!important] Caso particolare
>Se $\nu f < \nu g$, allora è sicuramente possibile effettuare la divisione di $f$ per $g$: poniamo $q=0$ e $r=f$. ^casoparticolare

>[!abstract] Teorema
>Sia $A$ un [[Anello Commutativo Unitario|anello commutativo unitario]] e $f,g \in A_{[x]}$. Supponiamo $cd \, g \in \mathcal{U}(A)$.
>Allora $\exists !(q,r) \in A_{[x]} \times A_{[x]} : (f=gq+r) \land (\nu r < \nu g)$ ^th

>[!quote] Dimostrazione esistenza
>Supponiamo che:
>- $n= \nu f$
>- $m=\nu g$
>- $n \geq m$
>
L'ipotesi che $cd \; g$ sia [[Elementi invertibili (o simmetrizzabili)|invertibile]] garantisce che $cd \; g \neq 0_A$ ([[Divisori dello zero#^attenzione|per questo motivo]]), quindi $n,m \in \mathbb{N}$.
Ragionando [[Principio di Induzione|per induzione]] su $n$, supponiamo che, $\forall h \in A_{[x]}: \nu h < n, \;h|g$
> Siano $a= cd \, f$, $b= cd \, g$ e consideriamo il polinomio $k=ab^{-1}x^{n-m}g$, per questo polinomio vale la [[Regola di addizione dei gradi|regola di addizione dei gradi]], in quanto il prodotto dei [[Coefficiente direttore e termine noto|coefficienti direttori]] di questi polinomi è $(ab^{-1})\; cd(g)=ab^{-1}b=a\neq 0_A$. Quindi $\nu k = \nu(ab^{-1}x^{n-m}) \nu (g)=(n-m)+m=n=\nu f$, inoltre $cd \, k = a = cd \, f$.
> Sappiamo quindi che $f$ e $k$ hanno stesso grado e stesso coefficiente direttore, possiamo vedere (Proposizione 2) che $h:=f-k$ ha grado $< n$.
> Per ipotesi induttiva è garantita la possibilità di poter effettuare la divisione di $h$ per $g$, quindi:
> $\exists q_1,r_1 \in A_{[x]}: (h=gq_1+r_1) \land (\nu r_1 \leq \nu g)$. Ora, $f=k+h=ab^{-1}x^{n-m}g+gq_1+r_1$, a questo punto la coppia $(q,r)$, definita ponendo $q=ab^{-1}x^{n-m}+q_1$ e $r=r_1$, soddisfa le condizioni richieste. $\square$

>[!quote] Dimostrazione unicità
>Come prima:
>- $n= \nu f$
>- $m=\nu g$
>
Siano $(q,r)$ e $(\overline{q}, \overline{r})$ due coppie con le proprietà richieste dall'ipotesi.
Dunque $f=gq+r=g\overline{q}+\overline{r}$ e $\nu r, \nu \overline{r} < m$.
>$$gq+r=g\overline{q}+\overline{r} \iff gq-g\overline{q}=\overline{r}-r \iff g(q-\overline{q})=\overline{r}-r$$
>Dato che $cd \, g$ è [[Elementi invertibili (o simmetrizzabili)|invertibile]] $\implies$ [[Elementi invertibili (o simmetrizzabili)#^invimpcanc|è cancellabile]], inoltre vale la [[Regola di addizione dei gradi|regola di addizione dei gradi]], quindi $\nu (g(q-\overline{q}))=m+\nu(q-\overline{q})$. Abbiamo così $m+\nu (q - \overline{q})=\nu (\overline{r}-r) \textcolor{red}{<m} \text{.} \textcolor{red}{\text{ Questo vale solo se }} m+ \nu (q-\overline{q}) = \nu (\overline{r}-r)=- \infty$
>Quindi $q-\overline{q}=r-\overline{r}=0_A$, cioè $q=\overline{q} \land r=\overline{r}$, abbiamo così dimostrato l'unicità della coppia $(q,r)$. $\square$
