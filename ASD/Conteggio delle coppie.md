---
author: Lorenzo Tecchia
tags: [example, algorithm]
---
#### Algoritmo 1
Input: $n \in \mathbb{N}$ 
output: $\{(i,j) \in \mathbb{N} \times \mathbb{N} | i \leq j \leq n\}$ 
![[Pasted image 20230822170136.png]]
#### Tempo di esecuzione
$t_1$: dell'assegnazione
$t_2$: di un ciclo for (non del suo corpo, ma di tutto il resto)
$t_3$: stessa cosa
$t_4$: dell'$if$  (anche qui del corpo ma dell'istruzione in se)
$t_5$: di un incremento
$t_6$: della $return$ 

Il secondo $for$ viene eseguito $n+1$ volte, quindi (includo il corpo) impiega $(n+1)[t_{3}+t_{4}+t_{5}]$. Stesso discorso per il primo $for$, quindi alla fine impiega: $$n^2c_{1}+nc_2+c_3$$ L'algoritmo quindi impiega un tempo quadratico

----
#### Algoritmo 2
![[Pasted image 20230822170840.png]]
 