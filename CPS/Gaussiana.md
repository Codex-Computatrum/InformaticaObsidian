---
aliases:
  - Normale
tags:
  - definition
  - statistics
  - to-do
  - distribution/normal
author: Lorenzo Tecchia
---
>[!todo] 
> Inserire grafico

Una [[variabile aleatoria]] $X$ si dice ***normale*** oppure ***gaussiana*** di parametri $\mu$ e $\sigma^{2}$  e si scrive $X \sim \mathcal{N}(\mu,\sigma^{2})$, se $X$ ha funzione di densità data da: $$f(x)= \frac{1}{\sqrt{2\pi \sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}},\;\;\;\; \forall x \in \mathbb{R}$$ 
La densità normale è una curva a campana simmetrica rispetto all'asse delle $x=\mu$ dove ha il massimo pari a $(\sqrt{2\pi\sigma^{2}})^{-1} \approx 0.399/\sigma$
>[!important] Inserire qui grafico della Gaussiana

La [[funzione generatrice dei momenti]] di una variabile aleatoria gaussiana di paramatri $\mu$ e $\sigma^{2}$ si deduce come segue: $$
\begin{aligned}
\phi(t): & =E\left[e^{t X}\right] \\
& =\frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{\infty} e^{t x} \exp \left\{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right\} d x \\
& =\frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{\infty} e^{t(\sigma y+\mu)} e^{-y^{2} / 2} d x \vdots \\
& =\frac{e^{\mu t}}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{\infty} \exp \left\{\frac{2 \sigma t y-y^{2}}{2}\right\} d x \\
& =\frac{e^{\mu t}}{\sqrt{2 \pi} \sigma} e^{\sigma^{2} t^{2} / 2} \int_{-\infty}^{\infty} \exp \left\{-\frac{y^{2}-2 \sigma t y+\sigma^{2} t^{2}}{2}\right\} d x \\
& =\exp \left\{\mu t+\frac{\sigma^{2} t^{2}}{2}\right\} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi} \sigma} \exp \left\{-\frac{(y-\sigma t)^{2}}{2}\right\} d x \\
& =\exp \left\{\mu t+\frac{\sigma^{2} t^{2}}{2}\right\}
\end{aligned}$$ dove l'ultima uguaglianza segue perché l'espressione dentro l'integrale rappresenta la densità di [[probabilità]] di una variabile aleatoria normale di parametri $\sigma t$ e $1$, e come tale il suo integrale su tutto $\mathbb{R}$ è pari a $1$.

Derivando l'espressione della [[funzione generatrice dei momenti]] si ottiene $$
\begin{aligned}
& \phi^{\prime}(t)=\left(\mu+\sigma^{2} t\right) \exp \left\{\mu t+\frac{\sigma^{2} t^{2}}{2}\right\} \\
& \phi^{\prime \prime}(t)=\left[\sigma^{2}+\left(\mu+\sigma^{2} t\right)^{2}\right] \exp \left\{\mu t+\frac{\sigma^{2} t^{2}}{2}\right\}
\end{aligned}$$ da cui ricaviamo i primi due momenti e la [[varianza]] di una variabile aleatoria gaussiana: $$
\begin{aligned}
E[X] & =\phi^{\prime}(0)=\mu \\
E\left[X^{2}\right] & =\phi^{\prime \prime}(0)=\sigma^{2}+\mu^{2} \\
\operatorname{Var}(X) & =E\left[X^{2}\right]-E[X]^{2}=\sigma^{2}
\end{aligned}$$
Così che i parametri $\mu$ e $\sigma^{2}$ rappresentano rispettivamente la [[Valore atteso|media]] e la varianza della [[distribuzione]] normale.

>[!important]
>Un risultato importante riguardo questo tipo di variabili aleatorie è che se $X$ è gaussiana  e $Y$ è una trasformazione lineare di $X$, allora $Y$ è a sua volta guassiana

