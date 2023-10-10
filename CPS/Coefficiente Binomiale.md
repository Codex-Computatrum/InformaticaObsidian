---
author: Lorenzo Tecchia
tags: [combinatorics, definition, basics]
---
Siano $n$ e $k$ due numeri naturali tali che $k \leq n$. Il simbolo $n \choose k$ definito come:$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$ è detto coefficiente binomiale su $k$. Il simbolo con il punto esclamativo è detto [[Fattoriale|fattoriale]].

>[!note] Osservazione 1
> Non bisogna confondere $n \choose k$ con $n \over k$ 

>[!note] Osservazione 2
> Il coefficiente binomiale, $n \choose k$, fornisce il numero di sottoinsiemi di $k$ elementi di un insieme finito costituito da $n$ elementi. 

Si noti che, disponendo opportunamente i coefficienti binomiali $n$al crescere di $n$, è possibile $k$ ricostruire il [[Triangolo di Pascal]] (o di Tartaglia)

>[!note] Osservazione 3
> Ogni elemento nel triangolo di Pascal verifica la proprietà:$$\binom{n+1}{k}=\binom{n}{k}+\binom{n}{k-1}$$

>[!note] Osservazione 4
> Ogni riga del triangolo di Pascal contiene i coefficienti dello sviluppo della potenza (corrispondente) del binomio:$$(a+b)^{n} = \sum_{k=0}^{n} \binom{n}{k}a^{k}b^{n-k}$$