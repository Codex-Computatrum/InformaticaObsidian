---
author: Lorenzo Tecchia
tags: [definition, statistics, probability]
---
Vista la indeterminazione del parametro incognito $\theta$, in alcune situazioni può essere ragionevole considerarlo assumere la forma una [[variabile aleatoria]]: il valore vero del parametro da stimare diviene quindi il numero realizzato dalla [[variabile aleatoria]]. Tale approccio, che viene detto bayesiano, è di norma giustificato quando, prima di osservare gli esiti del [[campione]] di dati $X_{1}, X_{2}, \ldots, X_{n}$, abbiamo delle informazioni su quelli che possono essere i valori assunti da $\theta$, e magari sulla loro plausibità. Se queste informazioni a priori assumono la forma di una [[distribuzione]] di [[probabilità]], questa prende appropriatamente il nome di [[distribuzione]] a priori per $\theta$ (in inglese è la prior distribution). Per esempio supponiamo che, dall'esperienza passata, ci si aspetti che $\theta$ possa avere un qualunque valore compreso tra $0 \mathrm{e} 1$, ma non valori esterni a quell'intervallo. Se inoltre $\theta$ ha le stesse possibilità di essere vicino a qualunque punto di $(0,1)$, possiamo ragionevolmente assumere che si tratti di una [[variabile aleatoria]] [[uniforme]] su $(0,1)$.

Supponiamo allora di potere esprimere le nostre considerazioni a priori su $\theta$ nella forma di una [[distribuzione]] [[continua]], con densità di probabilità $p(\theta)$; osserviamo i valori di un [[campione]] di dati la cui distribuzione dipende da $\theta$, e denotiamo con $f(x \mid \theta)$ la funzione di likelihood - si tratta quindi della funzione di massa di probabilità nel caso discreto, oppure della funzione di densità di probabilità nel caso continuo - che esprime la plausibilità che uno dei dati sia uguale a $x$ quando $\theta$ è il valore del parametro. Se $\mathrm{i}$ valori osservati sono $X_{i}=x_{i}$, per $i=1,2, \ldots, n$, allora la densità di probabilità condizionale di $\theta$ è data da

$$
\begin{aligned}
f\left(\theta \mid x_{1}, x_{2}, \ldots, x_{n}\right) & =\frac{f\left(x_{1}, x_{2}, \ldots, x_{n}, \theta\right)}{f\left(x_{1}, x_{2}, \ldots, x_{n}\right)} \\
& =\frac{f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \theta\right) p(\theta)}{\int f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \theta^{\prime}\right) p\left(\theta^{\prime}\right) d \theta^{\prime}}
\end{aligned}
$$

La densità condizionale $f\left(\theta \mid x_{1}, x_{2}, \ldots, x_{n}\right)$ è detta densità di probabilità *a posteriori*. 
La migliore stima di $\theta$, assegnati i valori dei dati $X_{i} = x_{i}$, per $i=1, \dots, n$, è data dalla [[Valore atteso|media]] della distribuzione a posteriori $f(\theta|x_{1},x_{2},\dots, x_{m})d\theta$. Lo stimatore appena descritto è detto *stimatore bayesiano*, si indica con $E[\theta|X_{1},X_{2}, \dots, X_{n}]$ il suo valore si calcola nel modo usuale:
$$
E\left[\theta \mid X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right]=\int_{-\infty}^{\infty} \theta f\left(\theta \mid x_{1}, x_{2}, \ldots, x_{n}\right) d \theta
$$