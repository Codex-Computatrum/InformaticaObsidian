---
author: Lorenzo Tecchia
tags:
  - statistics
  - theorem
---
Grazie alla [[Disugaglianza di Chebyshev|disuguaglianza di Chebyshev]] possiamo enunciare e provare la ***legge debole dei grandi numeri***:
>[!definition]
> La [[Valore atteso|media]] aritmetica di $n$ copie indipendenti di una [[variabile aleatoria]] tende al [[valore atteso]] di quest'ultima per $n$ che tende all'infinito. 
> Tale convergenza si precisa dicendo che scelto un $\varepsilon$ comunque piccolo, la media aritmetica si discosta dal valore atteso per più di $\varepsilon$ con probabilità che tende a zero, quando $n$ tende all'infinito
> > [!important]
> >  Sia $X_{1}, X_{2}, \dots$ una successione di variabile aleatoria (indipendenti e identicamente distribuite), tutte con media $E[X_{i}] =: \mu$. Allora per ogni $\varepsilon > 0$.
> >  $$ \mathbb{P}\left(\left|\frac{X_{1}+\cdots+X_{n}}{n}-\mu\right|>\varepsilon\right) \rightarrow 0 \quad \text { quando } n \longrightarrow \infty$$

***Dimostrazione:*** proveremo il risultato solo sotto l'ipotesi aggiuntiva che le $X_{i}$ abbiano [[varianza]] finita $\sigma^{2}$. Dalle proprietà di [[Valore atteso#^prop-valoreAtteso|media]] e [[Varianza#^2cf295|varianza]] segue che
$$E\left[\frac{X_{1}+\cdots+X_{n}}{n}\right]=\mu \quad \text { e } \quad \operatorname{Var}\left(\frac{X_{1}+\cdots+X_{n}}{n}\right)=\frac{\sigma^{2}}{n}$$
La seconda ad esempio si prova in questo modo: 
$$
\begin{aligned}
\operatorname{Var}\left(\frac{X_{1}+\cdots+X_{n}}{n}\right) & =\frac{1}{n^{2}} \operatorname{Var}\left(X_{1}+\cdots+X_{n}\right) & & \text { per la (4.6.3) } \\
& =\frac{\operatorname{Var}\left(X_{1}\right)+\cdots+\operatorname{Var}\left(X_{n}\right)}{n^{2}} & & \begin{array}{l}
\text { per l'indipendenza } \\
\text { e il Teorema 4.7.3 }
\end{array} \\
& =\frac{n \sigma^{2}}{n^{2}}=\frac{\sigma^{2}}{n} & &
\end{aligned}$$
Segue allora dalla disuguaglianza di Chebyshev applicata alla variabile aleatoria $\frac{X_{1}+ \dots + X_{n}}{n}$ che $$
\mathbb{P}\left(\left|\frac{X_{1}+\cdots+X_{n}}{n}-\mu\right|>\varepsilon\right) \leq \frac{\sigma^{2}}{n \varepsilon^{2}}$$
Poiché il secondo membro tende a zero per $n$ che tende all'infinito, l'enunciato è provato.


Un'applicazione di questo teorema è la seguente, che permette anche di giustificare l'[[Probabilità#Interpretazione empirica(o frequentista)|interpretazione frequentista]] della probabilità di un evento. Supponiamo di ripetere in successione molte copie indipendenti di un esperimento, in ciascuna delle quali può verificarsi in un certo evento $E$. Ponendo $$
X_{i}:= \begin{cases}1 & \text { se } E \text { si realizza nell'esperimento } i \text {-esimo } \\ 0 & \text { se } E \text { non si realizza nell'esperimento } i \text {-esimo }\end{cases}$$
la sommatoria $X_{1}+ X_{2}+ \dots X_{n}$, rappresenta il numero di prove - tra le prime $n$- in cui si è verificato l'evento $E$. Poiché $$E[X_{1}] = \mathbb{P}(X_{i}=1)=\mathbb{P}(E)$$
si deduce che la frazione delle $n$ prove nelle quali si realizza $E$, tende (nel senso della legge debole dei grandi numeri) alla probabilità $\mathbb{P}$.