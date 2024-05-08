---
tags:
  - definition
  - dataStructure
  - graph
---
Ci sono due modi per rappresentare un [[Graph|grafo]] in un computer:
- come una collezione di ***lista d'adiacenza***
- come una ***matrice di adiacenza***

La rappresentazione con liste di adiacenza consiste in un array $Adj$ (adjacent - adiacenti) di $|V|$ liste, una per ogni ogni vertice di $V$ ; per ogni $u\in V$ , la lista $Adj[u]$ contiene tutti i vertici adiacenti a $u$.   ^94590e

Metodo maggiormente utilizzato per i ***grafi sparsi***, ovvero $|E|$ è molto più piccola di $|V|^2$.
[[Grafo esempi#Grafo con liste di adiacenza|Esempio con lista d'adiacenza]]

La rappresentazione con ***matrice di adiacenza*** suppone che i vertici siano numerati (non importa l’ordine).
Consiste in una matrice $|V|\times|V|$ tale che:
$$\begin{align}
a_{i,j} = \begin{cases}
1 \;\;\;\;\;\;&\text{se}\; (i,j) \in E \\
0&\text{altrimenti}
\end{cases}
\end{align}$$
- Quindi $1$ rappresenta l'esistenza di un arco fra il vertice all'indice $i$ e il vertice all'indice $j$
- $0$ la non esistenza
Metodo maggiormente utilizzato per i grafi densi, ovvero $|E|$ è vicina a $|V|^2$ 
[[Grafo esempi#Grafo con matrice di adiacenza|Esempio con matrice d'adiacenza]]

