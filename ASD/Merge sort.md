---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

[[Algoritmo]] basato su confronto che utilizza un processo di risoluzione ricorsivo, sfruttando la tecnica del [[Dividi et impera]].

![[Pasted image 20231120211540.png|500]]
>[!note]
> La sequenza di un elemento sarà il nostro caso base per l'algoritmo ricorsivo.

Prendendo in considerazione una sequenza vuota come caso base otterremmo un loop con sequenze di un elemento (una sequenza di un elemento può essere divisa solo in una sequenza vuota ed un'altra sequenza da un elemento, quest'ultima dovrà nuovamente essere divisa). 

>[!important]
> Bisogna fare attenzione che l'algoritmo ricorsivo termini per il caso base scelto come nel nostro caso

Con caso base $1$ risulta che $\forall n \geq 2$ si ha $1 \leq |\frac{n}{2}| \land 1 \leq n - | \frac{n}{2}|$ con $n=1$ abbiamo una sequenza ordinata.
Definiamo per tanto in questo modo il nostro algoritmo:

```python 
def algorithmMergeSort(A, n):
	MergeSort(A, 0, n-1)
```
^Algorithm-MergeSort

```python
def MergeSort(A, p, r):
	if p < r:
		q = ((p + r) / 2)
		MergeSort(A, p, q)
		MergeSort(A, q + 1, r)
		Merge(A, p, q, r)
```
^MergeSort

Tramite il concetto di [[dividi et impera]] le due chiamate ricorsive, dividono la sequenza a metà.

### Correttezza dell'algoritmo
La sequenza iniziale ha $r-p+1$ elementi. Affinché il nostro algoritmo funzioni, dobbiamo garantire che:$$r-p+1>q-p+1 \wedge r-p+1>\underbrace{r-q}_{r-(q+1)+1}$$
Dove $q = | \frac{p+r}{2}|$. Sappiamo che $| \frac{p+r}{2}| \leq \frac{p+r}{2}$, pertanto risulta:$$
r-p+1>\frac{p+r}{2}-p+1 \Longrightarrow 2 r>p+r \Longrightarrow r>p$$
Essendo la nostra ipotesi proprio $p < r$ (condizione dell'`if`) abbiamo dimostrato la prima implicazione. Analogamente procede la seconda:$$
r-p+1>r-\frac{p+r}{2} \Longrightarrow-p>-\left(\frac{p+r}{2}+1\right) \Longrightarrow 2 p<p+r+2 \Longrightarrow p<r+2$$
Resta da dimostrare che, per qualsiasi input, l'algoritmo faccia un numero finito di chiamate ricorsive e che quindi, prima o poi, raggiungerà il caso base; quando `r` è molto vicino a `p`(ovvero quando $r < p +1$) è evidente che sarà $q = | \frac{p+r}{2}| = p$ e quindi entrambe le chiamate ricorsive non verranno effettuate (la condizione dell'`if` sarà dalla prima chiamata $p < p$ e alla seconda $p + 1 < r$, condizioni entrambe false).
### Occupazione in memoria

```python
def Merge(A, p, q, r):
	k = p # Indice che scorre la posizione di B
	i = p
	j = q + 1
	while i <= q && j <= r:
		if A[i] <= A[j]:
			B[k] = A[i]
			i = i + 1
		else:
			B[k] = A[j]
			j = j + 1 
	if i < q:
		j = i
# Restano da copiare gli elementi della sequenza sinistra
# In caso contrario non modifico j visto che l'indice è già corretto
	while k <= r:
		B[k] = A[j]
		j = j + 1
		k = k + 1
# A questo punto andrebbero copiati gli elementi di B nuovamente in A
```
^Merge

Il tempo di **Merge** è lineare poiché vado ad effettuare almeno $n$ scritture in memoria. È interessante notare che è stato necessario utilizzare un altro vettore $\rightarrow$ Questo significa che **MergeSort** ha bisogno di uno spazio aggiuntivo in memoria anch'esso lineare (un vettore pari all'input del programma oltre alle variabili locali) a causa dell'algoritmo **Merge**.

Anche senza considerare **Merge** l'algoritmo MergeSort ha bisogno di uno spazio aggiuntivo a causa delle chiamate ricorsive $\rightarrow$ Per ogni chiamata ricorsiva, prima di chiamare alla chiamata figlia, è necessario salvare i dati sullo stack di attivazione.

### Tempo di esecuzione
Sarebbe assurdo dover calcolare il valore del tempo di esecuzione della funzione se per farlo devo conoscere il tempo di esecuzione della funzione stessa.

Ma visto che la funzione è definita in modo induttivo, è possibile calcolarla su input più piccoli, dunque, è possibile sfruttare la definizione induttiva e definire in maniera induttiva anche la funzione tempo.

Con buona approssimazione avremo che:$$
T_{M S}(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ \Theta(1)+T_{M S}\left(\frac{n}{2}\right)+T_{M S}\left(\frac{n}{2}\right)+T_{M e r g e}(n) & \text { altrimenti }\end{cases}$$
Ma $T_{Merge}(n) = \Theta(n)$ e $\Theta(1)$ è assimilato dal $\Theta(n)$, pertanto l'equazione di ricorrenza da risolvere sarà:$$
T_{M S}(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ 2 T_{M S}\left(\frac{n}{2}\right)+T_{M e r g e}(n) & \text { altrimenti }\end{cases}$$
Da cui ricaviamo l'albero di ricorrenza:
![[Pasted image 20231120221046.png]]

Quindi il nodo del livello $0$ contribuisce per un $Theta(n)$, ciascun nodo del livello $1$ produce un $\Theta(n)$ poiché fa $\frac{n}{2}$ operazioni
>[!note]
> Da non confondere con il numero di elementi, infatti il nostro $Theta(n)$ deriva dal contributo $2T_{MS}\left(\frac{n}{2}\right)+ \Theta(n)$

Analogamente si comportano tutti i livelli (fatta eccezione per l'ultimo)$\rightarrow$ In pratica tutti i libelli hanno contributo lineare eccetto quello della foglia.

Ogni nodo foglia contribuisce per un $\Theta(1)$, tuttavia per conoscere il contributo totale del livello devo prima conoscere il numero di foglie presenti, in modo da poter calcolare il tempo di esecuzione con la seguente equazione:$$
T_{M S}(n)=\Theta(1) \cdot \# \text { foglie }+\sum_{i=0}^{\# \text { livelli interni }} \Theta(n)$$
- **Numero di livelli interni**$\rightarrow$ Dalla composizione dell'albero (è un albero binario completo) possiamo dire che ad un livello $i$ ogni nodo prende in input $\frac{n}{2^{i}}$; ciò significa che alle foglie avrò $1 = \frac{n}{2^{i}} \Longrightarrow 2^{i} = n \Longrightarrow \log(n) = \log(2^{i}) \Longrightarrow i = \log(n)$(il numero di livelli interni è $\log(n) - 1$)
- **Numero di foglie**$\rightarrow$ Sappiamo che le foglie sono a profondità $\log(n)$; sappiamo inoltre che un livello $i$ ha $2^{i}$ nodi; pertanto il numero delle foglie è $2^{\log(n)} = n$

$$
T_{M S}(n)=\Theta(1) \cdot n+\sum_{i=0}^{\log n-} \Theta(n)=\Theta(n)+\Theta(n) \sum_{i=0}^{\log n-} 1=\Theta(n)+\Theta(n)(\log n-1)=\Theta(n \log n)$$

#### Analisi
![[appuntiIngenito.pdf#page=15]]

---
## Implementazione in C
```C
// da implementare
```
