---
author: Simone Parente
tags:
  - prolog
---

>[!summary] Definizione
>Un'unificazione tra due espressioni $E_1$ e $E_2$ è una [[Sostituzione|sostituzione]] $\theta$ tale che
>$$E_1 \theta = E_2 \theta$$

^7f83e4
## Most General Unifier
L'unificatore costruito dall'algoritmo di prolog è detto **Most General Unifier (MGU)**, esso è così definito perché:
- non sostituisce una variabile con un termine se non necessario
- in pratica vincola il meno possibile il risultato di $E_1\theta$ lasciando libere quante più variabili possibili, quindi
	- esiste una sostituzione $\sigma$ tale che $(E_1 \theta) \sigma = E_1 \theta'$
## Esempio
![[Sostituzione#^32cd6b]]
![[Sostituzione#^33a9bf]]
![[Sostituzione#^2694eb]]
![[Sostituzione#^02a195]]
Tutte le sostituzioni precedenti sono **unificatori** delle espressioni $E_1$ ed $E_2$.
La più generale sarà $\theta_1$, dato che sostituisce solo le variabili necessarie per creare un match tra le due espressioni, lasciando libere le altre.