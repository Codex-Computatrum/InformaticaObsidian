---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - example
---
>[!important]
> Per quanto riguarda la varianza la [[Valore atteso#^prop-valoreAtteso|proprietà del valore atteso]] non è valida. Ad esempio $$
\begin{aligned}
\operatorname{Var}(X+X) & =\operatorname{Var}(2 X) \\
& =2^{2} \operatorname{Var}(X) \\
& =4 \operatorname{Var}(X) \neq \operatorname{Var}(X)+\operatorname{Var}(X)
\end{aligned}$$

Vi è tuttavia un caso importante in cui la varianze della somma di due variabile aleatorie è pari alla somma delle loro varianze, ovvero quando le variabili aleatoria sono indipendenti. Prima di dimostrare questo risultato però, dobbiamo definire il concetto di ***covarianza*** di due variabili aleatorie.

Siano assegnate due variabili aleatorie $X$ e $Y$ di [[Valore atteso|media]] $\mu_{X}$ e $\mu_{Y}$ rispettivamente. La loro ***covarianza***, che si indica con $\operatorname{Cov}(X, Y)$ è (se esiste) la quantità $$
\operatorname{Cov}(X, Y):=E\left[\left(X-\mu_{X}\right)\left(Y-\mu_{Y}\right)\right]$$
Si può ottenere anche una formula alternativa più semplice, analoga a quella qui sopra, per la varianza. Si trova espandendo il prodotto al secondo membro.
$$
\begin{aligned}
\operatorname{Cov}(X, Y) & =E\left[X Y-\mu_{X} Y-\mu_{Y} X+\mu_{X} \mu_{Y}\right] \\
& =E[X Y]-\mu_{X} E[Y]-\mu_{Y} E[X]+\mu_{X} \mu_{Y} \\
& =E[X Y]-\mu_{X} \mu_{Y}-\mu_{X} \mu_{Y}+\mu_{X} \mu_{Y} \\
& =E[X Y]-E[X] E[Y]
\end{aligned}$$
Quindi si deduce la simmetria:

$$\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$$^cov-simmetria

così come la generalizzazione del concetto di [[varianza]] 

$$\operatorname{Cov}(X, X)=\operatorname{Var}(X)$$^cov-var

Un'altro enunciato interessante è che per ogni costante $a$: $$\operatorname{Cov}(a X, Y)=a \operatorname{Cov}(X, Y)=\operatorname{Cov}(X, a Y)$$

---
### Lemma 
Se $X, Y$ e $Z$ sono variabili aleatorie qualsiasi, $$\operatorname{Cov}(X+Y, Z)=\operatorname{Cov}(X, Z)+\operatorname{Cov}(Y, Z)$$ ***Dimostrazione***: $$
\begin{aligned}
\operatorname{Cov}(X+Y, Z) & =E[(X+Y) Z]-E[X+Y] E[Z] \\
& =E[X Z+Y Z]-\{E[X]+E[Y]\} E[Z] \\
& =E[X Z]-E[X] E[Z]+E[Y Z]-E[Y] E[Z] \\
& =\operatorname{Cov}(X, Z)+\operatorname{Cov}(Y, Z) \quad \square
\end{aligned}$$
Il lemma può essere facilmente generalizzato a più di due variabili aleatoria, ottenendo che, se $X_{1}, \dots, X_{n}$ e $Y$ sono variabili aleatorie qualsiasi: $$
\operatorname{Cov}\left(\sum_{i=1}^{n} X_{i}, Y\right)=\sum_{i=1}^{n} \operatorname{Cov}\left(X_{i}, Y\right)$$
### Proposizione
Se $X_{1}, \dots, X_{n}$ e $Y_{1}, \dots, Y_{n}$ sono variabili aleatorie qualsiasi: $$
\operatorname{Cov}\left(\sum_{i=1}^{n} X_{i}, \sum_{j=1}^{m} Y_{j}\right)=\sum_{i=1}^{n} \sum_{j=1}^{m} \operatorname{Cov}\left(X_{i}, Y_{j}\right)$$ ***Dimostrazione:*** $$
\begin{aligned}
& \operatorname{Cov}\left(\sum_{i=1}^{n} X_{i}, \sum_{j=1}^{m} Y_{j}\right)=\sum_{i=1}^{n} \operatorname{Cov}\left(X_{i}, \sum_{j=1}^{m} Y_{j}\right)\\
& =\sum_{i=1}^{n} \operatorname{Cov}\left(\sum_{j=1}^{m} Y_{j}, X_{i}\right)  \\
& =\sum_{i=1}^{n} \sum_{j=1}^{m} \operatorname{Cov}\left(Y_{j}, X_{i}\right) 
\end{aligned}$$ Il risultato richiesto segue allora applicando una seconda volta la proprietà di simmetria data dall'[[Covarianza#^cov-simmetria|equazione]].
Utilizzando a questo punto l'[[Covarianza#^cov-var|equazione]] sulla variabile aleatoria $\sum\limits_{i}X_{i}$, si ottiene finalmente la formula che fornisce la varianza di una somma di variabili aleatorie.
$$
\begin{aligned}
\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right) & =\operatorname{Cov}\left(\sum_{i=1}^{n} X_{i}, \sum_{j=1}^{n} X_{j}\right) \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n} \operatorname{Cov}\left(X_{i}, X_{j}\right) \\
& =\sum_{i=1}^{n} \operatorname{Var}\left(X_{i}\right)+\sum_{i=1}^{n} \sum_{\substack{j=1 \\
j \neq i}}^{n} \operatorname{Cov}\left(X_{i}, X_{j}\right)
\end{aligned}$$
Nel caso in cui $n=2$, l'equazione soprastante si riduce a $$
\begin{aligned}
\operatorname{Var}(X+Y) & =\operatorname{Var}(X)+\operatorname{Var}(Y)+\operatorname{Cov}(X, Y)+\operatorname{Cov}(Y, X) \\
& =\operatorname{Var}(X)+\operatorname{Var}(Y)+2 \operatorname{Cov}(X, Y)
\end{aligned}$$

