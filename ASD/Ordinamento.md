---
author: Lorenzo Tecchia
tags: [definition]
---
Il problema dell'ordinamento è tale che:
**Input**: una sequenza di $n$ numeri $a_{1}, a_{2}, \dots, a_{n}$ 
**Output**: una permutazione $a_{1}', a_{2}', \dots, a_{n}'$  della sequenza di input tale che $a_{1}'\leq a_{2}'\leq \dots \leq a_{n}'$

I numeri da ordinare sono anche detti ***chiavi***. Sebbene si stia ordinando una sequenza, l'input di solito si presenta come un'array di interi.

Possiamo formalizzare meglio la definizione di permutazione ordinata nel seguente modo:
- Proprietà della **permutazione** $\rightarrow \exists f : \{1, \dots, n\} \rightarrow \{1, \dots, n\}$ biettiva : $a_{i}=a'_{f(i)}$ con $1 \leq i \leq n$
	- Grazie alla biettività della funzione possiamo essere certi che ogni elemento in $A$ sarà anche in $A^{I}$ e viceversa
	- La condizione: $a_{i} = a'_{f(i)}$ ci dice che ogni elemento di $A$ in posizione $i$ avrà $A^{I}f(i)$
- Proprietà dell'ordinamento $\rightarrow a'_{i} \leq a'_{i+1}$ con $i \leq i+1 \leq n$
Prendendo l'esempio $A = (2,6,2)$ ci sono due funzioni che rispettano le seguenti proprietà:$$f_1:(1,1),(2,3),(3,2) \text { e } f_2:(1,2),(2,3),(3,1)$$
Possiamo dunque. descrivere l'output anche come $A' = (a_{j_{1}}, a_{j_{2}}, \dots, a_{j_{n}})$ con $a_{j_{k}} \in A$ e $a_{k} \in A'$ con $1 \leq k \leq k$ e tale che $j_{k} = f^{-1}(k)$

>[!example]
> $A = 42 \; \land \; A' = 24$ allora $j_{2}= f^{-1}(2)= 1$

>[!tl-dr]
> Dalle definizioni di `input/output` capiamo che il problema è, data una sequenza, una sua permutazione con determinate proprietà

---
### Primo approccio
Sappiamo che il numero di permutazione è finito per insiemi finiti, più precisamente se $|A| = n$ allora il numero di permutazioni è $\prod^{i=1}_{n} i = n!$

Essendo la relazione d'ordine in $\mathbb{Z}$ totale è evidente che tra queste permutazioni ce ne sia almeno una ordinata. Quindi si potrebbero generare tutte le permutazioni ed andarne a prelevare una ordinata.

Questa soluzione è corretta, ma utilizzare un algoritmo di tipo *brute force* è inefficiente $\rightarrow$ dovremmo generare $n!$ permutazioni quindi scrivere $n^{2,20} = \Theta(n^{2,21})$ è un grave errore poiché crescono in maniera differente.

Da questo deduciamo che per qualsiasi algoritmo di *brute force* esiste almeno un input che costringe a esplorare tutti gli elementi dell'insieme prima di arrivare alla soluzione.

Anche supponendo per assurdo che si potrebbe generare una permutazione in tempo costante per verificare che la permutazione sia ordinata dobbiamo controllare tutti gli elementi (tempo lineare). Nel caso peggiore potrebbe generare $n! = \Omega(n^{n})$ permutazioni.

Da questa analisi deduciamo che un algoritmo di questo tipo non è applicabile.

---
### Secondo approccio
Bisogna cercare un algoritmo che da una sequenza ordinata cerchi di passare ad una sequenza un minimo più ordinata fino ad arrivare alla sequenza ordinata, escludendo alcune permutazioni. Tutti gli algoritmi che vedremo saranno $T(n) = \Theta(n^{2})$ proprio grazie a tale approccio.

Un modo per ordinare la sequenza è quello di prendere tutte le coppie e confrontarne a due a due gli elementi. 

>[!example]
> Per $(a_{1}, a_{2,}, a_{3})$ arrivo alla sequenza ordinata tramite i seguenti confronti:$$a_1 \leq a_2\left\{\begin{array}{l}
a_1 \leq a_3\left\{\begin{array}{l}
a_2 \leq a_3 \rightarrow\left(a_1, a_2, a_3\right) \\
a_3<a_2 \rightarrow\left(a_1, a_3, a_2\right)
\end{array}\right. \\
a_3<a_1 \rightarrow\left(a_3, a_1, a_2\right)
\end{array}\right.$$
> Nel peggiore dei casi devo confrontare tutte le coppie della sequenza con un tempo quadratico, o nel caso migliore i confronti impiegheranno $T(n) = O(n)$

>[!important]
> Ne consegue che i nostri algoritmi saranno $n \leq T(n) \leq n^{2}$ e si differenzieranno per le politiche di confronto utilizzate e di come tengono traccia dei confronti fatti.

