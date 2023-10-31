---
author: Simone Parente
---

Il RdA di una funzione contiene (a differenza del blocco anonimo):

- Puntatore di catena dinamica \[link a rda precedente o sottostante (immagina fisicamente una pila)].
- Puntatore di catena statica (opzionale, serve per scoping statico).
- Indirizzo di ritorno.
- Indirizzo del risultato.
- Parametri.
- Ambiente locale (variabili locali e spazio per risultati intermedi).

L’ambiente non locale di una funzione viene ricavato tramite il puntatore di catena dinamica (scoping dinamico) o statica (scoping statico).
![[stack.gif]]