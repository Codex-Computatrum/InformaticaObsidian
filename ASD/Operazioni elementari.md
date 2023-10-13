---
author: Lorenzo Tecchia
tags: [definition, dataStructure]
---
Nelle [[Struttura dati|strutture dati]]  in generale esistono un numero di operazioni in comune, queste possono essere:
- $Search(S, d): x | NULL$ 
	- Cerca nella struttura $S$ un elemento che possiede il dato $d$.
	- Se la trova restituisce il puntatore $x$ a quell'elemento, altrimenti restituisce $NULL$
- $Insert(S,d): S'$
	- Inserisce nella struttura $S$ un nuovo elemento con dato $d$
	- Restituisce una nuova struttura $S'$, ovvero con l'elemento inserito
- $Delete(S,d):S'$
	- Elimina dalla struttura S l'elemento con dato $d$
	- Restituisce una nuova struttura $S'$, con il dato $d$ eliminato
- $IsEmpty(S): bool$
	- Restituisce $true$ se la struttura $S$ è vuota, $false$ altrimenti

>[!important] 
>Ovviamente ogni struttura può avere delle proprie operazioni e proprietà specifiche per la struttura dati in sé

