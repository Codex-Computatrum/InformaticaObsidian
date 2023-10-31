>[!info]
>La funzione `map` prende in input una funzione `f` e una lista, applica `f` a tutti gli elementi della lista e ritorna la lista risultante.

```SML
fun map f [] = []
 |  map f (X::Xs) = f X :: (map f Xs);
```

^definizione
