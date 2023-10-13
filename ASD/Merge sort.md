---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

## [[Algoritmo]]
![[Pasted image 20230828160123.png]]
Tramite il concetto di [[dividi et impera]] le due chiamate ricorsive, dividono la sequenza a metà.

Il caso base è $p<r$,dove $p$ è l'indice di inizio del vettore, $r$ è quello della fine. Se $p > r$ allora il vettore non è più divisibile.
![[Pasted image 20230828160338.png]]
$i \leq q-p$ controlla se l'array $L$ è finito. Infatti la dimensione di $L$ è proprio $q-p$. 
- Nel caso in cui $i>q-p$, l'$if$ sarà falso, dunque entrerà sempre nell'$else$; ovvero inserisce i rimanenti elementi d $R$.
- Altrimenti controlla lo stesso per il sotto-vettore $R$ con $j \leq r-q$
#### Analisi
![[appuntiIngenito (dragged) 1.pdf]]

---
## Implementazione in C
```C
```