>[!important] ## Teorema
> Se $X$ e $Y$ sono variabili aleatorie indipendenti, allora $$E[XY] = E[X]E[Y]$$ Questo implica inoltre che $$Cov(X, Y) = 0$$ e quindi che, se $X_{1}, \dots, X_{n}$ sono indipendenti, $$\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right)=\sum_{i=1}^{n} \operatorname{Var}\left(X_{i}\right)$$
> ***Dimostrazione*** Proviamo che  $E[XY] = E[X]E[Y]$. Se $X$ e $Y$ sono entrambe discrete: $$
\begin{aligned}
E[X Y] & =\sum_{i} \sum_{j} x_{i} y_{j} P\left(X=x_{i}, Y=y_{j}\right) \\
& =\sum_{i} \sum_{j} x_{i} y_{j} P\left(X=x_{i}\right) P\left(Y=y_{j}\right) \\
& =\sum_{i} x_{i} P\left(X=x_{i}\right) \sum_{j} y_{j} P\left(Y=y_{j}\right) \\
& =E[X] E[Y]
\end{aligned}$$

>[!example]- Si determini la varianza del numero di teste su $10$ lanci indipendenti di una moneta non truccata.
> Sia $I_{f}$ la funzione indicatrice dell'evento "il lancio $j-$esimo è testa": $$
I_{j}:= \begin{cases}1 & \text { se il lancio } j \text {-esimo è testa } \\ 0 & \text { se il lancio } j \text {-esimo è croce }\end{cases}$$
> Allora, il numero totale di test è $\sum_{j=1}^{10}I_{f}$, e quindi grazie all'indipendenza, $$
\operatorname{Var}\left(\sum_{j=1}^{10} I_{j}\right)=\sum_{j=1}^{10} \operatorname{Var}\left(I_{j}\right)$$
> Siccome $I_{f}$ è la funzione indicatrice di un evento con probabilità $\frac{1}{2}$, segue che la varianza di una singola $I_{f}$ e della somma di tutte e $10$ sono, $$
\begin{aligned}
& \operatorname{Var}\left(I_{j}\right)=\frac{1}{2}\left(1-\frac{1}{2}\right)=\frac{1}{4} \\
& \operatorname{Var}\left(\sum_{j=1}^{10} I_{j}\right)=10 \cdot \frac{1}{4}=\frac{5}{2}
\end{aligned}$$

Se due variabili aleatoria non sono indipendenti, la loro covarianza è un importante indicatore della relazione che sussiste tra loro. Come esempio, si consideri la situazione in cui $X$ e $Y$ sono le funzioni indicatrici di due eventi $A$ e $B$, ovvero $$
X:=\left\{\begin{array}{ll}
1 & \text { se } A \text { si verifica } \\
0 & \text { altrimenti }
\end{array}, \quad Y:= \begin{cases}1 & \text { se } B \text { si verifica } \\
0 & \text { altrimenti }\end{cases}\right.$$
Si noti intanto che anche $XY$ è una funzione indicatrice: $$
X Y= \begin{cases}1 & \text { se } X=1, Y \stackrel{ }{=} 1 \\ 0 & \text { altrimenti }\end{cases}$$ Si ottiene quindi che $$
\begin{aligned}
\operatorname{Cov}(X, Y) & =E[X Y]-E[X] E[Y] \\
& =P(X=1, Y=1)-P(X=1) P(Y=1)
\end{aligned}$$ da cui deduciamo che $$
\begin{aligned}
\operatorname{Cov}(X, Y)>0 & \Leftrightarrow P(X=1, Y=1)>P(X=1) P(Y=1) \\
& \Leftrightarrow \frac{P(X=1, Y=1)}{P(Y=1)}>P(X=1) \\
& \Leftrightarrow P(X=1 \mid Y=1)>P(X=1)
\end{aligned}$$

>[!important] 
> Perciò la covarianza di $X$ e $Y$ è positiva se condizionando $\{Y=1\}$, è più probabile che $X=1$ (si noti che vale anche l'enunciato simmetrico)
> In generale si può mostrare che un valore positivo di $\operatorname{Cov}(X,Y)$ indca che $X$ e $Y$ tendenzialmente assumono valori grandi o piccoli contemporaneamente. La forza della relazione tra $X$ e $Y$ è misurata più precisamente dal *coefficiente di correlazione lineare*, un numero puro (senza unità di misura) che tiene conto anche delle deviazioni standard di $X$ e $Y$[^1]. Esso si indica con $\operatorname{Corr}(X, Y)$ ed è definito come $$
\operatorname{Corr}(X, Y):=\frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X) \operatorname{Var}(Y)}}$$
 > Si può dimostrare che questa quantità è sempre compra tra $-1$ e $+1$
 
 [^1]: Si noti infatti come la covarianza tra $2X$ e $2Y$ sia sempre molto più forte (quattro volte maggiore in effetti) di quella tra $X$ e $Y$. Per il coeffciente di correlazione lineare invece, le due situazioni portano al medesimo valore




