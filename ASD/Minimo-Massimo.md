---
author: Lorenzo Tecchia
tags:
  - operation
  - dataStructure/abr
  - to-do/implementation
---
###### Minimo Ricorsivo
```python
def Min(x):
	if x.sx = NULL:
		return x
	else
		return Min(x.sx)	
```
###### Minimo Iterativo
```python
def Min(x):
	while x.sx != NULL:
		x = x.sx
	return x
```
###### Massimo Ricorsivo
```python
def Max(x):
	if x.dx = NULL:
		return x
	else
		return Max(x.dx)

```
###### Massimo Iterativo
```python
def Max(x):
	while x.dx != NULL:
		x = x.dx
	return x
```

---
### $GetAndDeleteMIN$
Come prima, lavoriamo con il MIN del ramo destro e definiamo la funzione che restituisce il minimo ed [[Cancellazione|elimina]] il nodo.

```python
def GetAndDeleteMin(x):
	if x.sx = NULL:
		d = x.dato
		r = x.dx
		Deallocate(x)
		return(d, r)
	else
		(d, r) = GetAndDeleteMin(x.sx)
		x.sx = r
		return(d, r)		
		
```

^get-delete-min
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

- Salvo il figlio sinistro in $tmp$
- $Deallocate(x)$
- Restituisco $tmp$
---
### $\textbf{GetAndDeleteMIN}$ (Versione con il padre $p$ passato per riferimento)

```python
def GetAndDeleteMin(x, p):
	if x.sx = NULL:
		d = x.dato
		SwapChild(p, x, x.dx)
		return d
	else
		return GetAndDeleteMin(x.sx, x)
```

```python
def SwapChild(p, x, y):
	if p.sx = x:
		p.sx = y
	else
		p.dx = y
	Deallocate(x)
```

- Rispetto alla versione precedente, non c’è bisogno di restituire il padre ma lo si passa per riferimento.
 - $SwapChild$ scambia il figlio $x$ (di $p$) con un certo nodo $y$ . L’if controlla se $x$ è il figlio sinistro o destro di $p$  
- Avviene lo scambio con $y$ e poi dealloca $x$


## Implementazione
```C
// da implementare
```
