---
author: Lorenzo Tecchia
tags:
  - definition
  - operation/graph
  - to-do
  - theorem
  - graph
---
Una proprietà della visita in profondità è che i tempi di scoperta e di completamento di un vertice, hanno una struttura a parentesi.

Se rappresentiamo la scoperta di un vertice con una parentesi aperta ”$(v$” e il completamento con una parentesi chiusa ”$v)$”, allora la storia delle scoperte e dei completamenti produce un’espressione in cui le parentesi sono ben annidate.
![[Pasted image 20230910122938.png]]

---
## Dimostrazione
Supponiamo per assurdo che questo sia corretto: $(_{1}v(_{2}w\;\; v)_{1} w)_{2}$ 

Se rappresentassimo l’apertura e la chiusura dei vertici come il $push$ e il $pop$ in uno [[stack]], avremmo uno stack del genere dove prima viene fatto il push di $v$ e poi il $push$ di $w$.

Successivamente viene chiuso $v$, ma per fare il pop di $v$ dallo stack:  
- o questo si trova al top dello stack, ma ciò vuol dire che $v$ è stato scoperto due volte e questo non può accadere  
- o è assurdo dato che devo fare prima il $pop$ di $w$
![[Pasted image 20230910123643.png|250]]
