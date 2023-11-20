---
author: Lorenzo Tecchia
tags:
  - definition
  - example
---
## Notazione
La notazione che usiamo per descrivere il tempo di esecuzione asintotico di un algoritmo sono definite in termini di funzioni il cui dominio è l'insieme dei numeri naturali $\mathbb{N} = \{0,1,2,\dots\}$. 

Tali notazioni sono comode per descrivere la funzione $T(n)$, tempo di esecuzione nel caso peggiore, che di solito è definita soltanto con dimensioni intere dell'input.

Nel calcolo del tempo di esecuzione di un algoritmo, quando l’input è sufficientemente grande, le costanti moltiplicative e i termini di ordine inferiore diventano trascurabili.

Ci interessa quindi sapere come il tempo di esecuzione aumenta all’aumentare dell’input, al ***limite***.

Infatti, un algoritmo asintoticamente più efficiente sarà il migliore con tutti gli input tranne con quelli molto piccoli.

Le notazioni utilizzate per descrivere il tempo di esecuzione asintotico di un algoritmo, sono funzioni:
$$f: \mathbb{N} \rightarrow \mathbb{R}$$
In particolare $f$:
- ***positiva***
	- $\exists n_{0}\in \mathbb{N}: \forall n \geq n_{0} \; \; f(n)\geq 0$
- ***crescente***
	- $\exists n_{0}\in \mathbb{N}: \forall n \geq n_{0} \; \; f(n)\leq f(n+1)$

