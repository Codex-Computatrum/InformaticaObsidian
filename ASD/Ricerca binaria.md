---
tags: [algorithm/search, basics]
author: Lorenzo Tecchia
---
Se un [[array]] non è ordinato per fare la ricerca di un elemento bisogna per forza scorrere al più tutti gli elementi; se però l'array è ordinato la soluzione al problema cambia.

`Rircera(S, k)`$\rightarrow$ Vado a dividere la sequenza in due, quindi $\lfloor \frac{n}{2} \rfloor$

- Se $S[q] = k$, allora ho trovato l'elemento e restituisco l'indice
- Se $S[q] < k$, allora significa che nel caso $k$ fosse presente all'interno della struttura si troverebbe certamente a destra della sequenza, visto che per ogni elemento $x$ della sequenza a sinistra vale la seguente proprietà $\rightarrow x \leq S[q] < k$. Il nuovo $q$ sarà $\lfloor \frac{q+1+n}{2} \rfloor$ avendo già escluso $q$
- Se $S[q] > k$, allora cercherò nella sottosequenza di sinistra

Mi fermerò in due casi:
- Ho trovato l'elemento
- Mi trovo in una sequenza di un elemento (in questo caso se la cella non contiene l'elemento allora $k \in S$)

Ne consegue che la ricerca di un elemento in una sequenza si riduce alla ricerca dello stesso in una sottosequenza di grandezza dimezzata; più precisamente, dopo la prima operazione sarò in una sequenza di dimensione $\frac{n}{2}$, dopo la seconda in una dimensione $\frac{n}{2^{2}}$, dopo la terza in una di $\frac{n}{2^{3}}$, e così via.

Dopo $i$ operazioni avrò una sequenza di grandezza $\frac{n}{2^{i}}$, raggiungerò quindi la soluzione quando dopo $i$ operazioni avrò una sequenza di un elemento, quindi $\frac{n}{2^{i}} = 1 \Longrightarrow i = \log(n)$

Avere una sequenza ordinata permette, come appena visto, di ottenere un algoritmo di ricerca in tempo logaritmico; più precisamente `Ricerca(S, k)` sarà un $O(\log(n))$, mentre per una sequenza non ordinata $O(n)$

Andiamo ad implementare l'algoritmo nel seguente modo:
- `RicercaBinaria(S, p, r, k)` che restituisce l'indice dove dovrebbe trovarsi $k$ e implementerà il ragionamento visto precedentemente ($p$ e $r$ sono gli indici di inizio e fine sequenza);
- `Ricerca(S, k)`, che restituisce l'indice giusto se $k \in S$ altrimenti un valore non valido.

```python
def RicercaBinaria(S, p, r, k):
	if p < r:
		q = (p + r) / 2
		if k == S[q]:
			ret = q
		else if k < S[q]:
			ret = RicercaBinaria(S, p, q + 1, k)
		else:
			ret = RicercaBinaria(S, q + 1, r, k)
	else:
		ret = p
	return ret
```
^BinarySearch

1.  Restituiamo $p$ poiché $r$ non è detto che appartenga all'array essendo che $q + 1$ potrebbe essere un indice al di fuori delle sequenza infatti $p \leq q < r \Longrightarrow q + 1 \leq r$ (dopo $i$ operazioni potrebbe esserci la chiamata `RicercaBinaria(S, n, n + 1, k)` che restituirebbe $n + 1$); quindi con $p$ sono sicuro di non andare mai in *segmentation fault*.

```python
def Ricerca(S, k):
	i = RicercaBinaria(S, 1, n, k)
	if S[i] == k:
		ret = i
	else:
		ret = -1
	return ret
```
^General-Search

Tutto quello di cui abbiamo discusso finora ci dice che il problema della ricerca è risolvibile in un tempo **esponenzialmente** minore di lineare (ovvero logaritmico). Ma array ordinati hanno anche argomenti a sfavore poiché operazioni di inserimenti e/o cancellazione sono lineari, anche se in realtà ad essere problematico non è il vincolo dell'orientamento ma il fatto di avere una struttura sequenziale.