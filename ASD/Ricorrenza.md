---
author: Lorenzo Tecchia
tags:
  - definition
---
Una ***ricorrenza*** è una equazione o disequazione che descrive una funzione in termini dei suoi valori su input più piccoli.

>[!tip]-
> Per risolvere al pieno equazioni di ricorrenza ricorre in ogni caso, utilizzare un mix dei metodi proposti qui sotto.

>[!important]
> Permette di descrivere i [[Analisi asintotica#Notazione $ Theta$|tempi di esecuzione]] degli algoritmi divide et impera.

>[!note] Albero di ricorrenza
> Un albero dove i nodi rappresentano le chiamate ricorsive e ad ogni nodo è associato il numero di ricorrenza e il contributo locale di tale nodo(abbiamo in questo modo anche il contributo di ogni livello dell'albero)

>[!example]- # Esempio fattoriale
> Prendiamo come esempio la funzione del fattoriale
> $$n= \begin{cases}1 & \text { se } n=1 \\ n \cdot(n-1) ! & \text { altrimenti }\end{cases}$$
> Che sarà in termini di equazioni di ricorrenza:$$T_F(n)= \begin{cases}\Theta(1) & \text { se } n=1 \\ T_F(n-1)+\Theta(1) & \text { altrimenti }\end{cases}$$
> C'è una corrispondenza tra il livello dell'albero e l'output del programma. Avremmo infatti al livello $i$ un output $n -1$. 
> La foglia invece, per essere definita tale deve ricevere l'input del caso base (si noti infatti che il $\Theta(1)$ della foglia non è lo stesso $\Theta(1)$ degli altri livelli).
> Il livello foglia se $n- i = 1 \Longrightarrow i = n -1$
> A questo punto possiamo calcolare, partendo dal livello $0$ il tempo di esecuzione della funzione fattoriale:$$T_F(n)=\sum_{i=0}^{n-1} \Theta(1)+\Theta(1)=\Theta(n)$$
> ![[Pasted image 20231117144545.png|200]]

>[!important]
> Per comprendere il numero di chiamate ricorsive che la suddetta funzione compie bisogna analizzare la struttura utilizzando l'albero di ricorrenza
## Forma generale di equazioni di ricorrenza con funzioni a un solo parametro
Forniamo una generalizzazione della struttura dell'equazione di ricorrenza:$$
T(n)=\left\{\begin{array}{l}
\Theta(1) \text { se } n \leq k \\
z(n) \\
\sum_{i=0}^{z(n} T\left(f_i(n)\right)+g(n) \text { se } n>k
\end{array}\right.$$
- Il caso base, in linea di massima, è una costante $\rightarrow$ Potrebbero presentarsi casi in cui il caso base abbia un numero di operazioni lineare e quindi invece di avere un $\Theta(1)$ avremo un $\Theta(n)$
- $g(n)$ è il contributo delle operazioni nelle chiamate ricorsive
- $z(n)$ è il numero di chiamate
> [!note] alcune note su $z(n)$
> $z(n)$ viene definita come una funzione e non come una costante in quanto il numero di chiamate potrebbero dipendere dal valore in input $\rightarrow$ Non è detto che una chiamata debba fare lo stesso numero di chiamate ricorsive di un'altra chiamate nello stesso algoritmo

- $f_{i}(n)$ è l'input che prende ogni chiamata ricorsiva (non è detto che sia la stessa per ogni chiamante), ed ovviamente, affinché risulti corretto l'algoritmo deve risultare $f_{i}(n) < n$
È importante notare che per calcolare il numero di nodi di un livello basta moltiplicare tra loro le espressione dei livelli precedenti, ad esempio:
![[Pasted image 20231117145247.png]]

>[!example]- # Primo esempio sulle equazioni di ricorrenza
> Sia $z(n) = 2$ (si hanno $2$ chiamate ricorsive per ogni chiamata $\rightarrow$ questo si traduce in un albero binario) e siano:
> - $f_{i}(n) = \frac{n}{4}$(suddivisione input)
> - $g(n) = n^{2}$(tempo di esecuzione della altre istruzioni)
> Avremo la seguente equazione asintotica:$$T(n)= \begin{cases}1 & \text { se } n \leq 1 \\ 2 T\left(\frac{n}{4}\right)+n^2 & \text { se } n>1\end{cases}$$
> Dall'albero di ricorrenza capiamo che il termine generale di un input al livello i-esimo è $\frac{n}{4^{i}}$(termine che ci permette di calcolare l'altezza dell'albero)
> Si noti che vale la seguente proprietà: $$f_i(n)=f_j(n), \forall 1 \leq i, j \leq z(n)$$
> Quindi ogni nodo di ciascun livello ha lo stesso input $\rightarrow$
> - A livello $0$ avremo contributo $g(n) = n^{2}$
> - A livello $1$ avremo contribuito $g\left(\frac{n}{4}\right)= (\frac{n}{4})^2$
> - A livello $2$ avremo contributo $g\left(\frac{n}{4^{2}}\right)= \left(\frac{n}{4}\right)^{2}$
> - E così via
> È conveniente mantenere i risultati il più generale possibile(senza semplificare) in modo da non perdere le relazioni tra i livelli e poterne ricavare più semplicemente la somma
> Per il calcolo totale possiamo isolare i livelli (quindi calcolare il contributo di ongi livello) e in seguito effettuare un'unica somma in verticale(è necessario conoscere l'altezza dell'albero). 

![[Pasted image 20231117153222.png]]
Dunque:

 |   Livello   | Contributo                                  |
 |-----------| ------------------------------------------- |
 | Livello $0$ | $n^{2}$                                     |
 | Livello $1$ | $2 \cdot \left(\frac{n}{4}\right)^{2}$      |
 | Livello $2$ | $2 \cdot 2\left(\frac{n}{4^{2}}\right)^{2}$ |
 | Livello $3$ | $2^{3}\left(\frac{n}{4^{3}}\right)^{3}$     |
 |   $\dots$   | $\dots$                                     |

 >[!example]- # Primo esempio sulle equazioni di ricorrenza
 > Per quanto riguarda l'altezza dell'albero bisogna ragionare sul  contributo delle foglie, che sappiamo essere $1 \rightarrow$ Tale contributo può essere relazionato alla dimensione dell'input di un livello $i$ (nel nostro caso $\frac{n}{4^{i}}$). Per calcolare l'altezza dell'albero:$$\begin{align}
\frac{n}{4^i}=1 \Longrightarrow n=4^i \Longrightarrow \log _4 n=i \log _4 4 \stackrel{\log _a}{\Longrightarrow} \stackrel{x=\frac{\log _n x}{\log _n a}}{\Longrightarrow} \frac{\log _2 n}{\log _2 4}=i \Longrightarrow \frac{\log n}{2 \log 2}=i\\ \Longrightarrow i=\frac{\log n}{2}\end{align}$$
 > Visto che l'altezza dell'albero è $h = \frac{1}{2}\log(n)$, il numero delle foglie sarà il numero dei figli elevato all'altezza dell'albero. 
 > Nel nostro caso:$$\begin{align}
T(n)=\text { contributo c.b. }\cdot  n_f+\sum_{i=0}^{h-1}\left(\begin{array}{c}
\text { termine } \\
\text { generale }
\end{array}\right)=\sqrt{n}+\sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{n^2}{8^i}\right) \Longrightarrow \\ \sqrt{n}+n^2 \sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{1}{8^i}\right)^i\end{align}$$
> Ma essendo $0 < \frac{1}{8}< 1$ si tratta di una serie geometrica convergente $\rightarrow$ Questo ci semplifica lo studio della sommatoria grazie al seguente ragionamento:$$
\underbrace{\sum_{i=0}^0 x^i}_{x^0=1} \leq \sum_{i=0}^z x^1 \leq \underbrace{\sum_{i=0}^{\infty} x^i}_{\frac{1}{1-x}} \Longrightarrow 1 \leq \underbrace{\sum_{i=0}^z x^i}_{\text {tende ad una costante }} \leq \frac{1}{1-x}$$
> Visto che la nostra serie tende ad una costante $k$ avremo che:$$
T(n)=\sqrt{n}+k n^2=k n^2+n^{\frac{1}{2}}=\Theta\left(n^2\right)$$
> Volendo utilizzare la forma chiusa invece delle proprietà di converga avremo che:$$\begin{align}
\sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{1}{8}\right)^i=\frac{\left(\frac{1}{8}\right)^{\frac{\log n}{2}}-1}{\frac{1}{8}-1}=\frac{-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}}{-\frac{1}{8}+1}=\frac{1-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}}{\frac{7}{8}}=\frac{8}{7}\left(1-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}\right)=\frac{8}{7} \\ \left(1-\left(\frac{1^3}{2^3}\right)^{\frac{\log n}{2}}\right)= \frac{8}{7}\left(1-\left(\left(\frac{1}{2}\right)^{\log n}\right)^{\frac{3}{2}}\right)=\frac{8}{7}\left(1-\frac{1}{\left(2^{\log n}\right)^{\frac{3}{2}}}\right)=\frac{8}{7}\left(1-\frac{1}{\sqrt{n^3}}\right)\end{align}$$
>
> La funzione $f(n) = 1 - \frac{1}{1\sqrt{n^{3}}}$ tenderà a $1$ per $n \rightarrow \infty$; pertanto $\frac{8}{7}$ sarà il limite superiore della nostra sommatoria.
> Per $n = 1$ risulta $f(1) = 0$, ma allora la nostra sommatoria tenderà ad una costante $c$ tale che $0 \leq c \leq \frac{8}{7}$ dunque:$$
T(n)=\sqrt{n}+c n^2 \Theta\left(n^2\right)$$

