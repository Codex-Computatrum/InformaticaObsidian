---
author: Lorenzo Tecchia
tags:
  - definition
  - probability
  - to-do
  - distribution
---
>[!todo] Inserire grafico

Una variabile aleatoria di *Poisson* o poissoniana di parametri $\lambda, \lambda > 0$, se la sua funzione di massa di probabilità è data da $$\mathbb{P}(X=i) = \frac{\lambda^{i}}{i!}e^{-\lambda}\;\;\;\;\; i = 0,1,2 \dots$$ È possibile verificare che l'equazione soprastante rappresenta una funzione di massa perché la componente dell'equazione $\sum_{i=0}^{\infty}\frac{\lambda^{i}}{i!}$ è la funzione generatrice dell'esponenziale da cui possiamo ricavare $$\sum_{i=0}^{\infty}\mathbb{P}(X = i) = e^{-\lambda}\sum_{i=0}^{\infty}\frac{\lambda^{i}}{i!} = 1$$

Sia $X$ una variabile aleatoria di Poisson. Per determinare la media e la varianza, calcoliamo la sua funzione generatrice dei momenti. $$
\begin{aligned}
\phi(t) & :=E\left[e^{t X}\right] \\
& =\sum_{i=0}^{\infty} e^{t i} P(X=i) \\
& =e^{-\lambda} \sum_{i=0}^{\infty} e^{t i} \frac{\lambda^{i}}{i !} \\
& =e^{-\lambda} \sum_{i=0}^{\infty} \frac{\left(\lambda e^{t}\right)^{i}}{i !} \\
& =e^{-\lambda} e^{\lambda e^{t}}=\exp \left\{\lambda\left(e^{t}-1\right)\right\}
\end{aligned}$$
Derivando si trova allora $$
\begin{aligned}
\phi^{\prime}(t) & =\lambda e^{t} \exp \left\{\lambda\left(e^{t}-1\right)\right\} \\
\phi^{\prime \prime}(t) & =\left(\lambda e^{t}\right)^{2} \exp \left\{\lambda\left(e^{t}-1\right)\right\}+\lambda e^{t} \exp \left\{\lambda\left(e^{t}-1\right)\right\}
\end{aligned}$$
e valutando le due espressioni in $t=0$, si ottiene $$
\begin{aligned}
E[X] & =\phi^{\prime}(0)=\lambda \\
\operatorname{Var}(X) & =\phi^{\prime \prime}(0)-E[X]^{2} \\
& =\lambda^{2}+\lambda-\lambda^{2}=\lambda
\end{aligned}$$
Quindi il valore atteso, sia la varianze delle poissoniane coincidono con il parametro $\lambda$

La poissoniana può essere utilizzata come approssimazione di una binomiale di parametri $(n,p)$, quando $n$ è molto grande e $p$ è molto piccolo. Per convincerci di questo fatto, sia $X$ una variabile aleatoria binomiale di parametri $(n,p)$, e si ponga $\lambda = np$. Allora $$\begin{align}
	\mathbb{P}(X = i) =& \frac{i!}{(n-i)!i!}p^{i}(1-p)^{n-i} \\
	=& \frac{n(n-1)\dots (n-i+1)}{i!}\left(\frac{\lambda}{n}\right)^{i}\left(1-\frac{\lambda}{n}\right)^{n-i} \\
	=&  \frac{n(n-1)\dots (n-i+1)}{n^{i}}\frac{\lambda^i}{i!}\frac{(1- \lambda/n)^n}{(1- \lambda/n)^i}	 
\end{align}$$
Se si suppone che $n$ sia molto grande e $p$ molto piccolo, valgono le seguenti approssimazioni$$\left(1- \frac{\lambda}{n}^{n}\right)\approx e^{-\lambda}\;\;\;\;\;\;\; \frac{n}{n} \cdot \frac{n-1}{n}\dots \frac{n-i+1}{n} \approx 1 \;\;\;\;\;\;\; \left(1- \frac{\lambda}{n}\right)^{i}\approx 1$$
E quindi se $n$ è grande, $p$ piccolo, e $\lambda = np$,$$\mathbb{P}(X = i) \approx \frac{\lambda^{i}}{i!}e^{-\lambda}$$
In altri termini, il totale dei "successi" in un gran numero $n$ di ripetizioni indipendenti di n esperimento che ha una piccola probabilità di riuscita $p$, è una variabile aleatoria con distribuzione approssimativamente di Poisson, con media $\lambda = np$