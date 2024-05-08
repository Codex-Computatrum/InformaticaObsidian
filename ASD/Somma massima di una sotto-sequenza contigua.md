---
tags: [algorithm, example]
alias: [max-sub-sequene-sum]
author: Lorenzo Tecchia
---
Descriviamo un [[algoritmo]] che accetta in input una sequenza di numeri di una certa lunghezza $A = (a_{1}, a_{2}, \dots, a_{n})$ dove $\forall i \in \mathbb{N}, \;\; a_{i} \in \mathbb{Z}$ ed un intero $n > 0$ che rappresenta la lunghezza della sequenza

L'output di tale algoritmo è invece un numero $v \in \mathbb{N}$ che rappresenta il [[massimo]] valore tra le somme di tutte le sotto-sequenze contingue di $A$(ads esempio una sotto-sequenza contigua di $a_{1}a_{2}a_{3}a_{4}$ è $a_{2}a_{3}$ oppure $a_{4}$, mentre non è sotto-sequenza contingua $a_{1}a_{2}a_{5}$) . Formalizziamo meglio il problema:
##### Input $\rightarrow$
- Una sequenza $A = (a_{1}, a_{2}, \dots, a_{n})$ con $a_{i} \in \mathbb{Z} \forall i \in \mathbb{N},$
- Un intero $n \geq 1$
- **Esempio**$\rightarrow (2, -4, 8, 3 -5, 4, 6, -7, 2), n = 9$
##### Output $\rightarrow$
- Un intero $V$ tale che $V \;\; \sum\limits_{k=1}^{j}a_{k}$ dove $1 \leq i \leq j \leq n$ e $V$ è il più grande possibile
- Tutti gli elementi nella sommatoria devono essere contigui nella sequenza dell'input
- **L'output del precedente esempio** $\rightarrow \;\; 8 +3 -5+4+6 = 16$ 
---
### Soluzione 1 (naive)
Un primo approccio potrebbe essere quello di trovare la somma di tute le sotto-sequenze e restituire la maggiore.

Sappiamo che il numero di sotto-sequenze è finito per sequenze continue. Inoltre, tutte le sotto-sequenze contigue non vuote sono [[corrispondenza]] biunivoca con la propria vista per il `CONTACOPPIE`, ne consegue che il numero di sotto-sequenze contigue, compresa quella vuota è pari a $\frac{n(n+1)}{2} + 1$.

Abbiamo quindi decomposto il problema in:
- Generare tutte le sotto-sequenze
- Sommare tutti gli elementi di una sotto-sequenza

Si noti che poiché il valore di una sotto-sequenza vuota è $0$, possiamo dire con certezza che $V \geq 0$ per qualsiasi sotto-sequenza.

Un possibile algoritmo è il seguente:

```python
def maxSUM(A, n):
	V = 0
	for i = 1 in range(n):
		for j = in range(n):
		# questo è l'unico blocco di codice che differisce dalla soluzione 2 svolta per il contaCoppie
		sum = 0
		for k = i in range(j):
			sum = sum + A[k]
		if sum > V:
			V = sum
	return V
```
^MaxSum1

Ci si aspetta che questo algoritmo abbia almeno un $\Theta(n^{2})$ vista la similitudine con la soluzione $2$ di `contaCoppie`. 
>[!note]
> Più precisamente se il blocco in analisi risulta essere costante allora $T(n) = \Theta(n^{2})$

Possiamo sfruttare pertanto il fatto che il blocco viene eseguito tante volto quanti $i$ e $j$ generati, ovvero $\frac{n(n+1)}{2}$ volte, per semplificare l'analisi dell'algoritmo(anche se andrebbe svolta nella sua totalità) andando a studiare le linee di codice da $5$ a $9$.

La linea $5$ ha un costo di $1$ e viene eseguita un numero di volte pari a:$$
\underbrace{\sum_{i=1}^N \sum_{j=1}^N 1}_{\text {primo e secondo for }}=\sum_{i=1}^N(N-i+1)=\frac{N(N+1)}{2}$$
In maniera analoga, le linee $8$ e $9$ hanno un contributo totale di circa $4 \frac{n(n+1)}{2}$

Per le linee $6$ e $7$ basta notare che una volta fissato $i$ e $j$ la differenza tra la testa del *for* ed il corpo è $1$
>[!note] In pratica
> Il ciclo *for* viene eseguito una volta in più del corpo dovendo eseguire la condizione di uscita

Tale differenza avviene ogni volta che genero una coppia $(i, j) \rightarrow$ la linea $6$ viene eseguita, alla fine dell'algoritmo, $\frac{n(n+1)}{2}$ volte in più della linea $7$.

