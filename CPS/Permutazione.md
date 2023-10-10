---
author: Lorenzo Tecchia
tags: [combinatorics, basics, definition]
---
Ogni $n-$disposizione semplice è detta essere una **permutazione** (semplice) degli $n$ elementi di $S$. ^574974
## Permutazioni semplici
>[!important] Corollario 1 al [[Disposizione#^98a51f|Teorema 1]]
> l numero $P_{n}$ di tutte le permutazioni semplici di $S$ è ottenuto ponendo $k = n$ nella formula per il calcolo di $D_{n,k}$ e, quindi:$$P_{n}= D_{n,n}= \frac{n!}{(n-n)!}= \frac{n!}{0!} = n!$$ dove il simbolo con il punto esclamativo è detto [[fattoriale]].

>[!note] 
> Gli anagrammi delle parole aventi lettere tutte distinte tra loro forniscono un’applicazione del concetto di permutazione.

Sia $S = {e_1,e_2,\dots,e_s}$ e sia, inoltre $n = k_1 +k_2 +\dots+k_s$. Una n-selezione di $S$ avente $k_1$ elementi uguali al primo elemento di $S$, $k_2$ elementi uguali al secondo elemento di $S$ e così via fino a $k_s$ è detta essere una $(k1, k2,\dots, ks)-$permutazione con ripetizione di $S$.

## Permutazioni con ripetizioni
>[!important] Corollario 2 al [[Disposizione#^98a51f|Teorema 1]]
> Il numero $P_{n;k_{1},k_{2},\dots,k_{s}}^{r} (\text{o anche} \;\;_{k_{1},k_{2},\dots,k_{s}} P_{n}^{r})$ di tutte le $(k_{1},k_{2},\dots,k_{s})-$***permutazioni con ripetizioni*** di $S$ è dato da:$$P_{n;k_{1},k_{2},\dots,k_{s}}^{r} = \frac{n!}{k_{1}!k_{2}!\dots k_{s}!}$$

Si osservi che nel caso s = n e $k_{1} = k_{2} = \dots = k_{n} = 1$ si ottengono le permutazioni semplici. Risulta, inoltre:$$P_{n;1,1,\dots,1}^{r} = \frac{n!}{1!1!\dots 1!} = P_{n}$$