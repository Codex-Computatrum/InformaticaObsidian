---
author: Lorenzo Tecchia, Simone Parente
tags: [SML]
aliases: [diffImpFun]
---
# Imperativo
`env`: nomi $\rightarrow$ indirizzi
`mem:`: indirizzi $\rightarrow$ valori

`x` è un generico indirizzo

```C
int a = 1;
a = 2;
```

**equivale a fare** 

```
env(a) := x;
mem(x) = 1;
mem(x) := 2
```

# Funzionale
`env`: nomi $\rightarrow$ valori

```sml
val a = 1;
val a = 2;
a = 3
```

**equivale a fare**

```
env(a) := 1;
env(a) := 2;
la terza istruzione è un espressione di controllo equivalente a "a ==" in C
```

#### Esempio

```sml
val pi = 3.14;
fun area r = r * r * pi;
val pi = 0.0; (*non modifica il valore ma maschera il vecchio valore di pi da questo
 momento in poi*)
area 2.0; (*la funzione area ha catturato l'ambiente nel momento in cui è stata 
dichiarata, quindi vale ancora 12*)
```

### Trafiletto mem-env
| Descrizione           | c/c++/ | mem&env               |
| --------------------- | ------ | --------------------- |
| operando a sx         | $x=?$    | env(x)                |
| operando a dx         | $?=y$    | mem(env(y))           |
| puntatore a sx        | $*x=?$   | mem(env(x))           |
| puntatore a dx        | $?=*y$   | mem(mem(env(y)))      |
| doppio puntatore a sx | $**x=?$  | mem(mem(env(x)))      |
| doppio puntatire a dc | $?=**y$  | mem(mem(mem(env(y)))) |
| array a sx            | $x[z]=?$ | env(x) + z            |
| array a dx            | $?=y[z]$ | mem(env(y)) + z       |
| indirizzo-di a sx     | $\&x=?$   | not allowed           |
| indirizzo-di a dx     | $?=\&y$   | env(y)                |
