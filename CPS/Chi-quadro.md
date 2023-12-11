---
tags:
  - definition
  - statistics
  - example
author: Lorenzo Tecchia
---
Se $Z_{1}, Z_{2}, \dots, Z_{n}$, sono variabili normali standard e indipendenti, allora la somma dei loro quadrati, $$X:=Z_{1}^{2}+Z_{2}^{2}+\cdots+Z_{n}^{2}$$
è una [[variabile aleatoria]] che prende il nome di ***chi-quadro a $n$ gradi di libertà***. La notazione che useremo per indicare questo fatto è la seguente: $$X \sim \chi_{n}^{2}$$ La [[distribuzione]] ***chi-quadro*** è riproducibile, nel senso che se $X_1$ e $X_{2}$ sono due chi-quadro indipendenti, con $n_{1}$ e $n_{2}$ gradi di libertà rispettivamente, allora la loro somma $X_{1}+X_{2}$ è un chi-quadro con $n_{1}+n_{2}$ gradi di libertà. 

Per dimostrare questo fatto non è necessario ricorrere alle funzioni generatrici, poiché dalla definizione è evidente che $X_{1}+X_{2}$ è la somma dei quadrati di $n_{1}+n_{2}$ normali standard indipendenti, e quindi è una chi-quadro con altrettanti gradi di libertà.

Per la distribuzione [[Gaussiana|normale]] standard, se $X$ è una chi-quadro con $n$ gradi di libertà e $\alpha$ è un reale compreso tra $0$ e $1$, definisce la quantità $\chi^{2}_{\alpha, n}$, tramite la seguente equazione: $$\mathbb{P}\left(X \geq \chi_{\alpha, n}^{2}\right)=\alpha$$

>[!example]-
> Si determini $\mathbb{P}(X \leq 30)$ quando $X$ è una variabile aleatoria chi-quadro con $26$ gradi di libertà.
> Usando il programma riferito sul libro $$\mathbb{P}(X \leq 30) \approx 0.7325 \quad \square$$