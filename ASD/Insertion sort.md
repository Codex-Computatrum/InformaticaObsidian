---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Insertion-Sort è un [[algoritmo]]  di [[ordinamento]] abbastanza efficiente per l'ordinamento di array di piccole dimensioni.
L'idea dell'algoritmo è quella di dividere la sequenza in una parte ordinata e una no.

All'inizio possiamo supporre che la sequenza ordinata sia composta solo dal primo elemento, ed il resto degli elementi contengono la sequenza disordinata.
Insertion-Sort prende il primo elemento della parte disordinata (nel nostro caso $j$) e lo inserisce nella giusta posizione nella parte disordinata.

Quindi se $a_{j-1} \leq a_{j}$ allora mantiene la stessa posizione. In caso contrario $a_{j-1}$ andrà in posizione $j$ e dovrà confrontare $a_{j}$ con $a_{j-2}$; anche in questo caso se $a_{j-2} \leq a_{j}$ andrà nella posizione precedentemente liberata ($j-1$), altrimenti è $a_{j-2}$ a spostarsi nella posizione $j-1$

![[Pasted image 20231120160145.png|400]]

Ripetendo questo processo posso arrivare a confrontare $a_{j}$ con $a_1$:
- Se $a_{1}\leq a_j$ posizionerò $a_{j}$nella posizione $2$ (che sarà libera);
- In caso contrario andrà in posizione $1$ ed $a_{1}$ in posizione $2$ (questi spostamenti hanno ovviamente un costo loro).

###### Algoritmo Ricorsivo

```python
def InsertionSort(A, n):
	if n > 1:
		InsertionSort(A, n-1)
		Insert(A, n-1)
```
^InsertionSortRecursive

###### Algoritmo Iterativo

```python
def InsertionSort(A, n):
	for i = 1 in range(n-1):
		Insert(A, i)
```
^InsertionSort-Iterative

```python
def Insert(A, i):
	x = A[i]
	j = i - 1
	while (j >= 0 and A[j] > x):
		A[j+1] = A[j]
		j--
	A[j+1] = x
```
^Insert

A prescindere dalla condizione di terminazione del ciclo `while`(riga $6$), la riga $9$ è sempre la stessa infatti:
![[Pasted image 20231120160415.png]]

---
## Analisi
Studiamo solo il ciclo `while` in quanto unico a determinare il comportamento asintotico dell'algoritmo.

Questo ciclo può essere diverso per istanze con stessa dimensione a causa del confronto $\text{elem} \geq A[i]$ (questo è il motivo della preferenza del ciclo for)

Ne consegue che no possiamo associare un valore a $T(n)$ poiché non è detto che abbia lo stesso tempo di ogni istanza di $n$ elementi.

>[!example]-
> Per $(4,3,2,1)$ non verrà mai eseguito il corpo del ciclo, mentre per $(3,4,2,1)$ le istruzioni nel corpo saranno eseguire $6$ volte.

Questa irregolarità costringe a fare i seguenti ragionamenti:
- Se l'algoritmo è sfortunato possiamo dire che $T(n) = O(T_{max}(n))$ che rappresenta il tempo di esecuzione dell'algoritmo per i casi peggiori (quelli che fanno il massimo numero di operazioni)
- Se è molto fortunato, analogamente risulterà $T(n) = \Omega(T_{min}(n))$
- Se risulterà $T_{max}(n) = \Theta(T_{min}(n))$ è evidente che $T(n)$ avrà anch'esso lo stesso ordine, altrimenti dovrò analizzare il caso medio

Prima di analizzare in maniera esaustiva il ciclo `while`, vediamo la complessità delle altre linee. 
Per quanto riguarda il ciclo `while` bisogna innanzitutto, notare di come ci sono delle sequenze diverse che si comportano allo stesso modo; ovvero, tutte le sequenze che hanno la stessa relazione per ogni elemento in posizione $i-$esimo.$$(1, 3, 2, 4), (10, 25, 17, 60), (7, 29, 12, 30)\dots$$
Abbiamo quindi tante classi di equivalenza quante permutazioni di una sequenza $\rightarrow$ Ne consegue che per lo studio del ciclo `while` bisogna formalizzare la suddetta dipendenza.

È chiaro che l'input ha impatto solo sul numero di esecuzione del `while`(le linee analizzate precedentemente mantengono lo stesso costo)

Fissato il $j$ il `while` viene ripetuto un tot di volte partendo da $0$ e, per $j \neq$ il numero di volte che viene ripetuto il blocco é diversi.

