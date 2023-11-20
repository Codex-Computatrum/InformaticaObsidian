---
author: Lorenzo Tecchia
tags: [example, algorithm]
---
Vogliamo descrivere un algoritmo che accetta come input un intero $n \geq 1$ e produce in output il numero di coppie ordinate $(i,j)$ tali che $i,j \in \mathbb{N}$ e $1 \leq i \leq j \leq \mathbb{N}$
> [!example]
> Input $\rightarrow n = 4$ 
> 	$(1,1), (1,2), (1,3), (1,4),(2,2),(2,3) \dots$
> Output $\rightarrow  10$

Una possibile soluzione potrebbe essere la seguente:
```python
def contaCoppie(N):
	ris = 0
	for i = 1 in range(n):
		for j = 1 in range(n):
			if i <= j:
				ris = ris + 1
	return ris
```

>[!note] La correttezza di questo algoritmo è ovvia, intuitivamente è la soluzione peggiore per poter risolvere il problema, generiamo anche coppie inutili.
> Parliamo, appunto di ***soluzione naive***.

Risulta naturale notare delle imprecisioni nel conteggio delle operazioni elementari in alcune linee (ad esempio alla riga $7$ oltre alla scrittura c’è anche una lettura), ma come sarà evidente, ciò non influisce sull’analisi (si potrebbe provare a rieseguire i seguenti calcoli con altri valori).

L’analisi precedente non basta a descrivere il comportamento dell’algoritmo (alcune linee sono ripetute più volte). Ne consegue che il calcolo totale del contributo di ogni linea sarà il prodotto tra il numero di operazioni elementari e il numero di ripetizioni della linea (ad esempio per la linea $2$ e $7$ il risultato sarà $1 \cdot 1 = 1$).

La riga $3$ si ripete $n + 1 \cdot \left(\sum\limits^{i=1}_{n+1}\right)\text{volte}$
>[!note]
> L'ultimo confronto è quello usato per uscire dal ciclo, quindi il contributo totale della linea è $2\cdot(n+1)$

La riga $4$ invece, $n+1$ volte per ogni volta che si ripete il precedente quindi: $\sum\limits^{i=1}_{n}(\sum\limits^{j=1}_{n+1}1)$. Il totale, quindi sarà $2 \cdot (n+1)$

La riga $5$ si ripete $\sum\limits_{i=1}^{n}\left(\sum\limits_{j=1}^{n+1}1\right)= n^{2}, \text{dunque} 3n^2$

La riga $6$ sicuramente si ripete un numero di volte compreso tra $0$ e $n^2$, quindi il valore della linea di codice è $0 \leq x \leq n^{2}$.

### Soluzione 1 (naive)
Ora non ci resta che analizzare la complessità totale:$$\begin{align}T_1(n) &= 1 + 2(n+1) + 2n(n+1)+3n^{2}+x+1 \\
&= 1 +2n+2+2n^{2}+2n+3n^{2}+x+1 \\ &= 5n^{2}+4n+4+x
\end{align}$$
È importante notare che il valore di $x$ non influisce sul risultato dell'analisi poiché l'espressione sarà sempre del tipo $an^{2}+bn + c$, dunque è una funzione parabolica. Avrà quindi tempo di esecuzione **quadratico** sulla dimensione dell'input.

### Soluzione 2
Visto che una coppia vale come contributo al risultato solo quando il secondo elemento è maggiore del primo è evidente che possiamo migliorare il precedente algoritmo nel seguente modo:
```python
def contaCoppie(n):
	ris = 0
	for i = 1 in range(n):
		for j = i in range(n):
			ris = ris + 1
```

Analizziamo la complessità