La precedente intuizione ci permette di semplificare ulteriormente l'analisi, infatti, essendo già nell'ordine del quadratico tale differenza non comporta differenze dal punto di vista asintotico.
Possiamo pertanto analizzare la linea $7$(che ha contributo singolo di $4$) e viene eseguita il seguente numero di volte.
$$
\begin{aligned}
& \sum_{i=1}^N \sum_{j=1}^N \sum_{k=1}^N 1=\sum_{i=1}^N \sum_{j=1}^N(j-i+1)=\sum_{i=1}^N \underbrace{\left(\sum_{j=1}^N j-\sum_{j=1}^N 1+\sum_{j=1}^N\right)} \\
& \sum_{j=i}^N j=\sum_{j=1}^N j-\sum_{j=1}^{i-1} j=\frac{N(N+1)}{2}-\frac{(i-1) i}{2} \\
& \sum_{j=i}^N i=i \sum_{j=i}^N 1=i(N-i+1) \\
& \sum_{j=i} 1=N-i+1 \\
& \sum_{i=1}^N(\overbrace{\frac{N(N+1)}{2}-\frac{(i-1) i}{2}}^{\sum_{j=1}^N}-\overbrace{i(N-i+1)}^{\sum_{j=1}^N i} \overbrace{N-i+1}^N \sum_{j=1}^N 1)= \\
& \sum_{i=1}^N \frac{N(N+1)}{2}-\sum_{i=1}^N \frac{i^2}{2}+\sum_{i=1}^N \frac{i}{2}-\sum_{i=1}^N i N+\sum_{i=1}^N i^2-\sum_{i=1} N i+\sum_{i=1}^N(N-i+1)= \\
& \frac{N^2(N+1)}{2}-\frac{1}{2} \cdot \frac{N(N+1)(2 N+1)}{6}+\frac{1}{2} \frac{N(N+1)}{2}-\frac{N^2(N+1)}{2}+\frac{N(N+1)(2 N+1)}{6}-\frac{N(N+1)}{2}+ \\
& \frac{N(N-1)}{2} \\
& =\frac{1}{2}\left(\frac{N^3}{3}+\frac{N^2}{2}+\frac{N}{6}\right)-\frac{1}{2}\left(\frac{N^2}{2}+\frac{N}{2}\right)+\frac{N^2}{2}-\frac{N}{2}=\frac{1}{6} N^3+\frac{1}{2} N^2-\frac{2}{3} N \\
&
\end{aligned}$$ 
Ciò conclude la nostra analisi $\rightarrow$ L'algoritmo descritto ha tempo di esecuzione $T(n) = \Theta(n^{3})$

