---
author: Lorenzo Tecchia
tags:
  - to-do
  - algorithm/sort
---
>[!todo] 
>- [ ] Implementazione in C

>[!tLdr]
> Possiamo veder questo algoritmo come il duale dell'Insertion sort$\rightarrow$ Seleziona una posizione e poi trova l'elemento da inserire all'interno

Sia la posizione che l'elemento vengono ovviamente scelti con condizione di causa

Se iniziamo dall'ultima posizione, ovvero $n$, allora si dovrà trovare il massimo elemento della sequenza e poi scambiarlo con quello in posizione $n$ (se invece si inizia dalla prima allora cercheremo il minimo).

A questo punto si prosegue con la posizione $n-1$ scambiando l'elemento in quella posizione con la sequenza restante (da $1$ a $n-1$) e si procede in questo modo fino alla posizione $2$ (ovviamente l'elemento in posizione $1$ sarà già ordinato per la sequenza $\rightarrow$ è evidente che dopo gli $n-1$ scambi in posizione $1$ sia presente il minimo).

```python
def SelectionSort(A, n):
	for i = n-1 in range(1):
		m = Max(A, i)
		Swap(A, i, n)
```
^SelectionSort

```python
def Max(A, i):
	m = 0
	for j = 1 in range(i):
		if A[m] < A[j]:
			m = j
	return m
```
^Max-SelectionSort

Visto che sappiamo che la scelta del massimo non può essere effettuata con un algoritmo meno che lineare (deve obbligatoriamente controllare tutti gli elementi) sembrerebbe che questa sia la soluzione migliore.
Tuttavia questo è un chiaro esempio di come utilizzare soluzione ottime per sotto-problemi non rende l'algoritmo così definito ***ottimale***.
Questo non implica che l'idea sopra descritta sia pessima $\rightarrow$ Infatti, a seconda di come viene implementata quest algoritmo avrà tempi di esecuzioni molto diversi (Sarà possibile arrivare ad un algoritmo che abbia $T(n) = \Theta(n \log(n)$)
Andiamo quindi a calcolare il tempo di esecuzione del precedente algoritmo:$$
\begin{aligned}
& T_{S S}(n)=\Theta(n)+\sum_{i=2}^n \underbrace{T_{\text {Max }(i)}}_{\Theta(i)}+\Theta(1)=\Theta(n)+\Theta\left(\sum_{i=2}^n i\right)=\Theta(n)+\Theta\left(\left(\sum_{i=1}^n i\right)-1\right) \\
& =\Theta(n)+\Theta\left(\frac{n(n+1)}{2}-1\right)=\Theta\left(n^2\right)
\end{aligned}$$
Si nota facilmente che il problema del nostro algoritmo è nella funzione `Max`$\rightarrow$ Non viene sfruttato il fatto che durante lo scorrimento per la ricerca del massimo vengono eseguiti già dei confronti con alcuni elementi, ma `Max`non ne tiene traccia e li "dimentica" alla successiva iterazione.

Per migliorare il nostro algoritmo si potrebbe pensare di salvare in una struttura dati l'informazione parziale dell'ordinamento degli elementi (durante una ricerca del massimo vengono fatti un numero lineare di confronti che ovviamente non bastano per l'ordinamento totale della sequenza)

Resta quindi da definire una struttura dati che ci permette di mantenere queste informazioni parziali allo stesso modo di come una sequenza sia la giusta struttura per rappresentare una relazione d'ordine totale. Possiamo utilizzare un albero dove gli archi rappresentato la relazione tra gli elementi:
![[Pasted image 20231121120527.png|200]]
Quindi l'albero sopra, con l'arco che rappresenta la relazione di $\geq$, presentava le seguenti informazioni:
- $x \geq y$
- $x \geq z$
- $y \geq k$
- $x \geq k$ (per transitività)
Quindi oltre alle informazioni dirette, abbiamo una relazione tra tutti gli elementi di uno stesso ramo

Dunque organizzando i valori in un albero dove l'arco rappresenterà la relazione di $\geq$ possiamo migliorare il tempo di esecuzione dell'algoritmo `Max` e di conseguenza anche di ***SelectionSort***.

---
## Implementazione in C
```C
```