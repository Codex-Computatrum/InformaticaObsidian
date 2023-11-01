---
author: Lorenzo Tecchia
tags: [aleatoryVariable, probability, definition, to-do]
---
>[!todo] Inserire grafico

Supponiamo di realizzare $n$ ripetizioni indipendenti di un esperimento, ciascuna delle quali può concludersi in un "successo" con probabilità $p$, o in un fallimento con probabilità $1-p$. Se $X$ denota il numero totale di successi, $X$ si dice variabile aleatoria *binomiale* di parametri $(n,p)$
La funzione di massa di probabilità per una variabile aleatoria binomiale di parametri $(n,p)$ è data da $$\mathbb{P}(X = i) = \binom{n}{i}p^{i}(1-p)^{n-i}, \;\;\;\;\; i = 0,1,\dots$$
dove ricordiamo il coefficiente binomiale:![[Coefficiente Binomiale]]
>[!important]
> La somma delle probabilità di tutti i valori possibili di una variabile aleatoria binomiale, è pari ad $1$ per la formula delle potenze del binomio:$$\sum_{i}\mathbb{P}(X = i) = \sum_{i=0}^{n}\binom{n}{i}p^{i}(1-p)^{n-i} = [p + (1-p)]^{n} = 1$$

