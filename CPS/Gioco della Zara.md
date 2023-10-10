---
author: Lorenzo Tecchia
tags: [example, combinatorics, probability]
---
La **zara** è un gioco d’azzardo in uso nel Medioevo. Si gioca con tre dadi (in questo problema consideriamo due dadi per semplicità): a turno ogni giocatore chiama un numero da $3$ a $18$, quindi getta i dadi. Vince chi per primo ottiene il punteggio pari al numero chiamato. Vogliamo determinare la [[probabilità]] di uscita di ogni possibile numero ottenuto sommando la coppia di numeri (in questo caso da $2$ a $12$).
![[Pasted image 20231001184543.png]]
Lo [[Spazio degli esiti|spazio campione]] (o degli esiti ) è $\Omega= {(1, 1), (1, 2), \dots, (6, 6)},|\Omega| = 36$. Notiamo che ogni [[esito]] dello spazio $\Omega$ ha la stessa probabilità di realizzarsi. Dunque, possiamo dire che per ogni elemento $x \in \Omega$, $\mathbb{P}(x) = \frac{1}{36}$ , dunque $\Omega$ è uno spazio [[Esiti Equiprobabili|equiprobabile]]. 

Consideriamo adesso questo insieme $S_z = {2, 3, 4, 5, ..., 12}$ detto ***spettro della trasformazione*** (in questo caso è una trasformazione che ad ogni coppia associa la sua somma $z \in \mathbb{R}$, chiamiamo questa trasformazione $f$). Analizzando la tabella di destra possiamo facilmente risalire alla probabilità di ogni evento.
![[Pasted image 20231001184920.png|350]]
Dunque la probabilità di ogni numero (da $2$ a $12$) è:
![[Pasted image 20231001185149.png|150]]
Quindi abbiamo avuto un riscontro della [[Esiti Equiprobabili#^17d378|Proprietà di equiprobabilità]] degli spazi equiprobabili. Abbiamo risolto il problema utilizzando anche il [[PF del calcolo combinatorio|principio di enumerazione]].