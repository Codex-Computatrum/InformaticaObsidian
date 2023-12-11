---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - probability
  - advanced
---
La simulazione al calcolatore costituisce un metodo molto potente per valutare gli integrali mono- e multidimensionali. Supponiamo infatti che $f$ sia una funzione $\mathbb{R}^{r}$ in $\mathbb{R}$, e che siamo interessati a stimare la quantità $\theta$, definita da $$
\theta:=\int_{0}^{1} \int_{0}^{1} \cdots \int_{0}^{1} f\left(y_{1}, y_{2}, \ldots, y_{n}\right) d y_{1} d y_{2} \cdots d y_{n}$$
Notiamo subito, che se $U_{1}, U_{2}, \dots, U_{r}$ sono variabili aleatorie uniformi su $(0,1)$ allora $$\theta=E\left[f\left(U_{1}, U_{2}, \ldots, U_{r}\right)\right]$$
Supponiamo ora di fare generare ad un computer $r$ numeri casuali, uniformi su $(0,1)$ e indipendenti[^1], e di valutare $f$ a quelle coordinate. Questo produrrà un numero casuale distribuito come $f(U_{1}, U_{2}, \dots, U_{r})$ che denotiamo con $X_{1}$. Si noti che $E[X_{1}] = \theta$. Se ripetiamo il procedimento un numero $n$ di volte, otteniamo una successione $X_{1}, X_{2}, \dots, X_{n}$ di variabili aleatorie i.i.d. ce hanno [[Valore atteso|media]] $\theta$; possiamo allora impiegare questo [[campione]] per stimare $\theta$. Questo metodo di approssimazione degli integrali è detto ***simulazione di Monte Carlo o metodo Monte Carlo***.
Pensiamo ad esempio alla stima dell'integrale seguente: 
$$
\theta:=\int_{0}^{1} \sqrt{1-y^{2}} d y=E\left[\sqrt{1-\dot{U}^{2}}\right]
$$
dove $U$ ha [[distribuzione]] [[uniforme]] su $(0,1)$. Siano $U_{1}, \dots, U_{100}$ delle variabili aleatorie con tale [[distribuzione]] e indipendenti, generate da un calcolatore. Ponendo 
$$
X_{i}:=\sqrt{1-U_{i}^{2}}, \quad i=1,2, \ldots, 100
$$
otteniamo un [[campione]] di $100$ variabili aleatorie di [[Valore atteso|media]] $\theta$. Realizzando questa simulazione abbiamo trovato una [[Valore atteso|media]] campionaria di $0.786$ e una deviazione standard campionaria di $0.23$. Allora, siccome $t_{0.025, 99} \approx 1.985$, si ottiene che un intervallo di confidenza al $95\%$ per $\theta$ è il seguente, 
$$
0.786 \pm 1.985 \cdot 0.023
$$
>[!success]
> Quindi possiamo affermare con il $95\%$ di confidenza, che $\theta$ (il cui valore esatto si può dimostrare essere $\pi/4 \approx 0.7854$) è compreso tra $0.740$ e $0.832$

[^1]: Si ricordi che questo tipo di variabili aleatorie sono le uniche direttamente riproducibili al calcolatore. Ogni altro tipo di [[distribuzione]] desiderata deve essere ricostruita a partire da essi.