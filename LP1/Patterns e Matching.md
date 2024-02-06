---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
alias: [PatMat]
---
## Pattern matching attraverso un esempio
Per scandire una lista dobbiamo controllare innanzitutto se è vuota:
```sml
- val L = nodo(1, nodo(2, vuota));
		val L = nodo(1, nodo(2, vuota)) : listaInt

- L = vuota;
		val it = false: bool
```

Se la lista non è vuota, potrebbe servirci il primo elemento, si estrae con il pattern matching:
```sml
- val nodo(p,_) = L; (*questa riga assegna a p il valore del primo elemento di L*)
	val p = 1 : int
```
La parte "`nodo(p, _)`" è chiamata pattern. Per ottenere il resto della lista faremo:
```sml
- val nodo(_,r) = L; (*questa riga assegna a r il resto della lista L*)
			val r = nodo(2, vuota) : listaInt
```

## Funzione che conta gli elementi della lista

Non essendo possibile l’utilizzo dell’iterazione, bisogna costruirla ricorsivamente

```sml
- fun conta x =
		if x = vuota then 0
			else
				let val nodo(_, r) = x in
					conta(r)+1
				end;

val conta = fn : listaInt -> int

- conta L;
val it = 2 : int
```

Il compilatore ha inferito il tipo della funzione:

1. x viene confrontato con “vuota”, che è di tipo listaInt, ciò significa che anche x è di tipo listaInt, di conseguenza l’input di `conta` è un listaInt.
2. Il then restituisce 0, che è un intero, quindi l’output di `conta` è un intero.

In più, il compilatore controlla che il resto della funzione sia compatibile con questi tipi

1. r corrisponde al secondo argomento del nodo, che è di tipo listaInt, è quindi corretto passarlo a conta che restituisce un intero
2. quindi anche l’else restituirà un intero, e tutto torna.

## Abbreviazione pattern

- Per estrarre tutti gli elementi di un costruttore in un colpo solo si può usare questo metodo:
    ```sml
    - val nodo(p, r) = L;
    	val p = 1 : int
    	val r = nodo (2, vuota) : listaInt
    ```    

Cioè dichiarare gli identificatori _p_ e _r_ nella stessa “chiamata”.
- È inoltre possibile definire una _**funzione per casi**_    

 ```sml
- fun conta (vuota) = 0
| conta(nodo(_, r)) = conta(r) + 1;
```


## Analogo dello Switch/Case del C

```sml
- case L of vuota => true
	| nodo(_, _)  => false;
val it = false: bool
```