--- 
>[!important] ### Proposizione
> Sia $X \sim \mathcal{N}(\mu, \sigma^{2})$, e sia $Y = \alpha X + \beta$ dove $\alpha$ e $\beta$ sono due costanti reali con e $\alpha \neq 0$. Allora $Y$ è una variabile aleatoria normale con media $\alpha \mu + \beta$ e varianza $\alpha^{2}\sigma^{2}$
> ***Dimostrazione:*** Calcoliamo la funzione generatrice di $Y$: $$
\begin{aligned}
E\left[e^{t(\alpha X+\beta)}\right] & =e^{\beta t} E\left[e^{\alpha t X}\right] \\
& =e^{\beta t} \phi_{X}(\alpha t) \\
& =e^{\beta t} \exp \left\{\mu \alpha t+\frac{\sigma^{2} \alpha^{2} t^{2}}{2}\right\}\\
& =\exp \left\{(\alpha \mu+\beta) t+\frac{\left(\alpha^{2} \sigma^{2}\right) t^{2}}{2}\right\}
\end{aligned}$$
> L'espressione ottenuta è la funzione generatrice di una variabile aleatoria gaussiana di media $\alpha \mu + \beta$ e varianza $\alpha^{2}\sigma^{2}$. Siccome la funzione generatrice di $Y$ ne determina la distribuzione questo dimostra l'enunciato

Un corollario della precedente proposizione è che se $X \sim \mathcal{N}(\mu, \sigma^{2})$, allora $$Z:=\frac{X-\mu}{\sigma}$$  è una variabile aleatoria normale con media $0$ e varianza $1$. Una tale variabile aleatoria si dice ***normale standard***; la sua funzione di ripartizione riveste un ruolo importante in statistica indicata col simbolo $\Phi$: $$\Phi(x):=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} e^{-y^{2} / 2} d y, \quad \forall x \in \mathbb{R}$$ Il fatto che $Z := (X - \mu)/\sigma$ abbia distribuzione normale standard quando $X$ è gaussiana di media $\mu$ e varianza $\sigma^{2}$ ci permette di esprimere le probabilità relative a $X$ in termini di probabilità di $Z$. Ad esempio per trovare $\mathbb{P}(X < b)$, notiamo che $X < b$ se  e solo se $$\frac{X-\mu}{\sigma}<\frac{b-\mu}{\sigma}$$ così che $$
\begin{aligned}
P(X<b) & =P\left(\frac{X-\mu}{\sigma}<\frac{b-\mu}{\sigma}\right) \\
& =P\left(Z<\frac{b-\mu}{\sigma}\right) \\
& =: \Phi\left(\frac{b-\mu}{\sigma}\right)
\end{aligned}$$ Analogamente, per ogni $a < b$, si ha che $$
\begin{aligned}
\mathbb{P}(a<X<b) & =\mathbb{P}\left(\frac{a-\mu}{\sigma}<\frac{X-\mu}{\sigma}<\frac{b-\mu}{\sigma}\right) \\
& =\mathbb{P}\left(\frac{a-\mu}{\sigma}<Z<\frac{b-\mu}{\sigma}\right) \\
& =\mathbb{P}\left(Z<\frac{b-\mu}{\sigma}\right)-\mathbb{P}\left(Z<\frac{a-\mu}{\sigma}\right) \\
& =: \Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)
\end{aligned}$$

>[!example]-
> Sia $X$ una variabile aleatoria normale con media $\mu = 3$ e varianza $\sigma^{2}=16$. Si trovino:
> 1. $\mathbb{P}(X < 11) \rightarrow$ Poniamo al solito $Z := (X - \mu)/\sigma$: $$
\begin{aligned}
\mathbb{P}(X<11) & =\mathbb{P}\left(\frac{X-3}{4}<\frac{11-3}{4}\right) \\
& =\mathbb{P}(Z<2) \\
& =\Phi(2) \approx 0.9972 .
\end{aligned}$$
> 2. $\mathbb{P}(X > -1) \rightarrow$ In modo del tutto analogo: $$
\begin{aligned}
\mathbb{P}(X>-1) & =\mathbb{P}\left(\frac{X-3}{4}>\frac{-1-3}{4}\right) \\
& =\mathbb{P}(Z>-1) \\
& =\mathbb{P}(Z<1) \\
& =\Phi(1) \approx 0.8413
\end{aligned}$$
> 3. $\mathbb{R}(2 < X < 7) \rightarrow$ infine $$
\begin{aligned}
\mathbb{P}(2<X<7) & =\mathbb{P}\left(\frac{2-3}{4}<\frac{X-3}{4}<\frac{7-3}{4}\right) \\
& =\mathbb{P}(-1 / 4<Z<1) \\
& =\Phi(1)-\Phi(-0.25) \\
& =\Phi(1)-1+\Phi(0.25) \approx 0.4400
\end{aligned}$$

