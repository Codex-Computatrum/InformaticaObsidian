---
tags:
  - statistics
  - theorem
  - probability
author: Lorenzo Tecchia
aliases:
  - TLC
  - CLT
---
>[!tldr]-
> La somma di un numero elevato di variabili aleatorie indipendenti, tende ad avere distribuzione approssimativamente normale.[^1]

>[!important] # Definition
> Siano $X_{1}, X_{2}, \dots, X_{n}$ delle variabili aleatorie i.i.d. (indipendenti e identicamente distribuite), tutte con media $\mu$ e varianza $\sigma^{2}$. Allora se $n$ è grande la somma $$X_{1}+ X_{2}+ \dots +X_{n}$$ è approssimativamente normale con media $n\mu$ e varianza $n\sigma^{2}$

Si può anche normalizzare la somma precedente in modo da ottenere una distribuzione approssimativamente *normale standard*. Si ha infatti che $$
\frac{X_{1}+X_{2}+\cdots+X_{n}-n \mu}{\sigma \sqrt{n}} \dot{\sim} \mathcal{N}(0,1)$$ dove con il simbolo $\dot{\sim}$ si intende "è approssimativamente distribuito come". Ciò significa che per $n$ grande  e $x$ qualsiasi vale l'approssimazione $$
P\left(\frac{X_{1}+X_{2}+\cdots+X_{n}-n \mu}{\sigma \sqrt{n}}<x\right) \approx \Phi(x)$$ dove $\Phi$ denota la funzione di ripartizione della normale standard.

>[!example]- Gli ingegneri che stanno studiando un ponte sono convinti che il numero di tonnellate $W$, che una singola campata può sostenere senza subire danni strutturali, sia una variabile aleatoria normale di media $200$ e deviazione standard $20$. Supponiamo che il peso in tonnellate degli autoveicoli che vi passano sia una variabile aleatoria di media $1.5$ e deviazione standard $0.15$. Quante automobili dovrebbero essere contemporaneamente sulla campata, affinché la probabilità di danno strutturale superi il $10\%$?
> Sia $P_{n}$ la probabilità di un danno strutturale, quando vi sono $n$ autoveicoli.
> $$\begin{aligned}
P_{n} & =P\left(X_{1}+X_{2}+\cdots+X_{n} \geq W\right) \\
& =P\left(X_{1}+X_{2}+\cdots+X_{n}-W \geq 0\right)\end{aligned}$$ 
dove $X_{1}, X_{2}, \dots, X_{n}$ sono pesi delle auto. Per il teorema del limite centrale, $\sum\limits_{i=1}^{n}X_i$ è approssimativamente normale, $\mathcal{N}(1.5n, 0.0225n)$. Quindi, siccome $W$ è indipendente da tutte le $X_{i}$ ed è normale, ne segue che $\sum\limits_{i=1}^{n}X_{i}-W$ è approssimativamente normale con media e varianza date da $$
\begin{aligned}
E\left[\sum_{i=1}^{n} X_{i}-W\right] & =1.5 n-200 \\
\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}-W\right) & =\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right)+\operatorname{Var}(W)=0.0225 n+400
\end{aligned}$$
> Perciò, se poniamo $$
Z:=\frac{\sum_{i=1}^{n} X_{i}-W-(1.5 n-200)}{\sqrt{0.0225 n+400}}$$ allora $$
\mathbb{P}_{n}=\mathbb{P}\left(Z \geq \frac{-(1.5 n-200)}{\sqrt{0 . 0225 n+400}}\right)$$ dove $Z$ è approssimativamente normale standard. Quindi se il numero di autoveicoli $n$ è tale che $$
\frac{200-1.5 n}{\sqrt{0.0225 n+400}} \leq 1.28$$ ovvero quando $n \leq 117$ (si trova ricavando $n$, o per tentativi), vi è ameno $1$ probabilità su $10$ che il ponte subisca danni strutturali.

---
Una delle dirette applicazioni del teorema del limite centrale riguarda le variabile aleatorie [[Binomiale|binomiali]]. Siccome una binomiale $X$ di parametri $(n, p)$ rappresenta il numero di successi in $n$ prove indipendenti, ciascuna con probabilità $p$ di riuscita, possiamo scrivere $$X=X_{1}+X_{2}+\cdots+X_{n}$$ dove $$ X_{i}:= \begin{cases}1 & \text { se l' } i \text {-esima prova ha successo } \\ 0 & \text { altrimenti }\end{cases}$$ Poiché, come sappiamo, $$
E\left[X_{i}\right]=p, \quad \operatorname{Var}\left(X_{i}\right)=p(1-p)$$ segue dal teorem a del limite centrale che, per $n$ grande, $$
\frac{X-n p}{\sqrt{n p(1-p)}} \dot{\sim} \mathcal{N}(0,1)$$ ovvero vale una *approssimazione normale* delle variabili aleatorie binomiali

---
>[!warning]-
> II teorema del limite centrale lascia aperta la questione di quanto grande debba essere la numerosità del campione $n$, affinché l'approssimazione normale sia valida. In effetti la risposta dipende dalla distribuzione da cui vengono campionati $i$ dati. Ad esempio, se la distribuzione della [[popolazione]] è normale, allora $\bar{X}$ sarà a sua volta normale indipendentemente dall'ampiezza del campione (questo perché la distribuzione normale è riproducibile: si veda a pagina 176 ). Una buona regola empirica è che si può essere confidenti nella validità dell'approssimazione se $n$ è almeno 30 . Questo vuole dire che, per quanto "poco gaussiana" sia la distribuzione considerata, la [[media campionaria]] di un gruppo di dati di numerosità 30 risulta comunque approssimativamente normale. Si tenga presente comunque che in molti casi è possibile che questo accada anche per $n$ molto più piccolo, e in effetti spesso $n=5$ è sufficiente ad ottenere approssimazioni non troppo sbagliate. La Figura 6.4 presenta la distribuzione delle medie campionarie di una [[popolazione]] esponenziale, per $n$ pari a $1,5 \mathrm{e}$ 10.


[^1]:  Spesso il "teorema del limite centrale" lo si trova abbreviato negli acronimi $\operatorname{TLC}$ o $\operatorname{CLT}$, dove il secondo deriva ovviamente dall'espressione inglese corrispondente, *central limit theorem*