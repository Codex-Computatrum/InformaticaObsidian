---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
***Heap sort*** è un [[algoritmo]] di [[ordinamento]].
>[!todo] 
>- [ ] Implementazione in C

```python
def HeapSort(A, n):
	BuildHeap(A,n)
	for i = n-1 in range(1): 
		Swap(A, 0, i)   # il max sta in A[0] perchè è un heap
		Heapify(A, i, 0)
```
^HeapSort

```python
def BuildHeap(A, n):
	for i = (n/2)-1 in range (0)
		Heapify(A, n, i)
```
^BuildHeap

```python
def Heapify(A, n, i):
	# Definiamo il figli della radice
	max = i
	l = 2i + 1
	r = 2i + 2
	if l < n && A[i] < A[l]:
	   max = l
	if r < n && A[max] < A[r]:
	   max = r
	if max != i:
		Swap(A, max, i)
		Heapify(A, n, max)
```
^Heapify

Un [[Ricerca binaria]] è già rappresentato in memoria come un [[Tree|albero]] quindi è possibile passare da una [[Struttura dati|struttura]] all'altra.

---
- Come prima cosa viene eseguito _BuildHeap_, che trasforma la sequenza in input in [[Proprietà Heap#^fd5f61|max-heap]]. 
- _BuildHeap_ esegue la funzione _Heapify_ a partire dall'indice $i=\frac{n}{2} -1$, ovvero l'indice dell'ultimo nodo non foglia.
- A questo punto avrò all'indice $0$ il massimo della sequenza(garantito dalla proprietà di max-heap e ovviamente da quella di [[Proprietà Heap|heap]]).
- Quindi scambio l'elemento all'indice $0$ con quello a indice $i$, questo perché l'indice $i$ sta scorrendo al contrario. 
- L'elemento appena scambiato ora si troverà nella posizione corretta, quindi viene "scollegato" dall'albero. L'indice $i$ scorre al contrario quindi al ciclo successivo (con $i-1$) quell'elemento non verrà più considerato.
Ora però non si possiede più la proprietà di max-heap, di conseguenza si esegue la funzione _Heapify_ che riparerà il danno creato dalla funzione _Swap_.
---
## [[Analisi asintotica|Analisi]]
#### Funzione Heapify
- La funzione _Heapify_ rende "heap" l'albero di dimensione $n$ a partire dalle radici $i$. 
- I primi due $if$, controllano quale dei due figli è maggiore della radice.
- Nella variabile $max$ verrà inserito l'indice del figlio di sx o di dx a seconda del caso. 
- Se nessuno dei due figli è più grande della radice, allora $max=i$ di conseguenza il terzo $if$ non viene eseguito.
- Altrimenti viene chiamato lo swap fra la radice e il figlio più grande.
- Viene poi chiamato nuovamente _Heapify_ per rendere "heap" anche i figli.

Ad esempio, nel BuildHeap si rende heap prima il sotto albero che ha come radice l’ultimo nodo **non** foglia, poi il penultimo e cosi via risalendo l’albero; così da creare un max-heap.

Essendo Heapify ricorsiva, prima rende heap un albero, successivamente rende heap i figli (nel caso non fossero foglie), poi i figli dei figli e così via fino ad arrivare alle foglie.

Se i figli non sono heap, una volta resi heap dalla chiamata ricorsiva, non ci sarebbero problemi con il padre data la proprietà di heap (ovvero il padre è ordinato rispetto ai figli). 
>[!important]
> reso il padre un heap, il problema viene passato ai figli, e una volta resi heap i figli, il problema poi non viene passato al padre.

Una volta trasformata la sequenza in un max-heap, all’interno del for della funzione _HeapSort_, viene eseguito lo _Swap_ tra l’elemento massimo (che si trova all’indice $0$ perché è un max-heap) e l’elemento all’indice $i$ (indice che sta scorrendo al contrario).

Così facendo si sposta il massimo alla fine del vettore, però c’è bisogno di eseguire _Heapify_ perché all’indice $0$ è stato inserito un valore potenzialmente scorretto; quindi bisogna rendere nuovamente_ max-heap_ l’intero albero ma escludendo di volta in volta gli elementi posizionati correttamente.

Viene chiamata _Heapify_ con il parametro $n=i$, ovvero l’altezza dell’albero meno uno (quindi si escludono gli elementi posizionati correttamente).

Invece il parametro $i$ (ovvero la radice dalla quale partire per costruire un heap) sarà sempre $0$ perché si deve ricostruire l’intero albero.

>[! Complessità Heapify]
>Data la ricorsività, Heapify scorre l’albero in altezza, ovvero $log(n)$. Il resto delle operazioni sono eseguite a tempo costante, quindi in totale il costo di Heapify è $\Theta(log(n))$

La chiamata viene fatta su un albero di dimensione i a partire dalla radice di indice $0$

Quindi scorre l’intero albero in altezza ad ogni chiamata, ovvero $log(i)$
_Heapify_ viene chiamata $n − 1$ volte nel for:
$$\sum^{n-1}_{i=1}\log(i)= \log{(\prod^{n-1}_{i}i)}= \log((n-1)!)$$ applichiamo l'[approssimazione di stirling](https://it.wikipedia.org/wiki/Approssimazione_di_Stirling)
$$=\log(\sqrt{2\pi n }(\frac{n}{e})^{n})= \log(\sqrt{2\pi}(\sqrt{n})(\frac{n^{n}}{e^{n}}))= \log(\sqrt{2\pi}) + \frac{1}{2}\log(n)+n\log(n)- n\log(e)$$
#### Funzione BuildHeap
Il costo di Heapify ad ogni iterazione nel for è di $\frac{n}{2^{i+1}} \cdot i$, avrò quindi:
$$
\sum_{i=1}^k\left[\frac{n}{2^{i+1}} \cdot i\right]=\sum_{i=1}^k\left[\frac{n}{2^{i-1} 2^2} \cdot i\right]=\frac{n}{4}\sum_{i=1}^k\left[i \cdot \frac{1}{2^{i-1}}\right]=\frac{n}{4} \sum_{i=1}^k\left[i \cdot\left(\frac{1}{2}\right)^{i-1}\right]=\frac{n}{4} \sum_{i=1}^k\left[i \cdot x^{i-1}\right]_{x=\frac{1}{2}}$$

Possiamo riscrivere $i \cdot x^{i-1}$ come la derivata di $x^i \quad \frac{d}{d x} x^i=i \cdot x^{i-1}$
$=\left[\frac{n}{4} \sum_{i=1}^k \frac{d}{d x} x^i\right]_{x=\frac{1}{2}}=\left[\frac{n}{4} \frac{d}{d x} \sum_{i=1}^k x^i\right]_{x=\frac{1}{2}} \quad$ approssimo alla serie geometrica
$=\left[\frac{n}{4} \frac{d}{d x} \sum_{i=1}^{\infty} x^i\right]_{x=\frac{1}{2}}=\left[\frac{n}{4} \frac{d}{d x} \frac{1}{1-x}\right]_{x=\frac{1}{2}}=\left[\frac{n}{4} \frac{1}{(1-x)^2}\right]_{x=\frac{1}{2}}=\frac{n}{4} \cdot 4=n$

>[!Importante] 
>Il costo dell’intero algoritmo sarà quindi $O(n \log(n))$

---
## Implementazione in C
```C
// da implementare
```
