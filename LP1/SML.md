---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
---
# Sintassi generalizzata
```yaml
<Prog> ::= <Dichiarazione>

<Dichiarazione> ::= val <nome> = <Espressione>
                  | fun <nome> <Args> = <Espressione>
                  | datatype <nome> = ...

<Espressione> ::= let <Dichiarazione> in <Espressione> end            | <Espressione> <op_infisso> <Espressione>
                #Per esempio val risultato = 5 + 3;
	| "(" (<Espressione>";")* <Espressione> ")"
                #Espressione sequenziale, il valore è quello dell'ultima                   espressione, gli altri 
			    #valori vengono calcolati e "buttati"
    | if <Espressione> then <Espressione> else <Espressione> 
    #Deve essere booleana. Devono essere dello stesso tipo
	| local <Dichiarazione> in <Espressione> end             
                #local serve per dichiarare variabili o definizioni visibili solo all'interno del blocco		       
                #delimitato da local ... in ... end
    | exception <nome>
    | type <nome> = ...                                      
    #Serve per assegnare alias
```

## Esempio
```sml
- val a = (1;3); (*equivale a scrivere val a = 3; *)
	> val a = 3: int;
-val a= (1, 3); (*indica che a è uguale alla coppia (1,3) *)
	> val a = (1, 3): int * int;
-val a = ("a";4); (* come prima, val a = 4*)
	> val a = 4: int;
-val a = ("a", 4) (*a è uguale alla coppia ("a", 4) *)
	> val a = ("a", 4): string * int

print accetta una stringa in input, è una espressione di tipo () unit, è una sorta di tipo void, è il tipo delle espressioni che non restituiscono nulla
print("a=" ^ Int.toString(a))

val b =print("a=" ^ Int.toString(a); a+1) stampa il valore di a e assegna a b il valore a+1
```
## Caratteristiche del linguaggio
- Fortemente e staticamente tipato
	- Il controllo dei tipi è effettuato a Runtime
- Non necessita dichiarazioni dei tipi
	- Sfrutta la type inference (quindi spesso capisce automaticamente)
