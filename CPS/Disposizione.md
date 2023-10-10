---
author: Lorenzo Tecchia
tags: [definition, basics, combinatorics]
---
Se nel contesto specifico l’ordine di scelta di un elemento dall’insieme $S$ è influente allora ogni selezione di elementi di $S$ è detta essere una _dis_-posizione.  ^ad766f

## Disposizioni semplici
Sia $k\leq n$. Se nel contesto specifico l’ordine di scelta di un elemento di $S$ è influente allora ogni $k-$selezione di $S$ costituita da elementi tutti distinti tra loro è detta essere una $k-$***disposizione semplice*** di $S$.

>[!important] Teorema 1
> Il numero $D_{n,k}$ di tutte le $k-$disposizioni senza ripetizione (***semplici***) di $S$ è dato da:$$D_{n,k} = n \cdot (n-1) \cdot \dots \cdot (n-k+1)= \frac{n!}{(n-k)!}$$
> dove il simbolo con il punto esclamativo corrisponde al simbolo di [[fattoriale]].

^98a51f

## Disposizioni con ripetizioni
Se nel contesto specifico l’ordine di scelta di un elemento di $S$ è influente allora ogni $k-$selezione (con $k$ qualsiasi) di $S$ è detta essere una $k-$***disposizione con ripetizione*** di $S$.

>[!important] Teorema 2
> Il numero $D_{n,k}^{(r)}$ di tutte le $k-$disposizioni con ripetizione di $S$ è dato da:$$D_{n,k}^{(r)} = n^{k}$$