| Linea     | Costo unitario | Ripetizioni                                                                                                                                                                                                                                                   | Totale     |
| --------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| $2$ e $6$ | 1              | 1                                                                                                                                                                                                                                                             | 1          |
| $3$       | 2              | $n+1$                                                                                                                                                                                                                                                         | $2(n+1)$   |
| $4$       | 2              | $\begin{align}&\sum\limits_{i=1}^{n}\left(\sum\limits_{j=1}^{n+1}1\right) = \sum\limits_{i=1}^{n}(n-i+2) =\\ &\sum\limits_{i=1}^{n}n- \sum\limits_{i=1}^{n}1+ \sum\limits_{i=1}^{n}2 =n^{2}- \frac{n(n+1)}{2} +n = \\ &\frac{n^2}{2}+\frac{3}{2}n\end{align}$ | $n^{2}+3n$ |
| $5$       | 1              | $\begin{align}&\sum\limits_{i=1}^{n}\left(\sum\limits_{j=1}^{n+1}1\right) = \sum\limits_{i=1}^{n}(n-i+1) = \\ &n^{2} - \frac{n(n+1)}{2} + n = \frac{n^{2}}{2} + \frac{n}{2}\end{align}$                                                                       | $\frac{n(n+1)}{2}$           |

Avremo quindi: $$T_{2}(n) = 1 +2n + 2 + n^{2} + 3n + \frac{n^{2}}{2} + \frac{n}{2} + 1 = \frac{3}{2}n^{2}+ \frac{11}{2}n + 4$$

Come il precedente algoritmo, anche questo algoritmo ha tempo di esecuzione **quadratico**, pertanto possiamo considerarli equivalenti dal punto di vista asintotico.

Ciò però non implica che impieghino lo stesso tempo, ma sul lungo periodo, il loro *peggioramento* la stessa andatura. Visto che dal punto di vista algoritmico non ci sono differenze, non abbiamo apportato nessun reale miglioramento.

### Soluzione 3
Dalle precedenti analisi abbiamo notato che, fissato $i$, eseguiamo l'istruzione di incremento del risultato tante volte quanto il valore totale (che abbiamo calcolato) da aggiungere a `RIS`. Risulta pertanto logico aggiungere direttamente il risultato totale, scrivendo il seguente algoritmo:
```python
def contaCoppie(n):
	ris = 0 # (-> 1)
	for i = 1 in range(n): # (2n + 2)
		ris = ris + (n - i + 1) # (sum from i to n of 5 = 5n)
	return ris # (-> 1)
```
Di conseguenza avremo che:$$T_{3}(n) = 7n + 4$$
Questo tipo di funzione cresce linearmente e quindi è nettamente migliore rispetto ai precedenti algoritmi poiché, per la stessa crescita di $\mathbb{N}$, questa soluzione cresce più lentamente.

### Soluzione 4
Il problema permette di ridurre ulteriormente il tempo di esecuzione.
Infatti sappiamo che per $i=1$, il risultato è $n -1 +1$.
Per $i=1$ il risultato è $n-2+1$ e così via, fino ad arrivare ad $n$ a cui dobbiamo sommare a $1$ ai precedenti risultati. Pertanto:$$RIS = \sum\limits_{i=1}^{n}i = \frac{n(n+1)}{2}$$
Pertanto il nostro algoritmo si riduce a:
```python
def contaCoppie(n):
	ris = (n(n+1)) / 2
	return ris
```
Ne deduciamo che il problema di partenza è risolvibile a tempo costante, più precisamente in $T_{4}(n) = 6$ . Ciò significa che **qualsiasi istanza** è risolta con lo stesso tempo.
Era possibile arrivare a questo soluzione anche geometricamente, infatti le coppie possono essere considerate come le celle di una matrice quadrata.
Le celle totali (ovvero tutte le coppie possibili) sono $\mathbb{N} \times \mathbb{N}$, ma quelle di nostro interesse sono tutte quelle sopra la ***diagonale principale***(diagonale compresa).
Quindi essendo $n$ elementi nella diagonale, sopra si trovano $\frac{n^{2}-n}{2} +n = \frac{n(n+1)}{2}$ elementi.

### Conclusione
![[Pasted image 20231116152637.png]]
#### Notazione asintotica
![[Pasted image 20231116152827.png]]
In simboli: $f(n) = O(g(n))$ pertanto $f$ o cresce di meno o allo stesso modo di $g$ (la si può considerare come la versione più permissiva dell'$o$-piccolo):![[Analisi asintotica#^O-grande]]
Di conseguenza più è piccolo $n_{0}$ più grande dovrà essere la costante $c$, che nel caso del limite superiore asintotico è usualmente compreso in un intervallo tra $0$ e $1$.
