---
author: Simone Parente
tags:
  - algebra/grafi/alberi
  - notReviewed
---
Sia $G=(V,L,f)$ un [[Multigrafo semplice|multigrafo]] finito. 
Un <span style="color:#00ff00">sottoalbero massimale</span> di $G$ è un [[sottografi|sottografo]] di $G$ con insieme di vertici $V$ che è un [[Foreste e alberi#^8fcaab|albero]] ed è unico $\iff G$ è [[Grafo connesso|connesso]].
Si dimostra facilmente che se elimino un lato da un [[circuito]] i $v \in V$ rimangono tutti connessi.
#### Osservazione
- Sia $G=(V,L,f)$ un [[Multigrafo semplice|multigrafo]] [[Grafo connesso|connesso]], $l_0 \in L$ tale che $l_0$ è parte di un [[Circuito|circuito]] in $G$. Allora il [[Sottografi|sottografo]] di $G$, $G'=(V,L',f')$, con $L'=L \setminus \{l_0\}$ è ancora connesso.
Dimostrazione:
	siano $a,b \in G$, se $a,b$ sono connessi da un circuito $\implies$ esistono almeno due [[cammino|cammini]] diversi $n \neq m$ da $a$ a $b$.
	Se $l_0$ è in $n \implies a \text{ e } b$ sono connessi da $m$ in $G$, o viceversa, se $l_0$ è in $m \implies a \text{ e } b$ sono connessi da $n$. 