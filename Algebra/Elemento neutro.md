---
author: Simone Parente, Mario Penna
tags:
  - definition/property
---
Data la [[Struttura algebrica|struttura algebrica]] $(S, +, \star$);
$\epsilon \in S$  è un elemento neutro $\Leftrightarrow \forall a \in S: (a \star \epsilon = \epsilon \star a = a)$.
---
### Unicità dell'elemento neutro
L'elemento neutro è unico, possiamo dimostrarlo ragionando per assurdo:
Supponiamo di avere la [[Struttura algebrica|struttura algebrica]] precedente, avente due elementi neutri distinti per l'operazione $(\star)$, siano essi  $\epsilon$ e $\epsilon_1$, di conseguenza $\epsilon \star \epsilon_1 = \epsilon$ , allo stesso modo $\epsilon_1 \star \epsilon = \epsilon_1$ (o viceversa), di conseguenza $\epsilon = \epsilon_1$, cioè esiste un unico elemento neutro. ^elementoneutro
## Caso 1
$\star$ è commutativa, di conseguenza basta studiare un solo lato dell'operazione.
## Caso 2
$\star$ non è commutativa $\implies$ bisogna assicurarsi che esista un neutro sia a sinistra che a destra (e che i due coincidano). Ci troviamo davanti 3 ulteriori casi:
- Non esiste alcun elemento neutro
- Esiste più di un elemento neutro $\implies$ [[Elemento neutro#^elementoneutro|non esiste alcun elemento neutro per l'operazione]]. ^215353
- Esiste un elemento neutro a destra, devo dimostrare che lo sia anche a sinistra.
### Esempio
Supponiamo di avere la struttura $(P(S), /)$.
- Neutro a destra:
	$$\forall x \in P(S), x / \emptyset = x$$
	$$\epsilon \neq \emptyset \implies \epsilon / \epsilon = \emptyset$$
- Neutro a sinistra:
	$$\forall x \in P(S): \emptyset / x = \emptyset $$
Di conseguenza anche $x$ sarebbe un neutro, ciò implica che non ne esiste nessuno [[Elemento neutro#^215353|per questo motivo]].