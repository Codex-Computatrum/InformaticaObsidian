---
author: Simone Parente
tags:
  - Java
---
>[!attention] 
>Per *firma* di un metodo si intende il suo nome, l'elenco dei tipi e l'elenco dei nomi dei suoi parametri formali

Consideriamo una invocazione `x.f(y1,...,yn)`
Una firma `f(T1 a,..., Tn z)` è *candidata* per la chiamata in questione se:
- Si trova nella classe *dichiarata* di `x`.
- È visibile dal punto in cui si trova la chiamata (quindi è public o al più protected se non si trova nella classe dell'object `x`)
- È compatibile con la chiamata, cioè il tipo **dichiarato** di `y1,...,yn` è assegnabile rispettivamente al tipo `T1,...,Tn`
## Confrontare le firme candidate
Date due firme con stesso nome e numero di argomenti:
`f(T1,...,Tn)` e `f(U1,...,Un)`
La prima firma è **più specifica** (a prescindere dai parametri passati alla chiamata) della seconda se:
- T1 è [[Assegnabilità#^b1919b|assegnabile]] a U1
- ...
- Tn è [[Assegnabilità#^b1919b|assegnabile]] a Un