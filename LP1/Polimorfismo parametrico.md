---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
---
>[!note]
> L’equivalente dei template di C++ e Java.

Il costruttore `::` può essere applicato a qualsiasi tipo: (`nil` è la lista vuota!!!)

```sml
1 :: nil (*oppure*) "abc" :: nil
	> val it = ["abc"]: string list;
- lenght;
	> val it = fn : 'a list -> int (* È ciò che c'è scritto sulle slide *)
	> val it = fn: ∀ 'a . 'a list → int;
```

La funzione `lenght` prende in input una lista di elementi il cui tipo `‘a` non è specificato:

- **accetta liste di qualsiasi contenuto**
- **non ha bisogno di sapere il tipo**, deve solo contare i nodi.

Un’altra funzione parametrica è `map`:

```sml
- map;
	> val it = fn : ('a -> 'b) -> 'a list -> 'b list (*Slides*)
	> val it = fn: ∀ 'a . 'a list → int;             (*SOSML*)
```

## Come definire tipi parametrici
```sml
(* generalizzazione di liste *)
-datatype 'a lista = vuota 
										 | nodo of ('a * 'a lista);

	> datatype ‘a lista = nodo of ‘a * ‘a lista | vuota;    (*Slides*)
	> datatype 'a lista = {
	    con vuota = vuota/1: ∀ 'a . 'a lista;
	    con nodo = nodo/1: ∀ 'a . 'a * 'a lista → 'a lista;
	  };                                                    (*SOSML*)
(* ------------------------------------------------------------------------------*)
(*alberi binari con etichette parametriche *)
- datatype 'a bt = emptybt 
	| btnode of ( 'a * 'a bt * 'a bt );
> datatype ’a bt = btnode of 'a * 'a bt * 'a bt | emptybt    (*Slides*)
> datatype 'a bt = {
    con emptybt = emptybt: ∀ 'a . 'a bt;
    con btnode = btnode: ∀ 'a . 'a * 'a bt * 'a bt → 'a bt;
  };                                                         (*SOSML*)
```

Per le funzioni non dobbiamo fare nulla di speciale (se il compilatore non ha bisogno di aiuto per stabilire il tipo, ci pensa la **type inference**)

```sml
- fun conta(vuota) = 0
	|  conta (nodo(x,l)) = conta (l) + 1;
	> val conta = fn : 'a lista -> int (* Slides *)
	> val conta = fn: ∀ 'a . 'a lista → int; (*SOSML*)

```

```sml
datatype 'a lista = vuota | nodo of ('a * 'a lista);

fun conta vuota = 0
 |  conta (nodo (_, l)) = conta(l) +1;

fun somma vuota = 0
 |  somma (nodo(x,l)) = somma(l)+x;

fun contiene vuota z = false
 |  contiene (nodo(x,l)) z = (x=z) orelse contiene l z;

due apici significa che la funzione accetta un tipo qualsiasi che supporti l'uguaglianza

```

Per dichiarare un tipo si usa `'`, per dichiarare un tipo che supporti anche l’uguaglianza si utilizza `''`(i tipi reali non supportano l’uguaglianza come vedremo nel prossimo esempio).

```sml
- fun diag (x,y) = x=y;
	> val diag = fn : ''a * ''a -> bool

-diag (1.0, 1.0);
	>	Elaboration failed: Type clash. Functions of type "''a * ''a → bool" cannot take an argument of type "real * real": Type "real" does not admit equality.
```