### Notazione $O$ grande
![[Pasted image 20230905172827.png|300]]
- Indichiamo con $O(g(n))$ l’insieme delle funzioni:
$$O(g(n))= \left\{ f(n): \exists c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0}, f(n)\leq c\;g(n)\right\}$$^O-grande
>[!hint] In altre parole
> $O(g(n))$ limita superiormente $f(n)$
### Notazione $\varOmega$ grande
![[Pasted image 20230905173744.png|300]]
- Indichiamo con $Ω(g(n))$ l’insieme delle funzioni:
$$\varOmega(g(n))= \left\{ f(n): \exists c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0}, f(n)\geq c\;g(n)\right\}$$
>[!hint] In altre parole
> $\varOmega(g(n))$ limita inferiormente $f(n)$
### Notazione $\Theta$
![[Pasted image 20230905173858.png|300]]
- Indichiamo con $\Theta(g(n))$ l’insieme delle funzioni:
$$\Theta(g(n))= \left\{ f(n): \exists c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0},\; c_{1}\;g(n)\leq f(n)\leq c_{2}\;g(n)\right\}$$
Infatti il $\lim_{n \rightarrow \infty}\frac{f(n)}{g(n)} = L$ 
![[Pasted image 20230905174711.png]]
>[!important] In altre parole
> $\Theta(g(n))$ limita sia superiormente che inferiormente $f(n)$
#### Dimostrazione 
Supponiamo che $g(n)$ ad un certo punto sia sempre positivo(supposizione più realistica essendo una funzione di tempo), quindi è possibile dividere la realzione per $g(n)$.
Sia $h(n) = \frac{f(n)}{g(n)}$, dopo la divisione avremmo che:$$c_{1}\leq h(n) \leq c_{2}$$
Ne segue che, essendo $h(n)$ sempre compreso tra $2$ costanti positive:$$\lim_{n \rightarrow \infty} h(n) = k,\text{con}\;\; c_{1}\leq k \leq c_{2}$$(In modo del tutto analogo si trattano le altre due implicazioni).
Non resta che dimostrare che le due constanti $c_{1}, c_{2}$ che delimitano l'andamento $h(n)$ esistano.
Supponiamo a tal scopo che $\lim_{n \rightarrow \infty}\frac{f(n)}{g(n)} = k$ e che quindi $k$ sia asintotico orizzontale per il rapporto $h(n) = \frac{f(n)}{g(n)}$.
Per tale asintoto esistono solo $2$ casi:
1. $h(n)$ tende a $k$ dall'alto
2. $h(n)$ tende a $k$ dal basso
##### Caso 1 h(n) dall'alto
$n_{0}$ sarà il punto da cui la funzione $h(n)$ sarà sempre decrescente (è irrilevante il punto preciso di $n_{0}$ l'importante è che esista e da quel punto in poi la funzione descresca).
Prendiamo ora la retta costante pari al valore di $h(n_{0})$, ed ora possiamo osservare che da $n_0$ in poi il rapporto è tale che $c_{1}=k \leq h(n) \leq h(n_{0}) = c_{2}$
![[Pasted image 20231116164426.png|250]]
>[!note]
>Le precedenti costanti sono state trovate avendo support che il rapporto $\frac{f(n)}{g(n)}$ esista e che la funzione (dopo lo studio della derivata prima di tale rapporto) sia decrescente per un intervallo $[n_{0}, +\infty)$
##### Caso 2 h(n) dal basso
Supposto che lo studio della derivata prima abbia portato alla conferma dell'esistenza di un intervallo per cui la funzione è sempre crescente abbiamo già trovato le nostre costanti.
infatti per $c_{2}$ è ovvio che basti prendere l'asintoto $k$ mentre per $c_{1}$ bisogna scegliere un $n_{0}$ da $[n_{0}, + \infty$ la funzione sia sempre crescente
![[Pasted image 20231116165310.png|250]]
>[!note]
> Si noti che stavolta non basta solo che l'intervallo $[n_{0}, \infty)$ sia crescente, ma deve anche essere sempre positiva (scegliere un punto in cui $\exists n \leq n_{0}\;\;:\;\; h(n)$ sia negativa andrebbe contro la nostra definizione di $\Theta$)
> Una volta determinato $n_{0}$, allora: $$c_{1}= h(n_{0})$$
#### Caso oscillatorio
Se la situazione è quella della rappresentazione nella [[Analisi asintotica#^caso-oscillatorio|figura]] (l'ampiezza dell'oscillazione deve essere $0$ ad un certo punto altrimenti $\lim_{n \rightarrow \infty}h(n) \neq k$) determinare le costanti è molto complesso. Bisogna scegliere un punto di minimo locale($n_{0}$) e un punto di massimo locale ($m_{0}$) in modo tale che i successivi minimi saranno sempre al di sopra del minimo locale scelto e i successivi massimi più bassi del massimo locale scelto; $n_{0}$ sarà il punto maggiore (nel nostro caso è il minimo locale) tra i $2$. Una volta scelto questi due punti le costanti saranno $c_{1} = h(n_{0})$ e $c_{2} = h(m_0)$.

![[Pasted image 20231116170752.png|250]]^caso-oscillatorio

>[!important]
> Questo tipo di funzioni sono molto rare e pertanto nei nostri studi ci imbatteremmo solo nei primi due casi

>[!example] # Esempio
> Importante notare che: $$\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = \infty \iff \lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} =\infty \iff \lim_{n \rightarrow \infty} = k > 0 \iff \lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} = \frac{1}{k} > 0$$
> Questo dimostra che studiare il limite del rapporto o il limite del suo reciproco ci porta alla stessa conclusione.
> 1. Siano $f(n) = n$ e $g(n) = 4n -10$
> > Avremo $\lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} = \lim_{n \rightarrow \infty} 4 - \frac{10}{4} = 4 \rightarrow g(n) = \Theta(f(n)) \rightarrow f(n) = \Theta(g(n))$
> > Stabiliamo quindi le costanti per tale relazione. Sia $h(n) = 4- \frac{10}{n}$ e facendone la derivata $\rightarrow$:$$\frac{d}{dn}(4-\frac{10}{n})= \frac{d}{dn}4 -\frac{d}{dn}\frac{10}{n} = -10 \frac{d}{dn}n^{-1}=\frac{10}{n^{2}}$$
> > Avremo quindi una funzione che è sempre crescente (essendo la derivata positiva)
> > Scegliamo ora un $n_{0}$ per cui la funzione sia sempre crescente e positiva(se ad es. scegliessimo 1 avremo $h(n) < 0$)
> > Sia $n_{0} = 3$. Da questo ricaviamo che:$$c_{1}= h(3) = \frac{2}{3}\;\text{e}\;c_{2}=4$$ Dunque $\forall n \leq 3, \;2f(n)\leq g(n) \leq \frac{2}{3}f(n)$; ovvero $\frac{3}{2}g(n)\leq f(n) \leq \frac{1}{2}g(n)$
> Se invece $f(n) = n$ e $g(n) = 4n + 10$ risulta $\lim_{n \rightarrow \infty} \frac{g(n)}{f(n)} = 4$; quindi, le $2$ funzioni sono sempre in relazione $\Theta$ tra di loro. In questo caso la funzione risulta decrescente essendo $h^{I}(n) = -\frac{10}{n^{2}}$
### Notazione $o$ piccolo
- Indichiamo con $o(g(n))$ l’insieme delle funzioni:
$$o(g(n))= \left\{ f(n): \forall c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0},\; f(n)\leq c \;g(n)\right\}$$
- Nella $O$ grande è sufficiente che ci sia ***ALMENO*** un $c>0$ tale che $f(n)\leq c\;g(n)$
- Nella $o$ piccola, invece, $f(n)\leq c\;g(n)$ ***PER OGNI*** $c>0$  
- Quindi se $f(n)$ è $o$ piccolo di $g(n)$, è anche $O$ grande di $g(n)$

