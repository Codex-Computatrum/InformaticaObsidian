---
author: Lorenzo Tecchia
tags: [operation, dataStructure/abr, to-do]
---
>[!todo] 
>- [ ] Implementazione in C

In un [[Tree|BST]], il successore di un qualsiasi numero (anche non presente nell'albero) è **il minimo dei maggioranti**.
>[!note]
> Partendo dalla radice, non so se esiste il successore, tantomeno non so se esiste un successore migliore; quindi man mano che scendo l’albero, salvo e aggiorno il successore con quello migliore trovato.

![[Pasted image 20230830161215.png]]
***Supponendo di voler trovare il successore di uno***.
![[Pasted image 20230830161317.png]]
- Posso scendere a sinistra, il successore sicuramente esiste, per adesso è $10$
- Continuo a sinistra, adesso il successore è aggiornato a $4$
- Posso ancora continuare a sinistra, il successore aggiornato è $3$
- Non posso più scendere a causa dello $0$

Quindi l’idea è quella di aggiornare la stima con $x$ quando il dato $d$ è minore di $x$, ovvero quando scendo a sinistra.

Vorrà dire che $x$ è un maggiorante di $d$, ma non sappiamo se è il minimo dei maggioranti. Se scendo a destra, non aggiorno la stima poiché $x$ è minore, non è un maggiorante, del dato $d$
### Versione iterativa

```python
def Successor(x, d):
	if x = NULL:
		return NULL
	else
		if d >= x.dato:
			return Successor(x.dx, d)
		else
			s = Successor(x.dx, d)
			if s = NULL:
				return x
			else
				return s
```
^SuccessorABR-Iterative

### Versione ricorsiva

```python
def Successor(x, d, s):
	if x == NULL:
		return s
	else
		 if d >= x.dato:
			 return Successor(x.dx, d, s)
		else
			return Successor(x.sx, d, x)
```
^SuccessorABR-Recursive

Viene passata la stima $s$ come parametro la quale verrà aggiornata solo se si scende a sinistra.  
Nella prima chiamata sarà $\bot$ 

---
## Implementazione in C
```C
//da implementare
```
