---
tags:
  - probability
  - definition
  - to-do
  - distribution
author: Lorenzo Tecchia
---
>[!todo] Inserire grafico

Una [[variabile aleatoria]] [[Continua|continua]] si dice ***uniforme*** sull'intervallo $[\alpha, \beta]$, se ha la funzione di densità data da:$$f(x) =\begin{cases} \frac{1}{\beta - \alpha} \;\; \ se \ \alpha \leq x \leq \beta \\
\ 0 \ \text{altrimenti}\end{cases}$$
Si noti che essa soddisfa le condizioni per essere una densità di probabilità, in quanto$$\int_{-\infty}^{\infty}f(x)dx=\frac{1}{\beta -\alpha}\int_{\alpha}^{\beta}dx = 1$$ 
Per poter assumere la distribuzione uniforme, nella pratica, occorre che la variabile aleatoria abbia come valori possibili i punti di un intervallo limitato $[\alpha, \beta]$; inoltre si deve poter supporre che essa abbia le stesse probabilità di cadere vicino ad un qualunque punto dell'intervallo.
>[!important] Inserire grafico di una distr. uniforme tra $\alpha$ e $\beta$

La probabilità che una variabile aleatoria $X$, uniforme su $[\alpha, \beta]$, appartenga ad un dato intervallo contenuto in $[\alpha, \beta]$ è pari al rapporto tra le lunghezze dei due intervalli.
Infatti se $[a,b]$ è contenuto in $[\alpha, \beta]$:$$\mathbb{P}(a < X < b)= \frac{1}{\beta - \alpha}\int_{a}^{b}dx=\frac{b-a}{\beta - \alpha}$$

>[!example]-
> Ad una certa fermata passa un autobus ogni $15$ minuti a cominciare dalle $7$ (quindi alle $7.00$ alle $7.15$ alle $7.30$). Se un passeggero arriva alla fermata in un momento causale con distribuzione uniforme tra le $7$ e le $7.30$, si calcoli con che probabilità dovrà aspettare meno di $5$ minuti per il prossimo autobus oppure almeno 12 minuti.
> Sia $X$ l'istante (espresso in termini di minuti dopo le $7$) in cui questa persona arriva alla fermata, $X$ è ovviamente uniforme sull'intervallo $[0, 30]$. Siccome il passeggero deve aspettare meno di $5$ minuti solo se arriva tra le $7.10$ e le $7.15$, oppure tra le $7.25$ e le $7.30$, la probabilità richiesta è data da $$P(10<X<15)+P(25<X<30)=\frac{5}{30}+\frac{5}{30}=\frac{1}{3}$$ Analogamente, egli deve attendere almeno $12$ minuti se arriva tra le $7$ e le $7.03$ o tra le $7.15$ e le $7.18$, quindi la probabilità cercata è pari a $$
P(0<X<3)+P(15<X<18)=\frac{3}{30}+\frac{3}{30}=\frac{1}{5}$$


Determiniamo ora la media di una variabile aleatoria $X$, uniforme su $[\alpha, \beta]$: $$
\begin{aligned}
E[X] & :=\int_{\alpha}^{\beta} \frac{x d x}{\beta-\alpha} \\
& =\frac{\beta^{2}-\alpha^{2}}{2(\beta-\alpha)} \\
& =\frac{(\beta-\alpha)(\beta+\alpha)}{2(\beta-\alpha)}=\frac{\alpha+\beta}{2}
\end{aligned}$$
Perciò il valore atteso di una variabile aleatoria uniforme è il punto medio del suo intervallo di definizione, come si poteva intuire direttamente senza fare i calcoli.

Per ottenere la varianza ci serve il momento secondo. $$
\begin{aligned}
E\left[X^{2}\right] & =\int_{\alpha}^{\beta} \frac{x^{2} d x}{\beta-\alpha} \\
& =\frac{\beta^{3}-\alpha^{3}}{3(\beta-\alpha)} \\
& =\frac{\alpha^{2}+\alpha \beta+\beta^{2}}{3}
\end{aligned}$$ Quindi $$
\begin{aligned}
\operatorname{Var}(X) & =\frac{\alpha^{2}+\alpha \beta+\beta^{2}}{3}-\left(\frac{\alpha+\beta}{2}\right)^{2} \\
& =\frac{\alpha^{2}-2 \alpha \beta+\beta^{2}}{12} \\
& =\frac{(\beta-\alpha)^{2}}{12}
\end{aligned}$$