---
author: Simone Parente
tags:
  - SML
---
>[!info] 
>Sono funzioni che non hanno nome, possono essere specificate ovunque all'interno del codice e la loro sintassi è:
>`fn <argomento> => <espressione>`

## Esempio
Sia map definita come:
![[Map#^definizione]]
```SML
map (fn x => x*2) [1,2,3];
(*ritorna*)
> val it = [2, 4, 6]: int list;
```
