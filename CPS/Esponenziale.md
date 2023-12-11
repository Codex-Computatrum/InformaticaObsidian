---
tags:
  - definition
  - probability
  - to-do
  - distribution
  - example
author: Lorenzo Tecchia
---
>[!todo]
> Inserire grafico

Una [[variabile aleatoria]] [[Continua|continua]] la cui funzione di densità di probabilità è data da: $$f(x) = \begin{cases} \lambda e^{-\lambda x} &se \ x \geq 0\\
0 & se \ x < 0
\end{cases}$$
per un opportuno valore della costante $\lambda > 0$, si dice esponenziale con parametro (*o densità*) $\lambda$.

La [[funzione di distribuzione]] di una tale variabile aleatoria è data da:$$\begin{align}
\mathcal{F}(x) &= \mathbb{P}(X \leq x) \\
&= \int_{0}^{x}\lambda e^{-\lambda y}dy \\
&= 1 - e^{- \lambda x}, \;\;\;\;\; x \geq 0
\end{align}$$
Nella pratica, la distribuzione esponenziale può rappresentare il tempo di attesa prima che si verifichi un certo evento causale. Come per esempio:

>[!example]-
> Il tempo che trascorrerà (a partire da questo momento), fino al verificarsi, di un terremoto; o allo scoppiare di un nuovo conflitto, o al giungere della prossima telefonata di qualcuno che ha sbagliato numero.

Sono tutte variabili aleatorie che in pratica tendono ad avere distribuzioni esponenziali.

