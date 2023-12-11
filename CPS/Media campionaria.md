---
tags:
  - definition
  - statistics
  - basics
  - sampling
author: Lorenzo Tecchia
---
>[!introduction]-
>Considerando una [[popolazione]] di elementi, a ciascuno dei quali è associata una grandezza numerica. La [[popolazione]] potrebbe ad esempio essere [[continua]] dagli individui adulti facenti parte di una qualche categoria di persone, e la grandezza numerica di interesse potrebbe essere il reddito annuale, la statura, l'età o altro. 
>Sia $X_{1}, X_{2}, \dots, X_{n}$ un campione di dati estratto da questa [[popolazione]]. È comune supporre che i valori numerici associati a ciascuno degli elementi del [[campione]], siano variabili aleatorie indipendenti e identicamente distribuite.
>Denotiamo con $\mu$ e $\sigma^{2}$ la loro [[Valore atteso|media]] e la loro [[varianza]], che prendono il nome di *media e varianza della [[popolazione]]*. 

Definiamo la ***media campionaria*** come $$\overline{X}:=\frac{X_{1}+X_{2}+\cdots+X_{n}}{n}$$ Si noti che $\bar{X}$ è una funzione delle variabili aleatorie $X_{1}, X_{2}, \dots, X_{n}$. In quanto tale è una ***statistica***, e in particola è a sua volta una [[variabile aleatoria]]. Ha senso quindi domandarsi quanto valgano il valore atteso della media campionaria e la sua varianza. 
È facile vedere che $$
\begin{aligned}
E[\overline{X}] & =E\left[\frac{X_{1}+X_{2}+\cdots+X_{n}}{n}\right] \\
& =\frac{E\left[X_{1}\right]+E\left[X_{2}\right]+\cdots+E\left[X_{n}\right]}{n} \\
& =\frac{n \mu}{n}=\mu
\end{aligned}$$ e, per la varianza, $$
\begin{aligned}
\operatorname{Var}(\overline{X}) & =\operatorname{Var}\left(\frac{X_{1}+X_{2}+\cdots+X_{n}}{n}\right) \\
& =\frac{\operatorname{Var}\left(X_{1}\right)+\operatorname{Var}\left(X_{2}\right)+\cdots+\operatorname{Var}\left(X_{n}\right)}{n^{2}} \quad \text { per l'indipendenza } \\
& =\frac{n \sigma^{2}}{n^{2}}=\frac{\sigma^{2}}{n}
\end{aligned}$$
>[!important]
> La media campionaria ha quindi lo stesso valore atteso della [[distribuzione]] da stimare, mentre la sua varianza risulta ridotta ad un fattore $n$. Da questo possiamo dedurre che $\overline{X}$ è centrata attorno a $\mu$, e la sua variabilità si riduce sempre di più con l'aumentare di $n

![|400](https://cdn.mathpix.com/cropped/2023_11_20_03d5e6ef9957032926fdg-111.jpg?height=500&width=752&top_left_y=187&top_left_x=320)

---
>[!improtant] # Distribuzione approssimata
> Sia $X_{1}, X_{2}, \dots, X_{n}$ un campione proveniente da una [[popolazione]] di media $\mu$ e varianza $\sigma^{2}$. Vediamo come il [[teorema del limite centrale]] ci permette di approssimare la distribuzione della media campionaria, $$\overline{X}:=\frac{1}{n} \sum_{i=1}^{n} X_{i}$$
> Siccome il prodotto di una variabile aleatoria [[Gaussiana|normale]] per una costante è ancora normale, ne segue che, quando $n$ è grande, $\overline{X}$ è approssimativamente gaussiana. Poiché inoltre la media campionaria ha un valore atteso $\mu$ e deviazione standard $\sigma / \sqrt{n}$, otteniamo che $$\frac{\overline{X}-\mu}{\sigma / \sqrt{n}} \dot{\sim} \mathcal{N}(0,1)$$ 

^a77156

---
