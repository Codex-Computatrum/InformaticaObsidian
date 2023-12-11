---
author: Simone Parente
tags:
  - algebra/grafi
  - notReviewed
---
Un multigrafo semplice è una terna ordinata $(V,L,f)$ dove $f:L\to P_2(V)$.
$e \mapsto \{a,b\}$
$m \mapsto \{b,c\}$
$n \mapsto \{b,c\}$
![[multigrafosemplice.jpg]]

## Osservazioni
- $\forall V, \; A=\{\rho \in Rel(V)\;|\;\ \rho$ è [[Antiriflessiva|antiriflessiva]] e [[Simmetrica|simmetrica]]$\}$, definiamo l'applicazione [[Biettività|biettiva]] $L \in P(P_2(V)) \mapsto \rho_L \in A$, la cui funzione inversa è $p \in A \mapsto \{a,b\}|a \rho b\} \in P(P_2(V))$.
- Due vertici si dicono <span style="color:#00ff00">adiacenti</span> se e solo se sono estremi dello stesso lato, ovvero se $a \,\rho_L \, b \iff \{a,b\} \in L.$
	Si considerino $L=\{\{x,y\} \in P(V) \, | \, x \, \rho \, y\} \subseteq P_2(V)$, posso definire un grafo come una coppia $(V,\rho)=G$.
- Due lati si dicono <span style="color:#00ff00">incidenti</span> se hanno un vertice in comune.
- Un vertice e un lato si dicono <span style="color:#00ff00">incidenti</span> se il vertice è un estremo del lato.
- Il <span style="color:#00ff00">grado</span> di un vertice è il numero dei lati di cui è estremo, ovvero $\forall x \in V, \, deg(x)=|\{l \in L \, | \, x \text{ è estremo di }l\}|$. ^grado
- Un vertice è <span style="color:#00ff00">pari</span> se il suo grado è pari e <span style="color:#00ff00">dispari</span> se il suo grado è dispari.