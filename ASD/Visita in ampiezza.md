---
author: Lorenzo Tecchia
tags:
  - definition
  - operation/graph
  - to-do/implementation
---
Dato un [[grafo]] $G = (V,E)$ e un vertice distinto $s$, detto **sorgente**, la ***visita in ampiezza*** ispezione sistematicamente gli archi di $G$ per "scoprire" tutti i vertici che sono raggiungibili da $s$.
[[Calcolo delle distanze|Calcola la distanza]](il numero minimo di archi) da $s$ a ciascun vertice raggiungibile.
Genera anche un [[Tree|albero]] $BF$ con radice $s$ che contiene tutti i vertici raggiungibili.

>[!note] 
> L'[[algoritmo]] opera su grafi orientati e non orientati

Se il grafo è rappresentato con delle [[Grafo rappresentazione#^94590e|liste]], non è possibile esplorarlo in [[ampiezza]] senza una [[coda]]

>[!important] 
> L'algoritmo scopre tutti i vertici che si trovano a distanza $k$ da $s$, prima di scoprire i vertici a distanza $k+1$. 

I nodi del grafo assumeranno, nel corso della visita, tre stati:
- Visitato  
- Scoperto non visitato (coda)
- Non scoperto
Per distinguere questi tre stati, su utilizzerà una ***colorazione del nodo***.
- ![[Pasted image 20230908115020.png|400]]
- ![[Pasted image 20230908115038.png|400]]
- ![[Pasted image 20230908115115.png|400]]
- ![[Pasted image 20230908115143.png|400]]
- ![[Pasted image 20230908115204.png|400]]
- ![[Pasted image 20230908115229.png|400]]


## Implementazione
```C
// da implementare
```
