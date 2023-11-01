---
tags: [aleatoryVariable, probability, definition, to-do]
author: Lorenzo Tecchia
---
>[!todo] Inserire grafico

Una [[variabile aleatoria]] [[ContinuaVA|continua]] si dice ***uniforme*** sull'intervallo $[\alpha, \beta]$, se ha la funzione di densità data da:$$f(x) =\begin{cases} \frac{1}{\beta - \alpha} \;\; \ se \ \alpha \leq x \leq \beta \\
\ 0 \ \text{altrimenti}\end{cases}$$
Si noti che essa soddisfa le condizioni per essere una densità di probabilità, in quanto$$\int_{-\infty}^{\infty}f(x)dx=\frac{1}{\beta -\alpha}\int_{\alpha}^{\beta}dx = 1$$ 
Per poter assumere la distribuzione uniforme, nella pratica, occorre che la variabile aleatoria abbia come valori possibili i punti di un intervallo limitato $[\alpha, \beta]$; inoltre si deve poter supporre che essa abbia le stesse probabilità di cadere vicino ad un qualunque punto dell'intervallo.
>[!important] Inserire grafico di una distr. uniforme tra $\alpha$ e $\beta$

La probabilità che una variabile aleatoria $X$, uniforme su $[\alpha, \beta]$, appartenga ad un dato intervallo contenuto in $[\alpha, \beta]$ è pari al rapporto tra le lunghezze dei due intervalli.
Infatti se $[a,b]$ è contenuto in $[\alpha, \beta]$:$$\mathbb{P}(a < X < b)= \frac{1}{\beta - \alpha}\int_{a}^{b}dx=\frac{b-a}{\beta - \alpha}$$