Possiamo introdurre una serie di parametri $t_{j}$ che indicano il numero di volte che la tesa del `while` viene eseguita all'iterazione $j-$esima del `for`; quest ultimo, variando da $2$ a $n$ avremo $t_{2},t_{3}, \dots, t_{n}$ parametri.

Se $t_{j}$ è il numero di volte che viene eseguita la testa del while, è evidente che per tutte le iterazioni la testa verrà eseguita $\sum\limits_{j=2}^{n}t_{j}$ volte (tale sommatoria non ha una forma chiusa), mentre $\sum\limits_{j=2}^{n}(t_{j}-1)$ volte il corpo.

Dunque, possiamo rappresentare il temo di esecuzione la seguente espressione:$$\begin{gathered}
T(N)=2 N+2(N-1)+2(N-1)+4 \sum_{j=2}^N t_j+3 \sum_{j=2}^N\left(t_j-1\right)+\sum_{j=2}^N\left(t_j-1\right)+3(N-1) \\
=4 \sum_{j=2}^N t_j+4 \sum_{j=2}^N\left(t_j-1\right)+9 N-7
\end{gathered}$$
---
### Caso peggiore
Se la seconda condizione del `while` è sempre verificata è chiaro che $i=0$(poiché all'inizio $i=j-1$) si verifica dopo $j$ iterazioni (uscendo quindi dal `while`)
Pertanto non è possibile eseguire più di $j$ iterazioni (questo corrisponde al nostro caso peggiore).
Bisogna ora verificare che esista un input tale per cui $\forall j,\; t_{j}=j$. 
Questo input esiste ed è la ***sequenza decrescente***:$$
\begin{aligned}
& T_{\max }(N)=9 N-7+4 \sum_{j=2}^N(j-1)=9 N-7+4\left(\sum_{j=1}^N j=1\right)+4 \sum_{j=1}^{N-1}(j-1)= \\
& =9 N-7+4\left(\sum_{j=1}^{N-1} j-1+N\right)+4 \sum_{j=1}^{N-1}(j-1)=9 N-7-4+4 N+8 \sum_{j=1}^{N-1} j-4 \sum_{j=1}^{N-1} 1= \\
& =13 N-11+8\left(\frac{(N-1)(N-1+1)}{2}\right)-4(N-1)=9 N-7+4 N(N-1)= \\
& =4 N^2+5 N-7=\Theta\left(N^2\right)
\end{aligned}$$
---
### Caso migliore
Con sequenze ordinate accade che $\forall j\;:\;2 \leq j \leq n$ risulta che $t_{j} = 1$.
>[!example]-
> Per $(3,7,8,10)$ la seconda condizione del `while` risulterà falsa per ciascun $j \rightarrow$ ci saranno quindi $4$ esecuzioni:$$
T_{\min }(N)=9 N-7+4 \sum_{j=2}^N 1+4 \sum_{j=2}^N 0=9 N-7+4(N-1)=13 N-11=\Theta(N)$$ 

---
### Caso medio
Ora resta capire con quanta frequenza avvenga il caso migliore e il caso peggiore, poiché non è in genere detto che il comportamento dell'algoritmo sia quadratico (per ora sappiamo che ci sono degli input che impiegano tempo quadratico e degli input che sono lineari).

Lo studio del caso medio in questo algoritmo è piuttosto semplice; infatti, per $j$ fissato il valore atteso di $t_{j}$ è, assumendo equiprobabilità, esattamente la media aritmetica, ovvero:$$t_j=\frac{1+2+\ldots+j}{j}=\frac{\sum_{k=1}^j k}{j}=\frac{1}{j} \cdot \frac{j(j+1)}{2}=\frac{j+1}{2}$$
Ma allora:$$
\begin{aligned}
& T_{\text {med }}(N)=9 N-7+4 \sum_{j=2}^N \frac{j+1}{2}+4 \sum_{j=2}^N\left(\frac{j+1}{2}-1\right)=9 N-7+2 \sum_{j=2}^N(j+1)+2 \sum_{j=2}^N(j-1) \\
& =9 N-7+2 \sum_{j=2}^N j+2 \sum_{j=2}^N 1+2 \sum_{j=2}^N j-\sum_{j=2}^N 1=9 N-7+4 \sum_{j=1}^{N-1} j-4+4 N= \\
& =13 N-11+4 \frac{N(N-1)}{2}=2 N^2-2 N-11=\Theta N^2
\end{aligned}$$
>[!Conclusion]
>Visto che il caso dominante è quello peggiore, possiamo assumere che l'algoritmo di ***Insertion sort è un algoritmo che tempo di esecuzione quasi sempre quadratico***

---
## Implementazione in C
```C
// da implementare
```