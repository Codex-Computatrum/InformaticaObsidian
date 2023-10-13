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
$$O(g(n))= \left\{ f(n): \exists c \in \mathbb{R}^{+}\;\; \land \;\; \exists n_{0}\in \mathbb{N} \; \text{tale che}\; \forall n\geq n_{0}, f(n)\leq c\;g(n)\right\}$$
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