---

La distribuzione normale è *riproducibile*, nel senso che la somma di variabili aleatoria normali e indipendenti ha essa stessa distribuzione normale. Siano infatti $X_{1}, X_{2}, \dots, X_{n}$ delle variabili aleatorie normali e indipendenti, dove $X_{i}$ ha media $\mu_{i}$ e varianza $\sigma^{2}_{i}$. La funzione generatrice $\sum\limits_{i=1}^{n}$ è data da $$
\begin{aligned}
\phi(t) & =E\left[\exp \left\{t X_{1}+t X_{2}+\cdots+t X_{n}\right\}\right] & & \\
& =E\left[e^{t X_{1}} e^{t X_{2}} \ldots e^{t X_{n}}\right] & & \\
& =\prod_{i=1}^{n} E\left[e^{t X_{i}}\right] & & \text { per l'indipendenza } \\
& =\prod_{i=1}^{n} \exp \left\{\mu_{i} t+\frac{\sigma_{i}^{2} t^{2}}{2}\right\} &  \\
& =\exp \left\{\bar{\mu} t+\frac{\bar{\sigma}^{2} t^{2}}{2}\right\} & &
\end{aligned}$$ dove si è posto $$
\bar{\mu}:=\sum_{i=1}^{n} \mu_{i}, \quad \quad \quad^{2}:=\sum_{i=1}^{n} \sigma_{i}^{2}$$ Poiché $\sum\limits_{i=1}^{n}X_{i}$ ha la medesima funzione generatrice di una variabile aleatoria $\mathcal{N}(\bar{\mu}, \bar{\sigma^{2}})$, e la funzione generatrice determina in maniera univoca la distribuzione, si conclude che $\sum\limits_{i=1}^{n}X_{i}$ è gaussiana con media $\sum\limits_{i=1}^{n}\mu_{i}$e varianza $\sum\limits_{i=1}^{n}\sigma_{i}^{2}$

>[!example]-
>  I dati a disposizione dei meteorologi indicano che le precipitazioni annuali a Los Angeles hanno distribuzione normale con media $12.08$ pollici e deviazione standard $3.1$ pollici. Assumiamo anche che le precipitazioni di anni successivi
siano indipendenti.
> 1. Si trovi la probabilità che le precipitazioni dei prossimi 2 anni superino complessivamente i 25 pollici.
> 2. Si trovi la probabilità che le precipitazioni dell'anno prossimo superino quelle dell'anno successivo per più di 3 pollici.
> 
> 1. Sia $Z \sim \mathcal{N}(0,1)$ e siano $X_{1}$ e $X_{2}$ le precipitazioni dei prossimi due anni. La somma $X_{1}+X_{2}$ è normale con media $2 \times 12.08=24.16 \mathrm{e}$ varianza $2 \times(3.1)^{2}=$ 19.22. Ne segue che$$
\begin{aligned}
P\left(X_{1}+X_{2}>25\right) & =P\left(\frac{X_{1}+X_{2}-24.16}{\sqrt{19.22}}>\frac{25-24.16}{\sqrt{19.22}}\right) \\
& \approx P(Z>0.1916) \approx 0.4240
\end{aligned}$$
>2. Siccome $-X_{2}$ è gaussiana con media $-12.08 \mathrm{e}$ varianza $(-1)^{2} \times(3.1)^{2}$ (per la Proposizione 5.5.1, applicata con $\alpha=-1$ e $\beta=0$ ), si ha che $X_{1}-X_{2}$ è gaussiana con media nulla e varianza 19.22. Quindi $$
\begin{aligned}
P\left(X_{1}>X_{2}+3\right) & =P\left(X_{1}-X_{2}>3\right) \\
& =P\left(\frac{X_{1}-X_{2}}{\sqrt{19.22}}>\frac{3}{\sqrt{19.22}}\right) \\
& \approx P(Z>0.6843) \approx 0.2469
\end{aligned}$$
> Riassumendo, vi è una probabilità del $42.4 \%$ che nei prossimi due anni cadano a Los Angeles più di $25$ pollici di pioggia, e vi è una probabiltà del $24.69 \%$ che le precipitazioni dell'anno prossimo superino quelle dell'anno successivo per almeno $3$ pollici
