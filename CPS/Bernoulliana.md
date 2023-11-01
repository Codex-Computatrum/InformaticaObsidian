---
tags: [aleatoryVariable, probability, definition, to-do]
---
>[!todo] Inserire grafico

Supponendo che venga realizzata una prova, o un esperimento, il cui esito può essere solo un "successo" o un "fallimento". Se definiamo la [[variabile aleatoria]] $X$ in modo che sia $X=1$ nel primo caso e $X = 0$ nel secondo, la funzione di massa di probabilità di $X$ è data da $$\begin{align}
\mathbb{P}(X=0)&=1-p \\
\mathbb{P}(X = 1)&= p
\end{align}$$
dove con $p$ abbiamo indicato la probabilità che l'esperimento registri un "successo". Ovviamente dovrà essere $0 \leq p \leq 1$

>[!definition]
> Una variabile aleatoria $X$ si dice di *Bernoulli* o bernoulliana se la sua funzione di massa di probabilità è del tipo delle equazioni soprastanti per una scelta opportuna del parametro $p$

In altri termini, una variabile aleatoria è bernoulliana se può assumere se può assumere solo i valori $0$ e $1$. Il suo valore atteso è dato da $$E[X]:= 1 \mathbb{P}(X = 1)+ 0 \mathbb{P}(X = 0)= p$$ ed è quindi pari alla probabilità che la variabile aleatoria assuma il valore di $1$