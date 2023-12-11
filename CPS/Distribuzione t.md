---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - distribution
---
>[!important] # Definizione 
> Se $Z$ e $C_{n}$ sono variabili aleatorie indipendenti, la prima normale standard e la seconda [[chi-quadro]] con $n$ gradi di libertà, allora la variabile aleatoria $T_{n}$, definita come $$T_{n}:=\frac{Z}{\sqrt{C_{n} / n}}$$ si dice avere *distribuzione* $t$ con $n$ gradi di libertà, cosa che si denota sinteticamente con $$T_{n} \sim t_{n}$$
> Tale variabile aleatoria viene anche detta $t$ *di Student* con $n$ gradi di libertà.

La densità delle distribuzioni $t$, proprio come quella normale standard, è simmetrica rispetto all'asse di ascissa $0$. In realtà è possibile mostrare che al crescere di $n$, la densità di $t_{n}$ converge a quella della normale standard. Per capirne il motivo, ricordiamo che $C_{n} \sim \chi^{2}_{n}$ può essere espressa come somma dei quadrata di $n$ gaussiane standard indipendenti, ovvero $$\frac{C_{n}}{n}=\frac{Z_{1}^{2}+\cdots+Z_{n}^{2}}{n}$$ dove $Z_{1}, \dots, Z_{n}$ sono appunto $\mathcal{N}(0, 1)$ e indipendenti.
La legge dei grandi numeri applicata a questa espressione, ci dice però che per $n$ grande, $C_{n}/n$ sarà, con probabilità prossima al $100\%$, molto vicino a $[Z_{i}^{2}]= 1$. Quindi per $n$ grande, $T_{n} := Z / \sqrt{C_{n}/n}$ avrà circa la stessa distribuzione di $Z$.