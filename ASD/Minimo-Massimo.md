---
author: Lorenzo Tecchia
tags:
  - operation
  - dataStructure/abr
  - to-do/implementation
---
###### Minimo Ricorsivo

```python
def Min(T):
	if T -> sx = NULL:
		return T
	else
		return Min(T -> sx)	
```
^min-rec

###### Minimo Iterativo

```python
def Min(T):
	while T.sx != NULL:
		T = x.sx
	return T
```
^min-iter

###### Massimo Ricorsivo

```python
def Max(T):
	if T -> dx = NULL:
		return T
	else
		return Max(T -> dx)

```
^max-rec

###### Massimo Iterativo

```python
def Max(T):
	while T -> dx != NULL:
		T = T -> dx
	return T
```
^max-iter

---
### $GetAndDeleteMIN$
Come prima, lavoriamo con il MIN del ramo destro e definiamo la funzione che restituisce il minimo ed [[Cancellazione|elimina]] il nodo.

```python
def GetAndDeleteMin(T, p):
	if T -> sx == NULL:
		d = T -> key
		SwapChild(p, T, T -> dx)
		return d
	else:
		return GetAnDeleteMin(T -> sx, T)
```
^GetAndDeleteMin-ABR

- Le istruzioni $4,5,6$ definiscono una funzione chiamata $\textbf{SkipRight}$
- Il padre $skippa$ al figlio destro rispetto ad $a$.
	- Sostituisce suo figlio sinistro, con il figlio destro del sinistro, questo succede solo al nodo che contiene il minimo 
- Quando la ricorsione risale non fa altro che ricopiare i figli **sinistri** nei figli sinistri
- È un lavoro apparentemente inutile, ma sarà fondamentale per l'ultima chiamata prima della risalita, la quale sposterà il figlio **destro** nel nodo che contiene il minimo. 
- Il dato $d$ sarà lo stesso per tutta la risalita e sarà quello che verrà sostituito al nodo da eliminare. 
### $\textbf{SkipRight}$

```python
def SkipRight(x):
	tmp = x.dx
	Deallocate(x)
	return tmp
```
^SkipRightABR

- Salvo il figlio destro in $tmp$
- $Deallocate(x)$
- restituisco $tmp$
### $\textbf{SkipLeft}$

```python
def SkipLeft(x):
	tmp = x.sx
	Deallocate(x)
	return tmp
```
^SkipLeft

- Salvo il figlio sinistro in $tmp$
- $Deallocate(x)$
- Restituisco $tmp$


```python
def SwapChild(p, x, y):
	if p.sx == x:
		p.sx = y
	else
		p.dx = y
	Deallocate(x)
```
^SwapChild

- Rispetto alla versione precedente, non c’è bisogno di restituire il padre ma lo si passa per riferimento.
 - $SwapChild$ scambia il figlio $x$ (di $p$) con un certo nodo $y$ . L’if controlla se $x$ è il figlio sinistro o destro di $p$  
- Avviene lo scambio con $y$ e poi dealloca $x$


## Implementazione
```C
// da implementare
```
