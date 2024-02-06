---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
alias: [EncSig]
---
>[!note] 
> Le **signatures** sono il costrutto di ML per definire le **interfacce** (di Java), definiscono tipi e funzioni senza specificare la loro implementazione.

 - Esempio di implementazione di uno stack
 
```sml
signature STACK =
sig
	type 'a stack
	val empty: 'a stack
	val push: ('a * 'a stack) -> 'a stack
	val pop: 'a stack -> ('a * 'a stack)
end;
```

- Dichiara un tipo parametrico `‘a stack` senza specificare come è definito
- Una funzione `empty` per inizializzare uno stack vuoto
- Una funzione `push` per inserire un elemento nello stack
- Una funzione `pop` per estrarre la testa dello stack

Per assegnare un tipo a una espressione si usa `:`.

## Structures

>[!note] 
>Le **structures** servono per definire **tipi di dato astratti**.


- Esempio di implementazione di uno **stack** tramite una lista

L’espressione Stack :> STACK indica che:
- Stack deve implementare gli identificatori dichiarati in stack
- I tipi di dato dichiarati in STACK possono essere utilizzati **solo** con le operazioni dichiarate in stack.
- Le funzioni definite nella structure non sono accessibili da fuori.

```sml
structure Stack :> STACK =
struct
	type 'a stack = 'a list;
	val empty = [];
	fun push(x,s) = x :: s;
	fun pop(x::s) = (x, s);
end;
```

- Esempio di implementazione di un Gruppo
```sml
signature Gruppo =
sig
	type dominio
	val oper: (dominio x dominio) -> dominio
	val inverso: dominio -> dominio
	val neutro: dominio
	val daInt: int -> dominio
end;
```
    
```sml
structure Interi1 =
struct
	type dominio = int;
	fun oper (a,b) = a+b;
	fun inverso: a = (tilde)a;
	val neutro = 0;
	fun daInt n = n;
end;
(* Scrivendo *) structure Interi2 :> Gruppo = Interi1 (*Dichiariamo una struttura che implementa Gruppo, precisamente si chiama *opaque signature matching* e **nasconde tutto ciò che non è dichiarato nella signature*)
```

## Incapsulamento
>[!note]
> Anche se il tipo stack è implementato come `list`, esso non potrà essere usato come `list`. La struttura Stack non mette a disposizione la funzione `lenght` sul tipo stack e l’implementazione di `List.lenght` è nascosta.