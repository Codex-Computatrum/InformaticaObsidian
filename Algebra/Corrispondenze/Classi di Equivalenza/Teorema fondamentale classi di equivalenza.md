---
tags:
  - Corrispondenze/ClassiDiEquivalenza
---
Sia $A \neq \emptyset$.
1. Se $\rho$ è una [[Relazione di equivalenza|relazione di equivalenza]] definita su $A$, allora l'insieme quoziente $\frac{A}{\rho}$ è una partizione di $A$.
2. Se $\rho$ è una [[Partizione di insiemi|partizione]] di A, allora la relazione $\rho_F$ definita come:
	$\rho_F : \forall x,y \in A, x \rho_F y \iff \exists x \in F : \{x,y\} \subseteq x$ è una relazione di equivalenza in $A$ e risulta $\frac{A}{\rho_F} = F$
### Dimostrazione 1.
$\frac{A}{\rho} = \{ [a]_\rho : a \in A \}$ è una [[Partizione di insiemi|partizione]] di $A \iff$
1. $\forall [a] \in \frac{A}{\rho} \; ([a] \neq \emptyset )$ Per la [[Prima Proprietà|prima proprietà delle classi di equivalenza]].
2. $\forall [a], [b] \in  \frac{A}{\rho} ([a] \neq [b] \implies [a] \cap [b] = \emptyset)$ per la [[Terza Proprietà|terza proprietà delle classi di equivalenza]].
3. $\bigcup [a] = A \; \; \text{con} \; \; a \in A$ | Bisogna dimostrare che $\textcolor{lightblue}{\bigcup [a] \subseteq A \land A \subseteq \bigcup [a]}$
	- $\textcolor{lightblue}{\forall a \in A, [a] \subseteq A \implies \bigcup [a] \subseteq A}$
	- $\forall a \in A, a \in [a] \subseteq \bigcup [a] \; \; \text{dove} \; \; a \in A \implies \forall a \in A, a \in \bigcup [a]$
	Cioè $A \subseteq \bigcup [a]$.
### Dimostrazione 2.
$\rho_F : (\forall x,y \in A)(x \, \rho_F \, y) \iff (\exists x \in F:\{x,y\} \subseteq x)$
La tesi dice che:
- $\rho_F$ è una **relazione di equivalenza**
- $\frac{A}{\rho_F}=F$
$\rho_F$ mette in corrispondenza $2$ elementi se essi sono nella stessa parte di F, cioè se sono nello stesso sottoinsieme della [[Partizione di insiemi|partizione]] F di A.
## Esempio 1.
$$A=\{x,y,z,t\} \; \; F=\{\{x\},\{y\}, \{z,t\}\}$$
Dove $F$ è una [[Partizione di insiemi|partizione]] di A.
$\rho_F$ è definita come segue
$$\rho_F = \{ \textcolor{lightblue}{(x,x), (y,y), (z,z)}, (t,t), (z,t), (t,z) \}$$
Possiamo notare quindi che $\rho_F$ è:
- [[Riflessiva]], visto che ognuno degli elementi di $A$ è in relazione con sé stesso.
- [[Simmetrica]], visto che $(z,t) \implies (t,z)$.
- [[Transitiva]], il motivo sarà più chiaro nel prossimo esempio.
## Esempio 2.
$$A= \{1,2,3,4,5\} \; \; F=\{ \{ 1 \}, \{2\}, \{3,4,5\} \}$$
$$\rho_F=\{(1,1),(2,2),(3,3),(4,4),(5,5),(3,4),(3,5),(4,3),(4,5),(5,3),(5,4)\}$$
Qui possiamo dimostrare che è [[Transitiva|transitiva]] visto che, per esempio:
$$(3 \rho 4) \land (4 \rho 5) \implies 3 \rho 5$$
E questo vale per ogni elemento che appartiene alla stessa parte di $A$.