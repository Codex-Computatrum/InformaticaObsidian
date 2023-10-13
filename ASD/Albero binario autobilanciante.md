---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure/abr
  - to-do/implementation
---
Gli ***AVL*** sono [[Albero binario di ricerca|alberi binari di ricerca]] auto bilancianti. Per cui le proprietà:
- $\forall x \in T, \lvert h(T_{x.sx})- h(T_{x.dx})\rvert \leq 1$ dove $T$ è l'albero, ossia l'[[altezza]] dei sotto alberi differisce al più di uno. 
![[Pasted image 20230831140231.png]]
---
### Alberi AVL minimi 
Un **AVL** minimo di altezza $h$, è l’**AVL** di altezza h con il minimo numero di nodi

La classe degli **AVL** minimi, sono i peggiori riguardo l’altezza.  
Questo **perché** gli algoritmi che scorrono l’altezza non dipendono dal numero di nodi.

Di conseguenza, se all’aumentare dei nodi non aumenta l’altezza, allora l’albero è migliore rispetto ad avere meno nodi con la stessa altezza (aumento la quantità dei dati mantenendo la stessa efficienza).

In particolare, se ad una certa altezza ho il minimo numero di nodi, allora ho l’albero peggiore per quell’altezza.

Si osserva dunque, che se si dimostra che per gli **AVL** minimi $h = \Theta(\log(n))$ allora lo è anche per quelli non minimi (ovvero per tutti gli **AVL**).

![[AVLminimiIngenito.pdf]]

---
## Inserimento di un nodo
>[!important] 
> L'inserimento di un nodo, può rompere la struttura di un AVL.

L'[[algoritmo]] di inserimento, quindi dovrà anche risistemare l'albero affinché conservi la proprietà di **AVL**.
![[Pasted image 20230831144205.png]]
- **Caso 1: Inserisco il nodo nel sotto-albero $\alpha$**
	- ![[Pasted image 20230831154929.png|300]]
		- Inserendo il nodo nel sotto-albero $\alpha$ , questo aumenta di altezza (da $h−1$ a $h$)  
		- Di conseguenza, anche $y$ aumenta di 1, lo stesso vale per $x$
		- A questo punto i sotto-alberi di $x$ non rispettano le condizioni per essere un **AVL**: c’è una differenza di $2$ tra il sotto-albero destro e sinistro di $x$
		- Spostando in un certo modo gli alberi $\alpha', \beta, \gamma$ è possibile mantenere la struttura di **AVL**.
	- ![[Pasted image 20230831160152.png|500]]
		- Facendo una rotazione da sinistra a destra centrata sul nodo $x$ (ovvero il nodo dove c’è il problema), riesco a mantenere la struttura di **AVL**.
		- Inoltre, continua a mantenere la struttura di **[[Albero binario di ricerca|BST]]**.
		- $\beta$ continua ad essere più grande di $y$ e più piccolo di $x$
		- $\alpha'$ e $\gamma$ non vengono spostati quindi mantengono la proprietà
- **Caso 2: Inserisco il nodo nel sotto-albero $\beta$**
	- ![[Pasted image 20230831163422.png|200]]
		- Inserendo il nodo nel sotto-albero $\beta$ , come nel caso precedente, aumentano le altezze e l’albero si sbilancia, perdendo le proprietà di **AVL**.
		- Una rotazione a destra come nel caso precedente, sposta il problema sull’altro lato dell’albero, ma non lo risolve. ![[Pasted image 20230831163736.png|200]] 
		- nella figura a destra è stata effettuata un $LLRotation(x)$
	- ![[Pasted image 20230831164037.png|300]]
		- Per risolvere il problema, si divide il sotto-albero $\beta$
		- Si estrae la radice $z$ (di $\beta$) che avrà altezza $h-1$ 
		- Le altezze dei due sotto-figli ($\beta_{1}, \beta_{2}$) possono essere: $h−2$ e $h−2$ , $h−2$ e $h−3$ , $h−3$ e $h−2$
		- Almeno uno dei due sotto-alberi sarà alto $h − 2$ ; ad esempio, se fossero entrambi alti $h − 3$ vuol dire che $h(z) = h − 2$ , il che non è vero dato che $h(z)=h−1$
		- Inoltre, non possono essere più bassi di $h − 3$: ad esempio, se uno dei due fosse alto $h − 4$ , e l’altro per forza sarà alto $h − 2$, vuol dire che non è un **AVL**
	- ![[Pasted image 20230831164608.png|300]]
		- Supponiamo di aggiungere un nodo in $\beta_{1}$ (_stesso ragionamento_ per $\beta_{2}$)
		- Inserendo in $\beta$ , avrò il caso in cui sia $\beta_{1}$ sia $\beta_{2}$ sono alti $h−2$ altrimenti il problema si troverà in un altro punto, che andrà risolto comunque con uno dei due casi.
		- In questo caso servono due rotazioni: una verso sinistra su $y$ e successivamente una verso destra su $x$