La proprietà centrale della distribuzione esponenziale è la sua assenza di *memoria*. Con questa espressione, riferita ad una variabile aleatoria positiva $X$ si s intende che:$$\mathbb{P}(X > s + t|X > t) =\mathbb{P}(X> s)\;\;\;\;\;\;\forall s,t \geq 0$$ ^31ded8
>[!example]-
> Si immagini che $X$ rappresenti il tempo di vita di un certo oggetto prima di guastarsi. Sapendo che tale oggetto è già in funzione da un tempo $t$ e non si è ancora rotto, qual è la probabilità che esso continui a funzionare per almeno un ulteriore intervallo di tempo $s$? Chiaramente la probabilità richiesta è quella espressa dal membro sinistro dell'equazione [[Esponenziale#^31ded8|soprastante]]. Infatti dire che l'oggetto non si è ancora guastato al tempo $t$ equivale a dire che il tempo in cui avverrà la rottura $(X)$ è superiore a $t$, mentre affermare che che l'oggetto funzionerà per un ulteriore tempo $s$ a partire dal tempo $t$, significa che il tempo $X$ dovrà essere maggiore di $t+s$. In questo senso, l'equazione [[Esponenziale#^31ded8|soprastante]] afferma che la distribuzione del tempo di vita rimanente dell'oggetto considerato, è la medesima sia nel caso in cui esso stia funzionando da un tempo $t$, sia nel caso in cui esso sia nuovo, o, in altri termini, se l'equazione è soddisfatta, non vi è alcun bisogno di tenere presente l'età dell'oggetto, perché fino a che esso funziona, si comporta esattamente come fosse "nuovo di zecca".

La condizione di assenza di memoria è equivalente a chiedere che: $$\frac{\mathbb{P}(X > s+t,X>t)}{\mathbb{P}(X > t)} = \mathbb{P}(X > s)$$
e quindi anche che:$$\mathbb{P}(X > s+t)=\mathbb{P}(X > s)\mathbb{P}(X > t)$$
Quest'ultima formulazione è facilmente verificabile se $X$ è esponenziale, visto che per $x > 0, \mathbb{P}(X> x)= e^{-\lambda x}$ e ovviamente $e^{- \lambda(s+t)}= e^{-\lambda s}e^{-\lambda t}$. Abbiamo quindi provato che le variabili aleatorie esponenziali sono prive di memoria.(*È possibile dimostrare che sono le uniche con tale proprietà*)

--- 
La funzione generatrice dei momenti di una variabile aleatoria esponenziale di intensità $\lambda$ è data da $$
\begin{aligned}
\phi(t) & :=E\left[e^{t X}\right] \\
& =\int_{0}^{\infty} e^{t x} \lambda e^{-\lambda x} d x \\
& =\lambda \int_{0}^ {\infty} e^{-(\lambda-t) x} d x \\
& =\frac{\lambda}{\lambda-t}, \quad t<\lambda
\end{aligned}$$ Derivando si trova che $$
\begin{aligned}
\phi^{\prime}(t) & =\frac{\lambda}{(\lambda-t)^{2}} \\
\phi^{\prime \prime}(t) & =\frac{2 \lambda}{(\lambda-t)^{3}}
\end{aligned}$$ e da cui è facile ottenere i primi due momenti e la varianza. $$
\begin{aligned}
E[X] & =\phi^{\prime}(0)=\frac{1}{\lambda} \\
E\left[X^{2}\right] & =\phi^{\prime \prime}(0)=\frac{2}{\lambda^{2}} \\
\operatorname{Var}(X) & =E\left[X^{2}\right]-E[X]^{2}=\frac{1}{\lambda^{2}}
\end{aligned}$$

Per una variabile aleatoria esponenziale, $\lambda$ è il reciproco del valore atteso, e la varianza è il quadrato di quest'ultimo.

>[!example]-
> Supponiamo che il numero di miglia percorse da una automobile prima che la sua batteria sia esausta sia una variabile aleatoria esponenziale di media $10000$ miglia. Se una persona intende intraprendere un viaggio di $5000$, qual è la probabilità che lo porti a termine senza dover sostituire la batteria? Cosa si può dire quando la distribuzione non è esponenziale?
> La proprietà di assenza di memoria della distribuzione esponenziale implica che il tempo di vita residuo della batteria dall'inizio del viaggio è esponenziale con intensità $\lambda = 1/10$. La probabilità cercata è data quindi da $$
\begin{aligned}
\mathbb{P}(\text { vita residua }>5) & =1-F(5) \\
& =e^{-5 \lambda} \\
& =e^{-0.5} \approx 0.607
\end{aligned}$$ Se on sapessimo che la distribuzione è esponenziale, la probabilità richiesta sarebbe data da $$
\mathbb{P}(\text { vita residua }>5)=\mathbb{P}(\text { vita totale }>t+5 \mid \text { vita totale }>t)
=\frac{1-F(t+5)}{1-F(t)}$$ dove $t$ è il numero di miglia di funzionamento della batteria fino al momento del viaggio. Perciò se la distribuzione è esponenziale, è necessario ottenere nuove informazione per poter calcolare la probabilità desiderata.

---
>[!important] ### Proposizione
> Se $X_{1}, X_{2}, \dots, X_{n}$ sono variabili aleatorie esponenziali e indipendenti, di parametri $\lambda_{1}, \lambda_{2}, \dots, \lambda_{n}$ rispettivamente, allora la variabile aleatoria $Y := \operatorname{min}(X_{1}, X_{2}, \dots, X_{n})$ è esponenziale di parametro $\sum\limits_{i=1}^{n}\lambda_{i}$
> ***Dimostrazione***: Basta dimostrare che $\mathbb{P}(Y > x)= exp(-x\sum\limits_{i=1}^{n}\lambda_{i})$. Siccome il minore di un insieme di numeri è più grande di $x$ se e solo se ciascuno dei numeri in questione è maggiore di $x$, abbiamo che $$
\begin{aligned}
P(Y>x) & =P\left(\min \left(X_{1}, X_{2}, \ldots, X_{n}\right)>x\right) \\
& =P\left(X_{1}>x, X_{2}>x, \ldots, X_{n}>x\right) \\
& =\prod_{i=1}^{n} P\left(X_{i}>x\right) \quad \text { per l'indipendenza } \\
& =\prod_{i=1}^{n}\left(1-F_{X_{i}}(x)\right) \\
& =\prod_{i=1}^{n} e^{-\lambda_{i} x} \\
& =e^{-x}{ }^{\mathrm{p}}{ }_{i=1} \lambda_{i}
\end{aligned}$$

---
### Intervalli di confidenza per la media della distribuzione esponenziale
Considerando un campione $X_{1}, X_{2}, \dots, X_{n}$ di variabili aleatorie esponenziali i.i.d. tutte con media $\theta$ incognita. È possibile dimostrare che lo stimatore di massima verosimiglianza per $\theta$ è costituito dalla media campionaria $\sum_{i=1}^{n}X_{i}/n$. Per ottenere gli intervalli di confidenza, ricordiamo che $\sum_{i=1}^{n}X_{i}$ ha distribuzione gamma con parametri $n$ e $1/\theta$. Deduciamo allora che
$$
\frac{2}{\theta} \sum_{i=1}^{n} X_{i} \sim \chi_{2 n}^{2}
$$
quindi per ogni $\alpha \in (0, 1)$,
$$
\begin{aligned}
1-\alpha & =P\left(\chi_{1-\frac{\alpha}{2}, 2 n}^{2}<\frac{2}{\theta} \sum_{i=1}^{n} X_{i}<\chi_{\frac{\alpha}{2}, 2 n}^{2}\right) \\
& =P\left(\frac{2 \sum_{i=1}^{n} X_{i}}{\chi_{\frac{\alpha}{2}, 2 n}^{2}}<\theta<\frac{2 \sum_{i=1}^{n} X_{i}}{\chi_{1-\frac{\alpha}{2}, 2 n}^{2}}\right)
\end{aligned}
$$
Dopo che il campione di dati viene osservato, e si trova che $X_{i}= x_{i}$, per $i=1, \dots, n$ si può affermare con un livello di confidenza di $1-\alpha$ che 
$$
\theta \in\left(\frac{2 \sum_{i=1}^{n} x_{i}}{\chi_{\frac{\alpha}{2}, 2 n}^{2}}, \frac{2 \sum_{i=1}^{n} x_{i}}{\chi_{1-\frac{\alpha}{2}, 2 n}^{2}}\right)
$$

>[!example]-
> Si pensa che gli oggetti prodotti da una azienda abbiano tempi di vita in ore che sono variabili aleatorie esponenziali indipendenti di media $\theta$. La loro densità è quindi
> $$
f(x)=\frac{1}{\theta} e^{-x / \theta} ; \quad x>0
> $$
> Se la somma dei tempi di vita di $10$ esemplati è pari a $1740$ ore, che intervallo di confidenza è pari al $95\%$ ne risulta , per la media della popolazione $\theta$?
> Scopriamo che:
> $$
\chi_{0.025,20}^{2} \approx 34.170, \quad \quad \chi_{0.975,20}^{2} \approx 9.591
> $$
> Possiamo quindi concludere che, con il $95\%$ di confidenza, $\theta$ appartiene all'intervallo 
> $$
\left(\frac{2 \times 1740}{34.170}, \frac{2 \times 1740}{9.591}\right) \approx(101.84, \quad 362.84)
> $$