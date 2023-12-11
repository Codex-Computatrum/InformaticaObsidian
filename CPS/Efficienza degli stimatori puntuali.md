---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - parametricEstimation
  - sampling
---
Sia $X := (X_{1}, X_{2}, \dots, X_{n})$ un [[campione]] causale estratto da una [[popolazione]] di [[distribuzione]] nota eccetto che per un parametro incognito $\theta$, e sia $d=d(X)$ uno stimatore di $\theta$. Come possiamo valutare la sua efficacia come stimatore? Un criterio potrebbe essere quello di considerare il quadrato della sua differenza tra $d(X)$ e $\theta$, però $(d(X)-\theta)^{2}$ è una [[variabile aleatoria]], quindi stabiliamo di adoperare $r(d, \theta)$, l'*errore quadratico medio dello stimatore* $d$, che è per definizione
$$
r(d, \theta):=E\left[(d(X)-\theta)^{2}\right]
$$
Sarà questo il nostro indicatore del valore di $d$ come stimatore di $\theta$.
Sarebbe ideale se esistesse un singolo stimatore $d$ che minimizzasse $r(d, \theta)$ per tutti i valori di $\theta$, però questo non accade tranne che in situazioni comunque banali.
Infatti se definiamo lo stimatore $d^{*}$ in modo che sia sempre uguale a $4$
$$
d^{*}(X) \equiv 4
$$
anche se questa scelta può sembrare assurda (ad esempio perché lo stimatore non fa alcun uso dei dati), è certamente vero che quando $\theta = 4$, questo stimatore, con il suo errore quadratico medio nullo, si comporta meglio di qualunque altro.
Anche se stimatori con errore quadratico medio minimo esistono raramente, a volte si può trovarne uno che minimizzi $r(d, \theta)$ tra tutti quelli che soddisfano una certa proprietà, come ad esempio quella di non essere distorti.

>[!important] ## Definzione
> Sia $d = d(X)$ uno stimatore del parametro $\theta$. Allora 
> $$
b_{\theta}(d):=E[d(X)]-\theta
> $$
> è detto *bias* di $d$ come stimatore di $\theta$. Se esso è nullo, diciamo che $d$ è uno stimatore *corretto* o anche *non distorto*
> In altri termini, uno stimatore è corretto se il suo [[valore atteso]] coincide con il parametro che esso deve stimare.

>[!example]
> Sia $X_{1}, X_{2}, \dots, X_{n}$ un [[campione]] proveniente da una [[popolazione]] di [[Valore atteso|media]] incognita $\theta$. Allora le due statistiche seguenti,
> $$
\begin{aligned}
& d_{1}\left(X_{1}, X_{2}, \ldots, X_{n}\right)=X_{1} \\
& d_{2}\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\frac{X_{1}+X_{2}+\cdots+X_{n}}{n}
\end{aligned}
> $$
> sono entrambe degli stimatori non distorti di $\theta$; la verifica è immediata,
> $$
E\left[X_{1}\right]=E\left[\frac{X_{1}+X_{2}^{1}+\cdots+X_{n}}{n}\right]=\theta
> $$
> Più in generale, $d_{3}(X_{1}, X_{2}, \dots, X_{n}):= \sum_{i=1}^{n}\lambda_{i}X_{i}$ è uno stimatore corretto di $\theta$ ogni volta che  $\sum_{i=1}^{n}\lambda_{i}=1$. Infatti
> $$
\begin{aligned}
E\left[\sum_{i=1}^{n} \lambda_{i} X_{i}\right] & =\sum_{i=1}^{n} \lambda_{i} E\left[X_{i}\right] \\
& =\sum_{i=1}^{n} \lambda_{i} \theta=\theta
\end{aligned}
> $$

>[!important]
>Se $d= d(X)$ è uno stimatore corretto, allora il suo errore quadratico medio è
>$$
\begin{aligned}
r(d, \theta) & =E\left[(d-\theta)^{2}\right] \\
& =E\left[(d-E[d])^{2}\right] \\
& =\operatorname{Var}(d)
\end{aligned}
> $$
> ***Quindi l'errore quadratico medio di uno stimatore corretto è pari alla sua [[varianza]]***

---

