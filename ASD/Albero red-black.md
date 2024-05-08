---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure/abr
  - to-do/implementation
aliases:
  - rb
  - RB
---

>[!todo] 
>- [ ] Implementazione in C

Un albero **red-black** è un [[albero binario di ricerca]] con un bit aggiuntivo di memoria per ogni nodo: il colore del nodo, che può essere `RED` o `BLACK`.

Inoltre i dati sono presenti solo nei nodi interni:
- Le foglie non contengono dati (contengono il valore `NULL`), sono quindi tutte identiche
- I genitori delle foglie punteranno tutti ad un unico nodo `NULL` cosi da evitare spreco di memoria.
### Vincoli
1. Tutti i nodi sono o **rossi** o **neri**
2. Tutte le foglie sono **nere**
3. Se un nodo è rosso, allora entrambi i figli sono neri. Ossia i nodi **rossi** non possono avere figli **rossi**:([[Path|path]])
$$\forall \; T \in T, \;\exists \; h\; \in \mathbb{N}:\; \forall \;\pi\; \in \;Path(T) \; \lvert \; \pi \; \rvert = h$$
4. Ogni cammino da un nodo interno ad una foglia deve contenere lo stesso numero di nodi **neri**.
>[!important]
> Il miglior modo per costruire un **RB** è a partire dal percorso più breve
> I nodi di tale percorso vanno colorati tutti di nero per massimizzare il più possibile i nodi neri
> 
> Se nel percorso più breve mettessi dei nodi rossi allora non è detto di poter garantire la proprietà **4**.
> 
> Una volta effettuato questa operazione ed aver determinato il numero di nodi neri di ogni percorso inizierò a colorare i percorsi restanti cercando di non violare la proprietà 3 e continuando a rispettare la proprietà **4**.
> 
> La colorazione di un albero non è necessariamente unica:
> Un esempio è l’albero pieno che ha il numero maggiore possibile di differenti colorazioni (posso farlo tutto nero, o alternando un livello nero con uno rosso, o ancora un livello rosso per ogni 2 neri, e così via) e man mano che sbilancio l’albero le variazioni di colorazione diminuiscono fino ad arrivare ad uno sbilanciamento tale da non permettere ulteriori colorazioni.
> > [!danger]
> > Ogni albero AVL è RB
---
### [[Altezza]] nera 
Definiamo altezza nera di un nodo $T$, indicata con $bh(T)$ (black height), il numero di nodi neri lungo un [[Cammino semplice|cammino semplice]] che inizia dal nodo $T$ e finisce a una foglia.

Il nodo $T$ è escluso dato che non influisce sull’altezza nera, che sia rosso o nero l’altezza nera rimane la stessa.

L’altezza nera è pari alla metà dell’altezza $bh(T)=⌈h(T)/2⌉$

Quindi se l’albero ha almeno un percorso la cui lunghezza è inferiore all’altezza nera, quell’albero così com’è non può essere un **red-black** (con opportune rotazioni lo può diventare).  

Se non c’è neanche un percorso con lunghezza inferiore all’altezza nera, è possibile colorare l’albero in un certo modo per renderlo **red-black**.

Il numero di nodi interni è: (Internal Nodes) $IN(T) \geq 2^{bh(h)}-1$
>[!Osservazione]
> Il numero di nodi in un albero binario è $2^{h+1} − 1$ , escludendo le foglie: $2^{h} − 1$

![[Pasted image 20230831183814.png]]

