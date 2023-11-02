---
author: Lorenzo Tecchia
tags:
  - definition
---
Un [[Tree|albero]] di decisione è un [[Albero binario#^ff6165|albero binario completo]] (tutti i nodi hanno entrambi i figli) che rappresenta i confronti fra gli elementi di un array.

L’[[ordinamento]], in un’albero di decisione, consiste nel tracciare un [[Path|percorso]] a partire dalla radice fino ad una foglia; ogni nodo attraversato rappresenta un confronto e la foglia contiene la sequenza ordinata.

---
Un algoritmo di ordinamento per confronti, dev’essere in grado di generare tutte le $n!$ permutazioni dell’array in input, dato che solo una di questa sarà la sequenza ordinata. ^cfb8cd

Di conseguenza, l’albero di decisione avrà $n!$ foglie, dato che ogni foglia rappresenta la sequenza ordinata in base alla sequenza in input.

La lunghezza di un percorso è paragonabile al tempo di esecuzione dell’algoritmo d’ordinamento: 
- il percorso più lungo è il caso peggiore dell’algoritmo  
- il percorso più breve è il caso migliore dell’algoritmo

Prendiamo ad esempio, una sequenza ($k_1, k_2, k_3$) questo è il suo albero di decisione
![[Pasted image 20230829131540.png]]
Un albero di altezza $h$ possiede $2^{h}$ foglie.
Essendo l'albero di decisione completo fino all'altezza $h-1$, e avendo $n!$ foglie, si ha che :
$$2^{h-1} \leq n! \leq 2^{h} \rightarrow h-1 \leq \log(n-1) \leq h \rightarrow \log(n!) \rightarrow
$$
$$\log(\sqrt{2\pi n }(\frac{n}{e})^{n})= \log(\sqrt{2\pi}) + \frac{1}{2}\log(n)+n\log(n)+n\log(e)=\Theta(n\log(n))$$
Si ottiene dunque che $\Theta(n\log(n)) \leq h$ ossia che $h=\Omega(n\log(n)$

>[!success] 
>Di conseguenza, un ordinamento per confronti, nel caso peggiore non può fare meno di $n\log(n)$ confronti


