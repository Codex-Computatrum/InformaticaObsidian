---
tags: [aleatoryVariable, definition, probability, to-do]
author: Lorenzo Tecchia
---
>[!todo]
> Inserire grafico

Una [[variabile aleatoria]] [[ContinuaVA|continua]] la cui funzione di densità di probabilità è data da: $$f(x) = \begin{cases} \lambda e^{-\lambda x} &se \ x \geq 0\\
0 & se \ x < 0
\end{cases}$$
per un opportuno valore della costante $\lambda > 0$, si dice esponenziale con parametro (*o densità*) $\lambda$.

La [[funzione di distribuzione]] di una tale variabile aleatoria è data da:$$\begin{align}
\mathcal{F}(x) &= \mathbb{P}(X \leq x) \\
&= \int_{0}^{x}\lambda e^{-\lambda y}dy \\
&= 1 - e^{- \lambda x}, \;\;\;\;\; x \geq 0
\end{align}$$
Nella pratica, la distribuzione esponenziale può rappresentare il tempo di attesa prima che si verifichi un certo evento causale. Come per esempio:
>[!example]
> Il tempo che trascorrerà (a partire da questo momento), fino al verificarsi, di un terremoto; o allo scoppiare di un nuovo conflitto, o al giungere della prossima telefonata di qualcuno che ha sbagliato numero.

Sono tutte variabili aleatorie che in pratica tendono ad avere distribuzioni esponenziali.

La proprietà centrale della distribuzione esponenziale è la sua assenza di *memoria*. Con questa espressione, riferita ad una variabile aleatoria positiva $X$ si s intende che:$$\mathbb{P}(X > s + t|X > t) =\mathbb{P}(X> s)\;\;\;\;\;\;\forall s,t \geq 0$$ ^31ded8
>[!example]
> Si immagini che $X$ rappresenti il tempo di vita di un certo oggetto prima di guastarsi. Sapendo che tale oggetto è già in funzione da un tempo $t$ e non si è ancora rotto, qual è la probabilità che esso continui a funzionare per almeno un ulteriore intervallo di tempo $s$? Chiaramente la probabilità richiesta è quella espressa dal membro sinistro dell'equazione [[Esponenziale#^31ded8|soprastante]]. Infatti dire che l'oggetto non si è ancora guastato al tempo $t$ equivale a dire che il tempo in cui avverrà la rottura $(X)$ è superiore a $t$, mentre affermare che che l'oggetto funzionerà per un ulteriore tempo $s$ a partire dal tempo $t$, significa che il tempo $X$ dovrà essere maggiore di $t+s$. In questo senso, l'equazione [[Esponenziale#^31ded8|soprastante]] afferma che la distribuzione del tempo di vita rimanente dell'oggetto considerato, è la medesima sia nel caso in cui esso stia funzionando da un tempo $t$, sia nel caso in cui esso sia nuovo, o, in altri termini, se l'equazione è soddisfatta, non vi è alcun bisogno di tenere presente l'età dell'oggetto, perché fino a che esso funziona, si comporta esattamente come fosse "nuovo di zecca".

La condizione di assenza di memoria è equivalente a chiedere che: $$\frac{\mathbb{P}(X > s+t,X>t)}{\mathbb{P}(X > t)} = \mathbb{P}(X > s)$$
e quindi anche che:$$\mathbb{P}(X > s+t)=\mathbb{P}(X > s)\mathbb{P}(X > t)$$
Quest'ultima formulazione è facilmente verificabile se $X$ è esponenziale, visto che per $x > 0, \mathbb{P}(X> x)= e^{-\lambda x}$ e ovviamente $e^{- \lambda(s+t)}= e^{-\lambda s}e^{-\lambda t}$. Abbiamo quindi provato che le variabili aleatorie esponenziali sono prive di memoria.(*È possibile dimostrare che sono le uniche con tale proprietà*)