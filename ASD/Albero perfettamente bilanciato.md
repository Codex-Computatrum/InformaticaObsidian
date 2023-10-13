---
author: Lorenzo Tecchia
tags:
  - definition
  - to-do
  - dataStructure/abr
---
>[!note] 
>APB: Albero Perfettamente Bilanciato oppure PBT: Perfect Balanced Tree

Un [[Tree|albero]] è **perfettamente bilanciato** quando il numero dei nodi del sotto-albero sinistro differisce al più di $1$ dal numero dei nodi del sotto-albero destro.

>[!important] 
>Un'albero $T$ è **perfettamente bilanciato** se $\forall x \in T, \lvert \lvert T_{x.sx} \rvert-\lvert T_{x.dx}\rvert \rvert \leq 1$ 
> 

Un **PBT** è l'albero più basso possibile, con altezza al più $\lfloor \log_{2}(n)\rfloor$ 
![[Pasted image 20230831114946.png]]
Con l’aggiunta di un nodo bisogna riposizionare i nodi affinchè l’albero rimanga perfettamente bilanciato.

In generale conviene usare i **PBT** se gli algoritmi che utilizzeremo lo scorrono in altezza $\log(n)$; come detto prima, un **PBT** è l’albero più basso possibile.

Esistono diversi tipi di PBT, uno di questi sono gli **[[Albero binario autobilanciante|AVL]]**

---

>[!todo] 
>- [ ] Implementazione in C

