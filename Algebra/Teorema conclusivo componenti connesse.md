---
author: Simone Parente
tags:
  - algebra/grafi/teorema
  - notReviewed
---
Sia $G=(V,L,f)$ un [[Multigrafo semplice|multigrafo]] finito con esattamente $k$ componenti [[Componenti connesse|connesse]], allora:
1. $G \text{ connesso } \implies |L| \geq |V|-1$; ^1
2. $|L| \geq |V| - k$ ^2
3. $|L|=|V| - k \iff G$ è una [[Foreste e alberi|foresta]]. ^3
4. Sono equivalenti:^4
	1. $G$ è un [[Foreste e alberi|albero]]^41
	2. $G$ è [[Grafo connesso|connesso]] e $|V|=|L|+1$^42
	3. $G$ è una [[Foreste e alberi|foresta]] e $|V|=|L|+1$ ^43
## Dimostrazioni
### Dimostrazione 1.
$G$ connesso $\implies G$ ha un [[Sottoalberi massimali|sottoalbero massimale]] $(V,L')$, con $L' \subseteq L \implies |V| = |L'| +1 \implies |L'|=|V|-1$ e visto che $|L'| \leq |L| \implies |L| \geq |V|-1$, vale a dire che $|V|=|L|+1 \iff |L|=|L'| \iff L=L'$.
### Dimostrazione 2.
Siano $(V_1,L_1,f_1),(V_2,L_2,f_2), \ldots, (V_k,L_k,f_k)$ le [[Componenti connesse|componenti connesse]] di $G$, $\forall i \in \{1,\ldots,k\}, |L_i| \geq |V_i|-1$ per [[Teorema conclusivo componenti connesse#^1|1.]],
$$|L|=\sum^{k}_{i=1}|L_i|$$
$$|V|=\sum^{k}_{i=1}|V_i|$$
$$\sum^{k}_{i=1}-1=-k$$
$$\implies |L| \geq |V|-k$$
### Dimostrazione 3.
Se $\forall i \in \{1,2,\ldots,k\}, |L_i|=|V_i|-1 \implies |L| = |V|-k$ per [[Teorema conclusivo componenti connesse#^2|2.]], inoltre $G_i=(V_i,L_i)$ è un [[Foreste e alberi|albero]] $\implies G$ è una [[Foreste e alberi|foresta]].
### Dimostrazione 4.
- [[Teorema conclusivo componenti connesse#^41|4.1]] $\implies$ [[Teorema conclusivo componenti connesse#^42|4.2]]: per [[Teorema conclusivo componenti connesse#^1|1.]], [[Teorema conclusivo componenti connesse#^42|4.2]] $\implies$ [[Teorema conclusivo componenti connesse#^41|4.1]] per dimostrazione precedente.
- [[Teorema conclusivo componenti connesse#^41|4.1]] $\implies$ [[Teorema conclusivo componenti connesse#^43|4.3]]: se $G$ è un [[Foreste e alberi|albero]], di conseguenza $G$ è anche una [[Foreste e alberi|foresta]], inoltre per [[Teorema conclusivo componenti connesse#^43|4.3]] $|V|=|L|+k$, dove $k$ sono le [[componenti connesse]] in $G$. Essendo $G$ un albero, $k=1$
- [[Teorema conclusivo componenti connesse#^43|4.3]] $\implies$ [[Teorema conclusivo componenti connesse#^41|4.1]]: per [[Teorema conclusivo componenti connesse#^43|4.3]] $G$ è una [[Foreste e alberi|foresta]] con $k=1$ [[componenti connesse]], dunque è un [[Foreste e alberi|albero]].