>[!important] È importante l'ordine con cui si effettuano le rotazioni altimenti non funziona

![[Pasted image 20230831165054.png]]
- Così facendo si è conservata la proprietà sia di **AVL** che **BST**:
	- $\beta_{1}'$ continua ad essere $y < \beta'_{1} < z$ 
	- $\beta_{2}'$ continua ad essere $y < \beta'_{2} < z$ 
	- $z$ continua $y < \beta_{2} < z$
---
### Costo
Riparare, e quindi mantenere, la struttura di **AVL** dopo un inserimento, ha tempo costante dato che vengono effettuati degli scambi fra puntatori.
>[!important] Serve riparare l’albero ad ogni inserimento che rompe l’albero.
 
---
## Cancellazione in AVL
>[!summary] 
>La cancellazione porta gli stessi problemi dell'inserimento e si risolvono allo stesso modo

![[Pasted image 20230831170902.png]]
![[appuntiIngenito (dragged) copy 2.pdf]]

---
## Funzionamento algoritmi per rotazioni
![[Pasted image 20230831171417.png]]
- I nodi di un **AVL**, a differenza di quelli di un **BST**, possiede un ulteriore attributo per memorizzare l’altezza.
- In questo modo è possibile sapere se ci sono violazioni.

| AVL | Node |
| --- | ---- |
| D   | ht   |
| SX  | DX   |

| BST | Node |
| --- | ---- |
| D   | D    |
| SX  | SX   |

---
- Restituisce dell'**AVL** con radice in $x$, se questa è $\bot$ allora restituisce $-1$
![[Pasted image 20230831172645.png]]
- Essendo un semplice $if$ la funzione ha tempo costante $\Theta(1)$
- ---
- Aggiorna l’altezza dell’**AVL** con radice in $x$ (utilizzata dopo una rotazione)
![[Pasted image 20230831172738.png]]
- Aggiorno l’altezza dell’albero radicato in $x$ con il massimo fra le altezze dei due figli
- Tutte e tre le istruzioni sono chiamate a funzioni a tempo costante, quindi l’intera funzione è costante $\Theta(1)$ 
---
![[Pasted image 20230831172914.png|300]]
- La rotazione su un **AVL** ha bisogno successivamente di aggiustare le altezze. Questa funzione racchiude le tre funzioni per fare ciò.
- Dopo la rotazione, $x$ si trova ”più in basso” di $y$ , logicamente è importante che venga aggiornata prima la sua di altezza e poi quella di $y$
- Essendo tutte le funzioni chiamate $\Theta(1)$, il costo totale sarà costante $\Theta(1)$
---
![[Pasted image 20230831173039.png|400]]
- Funzione che effettua la doppia rotazione al figlio sinistro (**Left-Double**)
- Farà quindi prima una $\textbf{R-L Rotation}$ e poi una $\textbf{L-R rotation}$. Speculare sarà per $\textbf{R-D-AVLRotation}$
- Anche questa è costante $\Theta(1)$
---
![[Pasted image 20230831173401.png|460]]
- Bilancia l’albero radicato in $x$ (input) nel caso in $h(x.sx) = h(x.dx) + 2$, ovvero l’altezza del sotto-albero sinistro è più $2$ del destro.
- Speculare l’algoritmo $\textbf{RBalanceAVL}$ nel caso in cui sia il sotto-albero destro ad essere più alto di $2$.
- Ad esempio, è importante chiamare questa funzione dopo un inserimento o una cancellazione.
- Ha tempo costante, in quanto tutte le funzioni che chiama sono a tempo costante
---
### Inserimento e cancellazione
![[Pasted image 20230831174124.png|400]]
- Simile all’inserimento in un **BST** ma con la differenza che bisogna bilanciare l’albero.
- Se inserisco a sinistra, rendo potenzialmente il sotto-albero sinistro più profondo del destro, effettuo quindi un $\textbf{LeftBalanceAVL}$.
- Discorso speculare se inserisco destra.
---
![[Pasted image 20230831174227.png|400]]
- Simile alla cancellazione in un BST ma con la differenza che bisogna bilanciare l’albero.
- Se cancello a destra, rendo potenzialmente il sotto-albero destro più basso (o meno alto) e di conseguenza rendo il sinistro più profondo, effettuo quindi un $\textbf{LeftBalanceAVL}$.
- Discorso speculare se cancello sinistra.
---
![[Pasted image 20230831174642.png]]

---
>[!todo] 
>- [ ] Implementazione in C

```C
//da implementare

```
