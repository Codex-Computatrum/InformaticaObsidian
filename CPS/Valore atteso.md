---
tags: [definition, aleatoryVariable, statistics]
alias: [aspettazione, media, momento-primo]
author: Lorenzo Tecchia
---
>[!definition]
> Sia $X$ una [[variabile aleatoria]] discreta che può assumere i valori $x_{1},x_{2}, \dots$; il **valore atteso** di $X$, che si indica con $E[X]$, è (se esiste[^1]) il numero:$$E[X] := \sum\limits_{i}x_{i}\mathbb{P}(X = x_{i})$$

In altri termini si tratta della media pesata dei valori possibili di $X$, usando come pesi le [[probabilità]] che tali valori vengano assunti da $X$. Per questo $E[X]$ è anche detta media di $X$, oppure **aspettazione**.

>[!example]- Per illustrare il concetto di media pesata, facciamo un semplice esempio.
> Se $X$ è una variabile aleatoria con [[funzione]] di massa: $$p(0) = \frac{1}{2}= p(1)$$ allora
> $$E[X] = 0 \times \frac{1}{2}+ 1 \times \frac{1}{2}= \frac{0+1}{2}=\frac{1}{2}$$
> é semplicemente la media aritmetica dei valori che $X$ può assumere. Però, se$$p(0) = \frac{1}{3}, \quad p(1) = 2/3$$ allora
> $$E[X] = 0 \times \frac{1}{3}+1 \times \frac{2}{3}=\frac{0+1\times2}{3}= \frac{2}{3}$$
> è una media pesata degli stessi valori $0$ e $1$, dove al secondo è stato dato un peso che è il doppio di quello del primo.

[^1]:Il valore atteso di $X$ è definito solo se la serie converge in valore assoluto, ovvero deve valere:$$\sum\limits_{i}^{X}|x_{i}|\mathbb{P}(X = x_{i})< \infty$$ In caso contrario si dice che $X$ non ha valore atteso.

---
>[!example]- Sia $X$ il punteggio che si ottiene lanciando un dado non truccato, quanto vale $E[X]$?
> Siccome $\mathcal{p}(1)=\mathcal{p}(2)=\mathcal{p}(3)=\mathcal{p}(4)=\mathcal{p}(5) = \mathcal{p}(6)=\frac{1}{6}$, ricaviamo che $$
E[X]:=1 \cdot \frac{1}{6}+2 \cdot \frac{1}{6}+3 \cdot \frac{1}{6}+4 \cdot \frac{1}{6}+5 \cdot \frac{1}{6}+6 \cdot \frac{1}{6}=\frac{7}{2}=3.5$$^esempio-valoreAtteso-dadoOnesto

>[!note]-
> Il valore atteso di $X$ non è uno dei valori che $X$ può assumere. Perciò anche se $E[X]$ è chiamato ***valore atteso*** di $X$, non vuole affatto dire che noi ci attendiamo di vedere questo valore, ma piuttosto che ci aspettiamo che sia il limite a cui tende il punteggio medio del dado su un numero crescente di ripetizioni


>[!example] Valore atteso della funzione indicatrice di un [[evento]] $A$
> Sia definita tale funzione $I$ in questo modo: $$
I:= \begin{cases}1 & \text { se } A \text { si verifica } \\ 0 & \text { se } A \text { non si verifica }\end{cases}$$
> allora $$E[I]:=1 \cdot P(I=1)+0 \cdot P(I=0)=P(I=1)=P(A)$$
> Quindi il valore atteso della funzione indicatrice di un evento è la possibilità di quest'utlimo.

---
# Proprietà del valore atteso
Se anziché voler calcolare il valore atteso di $X$, interessasse determinare quello di una sua qualche funzione $g(X)$, come potremmo fare?

Una prima strada è notare che $g(X)$ stessa è una variabile aleatoria, e quindi ha una sua [[distribuzione]] che in qualche modo si può ricavare; dopo averla ottenuta, il valore atteso $E[g(X)]$ si calcola con la definizione usuale applicata alla nuova variabile aleatoria

