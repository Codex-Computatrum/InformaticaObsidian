Sia $(\mathbb{Z},+,\cdot)$ un anello commutativo unitario e l'equazione $ax \equiv_m c \in \mathbb{Z}$:
- Se $a$ è [[Elementi invertibili (o simmetrizzabili)|invertibile]], la soluzione è $x=a^{-1}-c$.
- Se $a$ è [[Elementi cancellabili|cancellabile]], l'ordine dell'insieme delle soluzioni è 1.
- Se $a$ è un [[Divisori dello zero|divisore dello zero]] abbiamo 2 casi:
	- esiste più di una soluzione
	- non esiste nessuna soluzione
#### Casi Particolari
	![[Congruenza#^492ca3]]
	![[Congruenza#^9bc247]]
---
#### Spiegazione
Siano $m \in \mathbb{N}^*, a \in A, c \in C : A=[a]_m, C=[c]_m$, ottengo  $[a]_x=c$, prendo $u \in \mathbb{Z}, \; \; [u]_m$ è soluzione dell'equazione se e solo se $[a]_m \cdot [u]_m = [c]_m \iff [au]_m = [c]_m \iff au \equiv_m c$
Lo scopo di una equazione congruenziale è quello di trovare gli elementi $u$ che ne siano soluzione, cioè: $\iff m | c-au \iff \exists v \in \mathbb{Z} (mv=c-au) \iff \exists v \in \mathbb{Z} (au+mv=c) \iff \textcolor{blue}{\exists v \in \mathbb{Z}((u,v)}$ <span style="color:#0000CD">è soluzione dell'</span>[[Equazioni diofantee|equazione diofantea]] $\textcolor{blue}{au+mv=c}$, per il [[Teorema di Bezout|teorema di Bezout]], $au \equiv_m c$ ha soluzioni $\iff MCD(a,m)|c$.


## Teorema
