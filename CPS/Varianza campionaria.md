---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - sampling
  - distribution/normal
---
Sia $X_{1}, X_{2}, \dots, X_{n}$ un campione aleatorio, proveniente da una distribuzione di media $\mu$ e varianza $\sigma^{2}$. Sia $\bar{X}$ la sua [[media campionaria]]. Introduciamo quindi una seconda statistica.
>[!definition]
> La statistica $S^{2}$, definita da $$S^{2}:=\frac{1}{n-1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$$ si dice *varianza campionaria*. La sua radice quadrata, $S = \sqrt{S^{2}}$ prende invece il nome di *deviazione standard campionaria*

Volendo calcolare $E[S^{2}]$, possiamo sfruttare tale condizione: per qualsiasi $n-$upla di numeri $x_{1}, x_{2}, \dots, x_{n}$, $$
\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}=\sum_{i=1}^{n} x_{i}^{2}-n \dot{\bar{x}}^{2}$$ dove $\bar{x} = \sum\limits_{i=1}^{n}x_{i}/n$. Applicato a $X_{1}, X_{2}, \dots, X_{n}$ questo enunciato implica che $$
S^{2}=\frac{1}{n-1}\left(\sum_{i=1}^{n} X_{i}^{2}-n \bar{X}^{2}\right)$$ ovvero che $$
(n-1) S^{2}=\sum_{i=1}^{n} X_{i}^{2}-n \bar{X}^{2}$$
Prendendo il valore atteso di entrambi i membri di quest'ultima equazione, e ricordando che il momento secondo di una qualsiasi variabile aleatoria $W$ si può ottenere come $E[W^{2}] = \operatorname{Var}(W) + E[W]^{2}$, deduciamo che $$
\begin{aligned}
(n-1) E\left[S^{2}\right] & =E\left[\sum_{i=1}^{n} X_{i}^{2}\right]-E\left[n \bar{X}^{2}\right] \\
& =n E\left[X_{1}^{2}\right]-n E\left[\bar{X}^{2}\right] \\
& =n \operatorname{Var}\left(X_{1}\right)+n E\left[X_{1}\right]^{2}-n \operatorname{Var}(\bar{X})-n E[\bar{X}]^{2} \\
& =n \sigma^{2}+n \mu^{2}-n \frac{\sigma^{2}}{n}-n \mu^{2} \\
& =(n-1) \sigma^{2}
\end{aligned}$$ da cui $$
E\left[S^{2}\right]=\sigma^{2}$$
>[!success] Conclusioni
> Il valore atteso della varianza campionaria coincide con la varianza della [[popolazione]].