>[!example]-
> Quanto vale il valore atteso del quadrato di una variabile aleatoria $X$ con funzione di massa seguente? $$p(0)=0.2, \quad p(1)=0.5, \quad p(2)=0.3$$
> Poniamo $Y := X^{2}$. Questa è una variabile aleatoria che può assumere i valori $0^{2}$, $1^{2}$ e $2^{2}$, con probabilità: $$
\begin{aligned}
& p_{Y}(0):=P\left(Y=0^{2}\right)=0.2 \\
& p_{Y}(1):=P\left(Y=1^{2}\right)=0.5 \\
& p_{Y}(4):=P\left(Y=2^{2}\right)=0.3
\end{aligned}$$
> Quindi $$ E\left[X^{2}\right]=E[Y]=0 \cdot 0.2+1 \cdot 0.5+4 \cdot 0.3=1.7$$

>[!note] ### Proposizione
> 1. Se $X$ è una variabile aleatoria discreta con funzione di massa di probabilità $\mathcal{p}$, allora, per ogni funzione reale $g$ : $$E[g(X)]=\sum_{x} g(x) p(x)$$
> 2. Se $X$ è una variabile aleatoria continua con funzione di densità di probabilità $f$ allora, per ogni funzione reale $g$: $$E[g(X)]=\int_{-\infty}^{\infty} g(x) f(x) d x$$
>> [!note]- #### Corollario
>> Per ogni coppia di costanti reali $a$ e $b$: $$E[aX + b] = aE[X] + b$$
>> **Dimostrazione**. 
>> Nel caso discreto: $$\begin{aligned}E[a X+b] & =\sum_{x}(ax+b) p(x) \\& =a \sum_{x} x p(x)+b \sum_{x} p(x) \\& =a E[X]+b \end{aligned}$$
>> Nel caso continuo: $$\begin{aligned} E[a X+b] & =\int_{-\infty}^{\infty}(a x+b) f(x) d x \\ & =a \int_{-\infty}^{\infty} x f(x) d x+b \int_{-\infty}^{\infty} f(x) d x \\ & =a E[X]+b \end{aligned}$$
>> Se nel corollario si pone $a=0$, si scopre che $$E[b] = b$$^corollario-valoreAtteso

In altri termini, il valore atteso di una costante, è semplicemente il suo valore stesso. Se invece si pone $b= 0$, si ottiene che $$E[aX] = aE[X]$$ Ovvero il valore atteso di un fattore costante moltiplicato per una variabile aleatoria, è pari alla costante per il valore atteso della variabile aleatoria.

Come già accennato, il termine **valore atteso** ha tra i suoi sinonimi *aspettazione* e *media*. Un ulteriore denominazione è quella di ***momento primo***, con riferimento alla definizione seguente:

