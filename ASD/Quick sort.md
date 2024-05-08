---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Quick sort è un [[algoritmo]] di [[ordinamento]] che impiega, nel caso peggiore, $\Theta(n^2)$.
Mediamente però, impiega $\Theta(n\log(n))$ con costanti moltiplicative molto basse.

Nel quick sort, il [[dividi et impera]] agisce in questo modo:
- **Dividi**: 
	- partiziona l'array $A[p \dots r ]$ in due sotto-array $A[p\dots q-1]$ e $A[q\dots r]$ in modo tale che che $A[p \dots q-1]\leq A[q]\leq A[q+1\dots r]$
	- Ogni elemento del primo sotto-array è minore o uguale di $A[q]$ che a sua volta è minore o uguale di tutti gli elementi del secondo sotto-array.
	- I due sotto-array saranno disordinati, ma intanto si ha la proprietà  che gli elementi del primo sono minori o uguali agli elementi del secondo.
- **Impera**: si chiama ricorsivamente QuickSort
- **Combina**: non occorre ordinare i due sotto-array essendo già ordinati tra di loro
Mentre il MergeSort ha una decomposizione in sottoproblemi semplici a discapito della fusione che è più complessa, l'algoritmo di QuickSort decide di impiegare più tempo nella decomposizione così da semplificare di molto la fusione.

Infatti il QuickSort decomporrà la sequenza in una maniera tale che alla fine si avranno le seguenti sequenza:
![[Pasted image 20231121121701.png]]
Con $a_{1} \leq a_{i+1}$, e quindi poiché entrambe le sottosequenze sono già ordinate e l'ultimo elemento della prima sequenza sia $\leq$ al primo elemento della seconda, la funzione dei $2$ è già ordinata 
Il metodo utilizzato da QuickSort non riesce però a garantire che le $2$ sottosequenze contengano più o meno lo stesso numero di elementi e ciò va ad impattare sul tempo di esecuzione.
Qualsiasi livello di [[ricorsione]] avrà da una parte una sequenza di $q$ elementi e dall'altro $n-q$ con tutti gli elementi della sottosequenza sinistra minori o uguali a quelli dell'altra sottosequenza.

```python
def algorithmQuickSort(A, n):
	QuickSort(A, 0, n-1)
```
^Algorithm-QuickSort

```python
def QuickSort(A, p, r):
	if p < r:
	# Il punto in cui divide la sequenza è più complicato da calcolare
	# Partiziona si occuperà di restituire l'indice che dividerà la 
	# sequenza e farà in modo che tutti gli elementi della partizione
	# da --p-- a --q-- siano minori o uguali di quelli da --q+1-- a
	# --r--
		q = Partition(A, p, r)
		QuickSort(A, p, q)
		QuickSort(A, q + 1, r)
```
^QuickSort

Dopo le chiamate ricorsive non c'è bisogno di fare altro poiché questo algoritmo garantisce per transitività l'ordinamento totale della sequenza.

Se `Partition`, si comporta come descritto, **QuickSort** è corretto sotto le seguenti assunzioni:
>[!important]
> - La partizione da $p$ a $q$  è strettamente minore in dimensione della sequenza da $p$ a $r$
> - La partizione da $q$ a $r$ è strettamente minore della sequenza da $p$ a $r$
> - Al termine di `Partition(A, p, r)` vale che:$$
\forall i: p \leq i \leq q \wedge \forall j: q+1 \leq j \leq r, A[i] \leq A[j]$$
>> [!note]
>> qualunque elemento prendo a sinistra, esso è minore o uguale di qualunque elemento che prendo a destra