---
### Teorema albero red-black
![[appuntiIngenito.pdf#page=45]]

---
## Inserimento di un nodo
![[Pasted image 20230901100200.png|300]]
L’inserimento avviene come in un qualsiasi **[[Albero binario di ricerca|BST]]**, successivamente si colora il nodo di rosso per evitare di aumentare l’altezza nera solo su quel percorso, il che avrebbe portato alla violazione di una proprietà.

Essendo colorato di rosso:
- se il padre $y$ è **rosso**, vìola: ”un nodo rosso ha entrambi i figli neri” 
- se il padre $y$ è **nero**, allora non c’è violazione

***Le violazioni si dividono in tre casi***:
1. lo zio $z$ di $w$ è **rosso** (i fratelli $y$ e $z$ sono entrambi **rossi**):
	- Si colorano $y$ e $z$ di **nero** e il loro padre $T$ (nonno di $w$) si colora di **rosso**. 
	- ![[Pasted image 20230901100621.png|500]]
2. lo zio $z$ è nero e $y$ ha il figlio **rosso** a destra:
	- Si effettua una $RLRotation(y)$  
	- Non si risolve il problema, ma lo sposto a sinistra risolvendolo con il caso $3$
	- ![[Pasted image 20230901100759.png|500]]
 3. lo zio $z$ è **nero** e $y$ ha il figlio **rosso** a sinistra
	 - Si colora il padre $y$ di nero e il nonno $T$ di rosso 
	- Infine si effettua una $LRRotation(T)$
		- Colorando $y$ di **nero** si risolve il problema ”padre **rosso** figlio **rosso**” ma si alza l’**altezza nera**
		- quindi coloro il padre $T$ di rosso; così facendo abbasso l’**altezza nera** dell’albero destro in $z$
		- si effettua quindi una $LRRotation(T)$
	- ![[Pasted image 20230901101046.png|600]]
---
## Cancellazione di un nodo in red-black
La cancellazione di un nodo **rosso** non crea problemi, perché questo avrà padre **nero** e figli **neri**, quindi al più si sono collegati due nodi **neri**.

Invece, la cancellazione di un nodo **nero** porta ad uno sbilanciamento dell’**altezza nera**.

Per risolvere momentaneamente il problema dello sbilanciamento dell’**altezza nera** si propaga il colore **nero**.

Ovvero, il figlio del nodo da eliminare (a seconda del caso $SkipRight$ o $SkipLeft$):
- se è rosso, lo si colora di nero
- se è nero, diventa un doppio nero

Cosi facendo, l’altezza rimane bilanciata.  
Il colore doppio nero però va rimosso; sono $4$ i casi possibili:
> [!warning]- ### Caso 1: il fratello $z$, del doppio nero $y$, è rosso  
> - coloro $x$ di rosso
> - coloro $z$ di nero
> - RLRotation($x$)
> - ![[Pasted image 20230901101836.png|600]]


> [!warning]- ### Caso 2: il fratello $z$, del doppio nero $y$, è nero e $z$ ha entrambi i figli neri  
> - coloro $z$ di rosso
> - coloro $y$ di nero (tolgo il doppio nero)
> - se $x$ è rosso, diventa nero; se $T$ è nero, diventa doppio nero
> 
> Se $z$ ha entrambi i figli neri, basterà colorarlo di rosso e togliere il doppio nero ad $y$. Cosi facendo le altezze nere dei figli di $x$ sono corrette.
> 
> Il problema su $y$ è risolto, al più viene spostato più in alto e passato a $x$, il quale potrebbe essere nero ma anche rosso (visto che entrambi i figli sono neri), va quindi ricolorato.
> 
> Mi basta aggiungere un livello di altezza nera ad $x$ perché  
> • Avendo tolto il doppio nero a sinistra, l’altezza nera a sinistra si abbassa di $1$  
> • Avendo colorato di rosso il figlio destro di $x$, l’altezza nera a destra si abbassa di $1$
> 
> Se $x$ dovesse essere ricolorato come doppio nero, il problema verrà risolto risalendo la ricorsione.
> 
> ![[Pasted image 20230902153330.png]]


> [!warning]- ### Caso 3: il fratello $z$, del doppio nero $y$, è nero e $z$ ha il sinistro rosso e il destro nero
> L’obiettivo è di spostare il figlio sinistro rosso (del fratello del nodo doppio nero), a destra per ricondurci al caso $4$
> - $LRRotation(z)$
> - Coloro $u$ di nero e $z$ di rosso
> 
> >[!Obiettivo]
> >Questo sia per bilanciare l’[[Albero red-black#Altezza nera|altezza nera]], sia per non avere il problema rosso-rosso con il padre $T$ nel caso fosse rosso, ma anche perché è l’obiettivo (avere il rosso a destra).
> 
> ![[Pasted image 20230902153659.png]]

> [!warning]- ### Caso 4: il fratello $z$, del doppio nero $y$, è nero e $z$ ha il destro rosso
> 1. $RLRotation(x)$
> 2. Scambio i colori di $x$ e di $z$
> 	- Ovvero coloro $x$ di nero e $z$ di **rosso/nero** 
> 3. Coloro il figlio di destro di $z$ di nero altrimenti avrei l’altezza nera sbilanciata e un probabile **rosso-rosso**
> 4. Rimuovo il **doppio nero**
> 	- sul percorso sinistro di **z** c’è infatti un **nero** in più
>
> ![[Pasted image 20230902154007.png]]
> Il figlio destro del fratello del **doppio nero**, è **rosso**
> 
> >[!note] I valori delle altezze nere sono solo un esempio per capire come variano passo dopo passo.
>
> ![[Pasted image 20230902154116.png]]
> 
> >[!note] L’albero in $T$ abbia a sinistra un nero in più rispetto a destra.
>>  $z$ **(rosso/nero)** non crea problemi nel caso in cui sia **rosso**, inizialmente $T$ era **rosso/nero**. Se il problema non c’era prima, non ci sarà neanche dopo.

## Algoritmi
### Algoritmi di inserimento e cancellazione
>[!tip] `NULLRB` è il puntatore al nodo foglia di un albero **red-black**, che è unico per evitare sprechi di memoria.
#### Algoritmo di inserimento
```python
def R-B-Insert(T, k):
	if T != NULL:
		if T -> key > k:
			T -> sx = R-B-Insert(T -> sx, k)
			T = L-Ins-BalanceRB(T)
		else if T -> key < k:
			T -> dx = R-B-Insert(T -> dx, k)
	else:
		x = RB-CreateNode()
		x -> key = k
		x -> c = R
		return x
	return T
```
^R-B-Insert

```python
def L-Ins-BalanceRB(T):
	if T -> sx != NULL:
		switch LInsViolationRB(T):
			case 1: T = LInsBalanceRB1(T)
			case 2: T = LInsBalanceRB2(T)
			case 3: T = LInsBalanceRB3(T)
	return T
```
^L-Ins-BalanceRB

>[!important] Esiste anche il duale $RInsBalanceRB$

```python
def L-Ins-ViolationRB(T):
	A = T -> sx
	if A -> c == R:
		C = T -> dx
		if C -> c == R:
			return 1
		else:
			if (C -> sx -> c) == R:
				return 2
			else if (C -> dx -> c) == R:
					return 3
	return 0
```
^L-Ins-ViolationRB
```python
def LInsBalanceRB1(T):
	T -> c = R
	(T -> sx) -> c = N
	(T -> dx) -> c = N
	return T
```
^LInsBalanceRB1

```python
def LInsBalanceRB2(T):
	A = T -> sx
	gamma = A -> dx
	A -> dx = T
	T -> sx = gamma
	A -> c = N
	(A -> dx) -> c = R
	return A
```
^LInsBalanceRB2

```python
def LInsBalanceRB3(T):
	A = T -> sx
	b = T -> dx
	beta = B -> sx
	B -> sx = A
	A -> dx = beta
	T -> sx = B
	return LInsBalanceRB2(T) 
```
^LInsBalanceRB3

#### Algoritmo di cancellazione

```python
def DeleteRB(T, k):
	if T != NULL:
		if T -> key > k:
			T -> sx = DeleteRB(T -> sx, k)
			T = BalanceDelSX(T)
		if T -> key < k:
			T -> dx = DeleteRB(T -> dx, k)
			T = BalanceDelDX(T)
		else:
			T = DeleteRB-Root(T)
	return T
```
^DeleteRB

```python
def DeleteRB-Root(T):
	if T -> sx != NULL || T -> dx != NULL:
		tmp = T
		if T -> sx == NULL:
			T = T -> dx
		else:
			T = T -> sx
		PropagateBlack(tmp, T)
		Deallocate(tmp)
	else:
		k = StaccaMinRB(T -> dx, T)
		T -> key = k
		T = BalanceDelDX(T)
	return T
```
^DeleteRB-Root

```python
def PropagateBlack(x, y):
	if y -> c == R:
		y -> c = N
	else:
		y -> c = N
```
^PropagateBlack

```python
def GetAndDeleteMinRB(T, p):
	if T -> sx != NULL:
		d = T -> dato
		y = SkipRightRB(T)
	else
		d = GetAndDeleteMinRB(T -> sx, T)
		y = LDelBalanceRB(T)
	SwapChild(p, T, y)
	return d
```
^GetAndDeleteMinRB

```python
def SkipRightRB(T):
	if T -> c == B:
		PropagateBlackRB(T -> dx)
	return SkipRight(T)
```
^SkipRightRB

- Se il colore di T è rosso, diventa nero  
- Se il colore di T è nero, diventa doppio nero

```python
def L-Del-BalanceRB(T):
	if T -> sT != NULL:
		switch LDelViolationRB(T):
			case 1: T = LDelBalanceRB1(T)
			case 2: T = LDelBalanceRB2(T)
			case 3: T = LDelBalanceRB3(T)
			case 4: T = LDelBalanceRB4(T)
	return T
```
^L-Del-BalanceRB

```python
def L-Del-ViolationRB(T):
	v = 0
	if S -> c == DN:
		if D -> c == R:
			v = 1
		else if (D -> dx) -> c == N && (D -> sx) -> sx == N:
			v = 2
		else if (D -> dx) -> c == N:
			v = 3
		else:
			v = 4
	return v
```
^L-Del-ViolationRB

```python
def LDelBalanceRB1(T):
	T = R-L-AVLROtation(T)
	T -> c = N
	(T -> sx) -> c = R
	return T
```
^LDelBalanceRB1

```python
def LDelBalanceRB2(T):
	(T -> dx) -> c = R
	(T -> sx) -> c = N
	PropagateBlack(T -> sx, T)
	return T
```
^LDelBalanceRB2

```python
def LDelBalanceRB3(T):
	T -> dx = L-R-AVLRotation(T)
	(T -> dx) -> c = N
	((T -> dx) -> dx) -> c = R
	T = LDelBalanceRB4(T)
	return T
```
^LDelBalanceRB3


```python
def LDelBalanceRB4(T):
	T = L-R-AVLRotation(T)
	(T -> dx) -> c = T -> c
	T -> c = (T -> sx) -> c
	(T -> sx) -> c = N
	((T -> sx) -> sx) -> c = N
	return T
```
^LDelBalanceRB4

---
### Problemi che risolve un albero red-black
Un [[albero binario]] di ricerca di altezza $h$, è in grado di eseguire operazioni elementari sugli insiemi ($insert, delete, maT, min, search$, ...) nel tempo $O(h)$.

Queste operazioni sono veloci se l’albero è basso, ma se l’altezza è grande, le prestazioni ne risentono (si potrebbe arrivare anche ad un costo lineare).

Gli alberi red-black rappresentano uno dei modi in cui gli alberi di ricerca vengono bilanciati, in modo tale da garantire alle operazioni elementari di essere eseguite in tempo $O(\log(n))$

Negli ***alberi red-black***, i nodi contengono anche il loro colore, oltre che il puntatore al figlio destro e sinistro, e le variabili per i dati.

---
```C
// da implementare
```
