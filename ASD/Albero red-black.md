---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure/abr
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Un albero **red-black** è un [[albero binario di ricerca]] con un bit aggiuntivo di memoria per ogni nodo: il colore del nodo, che può essere RED o BLACK.

Inoltre i dati sono presenti solo nei nodi interni:
- Le foglie non contengono dati (contengono il valore `NULL`), sono quindi tutte identiche
- I genitori delle foglie punteranno tutti ad un unico nodo `NULL` cosi da evitare spreco di memoria.
### Vincoli
1. Tutti i nodi sono o **rossi** o **neri**
2. Tutte le foglie sono **nere**
3. Se un nodo è rosso, allora entrambi i figli sono neri. Ossia i nodi **rossi** non possono avere figli **rossi**:([[Path|path]])
$$\forall x \in T, \exists h \in \mathbb{N}: \forall \pi \in Path(x) \lvert \pi \rvert = h$$
4. Ogni cammino dalla radice ad una foglia deve contenere lo stesso numero di nodi **neri**.
---
### [[Altezza]] nera 
Definiamo altezza nera di un nodo $x$, indicata con $bh(x)$ (black height), il numero di nodi neri lungo un [[Cammino semplice|cammino semplice]] che inizia dal nodo $x$ e finisce a una foglia.

Il nodo $x$ è escluso dato che non influisce sull’altezza nera, che sia rosso o nero l’altezza nera rimane la stessa.

L’altezza nera è pari alla metà dell’altezza $bh(x)=⌈h(x)/2⌉$

Quindi se l’albero ha almeno un percorso la cui lunghezza è inferiore all’altezza nera, quell’albero così com’è non può essere un **red-black** (con opportune rotazioni lo può diventare).  

Se non c’è neanche un percorso con lunghezza inferiore all’altezza nera, è possibile colorare l’albero in un certo modo per renderlo **red-black**.

Il numero di nodi interni è: (Internal Nodes) $IN(x) \geq 2^{bh(h)}-1$
>[!Osservazione]
> Il numero di nodi in un albero binario è $2^{h+1} − 1$ , escludendo le foglie: $2^{h} − 1$

![[Pasted image 20230831183814.png]]

---
### Teorema albero red-black
![[appuntiIngenito (dragged) copy 3.pdf]]

---
## Inserimento di un nodo
![[Pasted image 20230901100200.png|300]]
L’inserimento avviene come in un qualsiasi **[[Albero binario di ricerca|BST]]**, successivamente si colora il nodo di rosso per evitare di aumentare l’altezza nera solo su quel percorso, il che avrebbe portato alla violazione di una proprietà.

Essendo colorato di rosso:
- se il padre $y$ è **rosso**, vìola: ”un nodo rosso ha entrambi i figli neri” 
- se il padre $y$ è **nero**, allora non c’è violazione

***Le violazioni si dividono in tre casi***:
1. lo zio $z$ di $w$ è **rosso** (i fratelli $y$ e $z$ sono entrambi **rossi**):
	- Si colorano $y$ e $z$ di **nero** e il loro padre $x$ (nonno di $w$) si colora di **rosso**. 
	- ![[Pasted image 20230901100621.png|500]]
2. lo zio $z$ è nero e $y$ ha il figlio **rosso** a destra:
	- Si effettua una $RLRotation(y)$  
	- Non si risolve il problema, ma lo sposto a sinistra risolvendolo con il caso $3$
	- ![[Pasted image 20230901100759.png|500]]
 3. lo zio $z$ è **nero** e $y$ ha il figlio **rosso** a sinistra
	 - Si colora il padre $y$ di nero e il nonno $x$ di rosso 
	- Infine si effettua una $LRRotation(x)$
		- Colorando $y$ di **nero** si risolve il problema ”padre **rosso** figlio **rosso**” ma si alza l’**altezza nera**
		- quindi coloro il padre $x$ di rosso; così facendo abbasso l’**altezza nera** dell’albero destro in $z$
		- si effettua quindi una $LRRotation(x)$
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
1. il fratello $z$, del doppio nero $y$, è rosso  
2. il fratello $z$, del doppio nero $y$, è nero e $z$ ha entrambi i figli neri  
3. il fratello $z$, del doppio nero $y$, è nero e $z$ ha il sinistro rosso e il destro nero
4. il fratello $z$, del doppio nero $y$, è nero e $z$ ha il destro rosso

