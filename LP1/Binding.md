---
author: Simone Parente
tags:
  - Java
---
In Java il binding dei metodi (cioè il collegamento di ogni chiamata a un metodo vero e proprio) avviene in due fasi:
1. Early binding, dove il compilatore risolve l'overloading, scegliendo la firma più appropriata alla chiamata.
2. Late binding, dove la JVM risolve l'overriding (non necessario per i metodi [[Private]], [[Static]], [[Final]]).


>[!info] Binding dinamico
>È il meccanismo tramite cui la JVM decide quale metodo invocare per una data chiamata a metodo.
>Si tratta di stabilire il legame di locazione di un nome di metodo nel contesto di una invocazione.

L'esistenza del binding dinamico è una diretta conseguenza del polimorfismo e dell'overriding.