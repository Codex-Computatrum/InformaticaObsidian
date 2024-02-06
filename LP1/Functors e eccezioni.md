---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
alias: [FuncEcc]
---

## Functors

>[!note] 
>I **funtori** in SML sono funzioni che prendono un modulo come input e restituiscono un nuovo modulo come output, permettendo di creare moduli parametrici per favorire l'astrazione e la riusabilità del codice.

```sml
(*Supponiamo di avere due [strutture](<https://www.notion.so/Polimorfismo-parametrico-Encapsulation-Structures-Functors-Exceptions-ec2a5220f7254f87862bf92dd375c848?pvs=21>) RGB e CMYK, entrambe implementano la signature COLOR*)
functor Image (X: COLOR)=
	struct
	(*Qui X si può usare come un tipo avente le operazioni definite da COLOR*)
end

structure Image_RGB = Image(RGB);
structure Image_CMYK = Image(CMYK);
```

## Eccezioni e integrazione con type checking
La gestione delle exception è integrata col type checking.
```sml
fun pop(x::s) = (x,s);
> WARN: Pattern matching is not exhaustive.
pop [];
> Uncaught SML exception: Match
```

1. La type inference capisce che l’input di pop è `list`.
2. Il datatype lista ha due costruttori `::` e `[]`.
3. La definizione per casi di pop ha un caso solo per `::`.
4. Da cui il warning.
5. Il compilatore inserisce automaticamente una eccezione `Match` nei casi mancanti.

### Dichiarazione e generazione eccezioni

È possibile definire nuove eccezioni con questa sintassi:
```sml
exception NomeException;
```

Per chiamarle si usa la keyword `raise` (come in PostGreSQL, equivalente a `throw` in Java). L’exception lanciata di default è `Match`.

È possibile catturare e gestire le exception tramite `handle` e una funzione anonima.

```sml
pop x
	handle NomeException =>
		(print "messaggio di errore";
		 raise NomeException);
```

$$ \large{\text{Handle}} $$

Soffermandoci un attimo sulla keyword `handle`, essa può essere messa dopo qualunque espressione che può generare exceptions, è anche possibile gestire diverse exception con lo “stesso” `handle`.

Esistono 2 modi per usarlo in ML per passare il type checking senza errori:

1. Fare qualcosa (es. stampare un messaggio e rilanciare l’exception)
2. Sistemare l’errore restituendo un valore dello stesso tipo dell’espressione che ha sollevato l’exception.

### Eccezioni con parametri

Si possono aggiungere dettagli agli errori verificatisi specificando dei parametri per le eccezioni

```sml
exception SyntaxError of string (*of string è il parametro*)
(*È possibile lanciarla tramite*)
raise SyntaxError "Messaggio da visualizzare"

(*E il parametro viene letto col pattern matching*)
handle SyntaxError x => ... (*Qui è possibile usare x*)
```

## Esempio
![[Paradigma-funzionale.pdf#page=201]]