- Usa sia structural equivalence che name equivalence
- Permette di definire tipi ricorsivi (liste, alberi, ecc)
- Supporta il polimorfismo parametrico
- Supporta encapsulation nonostante non sia object oriented (non avendo la gerarchia dei tipi e conseguentemente l'ereditarietà)

## Implementazioni
È possibile usare ML in due modi:
1. Interagendo con l'interprete
	1. Inserendo definizioni ed espressioni una alla volta
	2. Oppure caricando programmi da file usando la keyword `use` seguito da "nome del file" nella shell.
2. Compilando un programma in codice oggetto direttamente eseguibile
	1. per esempio usando il compilatore `mlton` seguito da "nome del file.sml" che creerà un eseguibile con stesso nome di quello .sml ma senza estensione

## Tipi primitivi
`0, 1, ~1, 2, ~2, ..., 0xff, ~0x32, ...`
`int, ~ si usa al posto del segno -`

```sml
0w44, 0w15, ... , 0wxff, ...
(*word, unsigned integers, che hanno come prefisso 0w*)
```

```sml
3.14, 2.0, 0.1EA
(*------------------------------*)
+, -, *, /, <, ...
```
`real e alcuni operatori utilizzabili su di essi`

```sml
#"a", #"\n", #"\163", ...
(*------------------------------*)
ord, chr, =, <, ...
```
`char e alcuni operatori utilizzabili su questi ultimi`

```sml
"abc", "123"
(*------------------------------*)
^ (* è l'operatore di concatenazione*)
```
`string`

```sml
true, false
(*------------------------------*)
not, andalso, orelse, =
```
`bool e alcuni operatori`

>[!important] 
> - L'operatore per il confronto di uguaglianza è `=` e non `==`.
> - Non esistono conversioni automatiche tra tipi numerici
> - Esistono basis library per ogni primitivo (`Int`, `Word`, `Real`) con funzioni per conversioni parsing e altre utility
> - `Real` non supporta l'uguaglianza, bisogna utilizzare `Real.==`
> - Esistono valori che risultano da operazioni non definite, saranno denominati *NaN* (Not a Number), che sono uguali a nessun altro numero, nemmeno sé stessi

## Interazioni con l'interprete
```sml
- 3;
	val it = 3 : int
(*- 0 w7 mod 0 w4 ;
	val it = 0 wx3 : word*)
- " Hello " ^ " world " ;
	val it = " Hello world " : string
```
`it` s riferisce all'espressione data, calcola il valore seguito dal tipo[^1]

## Dichiarazioni e scoping in ML
### Funzioni
Ci sono diversi modi per definire e invocare funzioni:
```sml
- fun quadr x = x * x;  (* fun nome  risultato = espressione *)
	val quadr = fn : int -> int
- quadr(3);
		val it = 9 : int
- quadr 3;
		val it = 9 : int
```
`In questo caso le parentesi sono opzionali`

```sml
- fun quadr (x : int ) : int = x * x
	val quadr = fn : int -> int
```
`È possibile indicare esplicitamente input e output di una funzione. In mancanza di specificazione, si attiva la type inference`

#### Funzione ricorsiva
```sml
- fun fatt x = if x = 0 then 1 else x * fatt(x-1)
	val fatt = fn : int -> int

- fatt(3)
val it = 6 : int

- fatt 3
val it = 6 : int
```
`anche qui le parentesi sono opzionali`

In ML il costrutto `if-then-else` è una espressione, in Java è uno statement (non ha valore)
>[!note] 
> `if-then-else` è simile a `?:`in Java
> ```sml
> //condizione ? valoreSeVero : valoreSeFalso
int x = 10;
int y = (x > 5) ? 20 : 30;
System.out.println(y); //stamperà 20
> ```

### Dichiarazioni di identificatori
>[!note]- 
> Con `val` si aggiunge un nuovo identificatore all'ambiente e gli si associa un valore.
>```sml
> - val x = 2+2;
>	val x = 4 : int;
> - x+2
> val it : 6 : int 
> ```

>[!note]- 
> Grammatica delle dichiarazioni viste fin ora
> ```
> declaration> ::=
> val < id name > = < expression > |
> fun < function name > < argument >* = < expression >
> ```

---

# ***Gli esempi del Parente***

```sml
(*Definizione di un tipo di lista di interi*)
datatype listaInt = vuota | nodo of int * listaInt;

(*Una lista di interi composta dai nodi 1 --> 2*)
val lista1 = nodo(1, nodo(2, vuota))
```
`Requisiti per la funzione size`


##### Funzione size che prende in input una lista di interi e ritorna il numero di nodi
```sml
fun size s: int ? 
	if s = vuota then 0
		else let val nodo(_, n) = s in size(n) + 1
end;
```

***fine intermezzo comico***

---

### Scoping
#### Lo scoping è statico infatti:
```sml
- let val x=2 in 3*x end;
	val it = 6 : int

- x
error: unbound variable or constructor: x

- let val x=2 in 
		let val x=3 in  (*la precedente x è mascherata da questa*)
			3*x
		 end;
	end;
	 val it = 9: int
```

```
local
	<dichiarazioni>
in
	<dichiarazione> (le dichirazioni sopra valgono solo qui)
```

#### Ambiente non locale delle funzioni
```
local
	<dichiarazioni>
in
	<espressione> (*le dichiarazioni valgono solo qui*)
end
```
`Simile a "let" ma dopo "in" c'è una dichiarazione invece di un espressione`

---

## Tipi strutturati
- Le $n-$*uple* sono definibili mettendo i valori tra parentesi tonde
- Il prodotto cartesiano è indicato con `*`
>[!check]- Si estrae l'n-esimo elemento da una $n-$*upla* con l'operatore prefisso `#i` dove `i` è un intero.
> ```sml
> - (1+1, "A");
>		val it = (2, "A") : int * string
>
> - val x = (1, "A", 3.5);
>		val x = () : int * string * real
>
> - #1(x)
>		val it = 1 int
> - #2(x)
>		val it = "A" : string
> - #3(x)
>		val it = 3.5 : real
> ```

### Record
>[!check]- Insiemi di espressioni i tipo <nome>=<valore>, notare come viene rappresentato il tipo.
>  ```sml
> - val r = {nome="Mario",nato=1998};
>		val r={nato=1998,nome="Mario"} : {nato: int, nome: string}
> ```
> Il valore associato al nome *N* si estrae con `#N`
> ```sml
> - #nome(r)
>		val it = "Mario" : string
>
> - #nato(r)
>			val it = 1998 : int
> ```
> `L'ordine delle coppie non è importante`

### Dichiarazioni di tipo
>[!check]- ML permette di definire nuovi tipi (similmente ai `typedef` in C) 
> ```sml
> - type coord = real * real
>		type coord = real * real
>
> (*È preferibile specificare i tipi dichiarati dall'utente*)
> - val x = (3.0, 4.0)
>		val x = (3.0, 4.0) : real * real (*Non vogliamo questo*)
>
> -val x:coord = (3.0, 4.0);
>		val x = (3.0, 4.0) : coord       (*Ma questo*)
>```
> I due tipi visti sopra sono *structurally equivalent* tra loro, è quindi possibile passare una espressione di tipo `coord` a un parametro di tipo `real * real` e viceversa.

### Datatypes e costruttori
>[!check]- Con *datatype* (simile a una enum in C) si può fare più che dare un nome a un tipo ML, si possono costruire per creare data objects:
> ```sml
> - datatype color = red | green | blue;
>	datatype color = blue | green | red
> //red, green e blue sono costruttori che definiscono i possibili valori del tipo color
> ```

In C le enum sono solo ed esclusivamente degli `int, i datatypes di ML definiscono dei tipi nuovi, che non hanno corrispondenza con gli int.

>[!check]- Ogni tipo definito con datatype è incompatibile con tutti gli altri tipi (name equivalence) 
> ```sml
> val c : color = 10;
>	Error: pattern and expression in val dec don’t agree
> - c = 0; (* c `e uguale a 0? *)
> Error : operator and operand don ’ t agree
> ```

### Costruttori con argomenti
Per definire un lista concatenata di interi si può utilizzare una definizione ricorsiva, dato che essa è:
- Una lista vuota (caso base)
- Seguita da un nodo che contiene un intero e una lista di interi (caso induttivo)
Ci serviranno quindi 2 costruttori: uno per la lista vuota e uno per i nodi 
```sml
(*Costruttore della lista*)
- datatype listaInt = vuota | nodo of int * listaInt;
		datatype listaInt = nodo of Int * listaInt | vuota 
```

```sml
(*Costruttore del nodo*)
- val L = nodo(1, nodo(2, vuota));
		val L = nodo (1, nodo(2, vuota)) : listaInt
```

>[!important]
> Per definire un albero binario con nodi etichettati da interi possiamo utilizzare una definizione ricorsiva, essa sarà:
> - un albero vuoto, oppure
> - un nodo che contiene un intero e due alberi dello stesso tipo (sotto-albero destro e sotto-albero sinistro)
> ```sml
> datatype albero = vuoto | nodoAlb of int * albero * albero
>
> (*Costruiamo ora un albero con radice 1, figlio sinistro 2 (che è una foglia) e nessun figlio destro*)
> nodoAlb(1, nodoAlb (2, vuoto, vuoto), vuoto)
> ```



[^1]:  L'espressioni con il segno "-" sono da intendere istruzioni scritte dall'utente. Quelle presenti all'interno dei blocchi di codice, senza alcun segno "-" davanti s'intendono risposte del compilatore.