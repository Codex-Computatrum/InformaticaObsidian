---
author: Simone Parente
tags: [SML]
---
## Datatype
```SML
datatype albero = vuoto | nodo of int * albero * albero;
```
## Dato un albero sommare tutti i nodi non foglia
```SML
fun sumNodes vuoto = 0
  | sumNodes (nodo(_, vuoto, vuoto)) = 0
  | sumNodes (nodo(value, dx, sx)) = value + sumNodes sx + sumNodes dx;
```
## Dato un albero sommare tutte le foglie
```SML
fun sumLeaves vuoto = 0
  | sumLeaves (nodo(value, vuoto, vuoto))= value
  | sumLeaves (nodo(_, sx, dx)) = sumLeaves sx + sumLeaves dx;
```
