---
author: Simone Parente, Mario Penna
tags:
  - definition
  - example
---
I diagrammi di Hasse sono rappresentazioni grafiche utilizzate per visualizzare e analizzare relazioni d'ordine in un [[Insieme Ordinato|insieme ordinato]] finito.

---
Sia $(A, \leq)$ un [[Insieme Ordinato|insieme ordinato]] finito:
1. Gli elementi di $A$ si disegnano come punti.
2. Se $(x,y \in A \land x<y)$ il punto $x$ verrà disegnato più **in basso** rispetto al punto $y$.
3. Se $((x<y) \land \; \nexists \; z \in A: (x<z<y))$, allora è possibile unire x e y.
4. I numeri disegnati sullo stesso livello non sono [[Elemento Confrontabile|confrontabili]].
### Esempio
$(D(12), |)$
$A=D(12)=\{1,2,3,4,6,12\}$
$\rho: \forall x,y \in A (x<y \iff x|y)$
![[diagrammaHasse.jpg|200]]
