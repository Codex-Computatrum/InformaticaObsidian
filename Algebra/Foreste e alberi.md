---
author: Simone Parente
tags:
  - notReviewed
  - algebra/grafi/alberi
---
Un grafo è una <span style="color:#00ff00">foresta</span> $\iff$ non esistono [[Circuito|circuiti]].
Un <span style="color:#00ff00">albero</span> è sempre una <span style="color:#00ff00">foresta</span>.
Una <span style="color:#00ff00">foresta connessa</span> è un <span style="color:#00ff00">albero</span>.
### Teorema
- Un grafo finito è una <span style="color:#00ff00">foresta</span> $\iff \forall (a,b) \in G,\text{ con a }\neq b$, esiste <span style="color:#00ff00"><strong>al più</strong></span> un cammino.
- Un grafo finito è un <span style="color:#00ff00">albero</span>  $\iff \forall (a,b) \in G, \text{ con } a \neq b,$esiste <span style="color:#00ff00"> <strong> esattamente </strong> </span> un cammino.
#### Dimostrazione
Siano $a,b \in V$, dove $V$ è l'insieme dei vertici delle foreste $G$, supponiamo esistano dei cammini diversi da $a$ a $b:$ $l=(l_1,l_2,\ldots,l_n) \text{ e  } m=(m_1,m_2,\ldots,m_p) \implies \exists v \in V$ tale che da $v$ in poi i due cammini non coincidono.
- se $v=b$ allora il lato $m_p$ è un lato che va da $b$ a $b$, ciò implica che il grafo è ciclico $\implies$ contraddizione.
	![[foreste_grafociclico1.jpg]]
- se $v \neq b, \exists u \in V$, tale che da $u$ in poi i due cammini $l,m$ non coincidono, prendendo in considerazione da $v$ ad $u$ e da $u$ a $v$, questi formano un [[Circuito|circuito]] $\implies$ contraddizione.
	![[foreste_circuito.jpg]]
