---
author: Lorenzo Tecchia
tags: [definition, probability]
---
Gli **assiomi** permettono di dedurre un gran numero di ***proprietà delle [[probabilità]] degli eventi***. Ad esempio, possiamo notare che $E$ e $E^{c}$ sono eventi disgiunti, e quindi usando il [[Assioma Primo|primo assioma]] e il [[Assioma Secondo|secondo assioma]]:$$1=\mathbb{P}(\Omega) = \mathbb{P}(E \cup E^{c})= \mathbb{P}(E) + \mathbb{P}(E^{c})$$

## Proposizione 1
Per tanto per ogni [[evento]] $E \subset \Omega$ vale:$$\mathbb{P}(E^{c}) = 1 - \mathbb{P}(E)$$
La probabilità che un evento qualsiasi non si verifichi è pari a $1$ meno la probabilità che si verifichi.

Ad esempio, se sappiamo che la probabilità di ottenere testa lanciando una certa moneta è $\frac{3}{8}$, allora evidentemente la probabilità di ottenere croce dalla stessa moneta è $\frac{5}{8}$.
## Proposizione 2
Tale proposizione fornisce la probabilità dell’**unione** di due eventi in termini della loro probabilità singole e di quella dell’**intersezione** (si noti che questa rappresenta una estensione del [[Assioma Terzo|terzo assioma]] che funziona anche con eventi non mutuamente esclusivi).

Se $E$ e $F$ sono due eventi qualsiasi, allora:$$\mathbb{P}(E \cup F) = \mathbb{P}(E)+\mathbb{P}(F) - \mathbb{P}(E \cap F)$$

>[!note] 
> Ci riferiamo al ***Principio di Inclusione-Esclusione(IN-EX)***


