---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
aliases:
  - funzione-generatrice
---
La ***funzione generatrice dei momenti*** o più semplicemente *funzione generatrice* $\phi$, di una variabile aleatoria $X$, è definita, per tutti i $t$ reali per i quali il [[valore atteso]] di $e^{tX}$ ha senso, dall'espressione $$
\phi(t):=E\left[e^{t X}\right]= \begin{cases}\sum_{x} e^{t x} p(x) & \text { se } X \text { è discreta } \\ \int_{-\infty}^{\infty} e^{t x} f(x) d x & \text { se } X \text { è continua }\end{cases}$$
Il nome adottato deriva dal fatto che tutti i momenti di cui è dotata $X$ possono essere ottenuti derivando più volte nell'origine la funzione $\phi(t)$. Ad esempio, $$
\phi^{\prime}(t)=\frac{d}{d t} E\left[e^{t X}\right]=E\left[\frac{d}{d t} e^{t X}\right]=E\left[X e^{t X}\right]$$ da cui $\phi^{\prime}(0) = E[X]$. Analogamente, $$
\phi^{\prime \prime}(t)=\frac{d^{2}}{d t^{2}} E\left[e^{t X}\right]=E\left[\frac{d^{2}}{d t^{2}} e^{t X}\right]=E\left[X^{2} e^{t X}\right]$$ da cui $\phi^{\prime \prime} = E[X^{2}]$, è il momento secondo di $X$. Più in generale, la derivata $n-$esima di $\phi(t)$ calcolata in $0$ fornisce il momento $n-$esimo di $X$: $$\phi^{(n)}(0)=E\left[X^{n}\right], \quad n \geq 1$$

---
### Proposizione 
Se $X$ e $Y$ sono variabili aleatorie indipendenti con funzioni generatrici $\phi_X$ e $\phi_{Y}$ rispettivamente, e se $\phi_{X+Y}$ è la funzione generatrice dei momenti di $X + Y$ allora $$\phi_{X+Y}(t)=\phi_{X}(t) \phi_{Y}(t)$$ ***Dimostrazione:*** Si noti intanto che se $X$ e $Y$ sono indipendenti, lo sono anche le variabili aleatorie $e^{tX}$ e $e^{tY}$. Infatti occorre mostrare che, comunque si scelgano $A$ e $B$, $$
P\left(e^{t X} \in A, e^{t Y} \in B\right)=P\left(e^{t X} \in A\right) P\left(e^{t Y} \in B\right)$$ D'altra parte, se $A^{\prime}$ è l'insieme formato dai numeri $z$ tali che $e^{tX} \in A$, allora $e^{tX} \in A \iff X \in A^{\prime}$. Se si definisce analogamente $B^{\prime}$, si vede che $$
\begin{array}{rlrl}
P\left(e^{t X} \in A, e^{t Y} \in B\right) & =P\left(X \in A^{\prime}, Y \in B^{\prime}\right) & & \text { per la definizione di } A^{\prime} \text { e } B^{\prime} \\
& =P\left(X \in A^{\prime}\right) P\left(Y \in B^{\prime}\right) & & \text { per l'indipendenza di } X \text { e } Y \\
& =P\left(e^{t X} \in A\right) P\left(e^{t Y} \in B\right) &
\end{array}$$ A questo punto, basta sfruttare il fatto che l'indipendenza implica che la media del prodotto è il prodotto delle medie, per concludere che $$
\begin{aligned}
\phi_{X+Y}(t) & :=E\left[e^{t(X+Y)}\right] \\
& =E\left[e^{t X} e^{t Y}\right] \\
& =E\left[e^{t X}\right] E\left[e^{t Y}\right] \\
& =\phi_{X}(t) \phi_{Y}(t)
\end{aligned}$$

>[!note]-
> Un ulteriore risultato che mostra l'importanza della funzione generatrice dei momenti è che essa *determina la distribuzione*, nel senso che due variabile aleatorie con identica funzione generatrice hanno necessariamente la stessa legge (e quindi la stessa funzione di ripartizione, e la stessa funzione di massa, ovvero la stessa identità).