---
### Soluzione 2
Un notevole miglioramento al precedente algoritmo può essere fatto notando che molti calcoli vengono ripetuti (sprecando tempo). Il problema è legato al calcolo di una sotto-sequenza data(l'ultimo *for* della soluzione precedente).
Infatti possiamo osservare che:$$\sum_{k=1}^j A[k]=\sum_{k=1} j-1 A[k]+A[j]$$
Ma $\sum\limits_{k=1}^{j-1}A[k]$ è la quantità gia presente in `SUM` ed è quindi già stata calcolata. Pertanto:$$\sum_{k=i}^{j-1} S U M+A[k]$$
È evidente che una linea di questo tipo ha contributo costante (ne traiamo vantaggio dalle iterazioni precedenti)

La suddetta osservazione non può essere utilizzata così come è $\rightarrow$ Bisogna comprendere quando azzerare `SUM` e sotto quali condizioni si può sfruttare il 
precedente algoritmo

Fintanto che l'indice resta `i` resta sempre lo stesso si vuole aggiornare il precedente valore di `SUM`, mentre quando varia allora `SUM` va azzerato poiché ci si trova in una nuova sotto-sequenza.

Questa idea può essere formalizzata nel seguente algoritmo:

```python
def maxSum(A, n):
	V = 0 # (Teta di 1)
	for i = 1 in range(n):
		 sum = 0 # La riga 3 e. 4 hanno contributo Theta(n)
		 for j = 1 in range(n):
			 sum = sum + A[i]
			 if sum > V:
				 V = sum # Le righe 5-8 hanno contributo Theta(n^2)
	return V # (Theta di 1) 
```
^MaxSum2

Questo algoritmo impiega tempo $T(n) = \Theta(n^{2})$ ed è quindi un miglioramento significativo dal punto di vista asintotico della soluzione $1$

---
### Soluzione 3
Dal precedente algoritmo si può dire che sia ottimale per il calcolo della somma di ogni sotto-sequenza contigua; infatti non è possibile crearne uno migliore se si vuole calcolare il valore di tutte le sotto-sequenze poiché, il numero di sotto-sequenze in una sequenza è di per sé quadratico.

Tuttavia il nostro algoritmo non richiede il calcolo di tutti i valori (è stata una nostra scelta questo approccio $\rightarrow$ l'algoritmo ottimale di un problema non è detto che sia ottimale per un altro problema).
Si noti infatti che è inutile valutare tutte le sotto-sequenze e di conseguenza non è necessario esplorare del tutto la nostra istanza attraverso un algoritmo di brute force, che quasi mai sono esaustivi.
>[!note]
> Per **brute force** s'intende un algoritmo che offre una soluzione esaustiva $\rightarrow$ Sonda tutti gli elementi possibili per quella istanza (nel nostro caso tutte le sotto-sequenze)

Attraverso l'analisi della nostra sequenza possiamo arrivare alla seguente intuizione:
Assumiamo che $\mathbb{SUM}(i, j -1) \geq 0$ e ciò significa che tutte le sotto-sequenze che vanno da $i$ a $j -1$ sono non negative $\rightarrow \mathbb{SUM}(i, k) \geq 0 \forall k \;:\; i \leq kj$
>[!note]
> $\mathbb{S U M}(i, k) \Longleftrightarrow \sum\limits_{k=i}^{j-1} a_k$

![[Pasted image 20231117130347.png]]

A questo punto è evidente che sommando anche il valore presente nella cella $j\;\;|(a_{j})$ si avrà o un risultato non ancora negativo oppure un risultato positivo.
#### Prima proprietà
$$\mathbb{S U M}(i, j) \geq 0 \Longrightarrow \mathbb{S U M}(r, l) \leq \mathbb{S U M}(i, l) \forall i \leq r \leq l \leq j$$
![[Pasted image 20231117130641.png]]
Ovvero, nessuna sotto-sequenza di una sequenza non negativa può essere migliore di quella partenza. Infatti:$$\underbrace{\sum_{k=1}^j a_k}_{\geq 0}=\underbrace{\sum_{k=1}^{r-1} a_k}_{\geq 0}+\sum_{k=r}^j a_k \Longrightarrow \sum_{k=r}^j a_k=\underbrace{\sum_{k=1}^j a_k}_{\geq 0}-\underbrace{\sum_{k=1}^{r-1} a_k}_{\geq 0} \Longrightarrow \sum_{k=r}^j a_k \leq \sum_{k=i}^j a_k$$
Da questa proprietà capiamo che possiamo ignorare tutte le sotto-sequenze di una sequenza non negativa.
#### Seconda proprietà
$\mathbb{SUM}(i, j) \leq 0 \rightarrow \mathbb{SUM}(r, l) < \mathbb{SUM}(j+1, l) \;\; \forall i \leq r \leq j \;\land \; \forall j +1 \leq l \leq n$. Quindi se da $i$ a $j - 1$ tutte le sotto-sequenze sono $\geq 0$ ma la sequenza da $i$ a $j$ è negativa significa che qualunque sotto-sequenza che parte da $r \leq j$ ed arriva a $l > j$ è sicuramente minore della sequenza che va da $j$ ad $l$.
![[Pasted image 20231117131144.png]]
Infatti:$$\sum_{k=j+1}^l a_k=\sum_{k=i}^l a_k-\underbrace{\sum_{k=i}^j a_k} \Longrightarrow \sum_{k=j+1}^l a_k>\sum_{k=i}^l a_k$$
Quindi la proprietà $2$ oltre a dirci di dover conservare la sequenza da $i$ a $j-1$ ci consente anche di ignorare altre sotto-sequenze.

Dopo queste analisi è abbastanza intuitivo che il codice seguente avrà complessità lineare poiché muoverò sempre in avanti:
1. Se $\mathbb{SUM}(i, j) \geq 0$ allora è lo stesso $i$ e incremento $j$
2. Se $\mathbb{SUM}(i, k) < 0$ allora parto direttamente da $j + 1$ e vado avanti

Dunque, i salti sono giustificati dalla proprietà $2$ e il fatto di non dover esaminare le sequenze intermedie della proprietà $1$. Ma allora l'algoritmo finale sarà il seguente:

```python
def maxSUM(A, n):
	V = 0 # (i = 1)
	j = 1 # (j = 1)
	sum = 0
	while j <= 0:
		sum = sum + A[j]
		# (caso 2 (V > sum))
		if sum <= 0:
			# (i = j + 1)
			sum = 0
		else if sum > V:
			V = sum
		j = j +1
	return sum
```
^MaxSum3

Si noti che tutte le soluzioni di questo problema possono essere adattate affinché memorizzi anche gli indici per cui la sotto-sequenza è quella massima; infatti, basta salvare gli indici di quando vado ad aggiornare $V$.

Risulta che questo algoritmo abbia $T(n) = \Theta(n)$, è ottimale poiché supponendo di avere un input con valori positivi, è evidente che `maxSum` è la somma di tutti i positivi, devo scorrere la sequenza sia per controllare che siano positivi, sia per calcolarne la somma.