$o(g(n))$ limita superiormente $f(n)$
Infatti il $\lim_{n \rightarrow 0} \frac{f(n)}{g(n)} = 0$ perché, al limite, $g(n)$ cresce più velocemente
### Notazione $\omega$ piccolo
- Indichiamo con $\omega(g(n))$ l’insieme delle funzioni:
$$\omega(g(n))= \left\{ f(n): \forall c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0},\; f(n)\geq c\;g(n)\right\}$$
- Nella $\varOmega$ grande è sufficiente che ci sia ***ALMENO*** un $c>0$ tale che $f(n)\geq c\;g(n)$
- Nella $\omega$ piccola, invece, $f(n)\geq c\;g(n)$ ***PER OGNI*** $c>0$  
- Quindi se $f(n)$ è $\omega$ piccolo di $g(n)$, è anche $\varOmega$ grande di $g(n)$

$\omega(g(n))$ limita inferiormente $f(n)$
Infatti il $\lim_{n \rightarrow 0} \frac{f(n)}{g(n)} = \infty$ perché, al limite, $g(n)$ cresce più lentamente
## Proprietà delle notazioni
### Riflessiva
- $f(n)$ = $O(f(n))$
- $f(n)$ = $\varOmega(f(n))$
- $f(n)$ = $\Theta(f(n))$
### Simmetrica
![[Pasted image 20230905183705.png|500]]
### Transitiva
![[Pasted image 20230905183731.png]]
>[!example] Esempio proprietà transitiva
> Questa proprietà risulta essere utile quando bisogna confrontare $2$ funzioni molto *distanti* tra loro e quindi difficili da confrontare. 
> Grazie alla transitività è possibile scegliere una funzione nel mezzo e confrontarla con entrambe (se risulta vera per una e falsa per l'altra allora non si arriva a nulla).
> Consideriamo ad es. $f(n) = n^{2}-3n + 4$ e $h(n) = 2n^{2}+7n -10$
> Supponiamo che $g(n) = n^{2}$ e dimostriamo che $c_{1}n^{2} n^{2}-3n + 4 \leq c_{2}n^{2}$
> Scegliendo $c_{2}= 1$ abbiamo:$$n^{2}-3n + 4 \leq n^{2}, \text{verificata per }n \geq \frac{4}{3}$$ mentre per $c_{1} = \frac{1}{2}$ si ha $\frac{n^{2}}{2} \leq n^{2}-3n +4 \iff 0 \leq \frac{n^{2}}{2}- 3n +4 \iff 3n -4 \leq \frac{n^{2}}{2}\;\; \text{verificata per}\;\; \forall n \geq 1$
> Analogamente si tratta il caso $g(n) = O(h(n))$ e di conseguenza si ha anche che $f(n) = O(h(n))$
> Questo esempio è banale, in quante fin dall'inizio si vedeva che le $2$ funzioni crescessero allo stesso modo, ma per funzioni esponenziali o logaritmiche potrebbe non esserlo, e quindi, risulta utile applicare questa proprietà transitiva come fatto in questo esempio
### Monotonicità
$$f(n) = \Theta(g(n)) \Longrightarrow \log(f(n)) = \Theta(\log(g(n)))$$
Per dimostrare la precedente implicazione utilizziamo la proprietà della monotonicità dei logaritmi, ovvero:$$x \leq x \Longrightarrow log(x) \leq \log(x)$$
Da $f(n) = \Theta(g(n))$ per definizione $\exists n_{0}, c_{1},c_{2}: \forall n \geq n_{0},\;\; c_{1}g(n) \leq f(n) \leq c_{2}g(n)$ ma quindi:$$\log(c_{1}g(n)) \leq \log(f(n)) \leq \log(c_{2}g(n))$$

A questo punto possiamo utilizzare un'altra proprietà dei logaritmi:$$\log(xy) = \log(x) + \log(y) \rightarrow \log(c_{1}) + \log(g(n)) \leq \log(f(n)) \leq \log(c_{2}) + \log(g(n))$$
>[!note] Questo non basta
> Se $c_{1}$ e/o $c_{2}$ sono compresi tra $0$ e $1$ il logaritmo sarà negativo.

Esiste però la seguente proprietà:
$$\forall h(n), \;\; \log(h(n)) + k = \Theta(\log(h(n)))$$
>[!note] Le costanti non sono le stesse per qualsiasi $k$
> A noi non interessa soltanto che queste esista ma che inoltre sia valido, $\forall k \in \mathbb{Z}$

Sfruttando la seguente proprietà: $$\begin{align}\exists n_1>0, \exists c_1^{\prime}, c_2^{\prime}>0: \forall n \geq n_1, c_1^{\prime} \log (g(n)) \leq \log c_1+\log (g(n)) \leq c_2^{\prime} \log (g(n))\\ \text{e} \\
\exists n_2>0, \exists c_1^{\prime \prime}, c_2^{\prime \prime}>0: \forall n \geq n_2, c_1^{\prime \prime} \log (g(n)) \leq \log c_2+\log (g(n)) \leq c_2^{\prime \prime} \log (g(n))\end{align}$$
Usando le definizioni precedenti:$$\begin{align}
\exists n_3=\max \left\{n_0, n_1, n_2\right\}, \exists c_1, c_1^{\prime}, c_2, c_2^{\prime \prime}>0: \forall n \geq n_3, c_1^{\prime} \log (g(n)) \leq \log c_1+\log (g(n)) \leq \\
\log (f(n)) \leq \log c_2+\log (g(n)) \leq c_2^{\prime \prime} \log (g(n))\end{align}$$
Da cui per la transitività del minore ed uguale otteniamo:$$
\exists n_3>0, \exists c_1^{\prime}, c_2^{\prime \prime}>0: \forall n \geq n_3, c_1^{\prime} \log (g(n)) \leq \log (f(n)) \leq c_2^{\prime \prime} \log (g(n))$$
Quindi l'implicazione è dimostrata sotto la supposizione che $\forall h(n), \;\; \log(h(n)) + k = \Theta(\log(h(n)))$, ma ciò è evidente, essendo:$$
\lim _{n \rightarrow \infty} \frac{k+\log (h(n))}{\log (h(n))}=\lim _{n \rightarrow \infty} \frac{k}{\log (h(n))}+\lim _{n \rightarrow \infty} \frac{\log (h(n))}{\log (h(n))}=1>0$$
>[!example] # Confutazione di una implicazione
> Essendo il logaritmo una funzione si potrebbe pensare di generalizzare un'implicazione precedente dicendo:$$
\forall h(n), f(n)=\Theta(g(n)) \Longrightarrow h(f(n))=\Theta(h(g(n)))$$ Questo risulta però falso, e per confutarlo basta descriver un esempio per cui la precedente implicazione non sia vera.
> A tal proposito siano $f(n) = n$ e $g(n) = 2n$ è evidente che siano in relazione $\Theta$ tra loro, infatti per $c_{1}= \frac{1}{2}$ e $c_{2}= 1$ abbiamo che:$$\forall n \geq 1, \frac{1}{2} 2 n \leq n \leq 1 \cdot 2 n$$
> Sia la nostra funzione $h(n) = 2^{n}$, risulta quindi $2^{f(n)}= 2^{n}$ e $2^{g(n)} = 2^{2n}$, ma calcolando il limite di tale rapporto:$$\lim _{n \rightarrow \infty} \frac{2^n}{2^{2 n}}=\lim _{n \rightarrow \infty} \frac{2^n}{2^n \cdot 2^n}=\lim _{n \rightarrow \infty} \frac{1}{2^n}=0$$
> Essendo il limite una costante diversa da $k > 0$ concludiamo che le due funzioni non sono in relazione $\Theta$ tra di loro e dunque abbiamo dimostrato falsa l'implicazione (basta un contro esempio per dire che la relazione è falsa, mentre per dire che è vera bisogna dimostrarla per ogni valido input).
### Altre proprietà
![[Pasted image 20230905183946.png|600]]
## Esempio maggiorazione
>[!example] 
>Dimostrare o confutare la seguente relazione: $\log_{2}(n^{2n})+n -\log_{2}(n)=\Theta(n \log_2(n))$ 

1. Applicare i limiti su entrambe le funzioni, per verificare l'andamento asintotico delle due: in particolare verificare(in questo caso per la notazione $\Theta$) che il limite abbia valore reale e che non sia né $0$ né $\infty$ per escludere le notazioni di $O$ grande e $\varOmega$ grande rispettivamente.

>[!tip] 
> Non è sempre detto che il valore $L$ del limite, sia una delle due costanti $c_{1}\;\text{o}\;c_{2}$ della nostra notazione $\Theta$.


2. Scrivere per esteso, la disequazione che mette in realzione la nostra funzione con le costanti per la notazione $\Theta$; appunto $c_{1},c_{2}$.$$c_{1}\;g(n)\leq f(n)\leq c_{2}\;g(n)$$
>[!warning] 
> Oltre ai valori delle costanti $c_{1}$ e $c_{2}$ bisogna anche andare a prendere un valore $n_{0}$ anch'esso $> 0$ per il quale vale la "costrizione" asintotica della notazione $\Theta$.

>[!tip] 
> Le due costanti $c_{1}$ e $c_{2}$ non rappresentano per forza due valori univoci, possono corrispondere anche a valori estremali con i quali possiamo andare a definire gli intervalli nei quali andare a prendere le costanti.

3. Analizzare separatamente i due lati della disequazione, per ottenere le costanti.
	- Se devo dimostrare che esiste un numero $x \leq a$  e conosco una relazione per cui un numero $b$ sia minore di $a$ in questo modo: $b < a$; allora posso estendere la mia relazione con $x$ sapendo che poi la seguente varrà in ogni caso: $x \leq b < a$.

>[!tip] 
> È spesso molto utile andare a maggiorare o minorare i termini della funzione all'interno della disequazione, per rendere più manipolabili i termini della stessa.

Nel caso dell'esempio $$c_{1}\;n \log_{2}(n) \leq 2n\log_{2}(n)+n-n < 2n\log_{2}(n)+n-\log_{2}(n)$$
- proprio perché $\log_{2}(n) < n$.
	- In questo caso $n_{0}=1$ perché la relazione per cui $\log_{2}(n) < n$ vale per valori maggiori di $1$
- Nella seconda parte della disequazione:
	-  $2n\log_{2}(n) +n -\log_{2}(n)\leq c_{2}\;\log_{2}(n)$
	- Possiamo andare a maggiorare il termine $n-\log_{2}(n)$ con queste due relazioni:
		- $-\log_{2}(n)\leq \log_{2}(n)$
		- $n+\log_{2}(n) \leq n\log_{2}(n)\rightarrow$ in particolare per $n\geq 4$ 
4. Svolgendo troveremo che $c_{1}=2$ e $c_{2}=3$ e mettendo in intersezione le due proprietà per cui valgono entrambe le maggiorazioni troveremo che $n_{0} \geq 4$
5. Risultato:$$2\;n\log_{2}(n)\leq 2n\log_{2}(n)+n-\log_{2}(n) \leq 3\;\log_{2}(n)\;\;\;\forall n \geq 4$$

## Esempio positività
>[!example] 
> Trovare le costanti o confutare :$$\log^{2n}(n) + n -log(n)=\Theta(\log(n^{n}))$$

Spesso non è semplice riuscire a trovare adeguate e/o semplici maggiorazioni per tutte le equazioni. Quindi si ricorre ad un metodo diverso, in generale più **meccanico**
1. Eseguiamo il limite come sempre per verificare che la notazione $\Theta$ possa essere applicata
	- Ciò che è stato fatto verificando che il limite abbia un valore $l$ è stato effettivamente trovare un asintoto orizzontale, appunto una retta per la quale il nostro limite del rapporto tende
2. Adesso andiamo a studiare la derivata del nostro rapporto, studiandone la positività, per capire il nostro valore $l$ se sia costante $c_{1}$ o $c_{2}$ della nostra notazione $\Theta$
	- Andando a studiare tale positività, in particolare, ci andremo ad accorgere che: 
		- se la nostra funzione tende a crescere verso l'asintoto orizzontale allora $l$ sarà costante $c_{2}$ (superiore)
		- se la nostra funzione tende a decrescere verso l'asintoto orizzontale allora $l$ sarà costante $c_{1}$ (inferiore)
3.  Dopo aver trovato il valore $l$, andare a sostituire un valore maggiore(minore) di quest ultimo all'interno della nostra funzione rapporto. Il risultato di tale applicazione, è una delle possibili costanti che possiamo usare per la rimanente costante per la notazione $\Theta$ 
>[!note] 
> In generale tutti gli accorgimenti e i consigli che valgono per il procedimento precedentemente spiegato in questo paragrafo valgono per il procedimento corrente