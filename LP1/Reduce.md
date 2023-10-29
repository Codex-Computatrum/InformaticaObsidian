---
author: Simone Parente
tags:
  - SML
  - todo/example
---

>[!info] 
>La funzione `reduce` serve per calcolare gli *aggregati* di una lista: min, max, somma, prodotto, media.
>Prende in input **una funzione a due argomenti `f`**, *un valore finale* e **una lista**.
>Effettua il calcolo $reduce \; f \; e [x_1,x_2,\ldots, x_n]= f(x_1,f(x_2,\ldots,f(x_n,e)\ldots))$

```SML
fun reduce f e [] = e
 |  reduce f e (X::Xs) = f (X, reduce f e y)
```