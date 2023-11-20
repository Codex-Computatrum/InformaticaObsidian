---
tags: [definition, aleatoryVariable, statistics]
alias: [aspettazione]
author: Lorenzo Tecchia
---
>[!definition]
> Sia $X$ una variabile aleatoria discreta che può assumere i valori $x_{1},x_{2}, \dots$; il **valore atteso** di $X$, che si indica con $E[X]$, è ([[Valore atteso#^nota-esistenza-valore-atteso|se esiste]]) il numero:$$E[X] := \sum\limits_{i}x_{i}\mathbb{P}(X = x_{i})$$

In altri termini si tratta della media pesata dei valori possibili di $X$, usando come pesi le probabilità che tali valori vengano assunti da $X$. Per questo $E[X]$ è anche detta media di $X$, oppure **aspettazione**.

>[!example] Per illustrare il concetto di media pesata, facciamo un semplice esempio.
> Se $X$ è una variabile aleatoria con funzione di massa: $$p(0) = \frac{1}{2}= p(1)$$ allora
> $$E[X] = 0 \times \frac{1}{2}+ 1 \times \frac{1}{2}= \frac{0+1}{2}=\frac{1}{2}$$
> é semplicemente la media aritmetica dei valori che $X$ può assumere. Però, se$$p(0) = \frac{1}{3}, \quad p(1) = 2/3$$ allora
> $$E[X] = 0 \times \frac{1}{3}+1 \times \frac{2}{3}=\frac{0+1\times2}{3}= \frac{2}{3}$$
> è una media pesata degli stessi valori $0$ e $1$, dove al secondo è stato dato un peso che è il doppio di quello del primo.


>[!note]
> Il valore atteso di $X$ è definito solo se la serie converge in valore assoluto, ovvero deve valere:$$\sum\limits_{i}|x_{i}|\mathbb{P}(X = x_{i})< \infty$$
> In caso contrario si dice che $X$ non ha valore atteso. ^nota-esistenza-valore-atteso