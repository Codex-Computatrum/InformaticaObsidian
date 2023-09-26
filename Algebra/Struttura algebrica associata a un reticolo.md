---
author: Simone Parente
tags:
  - definition/structure
  - definition/property
---

Sia $(S, \leq)$ un [[Insieme Ordinato|insieme ordinato]], in particolare un [[Reticolo|reticolo]].
![[Reticolo#^703fff]]
Definiamo quindi due operazioni reticolari:
1. $\inf\{x,y\} = x \land y$, $\land$ sta per **intersezione reticolare**
2. $\sup\{x,y\} = x \lor y$, $\lor$ sta per **unione reticolare**
La [[Struttura algebrica associata a un reticolo|struttura algebrica associata]] al reticolo $(S,\leq)$ è quindi $(S, \lor, \land)$, questo perché se un [[Insieme Ordinato|insieme ordinato]] ammette [[Minimo|minimo]], allora [[Estremo inferiore|inf]]=[[Minimo|min]] e se ammetta [[Massimo|massimo]], [[Estremo superiore|sup]]=[[Massimo|max]].

### Esempi di operazioni reticolari

```start-multi-column
ID: esempi_strutture_reticolari
Number of Columns: 2
Largest Column: standard
```

Per l'insieme $(P(S), \subseteq)$, 
$x \land y = x \cup y$,
$x \lor y =x \cup y$.

--- column-end ---

In $(\mathbb{N}, |)$,
$x \land y = MCD(x,y)$,
$x \lor y = mcm(x,y)$

--- end-multi-column
![[Proprietà della struttura algebrica associata a un reticolo|Proprietà]]