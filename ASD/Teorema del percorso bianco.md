---
author: Lorenzo Tecchia
tags:
  - theorem
  - definition
  - operation/graph
  - graph
---
$\forall v,w \in V$
Al tempo $d(v)$, ovvero quando $v$ viene scoperto, $w$ è discendente di $v$ se e solo se $w$ può essere raggiunto da $v$ solo da un ***percorso bianco***.
1. $w$ è discendente di $v$, ossia $\exists \pi \in Path(F, v, w)$	
 $$\big\Updownarrow$$
 2. al tempo $d(v), \exists  ∈ Path(G, v, w) : \forall i \in  (0,|\pi|)$ 

#### $\Downarrow)$
- Se $w$ è discendente di $v$, allora quando l'algoritmo si trova al tempo d'inizio visita di $v$, esiste un percorso che va da $v$ a $w$ totalmente **bianco**.
- Se il percorso non fosse **bianco**, $w$ non sarebbe discendente di $v$, questo perché l’algoritmo scende in profondità solo se il nodo in cui dovrà scendere è **bianco**.
### $\Uparrow)$
 - Se quando inizia la visita di $v$ esiste un percorso **bianco** che va da $v$ a $w$, allora $w$ è discendente di $v$.  
 - $w$ è discendente di $v$ ma supponiamo per assurdo che a tempo $d(v)$ il percorso che va da $v$ a $w$ non sia tutto **bianco**.

Dato che $w$ è un discendete di $v$, vuol dire che esiste un suo predecessore $p(w) = z$.  

Questo vuol dire che anche $z$ è un discendente di $v$ .  
Per il [[teorema della struttura a parentesi]], $z$ inizia dopo e termina prima di $v \;\;\; d(v)\;< \;d(z)\;<\;f(z)\;<\;f(v)$

Ma per come è formato l’algoritmo, $z$ non termina se non esplora tutta la sua stella uscente, quindi esplora per forza anche
$w\;\;\; d(v)\; < \;d(z)\; < d(w)\; < \;f(w)\; <\; f(z)\; <\; f(v)$

>[!conclusion]
> Di conseguenza non è possibile che $w$ sia discendente di $v$ senza che ci sia un percorso **bianco** quando inizia $v$

