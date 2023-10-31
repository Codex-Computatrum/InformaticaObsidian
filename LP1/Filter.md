---
author: Simone Parente
tags:
  - SML
---

>[!info] 
>La funzione filter prende in input una funzione booleana `f` e una lista `L`, restituisce una lista di elementi per cui `f` è vera.
```SML
fun filter f [] = []
 |  filter f (X::Xs) = if f X then X::(filter f Xs)
					   else filter f Xs
```
