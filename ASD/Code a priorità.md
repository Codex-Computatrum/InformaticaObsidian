---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure
  - to-do/implementation
---
Una [[coda]] di priorità è una [[struttura dati]] che serve a mantenere un [[Fundamentals#set|insieme]] $S$ di elementi, ciascuno con un valore associato detto **chiave**.

Una coda di ***max-priorità*** supporta le seguenti operazioni:
- $Insert(S,x)$: inserisce l'elemento $x$ nell'insieme $S$, che equivale all'operazione:$S = S \;\cup\; \{x\}$
- $MAXIMUM(S)$: restituisce l'elemento di $S$ con la chiave più grande
- $EXTRACT-MAX(S)$: rimuove e restituisce l'elemento di $S$ con la chiave più grande
- $INCREASE-KEY(S,x,k)$ aumenta il valore della chiave dell'elemento $x$ al nuovo valore $k$, che si suppone sia almeno grande quanto il valore corrente della chiave dell'elemento $x$