Ed è chiaro che queste proprietà siano fondamentali sia per il ragionamento di ipotesi induttiva (le prime due priorità) e sia per il fatto di non dover fare nessun merge alla fine (l'ultima)

>[!important]
> Vediamo di dimostrare che le prime due assunzioni, che possono essere rappresentate da un'unica equazione matematica:$$p \leq q < r$$
> Infatti se questo è il caso è evidente che $$r-p+1 < q-p+1 \;\land\;r-p+1<r-q+1$$
> La precedenti proprietà se non fosse soddisfatte distruggerebbero l'algoritmo.
> Supponiamo che $q = p-1$, avremmo una chiamata ricorsiva(`QuickSort(A, p, p - 1)`) ovvero un'istanza di $0$ elementi.
> 	Questa chiamata terminerebbe senza aver effettuato nulla (caso base), ma ciò comporta che la seconda chiamata, ovvero (`QuickSort(A, p + 1 -1, r)`, avrà tutti gli elementi della chiamata di partenza con la conseguenza che la suddetta chiamata si ripeterà in infinito e l'algoritmo non terminerà
> Caso analogo per $q = r\rightarrow$`QuickSort(A,p,r)` sarà la chiamata che manderà in loop e l'algoritmo `QuickSort(A, r+1, r)` la sequenza vuota.
> Quindi `Partition` deve garantire $2$ proprietà:
> 1. $p \leq q < r$ (per il motivo descritto precedentemente)
> 2. $\forall i : p \leq i \leq q \;\land\; \forall j: q +1 \leq j \leq r, A[i] \leq A[j]$(Scontato, in quanto non è che sia ha la certezza che la sequenza totale sia già ordinata)

## Partition
Quando viene chiamato `Partition`si ha la certezza che $p < r$, dunque possiamo scegliere un elemento $x \in A$, (detto anche **pivot**), metteremo nella parte sinistra tutti gli elementi minori od uguali di $x$, mentre a sinistra quelli maggiori o uguali
>[!note]
>Le condizioni di uguaglianza sono necessarie sia a destra che a sinistra per garantire che nessuna delle due sottosequenze sia vuota (altrimenti andremo in contro al loop precedentemente descritto). Se ad esempio avessi per la sequenza di sinistra la condizione di strettamente minore, potrebbe capitare di scegliere come **pivot** il minimo della sequenza e quindi nessun elemento verrebbe spostato a sinistra.

In linea di principio $x$ potrebbe essere scelto a piacimento, ma per come descriveremo l'algoritmo è necessario che venga spostato alla prima posizione.
Dunque per semplicità prenderemo direttamente il primo elemento della sequenza.

Per scorrere la sequenza avrò due indici, $i$ che partirà da sinistra  e $j$ che partirà da destra. Il primo indice $i$ si sposterà a destra fintanto che troverà un valore $y \geq x$ (i valori minori sono già nella posizione giusta), mentre $j$ verrà decrementato fino a quando non sarà su un valore $z \leq  x$ (quel valore dovrà andare nella sottosequenza di sinistra). Una volta che si sono fermati entrambi gli indici e $i < j$ scambierà i valori e ripeterà il processo fino a quando gli indici si incroceranno $i \geq j$.

![[Pasted image 20231121150437.png]]

Nello scrivere l'algoritmo utilizzeremo il ciclo `REPEAT ... UNTIL`(condizione), questo ripeterà il blocco interno (fa almeno una iterazione) fino a quando la condizione non è verificata

```python
def Partition(A, p, r):
	x = A[p]
	i = p - 1
	j = r + 1
	repeat
		repeat
			j--
		until(A[j] <= x)
		repeat
			i++
		until (A[i] >= x)
		if i < j:
			Swap(A, i, j)
	until (j <= i)
	return j
```
^Partition

### Correttezza
Per confermare la correttezza di questo algoritmo si veda se all'instante in cui viene eseguita la linea $15$ si ha $p \leq j < r$ poiché questo ci assicurerà la validità della prima proprietà necessaria per la correttezza di `QuickSort`, ovvero $p \leq j < r$

A tal proposito, dobbiamo dimostrare che i casi $j < p$ e $j \geq r$ siano impossibili; per fare ciò basta controllare che non si verificano i casi $j=p-1$ (essendo $i=p-1$ è l'unico $j<p$ che potrebbe verificarsi vista la scrittura del nostro algoritmo) e $j = r$(anche se $h=r+1$ all'inizio, viene per forza decrementato una volta).

#### Caso $j=r \rightarrow$
Sappiamo che $j$ viene decrementato almeno una volta e non riceve mai incrementi. Affinché sia $j=r$ significa che siamo al **primo** ciclo di iterazione del `REPEAT`esterno; bisogna quindi dimostrare che $i$ non arrivi mai ad $r$, poiché è l'unico modo che ha per uscire dal ciclo con $j=r$. Visto che siamo alla prima iterazione allora $i=p-1$ e al primo incremento di $i$ non abbiamo ancora fatto scambi. Dunque $x$ (il pivot). è ancora in prima posizione, ma allora al primo incremento di $i$ esco subito dal ciclo essendo $i=p$ e $A[i] = x$. A questo punto $i < j$ e quindi eseguo la riga $13$ (non si è ancora verificata la condizione di $i \geq j$). Ne consegue che devo fare almeno un'altra iterazione del blocco con la conseguenza che $j < r$.
#### Caso $j=p-1 \rightarrow$
Per dimostrare che questo caso non si verifichi basta garantire che il primo `REPEAT` interno ($6-8$) non si ripeta all'infinito visto che $p<r$(vero perché altrimenti non sarebbe eseguito lo stesso `Partition`) garantisce che $j$ si trovi tra $p$ ed $r$. Visto che non abbiamo modo di garantire di essere alla prima iterazione non è detto che $x$ sia ancora nella prima posizione della sequenza poiché potrebbero esserci degli scambi, ma se questi sono avvenuti significa che certamente che in $A[p]$ ci sia un valore minore o uguale a $x$. Ciò garantisce che $j$ si fermerà sicuramente in $p$ (ragionamento astratto, infatti se ci sono stati degli scambi allora $i >p$ e quindi $j$ si fermerà sicuramente prima di arrivare a $p$ essendo la condizione di uscita $i \geq j$; ovvero si esce dal ciclo quando gli indici si incrociano). Visto che la variabile $i$ può essere solo incrementata è evidente che non potrà essere minore di $p$ ma allora ciò significa che se $j$ arriva a $p$ in quella stessa iterazione la condizione $i \geq j$ sarà verificata e l'algoritmo terminerà con un valore $j\geq p$.

L'algoritmo `Partition` garantisce che alla sua terminazione, quando gli indici si incontrano, siano verificate le seguenti proprietà:$$
\forall z: p \leq z \leq j, A[z] \leq x \text { e } \forall t: j+1 \leq t \leq r, A[t] \geq x$$
Queste possono essere unite:$$
\forall z, t: p \leq z \leq j<t \leq r, A[z] \leq x \leq A[t]$$
Che rappresenta la seconda proprietà che volevamo garantire:$$
\forall i: p \leq i \leq q \wedge j: q+1 \leq j \leq r, A[i] \leq A[j]$$
>[!note]
> È facile osservare che se richiedessi il $<$ invece del $\leq$ (analogamente $>$ al posto di $\geq$) non riuscirei più a garantire la prima proprietà che deve verificarsi al termine di `Partiziona` per la correttezza di ***QuickSort***

## [[Analisi asintotica|Analisi]]
Per il `QuickSort` non bastano le tecniche viste sinora poiché non è facile sapere quante volte le istruzioni di `Partition` vengano eseguite; in particolare per i `REPEAT UNTIL` interni posso solo dire che la somma delle loro iterazioni sia $n +1$ o $n+2$ (visto che l'algoritmo termina o con i $i=j$ se l'input è dispari o $i=j+1$ se l'input è pari) essendo l'unica condizione di uscita $i\geq j$ (quindi contributo lineare)

Il corpo dell'`if`al massimo viene eseguito per $\frac{n}{2}$ volte e dunque $T_{P}(n) = \Theta(n) + O(n) = \Theta(n)$(Paragonandolo a MergeSort abbiamo praticamente spostato il contributo lineare di Merge all'inizio dell'algoritmo).

A causa di partiziona non sappiamo come viene diviso l'input tra le $2$ chiamate poiché dipende da come viene scelto il pivot e dall'istanza di input. Posso fare i seguenti ragionamenti:
- Se tutti gli elementi sono uguali avrò una divisione della sequenza in due parti quasi uguali e questo verrà per ogni chiamata ricorsiva
![[Pasted image 20231121170718.png]]
- Se invece ho una sequenza ordinata, verrà suddivisa in una partizione da un solo elemento (quella di sinistra) e l'altra con i restanti elementi
![[Pasted image 20231121170819.png]]

Questi due casi sono stati già studiati in precedenza. Se $q = \lfloor \frac{n}{2} \rfloor$, ma allora avremo $T_{QS}(n) = \Theta(n \log(n))$. Essendo:$$
T_{Q S}(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ T_{Q S}\left(\frac{n}{2}\right)+T_{Q S}\left(\frac{n}{2}\right)+\Theta(n) & \text { se } n>1\end{cases}$$
Esattamente come MergeSort, mentre per le sequenze ordinate si ha:$$
T_{Q S}(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ \underbrace{T_{Q S}(1)}_{\Theta(1)}+T_{Q S}(n-1)+\Theta(n) & \text { se } n>1\end{cases}$$
Quindi $T_{QS}(n) = \Theta(n^{2})$(simile all'esempio sul [[fattoriale]]). Più precisamente per le sequenze ordinate avremo un albero degenere dove un livello $i-$esimo (eccetto l'ultimo che è costante) ha un contributo di $n-1$; dunque:$$
\sum_{i=0}^{n-1}(n-1)=n+(n-1)+(n-2)+\ldots+\underbrace{(n-(n-1))}_1=\sum_{i=1}^n i=\frac{n(n+1)}{2}=\Theta\left(n^2\right)$$
Stranamente QuickSort si comporta nel modo peggiore per sequenze dove tecnicamente non ci sarebbe nessuna operazione da effettuare.

Si fa presente che a seconda del tipo di sequenza di dimensione $n$ l'albero di ricorrenza potrebbe essere molto diverso. Il nostro scopo è capire che tipo di forma potrebbero avere gli alberi generati dalla equazione di ricorrenza:$$
T_S(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ T_{Q S}(q)+T_{Q S}(n-q)+\Theta(n) & \text { se } n>1\end{cases}$$
Ovviamente $1 \leq q \leq n-1$ altrimenti l'algoritmo non potrebbe terminare (i casi di $q = 0$ e $q = n$ sono già stati discussi); da questo ricaviamo che tutti i nodi hanno grado $2$ poiché non trovandoci in un caso base l'algoritmo fa esattamente due chiamate ricorsive.

Visto che i casi base si hanno con sottosequenze di un elemento è evidente che ci saranno tante foglie quanti sono gli elementi della sequenza di input.

Questo ci permette di dimostrare che se il numero di foglie $n_{f}$ è $k$ allora tutti i nodi interni $n_{i}$ sono $k-1$.
Dimostriamo per induzione sull'altezza dell'albero che vale $n_{f} = n_{i}+1$
- Per $h=0$ avremo l'lavero composto dalla sola radice e quindi $\underbrace{1}_{n_f}=\underbrace{0}_{n_i}+1$
- Per $h=i > 0$, la radice avrà grado $2$ e quindi sia il sottoalbero destro che sinistro saranno non vuoti con altezza $h < i$ e dunque $n_{f_{sx}} = n_{i_{sx}} +1$ e $n_{f_{dx}} = n_{i_{dx}} +1$, mentre il numero totale delle foglie dell'albero sarà semplicemente $n_{f} = n_{f_{sx}} + n_{f_{dx}}$ in quanto una foglia non può appartenere ad entrambi i sottoalberi. 

![[Pasted image 20231121174644.png|300]]
Il numero di nodi interni nell'albero radicato in $x$ sarà evidentemente $n_{i}= n_{i_{sx}} + n_{i_{dx}} + 1$(la radice).

Mettendo insieme i precedenti ragionamenti, risulta:$$n_f=\underbrace{n_{i_{s x}}}_{n_{f s x}}+1+\underbrace{n_{i_{d x}}}_{n_{f d x}}+1=\underbrace{n_{i_{s x}}+n_{i_{d x}}+1}_{n_i}+1$$

> [!important] ### Caso medio
> Prendiamo l'albero di ricorrenza del caso peggiore e andiamo a calcolare il contributo di ogni livello:
>![[Pasted image 20231121175339.png|250]]
> Da questa rappresentazione ricaviamo che il contributo di un livello $l \geq 1$ è $n-l +1$ di conseguenza:$$T(n)=\underbrace{n}_{l=0}+\sum_{l=1}^n(n-l+1)=\Theta\left(n^2\right)$$

>[!note] ### Caso migliore
> ![[Pasted image 20231121175535.png|250]]
> Quindi $T(n) = \sum\limits_{l=0}^{h}n$ con $h$ altezza di un albero completo e quindi pari a $\log(n)$ ne consegue:$$T(n)=\sum_{l=0}^{\log n} n=\Theta(n \log n)$$
#### Analisi
È facile notare che per qualsiasi albero costruisca ogni livello sarà contributo lineare poiché sia quelli del caso migliore che del caso peggiore sono lineari e tutti gli alberi sono ovviamente nel mezzo.

Il tempo di esecuzione dipende quindi dall'altezza e non potendo sommare più un numero lineare di libelli (essendo l'altezza dell'albero peggiore $n$) il caso peggiore è ovviamente $\Theta(n^{2})$ mentre il migliore (parliamo dell'albero con altezza minima) è un $\Theta(n log(n))$.
Allo stato attuale non possiamo nemmeno affermare che questo algoritmo sia migliore di `InsertionSort`, il quale aveva un caso migliore addirittura lineare. Bisogna dunque calcolare la media tra caso migliore e peggiore, ma non possiamo farlo semplicemente con una media aritmetica tra come in `InsertionSort`.

Decomponiamo il problema sapendo che ad ogni livello di ricorsione l'algoritmo si occupa di scegliere, tramite `Partition`, su una certa istanza il valore di $q$ e quindi ogni nodo sceglie localmente un valore di $q$; fissato quest ultimo verranno generati i due sottoproblemi con dimensione $q$ e $n-q$.

#### Calcolo del tempo medio
Calcoliamo adesso il tempo medio di tutte le istanze in cui `Partition` fa la stessa scelta.

Dividiamo quindi il problema in classi di equivalenza $\rightarrow$ Ogni istanza di dimensione $n$ che partiziona la sequenza nello stesso modo (più precisamente la *prima* scelta di $q$ deve essere la stessa, altre non è detto che avvengano allo stesso modo) appartiene alla stessa classe di equivalenza.
Decomposto in classi calcoleremo la media di ogni classe facendone poi una media aritmetica.
Per effettuare il suddetto partizionamento, prendiamo istanze di dimensioni arbitraria in cui tutti gli elementi sono differenti $\rightarrow$ Tale assunzione è una approssimazione per eccesso visto che più elementi uguali ci sono e meno sproporzionata sarà la partizione (si faccia riferimento al caso migliore)

Secondo questa ipotesi la dimensione delle partizioni è univocamente determinata da quello che chiameremo il **rango del pivot**.

Data una sequenza e un pivot $x$, il rango $r(x)$ sarà il numero di elementi con valore $\leq$ ad $x$ nella sequenza. Essendo il pivot presente nella sequenza avremo $r(x) \geq 1$ perché almeno il pivot sarà $\leq$ di sé stesso, più precisamente se come pivot scegliessi il minimo della sequenza avrei esattamente $r(x) = 1$, mentre con il massimo sarà $r(x)= n$.

La scelta di $q$ è proprio il pivot; se il rango è uno avremo il pivot a sinistra e tutto il resto a destra, dunque:$$r(x) = 1 \Longrightarrow q = 1$$
Anche per:$$r(x) = 2 \Longrightarrow q = 1$$
perché con due valori minori o uguali al pivot avremo il seguente caso (sia $y \leq x$)
![[Pasted image 20231122111702.png]]

Dove avverrà l'unico scambio con la conseguenze di avere in questo caso una partizione di un elemento e l'altra con i restanti.

Seguendo questa logica per $r(x) = 3 \Longrightarrow q = 2, \; r(x) = 4 \Longrightarrow q = 3$ e così via (da due elementi in poi $q$ crescerà sempre). Pertanto: $$r(x) \geq 2 \Longrightarrow q = r(x)-1$$
Scegliere il pivot equivale dunque a scegliere la dimensione della partizione $q$, ed il nostro algoritmo sceglie proprio il rango dunque le classi di equivalenza esattamente $n$:
![[Pasted image 20231122111932.png]]
>[!note]
> Intuitivamente $T_{M}^{r}(n)$ rappresenta la funzione che dato il rango $r$ da il tempo medio delle sequenze di quella classe di equivalenza.

Il tempo medio può essere espresso con una media aritmetica di tutti i tempi delle classi di equivalenza, ovvero:$$T_M(n)=\frac{1}{n}\left(\sum_{r=1}^n T_M^r(n)\right)$$
Ma dato un certo rango $r$ avremo il seguente albero di ricorrenza:
![[Pasted image 20231122112135.png|300]]
>[!note]
> Intuitivamente $$T_{Q S}(n)= \begin{cases}\Theta(1) & \text { se } n \leq 1 \\ T_{Q S}(q)+T_{Q S}(n-q)+\Theta(n) & \text { se } n>1\end{cases}$$ 
> Dunque per l'albero a sinistra si ha $$T_M^r(n)=\Theta(n)+T_M\left(q^r\right)+T_M\left(n-q^r\right)$$

Da cui segue:$$
T_M(n)=\frac{1}{n} \cdot \sum_{r=1}^n\left(T_M\left(q^r\right)+T_M\left(n-q^r\right)+\Theta(n)\right)$$
Possiamo semplificare l'equivalenza $q^{r}=r-1$. Scorporando il caso del rango $r=1$ abbiamo una corrispondenza univoca per gli altri. Possiamo scrivere la precedente equazione come segue:$$
T_M(n)=\frac{1}{n}(\underbrace{\left(T_M(1)+T_M(n-1)+\Theta(n)\right)}_{r(x)=1 \Longrightarrow q=1}+\sum_{r=2}^n\left(T_M\left(n-q^r\right)+\Theta(n)\right))$$
Sappiamo che $T_{M}(1) = \Theta(1)$ e che $T_{M}(n-1) = O(n^{2})$ perché non può essere peggiore del caso peggiore (questa approssimazione sarà ininfluente). Inoltre $r = 1-q$, ma allora:$$
T_M(n)=\frac{1}{n}\left(\underbrace{\left(\Theta(1)+\Theta\left(n^2\right)+\Theta(n)\right)}_{O\left(n^2\right)}+\sum_{q=1}^{n-1}\left(T_M(q)+T_M(n-q)+\Theta(n)\right)\right)$$
Si noti che $\sum\limits_{q=1}^{n-1}(T_{M}(q))$ e $\sum\limits_{q=1}^{n-1}(T_{M}(n-q))$ sono esattamente gli stessi termini sommati in ordine inverso, quindi:$$
\begin{aligned}
T_M(n) & =\frac{1}{n}\left(O\left(n^2\right)+2 \sum_{q=1}^{n-1} T_M(q)+\sum_{q=1}^{n-1} \Theta(n)\right)=\frac{1}{n}(\underbrace{O\left(n^2+\Theta\left(n^2\right)\right)}_{\Theta\left(n^2\right)}+2 \sum_{q=1}^{n-1} T_M(q)) \\
& =\frac{\Theta\left(n^2\right)}{n}+\frac{2}{n} \sum_{q=1}^{n-1} T_M(q)=\Theta(n)+\frac{2}{n} \sum_{q=1}^{n-1} T_M(q)
\end{aligned}$$
>[!done] Conclusioni
> Abbiamo dimostrato che nel caso medio `QuickSort` ha un comportamento ottimo $\rightarrow$ Il tempo di esecuzione è quasi sempre $\Theta(n\log(n))$ rendendo nella pratica uno dei migliori algoritmi di ordinamento.


 

---
## Implementazione in C
```C
// da implementare
```