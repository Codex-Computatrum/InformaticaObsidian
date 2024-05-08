---
author: Lorenzo Tecchia
tags:
  - definition
---
Un [[Tree|albero]] di decisione è un [[Albero binario#^albero-binario-completo|albero binario completo]] (tutti i nodi hanno entrambi i figli) che rappresenta i confronti fra gli elementi di un array.

L’[[ordinamento]], in un’albero di decisione, consiste nel tracciare un [[Path|percorso]] a partire dalla radice fino ad una foglia; ogni nodo attraversato rappresenta un confronto e la foglia contiene la sequenza ordinata.

---
Un [[algoritmo]] di ordinamento per confronti, dev’essere in grado di generare tutte le $n!$ permutazioni dell’array in input, dato che solo una di questa sarà la sequenza ordinata. 

Di conseguenza, l’albero di decisione avrà $n!$([[Fattoriale|fattoriale]]) foglie, dato che ogni foglia rappresenta la sequenza ordinata in base alla sequenza in input.

La lunghezza di un percorso è paragonabile al tempo di esecuzione dell’algoritmo d’ordinamento: 
- il percorso più lungo è il caso peggiore dell’algoritmo  
- il percorso più breve è il caso migliore dell’algoritmo

Prendiamo ad esempio, una sequenza ($k_1, k_2, k_3$) questo è il suo albero di decisione
![[Pasted image 20230829131540.png]]
Un albero di [[altezza]] $h$ possiede $2^{h}$ foglie.
Essendo l'albero di decisione completo fino all'altezza $h-1$, e avendo $n!$ foglie, si ha che :
$$2^{h-1} \leq n! \leq 2^{h} \rightarrow h-1 \leq \log(n-1) \leq h \rightarrow \log(n!) \rightarrow
$$
$$\log(\sqrt{2\pi n }(\frac{n}{e})^{n})= \log(\sqrt{2\pi}) + \frac{1}{2}\log(n)+n\log(n)+n\log(e)=\Theta(n\log(n))$$
Si ottiene dunque che $\Theta(n\log(n)) \leq h$ ossia che $h=\Omega(n\log(n))$

>[!success] 
>Di conseguenza, un ordinamento per confronti, nel caso peggiore non può fare meno di $n\log(n)$ confronti

### Dimostrazione del teorema sull'ordinamento 
Fissato $n$ ho un numero finito di alberi di decisione, quindi il nostro scopo sarà vedere tra tutti gli alberi quello con altezza minima, in modo da trovare il numero minimo di confronti che un algoritmo che fa nel caso peggiore (analizziamo il tempo di esecuzione del miglior caso peggiore).

Qualunque sia l'albero $T_{n}$, esso avrà $n!$ foglie disposte su un'altezza $h$, ma visto che sappiamo che in un albero binario il numero di foglie è al massimo $2^{h}$ posso scrivere $n! \leq 2^{h} \Longrightarrow h \geq \log(n!)$
Ne consegue che l'altezza di un albero di decisione non può essere meno di $\log(n!)$. Ciò si traduce in:$$
n !=\prod_{i=1}^n i \Longrightarrow \log (n !)=\log \left(\prod_{i=1}^n i\right) \stackrel{\log (a \cdot b)=\log a+\log (b)}{=} \log (n !)=\sum_{i=1}^n \log i \leq h$$
Essendo interessati ad una stima di questa sommatoria, proviamo a maggiorarla. Cerchiamo quindi qualcosa di più piccolo in modo da poter avere $h \geq \sum\limits_{i=1}^{n}\log(i) \geq ( )$. Sappiamo che:$$
\sum_{i=1}^n \log i \leq \sum_{i=1}^n \log n=n \log n \Longrightarrow \sum_{i=1}^n \log i=O(n \log n)$$
(non molto utile $\rightarrow$ il nostro scopo è garantire che $h$ abbia un [[limite inferiore]] asintotico).
$$
\sum_{i=1}^n \log i \geq \underbrace{\sum_{i=\left\lceil\frac{n}{2}\right\rceil}^n \log i}_{\begin{array}{c}
\text { sommo meno } \\
\text { valori }
\end{array}} \geq \underbrace{\sum_{i=\left\lceil\frac{n}{2}\right\rceil}^n \log \frac{n}{2}}_{\begin{array}{c}
\text { sommo sempre } \\
\text { il più piccolo }
\end{array}}=\log \frac{n}{2} \cdot \sum_{i=\left\lceil\frac{n}{2}\right\rceil}^n \log 1=\frac{n}{2} \log \frac{n}{2}=\Theta(n \log n)$$
In questo modo abbiamo raggiunto l'obiettivo, infatti:$$
\frac{n}{2} \log \frac{n}{2} \leq \sum_{i=1}^n \log i \leq n \log n \Longrightarrow h \geq \Theta(n \log n)$$
Abbiamo dimostrato quindi che per il caso peggiore un algoritmo di ordinamento, dovendo per forza di cosa fare tanti confronti quanto la lunghezza del percorso più lungo del suo albero di decisione, non può essere meglio di $\Theta(n \log n)$

#### Dimostrazione per il caso medio
Il caso medio risulta più complesso $\rightarrow$ Per poter calcolare il tempo di esecuzione dovremo fare una media aritmetica tra la lunghezza del percorso esterno (somma dei percorsi della radice e ciascuna foglia) e il numero delle foglie dell'albero.
>[!example]-
> $T_{M}(n) = \frac{LPE}{\# \text{foglie}}$
> Calcoliamo la $LPE$ da sinistra a destra: $$T_{M}(3) = \frac{3+2+3+3+3+3}{3!} = \frac{17}{6}$$
> ![[Pasted image 20231122151405.png|300]]

Analogamente al caso peggiore, bisogna studiare il miglior caso medio e cercare tutti gli alberi che minimizzino il percorso esterno (per minimizzare quel rapporto o minimizziamo il numeratore o il denominatore; non possiamo modificare il numero di foglie).
Dimostriamo quindi che gli alberi che minimizzano la lunghezza del percorso esterno corrispondono all'albero completo
![[Pasted image 20231122151549.png]]
Andiamo a calcolare entrambi i percorsi esterni mettendoli in relazione.
Sia la lunghezza del percorso completo pari a $k$ e andiamo a calcolare il percorso dell'albero non completo in funzione di $k$ sapendo che $h$ sia l'altezza dell'albero completo:$$\mathrm{LPE}=k-2 h+h-1-h+2(h+1)=k+1$$
Il percorso esterno peggiore all'allontanarsi della completezza.

Ora, visto che si tratta di un albero completo sappiamo che le foglie sono ad altezza $h$ o ad altezza $h-1$. Sia $N_{h}$ il numero di foglie ad altezza $h$ e $N_{h-1}$ il numero di foglie ad altezza $h-1$.È evidente che il numero totale di foglie sarà $N_{h}+N_{h-1} = n!$, mentre$$\mathrm{LPE}=h \cdot N_h+(h-1) N_{h-1}$$
Sappiamo anche che per un albero binario pieno il numero di foglie sono $2^{h}$, che in relazione alle foglie del nostro albero risulta $2N_{h-1} + N_{h}= 2^{h}$
>[!note]
> Ogni foglia ad altezza $h-1$ avrà due figli

A questo punto avremo:$$
\left\{\begin{array} { l l } 
{ N _ { h } + N _ { h - 1 } } & { = n ! } \\
{ 2 N _ { h - 1 } + N _ { h } } & { = 2 ^ { h } }
\end{array} \Longrightarrow \left\{\begin{array}{ll}
N_h & =2 n !-2^h \\
N_{h-1} & =2^h-n !
\end{array}\right.\right.$$
Calcoliamo quindi il tempo medio:$$
\begin{aligned}
T_M(n) & =\frac{L P E}{n !}=\text { frach } \cdot N_h+(h-1) N_h-1 n !=\frac{2 h n-h 2^h+h 2^h-h n !-2^h+n !}{n !}= \\
& =\frac{h n !-2^h+n !}{n !}=h-\frac{2^h}{n !}+1 \stackrel{h \log !}{\Longrightarrow} T_M(n)=\log n !-\frac{2^{\log n !}}{n !}+1=\log n !
\end{aligned}$$

>[!important]
> Abbiamo dimostrato che $\log n! = \Theta(n \log n)$ e quindi abbiamo concluso che il tempo di esecuzione di un algoritmo d'ordinamento per una sequenza arbitraria di input $n$ non possa essere, nel caso medio e peggiore, migliore di $\Theta(n \log(n))$