### Caso $1$
- coloro x di rosso
- coloro z di nero
- RLRotation(x)
- ![[Pasted image 20230901101836.png|600]]
### Caso $2$
- coloro $z$ di rosso
- coloro $y$ di nero (tolgo il doppio nero)
- se $x$ è rosso, diventa nero; se $x$ è nero, diventa doppio nero

Se z ha entrambi i figli neri, basterà colorarlo di rosso e togliere il doppio nero ad y. Cosi facendo le altezze nere dei figli di x sono corrette.

Il problema su y è risolto, al più viene spostato più in alto e passato ad x.  
x potrebbe essere nero ma anche rosso (visto che entrambi i figli sono neri), va quindi ricolorato.

Mi basta aggiungere un livello di altezza nera ad x perché  
• Avendo tolto il doppio nero a sinistra, l’altezza nera a sinistra si abbassa di 1  
• Avendo colorato di rosso il figlio destro di x, l’altezza nera a destra si abbassa di 1

Se x dovesse essere ricolorato come doppio nero, il problema verrà risolto risalendo la ricorsione.

![[Pasted image 20230902153330.png]]
### Caso $3$
L’obiettivo è di spostare il figlio sinistro rosso (del fratello del nodo doppio nero), a destra per ricondurci al caso $4$
- $LRRotation(z)$
- Coloro u di nero e z di rosso
>[!Obiettivo]
>Questo sia per bilanciare l’[[Albero red-black#Altezza nera|altezza nera]], sia per non avere il problema rosso-rosso con il padre $x$ nel caso fosse rosso, ma anche perché è l’obiettivo (avere il rosso a destra).


![[Pasted image 20230902153659.png]]
### Caso $4$
1. $RLRotation(x)$
2. Scambio i colori di $x$ e di $z$
	- Ovvero coloro $x$ di nero e $z$ di **rosso/nero** 
3. Coloro il figlio di destro di $z$ di nero altrimenti avrei l’altezza nera sbilanciata e un probabile **rosso-rosso**
4. Rimuovo il **doppio nero**
	- sul percorso sinistro di **z** c’è infatti un **nero** in più
![[Pasted image 20230902154007.png]]
Il figlio destro del fratello del **doppio nero**, è **rosso**
>[!note] I valori delle altezze nere sono solo un esempio per capire come variano passo dopo passo.

![[Pasted image 20230902154116.png]]

>[!note] L’albero in $x$ abbia a sinistra un nero in più rispetto a destra.

>[!note] $z$ **(rosso/nero)** non crea problemi nel caso in cui sia **rosso**, inizialmente $x$ era **rosso/nero**. Se il problema non c’era prima, non ci sarà neanche dopo.

## Algoritmi
### Algoritmi di inserimento e cancellazione
>[!tip] `NULLRB` è il puntatore al nodo foglia di un albero **red-black**, che è unico per evitare sprechi di memoria.
#### Algoritmo di inserimento
![[Pasted image 20230902175636.png]]
![[Pasted image 20230902175655.png]]
>[!important] Esiste anche il duale $RInsBalanceRB$

![[Pasted image 20230902175738.png]]
#### Algoritmo di cancellazione
![[Pasted image 20230902175827.png]]
![[Pasted image 20230902175841.png]]
![[Pasted image 20230902175907.png|400]]
![[Pasted image 20230902175939.png|600]]
- Se il colore di x è rosso, diventa nero  
- Se il colore di x è nero, diventa doppio nero
![[Pasted image 20230902180020.png]]
---
### Problemi che risolve un albero red-black
Un [[albero binario]] di ricerca di altezza $h$, è in grado di eseguire operazioni elementari sugli insiemi ($insert, delete, max, min, search$, ...) nel tempo $O(h)$.

Queste operazioni sono veloci se l’albero è basso, ma se l’altezza è grande, le prestazioni ne risentono (si potrebbe arrivare anche ad un costo lineare).

Gli alberi red-black rappresentano uno dei modi in cui gli alberi di ricerca vengono bilanciati, in modo tale da garantire alle operazioni elementari di essere eseguite in tempo $O(\log(n))$

Negli ***alberi red-black***, i nodi contengono anche il loro colore, oltre che il puntatore al figlio destro e sinistro, e le variabili per i dati.

---
```C
// da implementare
```