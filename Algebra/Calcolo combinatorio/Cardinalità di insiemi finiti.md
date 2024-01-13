---
author: Simone Parente
tags:
  - algebra/combinatoria
---
## Cardinalità del prodotto cartesiano di due insiemi finiti
Siano $A$ e $B$ insiemi finiti, $|A \times B| = |A| \cdot |B|$
### Dimostrazione
$\forall x \in A, y \in B$ esistono $|B|$ elementi in $A \times B$ del tipo $(x,y)$, cioè che hanno $x$ come prima coordinata.
## Cardinalità dell'unione di due insiemi finiti
Siano $A$ e $B$ insiemi finiti, $|A \cup B| = |A| + |B| - |A \cap B|$, se i due insiemi non sono disgiunti.
### Dimostrazione
![[eulero-venn.png]]

Siano:
- $i=|A \setminus B|$
- $j=|A \cap B|$
- $k=|B \setminus A|$
$$|A|= i+j$$
$$|B|=k+j$$
$$\implies |A| + |B| - \textcolor{green}{|A \cap B|} = i+j+k+j\textcolor{green}{-j}=i+j+k=|A \cup B|$$

## Cardinalità di tre insiemi finiti non disgiunti
Siano $A,B, C$ tre insiemi finiti non disgiunti.
![[eulero-venn-2.png]]
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$
### Dimostrazione
Siano:
- $|A| = i+m+n+p$
- $|B| = j+l+n+p$
- $|C| = k+l+m+p$
Allora:
$$\textcolor{yellow}{|A|} + \textcolor{red}{|B|} + \textcolor{lightblue}{|C|} - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| =$$
$$=\textcolor{yellow}{(i+m+n+p)} + \textcolor{red}{(j+l+n+p)} + \textcolor{lightblue}{(k+l+m+p)}-(n+p)-(m+p)-(l+p)+p=$$
$$=i+j+n+k+l+m+p=|A \cup B \cup C|$$

