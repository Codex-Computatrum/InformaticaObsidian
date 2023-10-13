---
author: Lorenzo Tecchia
tags:
  - operation
  - dataStructure/abr
  - to-do/implementation
---
![[Pasted image 20230830092214.png]]

---
### $Get\&DeleteMIN$
Come prima, lavoriamo con il MIN del ramo destro e definiamo la funzione che restituisce il minimo ed [[Cancellazione|elimina]] il nodo.
![[Pasted image 20230830092431.png]]
- Le istruzioni $4,5,6$ definiscono una funzione chiamata $\textbf{SkipRight}$
- Il padre $skippa$ al figlio destro rispetto ad $a$.
	- Sostituisce suo figlio sinistro, con il figlio destro del sinistro, questo succede solo al nodo che contiene il minimo 
- Quando la ricorsione risale non fa altro che ricopiare i figli **sinistri** nei figli sinistri
- È un lavoro apparentemente inutile, ma sarà fondamentale per l'ultima chiamata prima della risalita, la quale sposterà il figlio **destro** nel nodo che contiene il minimo. 
- Il dato $d$ sarà lo stesso per tutta la risalita e sarà quello che verrà sostituito al nodo da eliminare. 
### $\textbf{SkipRight}$
![[Pasted image 20230830093113.png]]
- Salvo il figlio destro in $tmp$
- $Deallocate(x)$
- restituisco $tmp$
### $\textbf{SkipLeft}$
![[Pasted image 20230830093125.png]]
- Salvo il figlio sinistro in $tmp$
- $Deallocate(x)$
- Restituisco $tmp$
---
### $\textbf{Get\&DeleteMIN}$ (Versione con il padre $p$ passato per riferimento)
![[Pasted image 20230830094706.png]]
- Rispetto alla versione precedente, non c’è bisogno di restituire il padre ma lo si passa per riferimento.
 - $SwapChild$ scambia il figlio $x$ (di $p$) con un certo nodo $y$ . L’if controlla se $x$ è il figlio sinistro o destro di $p$  
- Avviene lo scambio con $y$ e poi dealloca $x$


## Implementazione
```C
// da implementare
```
