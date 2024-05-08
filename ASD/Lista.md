---
author: Lorenzo Tecchia
tags: [definition, dataStructure, to-do]
---
Una **lista puntata** è un insieme dinamico in cui ogni elemento ha una chiave (*key*) ed un riferimento all'elemento successivo (*next*) dell'insieme.
>[!important]
> La lista è una struttura dati ad accesso strettamente sequenziale $\rightarrow$ Da ciò ne deriva un tempo lineare per tutti gli algoritmi che necessitano di una ricerca
Una ***lista*** $L$ è un oggetto con le seguenti proprietà:
1. O è un insieme vuoto di nodi $\rightarrow L = \emptyset$
2. Oppure contiene un nodo con un dato e un riferimento ad un oggetto $L'$ dove $L'$ è una lista (non c'è ambiguità poiché $|L'| < |L|$ per definizione)
Da questa definizione induttiva risulta naturale scrivere algoritmi ricorsivi per implementare le operazioni sulla lista; infatti, per l'operazione di ricerca possiamo implementare il seguente algoritmi:

```python
def Ricerca(L, k):
	L != NULL:
		if L->key == k:
			ret = L
		else:
			ret = L
	return ret
```
^Ricerca-Lista

 Poiché ogni elemento della lista è indipendente dagli altri e non sono disposti in. maniera contigua in memoria, l'inserimento di un nuovo nodo in testa risulta banale
 
 ```python
 # L'algoritmo è costante, ma se si volesse inserire il nodo in una determinata posizione (con una conseguente ricerca) in una lista costante
 # L'algorimto risulta comunque lineare anche se il nodo viene aggiunto e creato in tempo costante

def Insert(L, k):
	tmp = crea_nodo()
	tmp -> key = k
	tmp -> next = L
	L = tmp
	return L

def OrdInsert(L, k):
	if L != NULL and L->key < k:
		L->next = OrderInsert(L->next, k)
	else:
		tmp = crea_nodo()
		tmp -> key = k
		tmp -> next = L
		L = tmp
	return L
 ```
 ^Insert-Lista
 
 Una ricerca risulta necessaria anche nel caso in cui volessi avere una lista senza duplicati:
 
```python
def InsertUnica(L, k):
	if L = NULL:
		tmp = crea_nodo()
		tmp -> key = k
		tmp -> next = NULL
		L = tmp
	else if L->key != k:
		L -> next = InsertUnica(L -> next, k)
	return L
```
^Insert-Unique-Lista

Per la cancellazione di un elemento è necessario la ricerca. Inoltre i casi ricorsivi da gestire sono due (si fa sempre affidamento alla definizione della lista):
- La lista è vuota
- La lista contiene un nodo con una chiave ed un riferimento ad un'altra lista
Da questo ne deriva il seguente algoritmo lineare:

```python
def Cancella(L, k):
	if L != NULL:
		if L -> key == k:
			L = L -> next
			dealloca(tmp)
		else:
			L -> next = Cancella(L -> next, k)
	return L
```
^Cancella-Lista

```python
# Cancella gli elementi pari
def CancellaPari(L):
   # Visto che la chiamata ricorsiva è fatta prima dell'eventuale cancellazione dell'elemento, l' algoritmo praticamente andrà a cancellare gli elementi partendo dall'ultimo
	if L != NULL:
	L -> next = CancellaPari(L -> next)
	if (L -> key) % 2 = 0:
		tmp = L
		L = L -> next
		dealloca(L)
	return L
```
^Cancella-Pari

```python
# Restituisce il numero degli elementi pari cancellati
# Visto che l'algoritmo non restituisce la lista ma un intero (che rappresenta il conteggio), abbiamo bisogno oltre al nodo da cancellare anche il suo precedente, in modo da poter ricostruire ala lista
def CancellaPariConta(L, Prev):
   counter = 0
   if L != NULL: 
   counter = CancellaPariConta(L-> next, L)
   counter = CancellaPariConta(L-> next, L)
   if (L -> next) % 2 = 0:
	   Prev -> next = L -> next
	   dealloca(L)
	   counter += 1
	return counter
```
^Cancella-Pari-Conta

```python
def CacncellaPariContaTesta(L):
	counter = CancellaPariConta(L -> next, L)
	if L -> key % 2 == 0:
		tmp = L
		L = L -> next
		dealloca(tmp)
		counter += 1
	return counter
```
^CacncellaPariContaTesta