---

>[!example]- # Secondo esempio sulle equazioni di ricorrenza
> $$T(n)\left\{\begin{array}{l}
1 \text { se } n \leq 2 \\
3 T(\sqrt{n})+1 \text { se n }>2
\end{array}\right.$$
> Da questa funzione, possiamo immaginare di avere una altezza dell'albero minore rispetto all'esempio precedente(la funzione cresce più lentamente di $\frac{n}{4} \rightarrow$ il numero di figli non influisce sull'altezza dell'albero ma solo sulla sua ampiezza). Ciò significa che arriverà al caso base più velocemente.

![[Pasted image 20231118161216.png]]

| Livello | Input per ogni nodo   | Contributo per ogni nodo | Contributo del livello |
| ------- | --------------------- | ------------------------ | ---------------------- |
| $0$     | $n$                   | $1$                      | $1$                    |
| $1$     | $n^{\frac{1}{2}}$     | $1$                      | $3$                    |
| $2$     | $n^{\frac{1}{2^{2}}}$ | $1$                      | $3^{2}$                |
| $3$     | $n^{\frac{1}{2^{3}}}$ | $1$                      | $3^{3}$                | 

>[!example]- # Secondo esempio sulle equazioni di ricorrenza
> Dunque, il contributo per il livello $i$ è $3^{i}$, mentre il suo input è $\frac{1}{2^{i}}$.
> Andiamo quindi a calcolare l'altezza dell'albero confrontandolo con il massimo input per cui è verificato il caso base (quindi sarà il contributo del caso base per la dimensione del massimo input $1 \cdot 2$):
> $$(n)^{\frac{1}{2^i}}=2 \Longrightarrow \log (n)^{\frac{1}{2^i}} \Longrightarrow \frac{1}{2^i} \log n=1 \Longrightarrow \log n=2^i \Longrightarrow \log (\log n)=i$$
> ***NOTA:*** $\log(n) > \log(\log(n)) \rightarrow$ La supposizione fatta all'inizio è ora evidentemente vera, infatti $\log(\log(n))$ è esponenzialmente minore di $\log(n)$.
> Per quanto riguarda il numero di foglie avremo $3^{h} = 3^{\log(\log(n))} = (\log(n))^{\log(3)}$ e dunque:
> $$\begin{gathered}
T(n)=(\log n)^{\log 3}+\sum_{i=0}^{\log (\log n)-1} 3^i=(\log n)^{\log 3}+\frac{3^{\log (\log n)}-1}{2}=(\log n)^{\log 3}+\frac{1}{2}(\log n)^{\log 3}-\frac{1}{2}= \\
\Theta\left((\log n)^{\log 3}\right)
\end{gathered}$$

---

>[!example]- # Terzo esempio sulle equazioni di ricorrenza
> Prendiamo la seguente equazione di ricorrenza che ha $f_{1}= \frac{n}{2}$ e $f_{2}=\frac{n}{3}$:
> $$T(n)=\left\{\begin{array}{l}
1 \text { se } n \leq 1 \\
T\left(\frac{n}{2}\right)+T\left(\frac{n}{3}\right)+n \text { se } n>1
\end{array}\right.$$
> Applichiamo quindi la tecnica dell'albero di ricorrenza

![[Pasted image 20231118162359.png]]

| Livello     | $n$                                                                    |
| ----------- | ---------------------------------------------------------------------- |
| Livello $1$ | $\frac{n}{2}+ \frac{n}{3} = \frac{5}{6}n$                              |
| Livello $2$ | $\frac{n}{4}+ \frac{n}{6} + \frac{n}{6} \frac{+n}{9} = \frac{25}{36}n$ |
| Livello $3$ | $\frac{n}{8} + \frac{3}{12}n + \frac{3}{18}n + \frac{n}{28} = \frac{5^{3}}{6^{3}}n$                                                                       |

>[!example]- # Terzo esempio sulle equazioni di ricorrenza
> Come si può notare anche dalla forma approssimata dell'albero, è evidente che ci saranno dei rami (sequenze discendenti di nodi) di questo arrivano che arrivano prima alle foglie e percorsi che arrivano dopo. Nello specifico il ramo più a sinistra decresce più lentamente del ramo più a destra $\rightarrow$ Al livello $3$ infatti avremo input di $\frac{n}{8}$ per primo e $\frac{n}{27}$ per secondo.
> Dall'associazione del contributo totale di ogni livello (sommando il contributo di ogni nodo) possiamo trarre che per un livello $i$ avremo $\left(\frac{5}{6}\right)^{i}n$ come termine genrale
> A questo punto non possiamo procedere come negli esempi precedenti $\rightarrow$ È importante notare che la relazione calcolata precedentemente vale solo per i livelli **pieni**, ovvero quei livelli che hanno il numero massimo di nodi possibile.
> L'albero in questione non è pieno, tuttavia prendendo solo i livelli pieni, è evidente che è possibile ottenere un nuovo albero con un tempo di esecuzione minore rispetto a quello da calcolare $\rightarrow$ Sarà quindi un limite inferiore asintotico per $T(n)$
> Analogamente, otterremo un notevole limite asintotico, se approssimando per eccesso, *fingiamo* che tutti i livelli del nostro albero siano pieni. Vale il termine generale:
> ![[Pasted image 20231118163442.png]]
> I $2$ diversi alberi avranno uno l'altezza del percorso più breve e l'altro quella del percorso più lungo.
> Per il calcolo di questi valori si utilizza sempre lo stesso metodo visto finora:
> - L'altezza del percorso più lungo, poiché si divide sempre per $2$, si otterrà con la seguente relazione $\frac{n}{2^{i}} = 1 \Longrightarrow \log(n) = 2^{i} = \log(n)$
> - L'altezza del percorso breve sarà invece $\log(n) = 3^{i} \Longrightarrow i = \log_{3}(n)$
> A questo punto è possibile calcolare i tempi di esecuzione delle $2$ approssimazioni
> ***NOTA*** Non useremo la forma completa poiché con buona approssimazione possiamo considerare il contributo dell'ultimo livello come se fosse un livello interno (andiamo ad approssimare per eccesso il contributo delle foglie):
> $$\begin{gathered}
T^i(n)=\sum_{i=0}^{\log _3 n}\left(\frac{5}{6}\right)^i=n \sum_{i=0}^{\log _3 n}\left(\frac{5}{6}\right)^i \underbrace{\Longrightarrow}_{\text {serie geometrica con ragione }<1} T^i(n)=\Theta(n) \\
T^{i i}(n) \sum_{i=0}^{\log n}\left(\frac{5}{6}\right)^i n=n \sum_{i=0}^{\log n}\left(\frac{5}{6}\right)^i=\Theta(n)
\end{gathered}$$
> Entrambe sono comprese tra 1 e $\frac{1}{1-\frac{5}{6}}=6$
> Ma allora $T(n) = \Theta(n)$ essendo limitata sia superiormente che inferiormente da funzioni lineari

---

>[!example]- # Quarto esempio sulle equazioni di ricorrenza
> $$
T(n)=\left\{\begin{array}{l}
1 \text { se } n \leq 1 \\
T\left(\frac{n}{2}\right)+T\left(\frac{n}{3}\right)+n \text { se } n>1
\end{array}\right.$$

![[screenShot 2023-11-18 at 16.42.32.png]]

| Livello | Contributo                      |
| ------- | ------------------------------- |
| $0$     | $n$                             |
| $1$     | $\frac{4}{3}n$                  |
| $2$     | $\left(\frac{4}{3}\right)^{2}n$ |
| $3$     | $\left(\frac{4}{3}\right)^{3}n$ |
| $\dots$ | $\dots$                         |
| $i$     | $\left(\frac{4}{3}\right)^{i}n$ | 

>[!example]- # Quarto esempio sulle equazioni di ricorrenza
> Anche se questo albero di ricorrenza ha una diversa struttura rispetto l'esempio precedente, i problemi sono gli stessi, e quindi anche il modo per risolverli:
> L'altezza dell'albero pieno che farà da limite inferiore asintotico sarà quello con percorso più breve, dunque
> $$n=3^h \rightarrow h=\log _3 n$$
> Invece l'albero che farà da limite superiore avrà altezza $\log(n)$. Dunque:
> $$T^i(n)=\sum_{i=0}^{\log _3 n}\left(\frac{4}{3}\right)^i n \wedge T^{i i}(n) \sum_{i=0}^{\log n}\left(\frac{4}{3}\right)^i n$$
> A differenza dell'esempio precedente, la serie geometrica in questione non ha ragione compresa tra $0$ e $1$; pertanto bisognerà usare la forma chiusa della serie geometrica:
> $$\begin{aligned}
& T^{\prime}(n)=n \sum_{i=0}^{\log _3 n}\left(\frac{4}{3}\right)^i=n \frac{\left(\frac{4}{3}\right)^{\log _3 n+1}-1}{\frac{4}{3}-1}=3 n\left(\frac{4}{3} \cdot\left(\frac{4}{3}\right)^{\log _3 n}-1\right)=3 n\left(\frac{4}{3} \cdot n^{\log _3 \frac{4}{3}}-1\right) \\
& =4 n \cdot n^{\log _3 \frac{4}{3}}-3 n=4 \underbrace{\left(n^{\log _3\left(\frac{4}{3}+1\right)}\right)}_{\text {cresce pi velocemente di un } \Theta(n)}-3 n=\Theta\left(n^{\log _3\left(\frac{4}{3}+1\right)}\right) \\
& T^{\prime \prime}(n)=n \sum_{i=0}^{\log }\left(\frac{4}{3}\right)^i=\Theta\left(n^{\log \left(\frac{4}{3}+1\right)}\right) \\
&\end{aligned}$$
> Per quanto siano molto vicine queste funzioni hanno **esponente diverso**$\rightarrow$ Per tanto la relazione:
> $$T^{\prime}(n) \leq T(n) \leq T^{\prime \prime}(n)$$
> Possiamo soltanto dire che $T(n)=\Omega\left(n^{\log \left(\frac{4}{3}+1\right)}\right)$ e $T(n)=O\left(n^{\log \left(\frac{4}{3}+1\right)}\right)$(nulla di più).
# Validare equazioni di ricorrenza
[[Quick sort]]
Dimostriamo che $T_{M}(n) = O(n)$ così da confermare $T_{M}(n) = \Theta(n \log(n))$; bisogna verificare (utilizzando l'induzione) che 
### Sostituzione
Nel ***metodo di sostituzione***, ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi sia corretta $$
\exists c, n_0>0: \forall n \geq n_0, T_M(n) \leq c(n \log n)$$
Il caso induttivo sarà evidentemente valido per $n\geq 2$, essendo il caso $n=1$ non verificato; visto che $\log(1) = 0$ risulta che $T_{M}\leq 0$(ciò è assurdo), e di conseguenza il caso base è $n=2$.
Grazie al fatto che $1 \leq q \leq n-1$ possiamo scrivere $T_{M}(q) \leq c(q\log(q))$ (questa sarà la nostre ipotesi induttiva); per transitività risulta:$$
T_M(n)=\Theta(n)+\frac{2}{n} \sum_{q=1}^{n-1} T_M(q) \leq \Theta(n)+\frac{2}{n} \sum_{q=1}^{n-1} c(q \log q)$$
Assumiamo per il momento che sia vera la seguente proprietà (che andremo a dimostrare successivamente):$$\sum_{q=1}^{n-1}(q \log q) \leq \frac{n^2 \log n}{2}-\frac{n^2}{8}$$
Da ciò segue:$$T_M(n) \leq \Theta(n)+\frac{2 c}{n} \sum_{q=1}^{n-1}(q \log q) \leq \Theta(n)+\frac{2 c}{n}\left(\frac{n^2 \log n}{2}-\frac{n^2}{8}\right)=\Theta(n)+c(n \log n)-\frac{c n}{4}$$
A questo punto se dimostriamo che $\Theta(n) - \frac{cn}{4} \leq 0$ allora risulterà (dopo la verifica del caso base) che $T_{M}(n) \leq c(n\log(n))$
Sappiamo che $\Theta(n)$ è assimilabile ad un $kn$, allora risulta che $kn \leq \frac{cn}{4}$

La costante $k$ è fissata della relazione $Theta$, ma la costante $c$ può essere scelta arbitrariamente. Basta scegliere pertanto $c \geq 4k$ per concludere che:$$T_M(n)=O(n \log n) \text { per } n \geq 2$$
### Validazione per il caso base $b=2$
$$
T_M(2)=\Theta(1)+\frac{2}{2} \sum_{q=1}^2 T_M q=\Theta(1)+T_M(1)=\underbrace{\Theta(1)}_{\begin{array}{c}
\text { costo di } \\
\text { partiziona }
\end{array}}+\underbrace{\Theta(1)}_{\begin{array}{c}
\text { cel'equazione dise } \\
\text { cricorrenza }
\end{array}}=k+a$$
Per $c \geq k +a$ anche il caso base è verificato.

Se scelgo un $c= max\{k+a, 4k\}$ vale sia il caso base che quello induttivo e quindi risulta dimostrata nella nostra tesi $T_{M}(n) = O(n\log(n))$, da cui per il teorema secondo il quale un algoritmo di ordinamento non può essere meno di $n\log(n)$, segue:$$T_{M}(n) = \Theta(n\log(n))$$
### Maggiorazione di una sommatoria
$$\sum_{q=1}^{n-1}(q \log q) \leq \frac{n^2 \log n}{2}-\frac{n^2}{8}$$

Dimostriamo la precedente assunzione, il modo più semplice per maggiorare $\sum\limits_{q=1}^{n-1}$ è sfruttare il fatto che $q < n$(ricavato da $1 \leq q \leq n-1$) e quindi $\log(n) \Longrightarrow q \log(q ) \leq q \log(n)$, dunque:$$\sum_{q=1}^{n-1}(q \log q) \leq \sum_{q=1}^{n-1}(q \log n)=\log n \sum_{q=1}^{n-1} q=\log n \cdot \frac{n(n-1)}{2}=\frac{n^2 \log n}{2}=\frac{n \log n}{2}$$
Tuttavia $frac{n\log\n}{2} \leq \frac{n^{2}{8}}\rightarrow$ Significa che la nostra maggioranza è stata eccessiva. Quello che possiamo fare è spezzare la sommatoria in due parti così da fare approssimazioni più precise:$$
\begin{aligned}
& \sum_{q=1}^{n-1}=\underbrace{\sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1}(q \log q)}_{q \leq\left\lceil\frac{n}{2}\right\rceil}+\underbrace{\sum_{q=\left\lceil\frac{n}{2}\right\rceil}^{n-1}(q \log q)}_{\text {approssimiamo }} \leq \sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1}\left(q \log \frac{n}{2}\right)+\sum_{q=\left\lceil\frac{n}{2}\right\rceil}^{n-1}(q \log q)= \\
& =\log \frac{n}{2} \sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1} q+\log n \sum_{q=\left\lceil\frac{n}{2}\right\rceil}^{n-1} q=(\log n-1) \sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1} q+\log n \sum_{q=\left\lceil\frac{n}{2}\right\rceil}^{n-1} q= \\
& =\underbrace{\log n \sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1} q+\log n \sum_{q=\left\lceil\frac{n}{2}\right\rceil}^{n-1} q}_{\text{uniamo le due sommatorie}}-\sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1} q=\log n \sum_{q=1}^{n-1} q-\sum_{q=1}^{\left\lceil\frac{n}{2}\right\rceil-1} q \\
\end{aligned}$$
Ora $\log(n)\sum\limits_{q=1}^{n-1}(q)$ l'abbiamo già risolta; visto che stiamo maggiorando non c'è problema a sottrarre qualcosa di più piccolo e quindi sfruttiamo il fatto che $\lceil \frac{n}{2} \rceil \geq \frac{n}{2}$
$$
\begin{aligned}
\sum_{q=1}^{n-1} \leq\left(\frac{n^2 \log n}{2}-\frac{n \log n}{2}\right)-\sum_{q=1}^{\frac{n}{2}-1} q & =\frac{n^2 \log n}{2}-\frac{n \log n}{2}-\frac{\frac{n}{2}\left(\frac{n}{2}+1\right)}{2}= \\
& =\frac{n^2 \log n}{2}-\frac{n \log n}{2}-\frac{n^2}{8}+\frac{n}{4} \leq \frac{n^2 \log n}{2}-\frac{n^2}{8}
\end{aligned}$$

Poiché $\frac{n\log(n)}{2} \geq \frac{n}{4}$ e quindi $\frac{n}{4} - \frac{n\log(n)}{2} \leq 0$, togliendo un valore negativo la maggioranza resta valida.