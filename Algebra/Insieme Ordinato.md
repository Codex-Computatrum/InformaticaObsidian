---
author: Simone Parente, Mario Penna
tags:
  - definition
  - basics
  - example
---
Un insieme si definisce ordinato se al suo interno è definita una [[Relazioni d'ordine|relazione d'ordine]].
### Esempio
#### Relazione d'ordine usuale in $\mathbb{Z (\leq)}$
Sia $(\mathbb{Z}, \rho)$ un insieme e sia $\rho : \forall a,b \in \mathbb{Z} (a \rho b) \iff (b-a) \in \mathbb{N}$.
- $2<3 \iff 3-2=1 \in \mathbb{N}$
##### Dimostrazione
Per dimostrare che $\rho$ è una [[Relazioni d'ordine|relazione d'ordine]] dobbiamo dimostrare che è:
1. Riflessiva:
$$\forall a \in \mathbb{Z} (a\rho a) \iff (a-a) \in \mathbb{N}$$
	Questo è vero perché $0 \in \mathbb{N}$
2. Antisimmetrica
$$\forall x,y \in \mathbb{Z} (x \rho y \land y \rho x \implies x=y) \iff (b-a) \in \mathbb{N} \land (a-b) \in \mathbb{N}$$
$a- b = -(b-a) \in \mathbb{N}$ e di conseguenza $b-a = a \implies a=b \implies \rho \text{ è antisimmetrica}$
3. Transitiva
$$\forall a,b,c \in \mathbb{Z} ((a \rho b) \land (b \rho c) \implies a \rho c)$$
$$b-a \in \mathbb{N} \land c-b \in \mathbb{N}$$
$$(\cancel{b}-a) + (c - \cancel{b}) = c-a \in \mathbb{N}$$
