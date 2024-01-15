---
tags:
  - definition
  - statistics
  - example
  - distribution/normal
author: Lorenzo Tecchia
---
Sia $X$ una [[variabile aleatoria]] con media $\mu$. La ***varianza*** di $X$, che si denota con $Var(X)$, è se esiste la quantità $$Var(X) := E[(X- \mu)^{2}]$$
Esiste una formula alternativa per la varianza, che si ricava in questo modo: $$
\begin{aligned}
\operatorname{Var}(X) & :=E\left[(X-\mu)^{2}\right] \\
& =E\left[X^{2}-2 \mu X+\mu^{2}\right] \\
& =E\left[X^{2}\right]-2 \mu E[X]+\mu^{2} \\
& =E\left[X^{2}\right]-\mu^{2}
\end{aligned}$$
Ovvero: $$Var(X) = E[X^{2}]- E[X]^{2}$$

>[!important]
> In altri termini, la varianza di $X$ è uguale al [[valore atteso]] del quadrato di $X$ (anche detto il momento secondo), meno il quadrato della media di $X$. Nella pratica questa formula è spesso il miglior modo di calcolare $Var(X)$.

>[!example]- Si calcoli la varianza del punteggio di un dado non truccato
> Sia $X$ il punteggio realizzato dal dado. Siccome $\mathbb{P}(X = i) = \frac{1}{6}$, per $i = 1,2, \dots, 6$ otteniamo $$
\begin{aligned}
E\left[X^{2}\right] & =\sum_{i=1}^{6} i^{2} P(X=i) \\
& =1^{2} \cdot \frac{1}{6}+2^{2} \cdot \frac{1}{6}+3^{2} \cdot \frac{1}{6}+4^{2} \cdot \frac{1}{6}+5^{2} \cdot \frac{1}{6}+6^{2} \cdot \frac{1}{6}=\frac{91}{6}
\end{aligned}$$
> Da cui [[Valore atteso#^esempio-valoreAtteso-dadoOnesto|ricordando che]] $E[X] = \frac{7}{2}$: $$
\operatorname{Var}(X)=E\left[X^{2}\right]-E[X]^{2}=\frac{91}{6}-\left(\frac{7}{2}\right)^{2}=\frac{35}{12}$$

>[!example] **Varianza della [[funzione]] indicatrice di un evento**
> Sia $I$ la funzione indicatrice di un [[evento]] A: $$
I:= \begin{cases}1 & \text { se } A \text { si verifica } \\ 0 & \text { se } A \text { non si verifica }\end{cases}$$
> Allora notando che $I^{2}= I$ sempre (infatti i valori possibili di $I$ sono solamente $0$ e $1$, che soddisfano $1^{2} = 1$ e $0^{2}= 0$), $$
\begin{array}{rlr}
\operatorname{Var}(I) & =E\left[I^{2}\right]-E[I]^{2} & \\
& =E[I]-E[I]^{2} & \\
& =E[I](1-E[I]) & \\
& =P(A)(1-P(A)) & \text { perché } I^{2}=I \text { con probabilità } 1 \\
& =P[I]=P(A) \text { dall'Esempio 4.4.2 }
\end{array}$$[[Probabilità| ]]
> >[!important] 
> > Una utile identità che riguarda la varianza è la seguente. Per ogni coppia di costanti reali $a$ e $b$, $$var(aX +b) = a^{2}Var(X)$$^proprieta-varianza
> > Per dimostrarla, poniamo $\mu := E[X]$ e ricordiamo che $E[aX +b] = aE[X]+b = a\mu + b$, in modo tale che $$
\begin{aligned}
\operatorname{Var}(a X+b) & :=E\left[(a X+b-E[a X+b])^{2}\right] & & \\
& =E\left[(a X+b-a \mu-b)^{2}\right] & & \text { usando } E[a X+b]=a \mu+b \\
& =E\left[a^{2}(X-\mu)^{2}\right] & & \text { semplificando e raccogliendo } \\
& =a^{2} E\left[(X-\mu)^{2}\right] & & \text { usando la (4.5.3) } \\
& =a^{2} \operatorname{Var}(X) & &
\end{aligned}$$
>> Se si sostituiscono valori particolari di $a$ e $b$ nell'equazione che vogliamo provare, si ottengono diversi risultati interessanti. Ad esempio se poniamo $a=0$ troviamo che $$Var(b) = 0$$ cioè che le costanti hanno varianza nulla. Scegliendo $a=1$ invece, si ottiene che $$Var(X +b) = Var(X)$$ ovvero che sommare una costante non cambia la varianza di una variabile aleatoria. Infine con $b=0$ diventa $$Var(aX) = a^{2}Var(X)$$

^2cf295



La quantità $\sqrt{Var(X)}$ è detta **deviazione standard** della variabile aleatoria $X$^deviazione-standard

>[!note]-
> In termini fisici, se la media è il baricentro di una distribuzione di masse, la varianza è il suo **momento di inerzia**
