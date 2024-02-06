---
author: Lorenzo Tecchia, Simone Parente
tags:
  - SML
---
Si utilizzano esclusivamente espressioni e funzioni, eventualmente ricorsive.

Non esistono assegnamenti né variabili che cambiano valore

Gli environment (la [[funzione env]]) mappano gli identificatori direttamente al loro valore (che è immutabile), invece che a una locazione di memoria (il cui contenuto sarebbe immutabile)

Come conseguenza della non esistenza di assegnazioni abbiamo che:
- l'iterazione è sostituita dalla ricorsione
- Le modifiche sono fatte sull'environment e non sulla memoria
- Possono essere creati identificatori con lo stesso nome tramite chiamate ricorsive.
- Possono esser creati nuovi identificatori con lo stesso nome che mascherano le versioni precedenti (simile allo scoping statico)

## Tipi di costrutti funzionali in Java
- Lambda expressions (funzioni anonime)
- Collezioni funzionali (`Stream`)
- Type inference per metodi parametrici
- Type inference per variabili locali (keyword `var`)
- Pattern matching su `instanceof`
- Pattern matching su `switch`
- Classi immutabili (**Record**)

## Tipi di costrutti funzionali in C++
- Lambda expressions
- Type inference (keyword `auto`)