---
author: Simone Parente
tags:
  - notReviewed
  - algebra/combinatoria
---
Siano $A \text{ e } B$ insiemi, l'insieme $Map(A,B)$,  è l'insieme delle [[Algebra/Funzione|funzioni]] $f$ di dominio $A$ e codominio $B$, in altre parole
$$Map(A,B)=\{f:A \rightarrow B\}$$
### Cardinalità
$$|Map(A,B)|= |B|^{|A|}$$
#### Dimostrazione
Poniamo $n=|A|$ e $A=\{a_1,a_2,\ldots,a_n\}$, $m=|B|$ e $B=\{b_1,b_2,\ldots,b_m\}$, per ogni $a_i$, dove $i=\{1,2,\ldots,n\}$, abbiamo $m$ possibili immagini, in particolare, sia $j=\{1,2,\ldots,m\}$:
$$a_1  \in A\mapsto b_j \in B$$
$$a_2 \in A \mapsto b_j \in B$$
$$\vdots$$
$$a_n \mapsto b_j \in B$$
di conseguenza avremo:
$$|Map(A,B)|=\underset{\text{n volte}}{m \cdot m \cdot \ldots \cdot m}$$
$$|Map(A,B)|=m^n$$
### Osservazioni
- Se $A=\emptyset \implies |Map(A,B)|=|B|^{|A|}=|B|^0=1$
- Se $B=A=\emptyset \implies |Map(A,B)|=0^0=1=\{id_\emptyset\}$
	cioè $Map(A,B)$ è composto dalla sola funzione $f:\emptyset \mapsto \emptyset$^osserv2
- Se $A \neq \emptyset \land B = \emptyset \implies |Map(A,B)| = 0^{|A|} = 0$
	vale a dire che non esiste nessuna funzione da $A$ a $B$, perché nessun elemento di $A$ può avere immagine. ^osserv3