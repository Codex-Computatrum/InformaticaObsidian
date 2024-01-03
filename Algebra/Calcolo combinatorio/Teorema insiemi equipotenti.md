---
author: Simone Parente
tags:
  - algebra/combinatoria
  - notReviewed
---
Siano $A$ e $B$ insiemi finiti [[Insiemi equipotenti|equipotenti]], allora $\forall f:A \to B$ vale:
1. $f$ è [[iniettività|iniettiva]]
2. $f$ è [[suriettività|suriettiva]]
3. $f$ è [[biettività|biettiva]]
Le tre proposizioni sono equivalenti.
### Dimostrazioni
#### Dimostrazione 1. $\implies$ 3.
Se per ipotesi so che $f$ è iniettiva e che $|A|=|B|$, per il [[Teorema sull'insieme delle applicazioni da A in B|teorema precedente]] è già dimostrata l'implicazione.
#### Dimostrazione 3. $\implies$ 2. e $3. \implies 1.$
È ovvio per definizione di biettività.
#### Dimostrazione $2. \implies 1.$
Per ipotesi $f$ è suriettiva $\implies$ $f$ ha una [[Sezione e retrazione|sezione]] $g:B \to A$ che è per definizione iniettiva, ma avendo dimostrato che $1. \implies 3.$, so che $g$ è biettiva. Allora $f$ è una [[Sezione e retrazione|retrazione]] dell'applicazione biettiva $g$, e l'unica retrazione di una funzione biettiva è la sua funzione inversa, che è a sua volta biettiva, ciò dimostra che $f$ è iniettiva.

### Osservazioni
Diremo quindi che $A$ e $B$ sono [[Insiemi equipotenti|equipotenti]] se e solo se esiste una applicazione biettiva $A \to B$, di conseguenza $|A|=|B|$.
Si dice che $|A|\leq|B|$ se e solo se esiste un'applicazione iniettiva $A \to B$.
Si dice invece che $|A| < |B|$ se e solo se esiste un'applicazione iniettiva $A \to B$ ma non esistono applicazioni biettive.
Risulta quindi:
$\forall A,B,C \text{ insiemi}$ 
- $|A|=|A| \xrightarrow{poiché} id_A \text{ è biettiva}$
- $|A|=|B| \implies |B|=|A| \xrightarrow{poiché} f \text{ biettiva } \implies f^{-1} \text{ biettiva}$
- $(|A|=|B|) \land (|B|=|C|) \implies |A|=|C| \xrightarrow{poiché} f \text{ e } g \text{ biettive } \implies g \circ f \text{ biettiva}$ 
- $A \subseteq B \implies |A| \leq |B| \xrightarrow{poiché} \text{ l'immersione è iniettiva}$
- $|A| = |B| \implies |A| \leq |B| \xrightarrow{poiché} \text{ biettiva}\implies \text{iniettiva per definizione}$
- $(|A| \leq |B|) \land (|B| \leq |C|) \implies |A| \leq |C|) \xrightarrow{poiché} f \text{ e } g \text{ iniettive } \implies g \circ f \text{ iniettiva}$