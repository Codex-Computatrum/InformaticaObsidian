---
author: Simone Parente
tags:
  - Java/JVM
---

>[!info] 
>Per garbage collection si intende il meccanismo per cui la JVM rilascia la memoria non più accessibile dal programma.
>NB: Le [[String|stringhe]] non sono mai elegibili per la garbage collection.

## Algoritmo *mark-and-sweep*
Si divide in due fasi:
1. Fase di mark: a partire dallo stack e dalla regione statica, esplora tutti gli oggetti accessibili e li marchia come tali
2. Fase di sweep: rilascia tutti i data object che non sono stati marcati come accessibili.
La fase di mark è in un certo senso analoga alla visita di un grafo, i nodi sono oggetti e gli archi sono riferimenti tra oggetti.
