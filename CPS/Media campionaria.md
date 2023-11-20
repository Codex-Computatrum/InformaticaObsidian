---
tags: [definition, probability]
author: Lorenzo Tecchia
---
Supponendo di avere un insieme $x_{1}, x_{2}, \dots, x_{n}$ di $n$ dati (o come anche si dice, un campione di *ampiezza* o *numerosità* pari a $n$). La ***media campionaria*** è la media aritmetica di questi valori.
>[!definition]
> Si dice **media campionaria** e si denota con $\bar{x}$, la quantità:$$\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n}x_{i}$$

Il calcolo manuale di questa grandezza può essere notevolmente semplificato se si note che, prese comunque due costanti $a$ e $b$, se si considera il nuovo insieme di dati $$y_{i}= ax_{i}+b, \qquad i= 1, \dots, n$$
allora la media campionaria di $y_{1}, y_{2},\dots, y_{n}$ è legata a quella dei dati iniziali della stessa relazione lineare:$$\bar{y}=\frac{1}{n} \sum_{i=1}^n\left(a x_i+b\right)=\frac{1}{n} \sum_{i=1}^n a x_i+\frac{1}{n} \sum_{i=1}^n b=a \bar{x}+b$$

>[!example]
> Si vuole calcolare la media campionaria di questo insieme di dati:$$284 \quad 280 \quad 277\quad 282 \quad 278 \quad 285 \quad 281 \quad 283 \quad 278 \quad 277$$
> Invece che applicare direttamente la definizione, si può usare la considerazione fatta sopra, costruendo ad esempio il nuovo insieme di dati $y_{i}= x_{i}-$, che é più maneggevole da trattare:$$4 \quad 0 \quad -3\quad 2 \quad -1 \quad 5 \quad 1 \quad 3 \quad -2 \quad -3$$
> La media campionaria dei dati trasformati si calcola molto facilmente:$$\bar{y}=\frac{4+0-3+2-1+5+1+3-2-3}{10}=\frac{6}{10}$$
> Ne segue che:$$\bar{x} = \bar{y} + 280 = 280.6$$