>[!example] Combinazione di stimatori corretti indipendenti
> Consideriamo due stimatori corretti e indipendenti di un parametro $\theta$, denotati $d_{1}$ e $d_{2}$, e siano $\sigma_{1}^{2}$ e $\sigma_{2}^{2}$ le rispettive varianze. Quindi per $i=1,2$,
> $$
E\left[d_{i}\right]=\theta \quad \operatorname{Var}\left(d_{i}\right)=\sigma_{i}^{2}
> $$
> Qualunque statistica della forma
> $$
d:=\lambda d_{1}+(1-\lambda) d_{2}
> $$
> sarà comunque uno stimatore corretto di $\theta$. Vogliamo allora trovare il valore di $\lambda$ che produce lo stimatore $d$ con minore errore quadratico medio. Notiamo intanto che
> $$
\begin{aligned}
r(d, \theta) & =\operatorname{Var}(d) \\
& =\lambda^{2} \operatorname{Var}\left(d_{1}\right)+(1-\lambda)^{2} \operatorname{Var}\left(d_{2}\right) \quad \text { per l'indipendenza di } d_{1} \text { e } d_{2} \\
& =\lambda^{2} \sigma_{1}^{2}+(1-\lambda)^{2} \sigma_{2}^{2}
\end{aligned}
> $$
> Per minimizzare questa espressione, ne calcoliamo la derivata,
> $$
\frac{d}{d \lambda} r(d, \theta)=2 \lambda \sigma_{1}^{2}-2(1-\lambda) \sigma_{2}^{2}
> $$
> e ne studiamo il segno, denotando con $\hat{\lambda}$ il valore di $\lambda$ che produce il minimo,
> $$
2 \hat{\lambda} \sigma_{1}^{2}-2(1-\hat{\lambda}) \sigma_{2}^{2}=0
> $$
> da cui
> $$
\hat{\lambda}=\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}}=\frac{1 / \sigma_{1}^{2}}{1 / \sigma_{1}^{2}+1 / \sigma_{2}^{2}}
> $$
> Altrimenti detto, il peso ottimale da dare a uno stimatore deve essere inversamente proporzionale alla sua [[varianza]] (solo nell'ipotesi che tutti gli stimatori siano corretti e indipendenti)
> Per vedere una applicazione di quanto detto, immaginiamo che una associazione per la conservazione ambientare voglia determinare l'acidità delle acque ddi un certo lago. Raccoglie quindi dei campioni d'acqua che invia a $n$ diversi laboratori di analisi. Questi ultimi effettueranno la titolazione indipendentemente l'uni dagli altri, ciascuno con le proprie attrezzature, dotate di livelli di precisioni diversi. IN particolare, ipotizziamo che per $i$ che va da $1$ a $n$, $d_{i}$ sia il risultato delle analisi del laboratorio $i-$ una [[variabile aleatoria]] con [[Valore atteso|media]] pari al livello di acidità $\theta$, e con [[varianza]] $\sigma^{2}_{i}$. Se le varianze sono conosciute, l'associazione dovrebbe stimare l'acidità dei campioni d'acqua con
> $$
d=\frac{\sum_{i=1}^{n} d_{i} / \sigma_{i}^{2}}{\sum_{i=1}^{n} 1 / \sigma_{i}^{2}}
> $$
> che è la migliore combinazione lineare delle $d_{i}$ per quanto riguarda l'errore quadratico medio:
> $$
\begin{aligned}
r(d, \theta) & =\operatorname{Var}(d) \quad \text { perché } d \text { è non distorto } \\
& =\left(\frac{1}{\sum_{i=1}^{n} 1 / \sigma_{i}^{2}}\right)^{2} \sum_{i=1}^{n}\left(\frac{1}{\sigma_{i}^{2}}\right)^{2} \sigma_{i}^{2} \\
& =\frac{1}{\sum_{i=1}^{n} 1 / \sigma_{i}^{2}}
\end{aligned}
> $$

Il fatto che per uno stimatore non distorto l'errore quadratico medio coincida con la [[varianza]] si può generalizzare ad uno stimare qualsiasi: la formula viene corretta sommando il quadrato dei *bias*, come si deduce dai passaggi seguenti
$$
\begin{aligned}
& r(d, \theta)=E\left[(d-\theta)^{2}\right] \\
& =E\left[(d-E[d]+E[d]-\theta)^{2}\right] \\
& =E\left[(d-E[d])^{2}+2(d-E[d])(E[d]-\theta)+(E[d]-\theta)^{2}\right] \\
& =E\left[(d-E[d])^{2}\right]+2(E[d]-\theta) E[d-E[d]]+E\left[(E[d]-\theta)^{2}\right] \\
& =\operatorname{Var}(d)+0+E\left[b_{\theta}(d)^{2}\right] \quad \quad \text { perché } d-E[d] \text { ha valore atteso nulla } \\
& =\operatorname{Var}(d)+b_{\theta}(d)^{2}
\end{aligned}
$$

>[!example]-
> Sia $X_{1}, X_{2}, \dots, X_{n}$ un [[Campione|campione aleatorio]] estratto da una [[popolazione]] [[distribuzione]] [[uniforme]] $(0, \theta)$, dove $\theta$ è un parametro incognito. Poiché $E[X_{i}] = \theta/2$, uno stimatore corretto "naturale" per $\theta$ è dato da
> $$
d_{1}=d_{1}(\boldsymbol{X}):=2 \bar{X}:=\frac{2}{n} \sum_{i=1}^{n} X_{i}
> $$
> Siccome $E[d_{1]}= \theta$, si ottiene che
> $$
\begin{aligned}
r\left(d_{1}, \theta\right) & =\operatorname{Var}\left(d_{1}\right) \\
& =\frac{4}{n} \operatorname{Var}\left(X_{i}\right) \\
& =\frac{4}{n} \frac{\theta^{2}}{12}\\
& =\frac{\dot{\theta}^{2}}{3 n}
\end{aligned}
> $$
> Un secondo stimatore possibile per $\theta$ è quello di massima verosimiglianza, che abbiamo dimostrato essere 
> $$
d_{2}=d_{2}(\boldsymbol{X}):=\max _{i} X_{i}
> $$
> Per calcolare l'errore quadratico medio di $d_{2}$ occorre prima conoscere la sua [[Valore atteso|media]] (per ottenere il *bias*) e la sua [[varianza]]. Cerchiamo per cominciare la funzione di ripartizione.
> $$
\begin{aligned}
F_{2}(x) & =P\left(d_{2}(\boldsymbol{X}) \leq x\right) \\
& =P\left(\max _{i} X_{i} \leq x\right) \\
& =P\left(X_{1} \leq x, X_{2} \leq x, \ldots, X_{n} \leq x\right) \\
& =\prod_{i=1}^{n} P\left(X_{i} \leq x\right) \quad \text { per l'indipendenza } \\
& =F_{X_{i}}(x)^{n}=\left(\frac{x}{\theta}\right)^{n}, \quad 0 \leq x \leq \theta
\end{aligned}
> $$
> Derivando la funzione di ripartizione si trova la densità di $d_{2}$,
> $$
f_{2}(x)=\frac{n x^{n-1}}{\theta^{n}}, \quad 0 \leq x \leq \theta
> $$
> e quindi possiamo calcolare i primi due momenti e la [[varianza]] di $d_{2}$,
> $$
\begin{aligned}
E\left[d_{2}\right] & =\int_{0}^{\theta} x \frac{n x^{n-1}}{\theta^{n}} d x=\frac{n}{n+1} \theta \\
E\left[d_{2}^{2}\right] & =\int_{0}^{\theta} x^{2} \frac{n x^{n-1}}{\theta^{n}} d x=\frac{n}{n+2} \theta^{2} \\
\operatorname{Var}\left(d_{2}\right) & =E\left[d_{2}^{2}\right]-E\left[d_{2}\right]^{2} \\
& =\frac{n}{n+2} \theta^{2}-\frac{n^{2}}{(n+1)^{2}} \theta^{2} \\
& =n \theta^{2}\left[\frac{1}{n+2}-\frac{n}{(n+1)^{2}}\right] \\
& =\frac{n \theta^{2}}{(n+2)(n+1)^{2}}
\end{aligned}
> $$
> Quindi 
> $$
\begin{aligned}
r\left(d_{2}, \theta\right) & =\operatorname{Var}\left(d_{2}\right)+\left(E\left[d_{2}\right]-\theta\right)^{2} \\
& =\frac{n \theta^{2}}{(n+2)(n+1)^{2}}+\frac{\theta^{2}}{(n+1)^{2}} \\
& =\frac{\theta^{2}}{(n+1)^{2}}\left[\frac{n}{n+2}+1\right] \\
& =\frac{2 \theta^{2}}{(n+1)(n+2)}
\end{aligned}
> $$
> Possiamo ora confrontare i due valori trovati per gli errori quadratici medi di $d_{1}$ e $d_{2}$, e siccome per ogni $n=1,2,\dots$,
> $$
\frac{2 \theta^{2}}{(n+1)(n+2)} \leq \frac{\theta^{2}}{3 n}
> $$
> ne segue che $d_{2}$ è migliore di $d_{1}$ come stimatore per $\theta$
> L'espressine per il [[valore atteso]] di $d_{2}$ fornita dall'equazione precedente, suggerisce ancora un altro stimatore, infatti se la [[Valore atteso|media]] di $d_{2}$ è $n \cdot \theta / (n+1)$, allora 
> $$
\frac{n+1}{n} d_{2}=\frac{n+1}{n} \max _{i} X_{i}
> $$
> è sicuramente uno stimatore corretto. Comunque, piuttosto che calcolare l'errore quadratico medio di questo stimatore in particolare, consideriamo tutti quelli della forma
> $$
d_{c}(\boldsymbol{X}):=c \cdot \max _{i} X_{i}=c \cdot d_{2}(\boldsymbol{X})
> $$
> dove $c$ è costante assegnata. Il corrispondente errore quadratico medio è 
> $$
\begin{aligned}
r\left(d_{c}, \theta\right) & =\operatorname{Var}\left(d_{c}\right)+\left(E\left[d_{c}\right]-\theta\right)^{2} & & \\
& =c^{2} \operatorname{Var}\left(d_{2}\right)+\left(c E\left[d_{2}\right]-\theta\right)^{2} & \\
& =\frac{c^{2} n \theta^{2}}{(n+2)(n+1)^{2}}+\theta^{2}\left(c \frac{n}{n+1}-1\right)^{2} & 
\end{aligned}
> $$
> Per determinare la costante $c^{*}$ cui corrisponda lo stimatore com il minore errore quadratico medio tra tutti quelli del tipo $d_{c}(X)$, deriviamo l'espressione di $r(d_{c}, \theta)$,
> $$
\begin{aligned}
\frac{d}{d c} r\left(d_{c}, \theta\right) & =\frac{2 c n \theta^{2}}{(n+2)(n+1)^{2}}+\frac{2 n \theta^{2}}{n+1}\left(c \frac{n}{n+1}-1\right) \\
& =\frac{2 n \theta^{2}}{(n+1)^{2}}\left[\frac{c}{n+2}+c n-(n+1)\right]
\end{aligned}
> $$
> quindi la poniamo uguale a zero,
> $$
\frac{c^{*}}{n+2}+c^{*} n-(n+1)=0
> $$
> ricaviamo $c^{*}$,
> $$
c^{*}=\frac{(n+1)(n+2)}{n^{2}+2 n+1}=\frac{n+2}{n+1}
> $$
> e infine scopriamo che il migliore stimatore tra quelli del tipo $d_{c}(X)$ è costituito da 
> $$
\frac{n+2}{n+1} \max _{i} X_{i}
> $$
> Si tratta di uno stimatore distorto con errore quadratico medio che (sostituendo $c^{*}$ nell'equazione precedente) è dato da 
> $$
\begin{aligned}
r\left(d_{c^{*}}, \theta\right) & =\frac{n(n+2) \theta^{2}}{(n+1)^{4}}+\theta^{2}\left(\frac{n(n+2)}{(n+1)^{2}}-1\right)^{2} \\
& =\frac{n(n+2) \theta^{2}}{(n+1)^{4}}+\frac{\theta^{2}}{(n+1)^{4}} \\
& =\frac{\theta^{2}}{(n+1)^{2}}
\end{aligned}
> $$
> Un confronto con i risultati precedenti ci permette di concludere che anche se l'ultimo stimatore trovato non è corretto (ha un *bias* non nullo), il suo errore quadratico medio è poco più della metà di quello dello stimatore di massima verosimiglianza.