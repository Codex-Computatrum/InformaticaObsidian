---
author: Lorenzo Tecchia
tags: definition
---
La ***macchina di Turing*** è un modello computazionale astratto. In particola una sestupla:$$M = <Q, \Sigma,\Gamma,\delta, q_{accept}, q_{reject}>$$
Dove:
1. $Q$ è l'insieme degli stati
2. $\Sigma$ è l'alfabeto di input dove $\sqcup$ non è presente  
3. $\Gamma$ è l'insieme dei simboli di nastro, incluso $\sqcup$ 
4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L,R\}$ è la funzione di transizione
5. $q_{0}\in Q$ è lo stato di partenza
6. $q_{accept} \in Q$ è lo stato di accettazione
7. $q_{reject} \in Q$ è lo stato di rigetto dove $q_{accept} \neq q_{reject}$

La ***macchina di Turing*** inoltre, è dotata di un nastro infinito e il modello comprende una testina che può leggere e scrivere sul nastro infinito reagendo a ciò che è scritto sulla testina in base alla funzione di transizione $\delta$. La testina può muoversi, in base sempre alla funzione di transizione a destra o sinistra sequenzialmente sul nastro, di quante caselle preveda la funzione di transizione. 

L'***importanza del modello astratto di Turing*** è la capacità di simulare qualsiasi calcolatore o algoritmo di calcolare mai inventabile. Sempre grazie alla non finitezza del nastro attraverso la quale la macchina opera.

La ***limitatezza del modello astratto di Turing*** è l'accesso ai dati. Data la sequenzialità del nastro l'accesso ai dati è molto lento.