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


