---
author: Lorenzo Tecchia
tags:
  - definition
  - dataStructure
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Un'[[Tree|albero]] si dice **binario** se ogni nodo ha al massimo due figli.
![[Pasted image 20230828170509.png]]
>[!hint] 
>Un albero binario è un ottimo compromesso tra un array e una [[lista concatenata]]
>	L'array è rigido ma poco flessibile
>	La lista è il viceversa

---
### Scorrimento
È possibile scorrere un **albero binario** principalmente in due modi:
- In **[[Ampiezza]]** (Breadth First Visit)
- In **[[Profondità]]** (Depth First Visit):
	- **[[Order-pre|pre-order]]**: viene visato prima il padre, poi il sinistro, poi il destro
	- **[[Order-in|in-order]]**: viene visitato prima il figlio sinistro, poi il padre, poi il destro
	- **[[Order-post|post-order]]**: viene visato prima il figlio sinistro, poi il destro, poi il padre

>[!hint] Quale scorrimento tra quelli visti è consigliabile scegliere?
>Dipende dal dominio di applicazione dell'albero e di conseguenza da quale forma assumerà
>
>Se l'albero tende ad essere **basso e ampio**, conviene uno scorrimento in profondità; la cui complessità sarà $O(n)$ o $\log(n)$ dove $h$ è l'altezza e $n$ è il numero di nodi
>
>Conviene invece uno scorrimento in **ampiezza** se l'albero è sbilanciato


---
### Albero binario completo
Un albero binario si dice anche **completo** se: 
- è pieno, ossia tutti i nodi hanno entrambi i figli.
- ogni sua foglia ha la stessa profondità. 

>[!note]
> Un nodo si dice foglia quando non ha figli _alternativamente quando il suo grado è uguale a 1_

#### Numero di nodi di un albero binario completo
$$n = 2^{h + 1} - 1$$
Dove $h$ è l'[[Altezza|altezza]] dell'albero.

Ogni nodo ha due figli, quindi all'$i$-esimo livello ci saranno $2^{i}$ figli.
Quindi l'intero albero avrà: $n = \sum^{h}_{i=0}2^{i}$ nodi 

Questa è la somma dei primi $h$ termini di una serie geometrica di ragione 2
>[!recall]
> Una serie geometrica di ragione $q\geq 1$ diverge positivamente $$\sum^{n}_{k=0}q^{k}=\frac{1-q^{n+1}}{1-q}$$

$$n = \sum^{h}_{i=0}2^{i}= \frac{1-2^{h+1}}{1-2} = -(1-2^{h+1}) = 2^{h+1}-1$$

---
### Albero binario quasi completo
Un albero binario si dice **quasi completo** se:
- è pieno fino al penultimo livello
- i nodi dell'ultimo livello sono inseriti da sinistra a destra
---
![[Pasted image 20230828171123.png]]

---
## Implementazione in C
```C

```