>[!note] ## Definizione
> Se $n =1,2,\dots$, la quantità $E[X^{n}]$, quando esiste[^1] è detta momento $n-$esimo della variabile aleatoria $X$.
> Volendo esser più espliciti, si può applicare il [[Valore atteso#^corollario-valoreAtteso|corollario]] per ricavare, $$
E\left[X^{n}\right]= \begin{cases}\sum_{x} x^{n} p(x) & \text { se } X \text { è discreta } \\ \int_{-\infty}^{\infty} x^{n} f(x) d x & \text { se } X \text { è continua }\end{cases}$$

---
La versione in due dimensioni della prima proposizione sopra citata afferma che se $X$ e $Y$ sono due variabile aleatorie e $g$ è una qualunque funzione di due variabili, allora, se $E[g(X, Y)]$ esiste, $$
E[g(X, Y)]= \begin{cases}\sum_{x} \sum_{y} g(x, y) p(x, y) & \text { nel caso discreto } \\ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f(x, y) d x d y & \text { nel caso continuo }\end{cases}$$ Si può applicare questo enunciato a $g(X, Y) = X + Y$, ottenendo che 

$$E[X+Y]=E[X]+E[Y]$$^prop-valoreAtteso

Tale risultato è valido sia nel caso discreto, sia in quello continuo, come è dimostato dai passaggi seguenti: $$
\begin{aligned}
E[X+Y] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}(x+y) f(x, y) d x d y \\
& =\int_{-\infty}^{\infty} x\left[\int_{-\infty}^{\infty} f(x, y) d y\right] d x+\int_{-\infty}^{\infty} y\left[\int_{-\infty}^{\infty} f(x, y) d x\right] d y \\
& =\int_{-\infty}^{\infty} x f_{X}(x) d x+\int_{-\infty}^{\infty} y f_{Y}(y) d y, \\
& =E[X]+E[Y]
\end{aligned}$$
Applicando ricorsivamente l'[[Valore atteso#^prop-valoreAtteso|equazione]] si può estendere la portata alla somma di un numero finito di variabili aleatoria. Ad esempio $$
\begin{array}{rlrl}
E[X+Y+Z] & =E[(X+Y)+Z] & & \\
& =E[X+Y]+E[Z] \\
& =E[X]+E[Y]+E[Z] X \text { e } Y
\end{array}$$
E in generale, per ogni $n$, $$
E\left[X_{1}+X_{2}+\cdots+X_{n}\right]=E\left[X_{1}\right]+E\left[X_{2}\right]+\cdots+E\left[X_{n}\right]$$

>[!example]- In un prodotto commerciale vengono inseriti dei buoni sconto in regalo. Vi sono $20$ tipi diversi di buoni, e in ogni confezione se ne trova uno qualsiasi con pari probabilità. Se si aprono $10$ confezioni, quant'è il valore atteso del numero di tipi diversi di buoni sconto che si trovano?
> Sia $X$ il numero di tipi diversi di buoni che troviamo nelle $10$ confezioni. Allora $X = X_{1}+ \dots + X_{20}$ dove $$
X_{i}:= \begin{cases}1 & \text { se il tipo } i \text {-esimo di buoni è presente nelle } 10 \text { confezioni } \\ 0 & \text { altrimenti }\end{cases}$$ Le $X_{i}$ si studiano facilmente, $$
\begin{aligned}
E\left[X_{i}\right] & =P\left(X_{i}=1\right) \\
& =P(\text { il tipo } i \text {-esimo di buoni è presente nelle } 10 \text { confezioni }) \\
& =1-P(\text { il tipo } i \text {-esimo di buoni non è presente nelle } 10 \text { confezioni }) \\
& =1-\left(\frac{19}{20}\right)^{10}
\end{aligned}$$ dove l'ultima uguaglianza segue dal fatto che ciascuno dei $10$ buoni sarà di tipo diverso da quello $i-$esimo (indipendentemente) con probabilità $\frac{19}{20}$. Concludendo, $$
E[X]=E\left[X_{1}\right]+\cdots+E\left[X_{20}\right]=20\left[1-\left(\frac{19}{20}\right)^{10}\right] \approx 8.025$$
>> [!note]
>> Vi è una interessante proprietà della media che emerge quando si vuole *predire* con il minore errore possibile il valore che verrà assunto da una variabile aleatoria. Supponiamo di voler predire il valore di $X$. Se scegliamo un numero reale $c$ e diciamo che $X$ sarà grande uguale a $c$, il quadrato dell'errore che commetteremo è $(X-c)^{2}$. Mostriamo di seguito che la media dell'errore al quadrato[^2] è minimizzata se per $c$ scegliamo il valore della media di $X$. Infatti, detta $\mu := E[X]$. $$
\begin{aligned}
E\left[(X-c)^{2}\right] & =E\left[(X-\mu+\mu-c)^{2}\right] \\
& =E\left[(X-\mu)^{2}+2(X-\mu)(\mu-c)+(\mu-c)^{2}\right] \\
& =E\left[(X-\mu)^{2}\right]+2(\mu-c) E[X-\mu]+(\mu-c)^{2} \\
& =E\left[(X-\mu)^{2}\right]+(\mu-c)^{2} \quad \text { infatti } E[X-\mu]=E[X]-\mu=0 \\
& \geq E\left[(X-\mu)^{2}\right]
\end{aligned}$$
>> Perciò la migliore previsione di $X$, in termini di minimizzazione dell'errore quadratico medio, è la sua aspettazione

[^2]: Più comunemente chiamato *errore quadratico medio*.