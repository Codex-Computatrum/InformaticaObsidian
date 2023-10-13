---
author: Lorenzo Tecchia
tags:
  - definition
---
Il processo si estende su tre step:
- **Dividi**: Dividi la sequenza di $n$ elementi da ordinare in due sotto-sequenze di $\frac{n}{2}$ elementi ciascuna
- **Impera**: Vengono effettuate le chiamate ricorsive
- **Combina**: Crea una sequenza ordinate combinando le sotto-sequenze
	La ricorsione "tocca il fondo" quando si è raggiunto il caso base.

Nei casi dell'ordinamento come [[Merge sort]] viene "toccato il fondo" quando la sequenza ha lunghezza 1, dato che una sequenza di lunghezza 1 è già di per sé ordinata.