---
author: Lorenzo Tecchia, Simone Parente
tags: [SML, list]
---
# Liste

I costruttori delle liste sono `nil` e `::`

```sml
nil                     (*Lista vuota*)
1 :: 2 :: 3 :: :: nil   (*Lista che contiene 1, 2, 3 *)  (*viene interpretata da **destra verso sinistra** 
														(l'interprete crea la lista vuota, aggiunge il 3, poi il 2 e poi l'1)
																(*Formato equivalente basato su parentesi quadre *)
[]                       (*Lista vuota*)
[1, 2, 3]

(*sono davvero equivalenti*)
- [] = nil;
val it = true : bool

-1::2::3::nil = [1,2,3];
val it = true : bool
```

## Operatori sulle liste

```sml
(*Data una lista L*)
- val L = [1, 2, 3];
val L = [1, 2, 3]: int list

(*null restituisce true se la lista è vuota.*)
- null L;
val it = false: bool;

(*lenght restituisce la lunghezza della lista.*)
- length L;
val it = 3: int;
```

```sml
(*hd (head) restituisce il primo elemento della lista.*)
- hd L;
val it = 1: int;

(*tl (tail) restituiscel’ultimo elemento della lista*)
-	tl L;
val it = [2, 3]: int list

(*@ applicato a due liste restituisce una concatenazione di queste ultime*)
- val M = [1,2] @ [3,4];
 val M = [1, 2, 3, 4]: int list;
```

Altre funzioni si trovano nella [struttura List](https://smlfamily.github.io/Basis/list.html)

- `List.nth(L, i)` restituisce l’n-esimo elemento di L (partendo da 0).
- `List.Last(L)` restituisce l’ultimo elemento di L.

Una struttura di ML è molto simile a un modulo o package