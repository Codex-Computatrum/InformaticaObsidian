---
author: Lorenzo Tecchia
tags:
  - probability
  - definition
  - to-do
  - distribution
  - example
---
>[!todo] Inserire grafico

Supponiamo di realizzare $n$ ripetizioni indipendenti di un esperimento, ciascuna delle quali può concludersi in un "successo" con probabilità $p$, o in un fallimento con probabilità $1-p$. Se $X$ denota il numero totale di successi, $X$ si dice variabile aleatoria *binomiale* di parametri $(n,p)$
La funzione di massa di probabilità per una variabile aleatoria binomiale di parametri $(n,p)$ è data da $$\mathbb{P}(X = i) = \binom{n}{i}p^{i}(1-p)^{n-i}, \;\;\;\;\; i = 0,1,\dots$$
dove ricordiamo il coefficiente binomiale:![[Coefficiente Binomiale]]

>[!important]
> La somma delle probabilità di tutti i valori possibili di una variabile aleatoria binomiale, è pari ad $1$ per la formula delle potenze del binomio:$$\sum_{i}\mathbb{P}(X = i) = \sum_{i=0}^{n}\binom{n}{i}p^{i}(1-p)^{n-i} = [p + (1-p)]^{n} = 1$$

>[!example]-
> Una azienda produce dischetti per PC che sono difettosi con probabilità $0.01$, indipendentemente l'uno dall'altro. Questi dischetti sono poi venduti in confezioni da $10$ pezzi, con la garanzia di rimborso in caso vi sia più di un pezzo difettoso. Che percentuale delle confezioni viene ritornata?
> Se $X$ è il numero di pezzi difettosi in una scatola da $10$ dischetti, $X$ è una variabile aleatoria binomiale di parametri $(19, 0.01)$. Perciò, assumendo che tutti i clienti che ne hanno la possibilità sfruttino la garanzia, la probabilità che una scatola sia ritornata è pari a $$
\begin{aligned}
\mathbb{P}(X>1) & =1-\mathbb{P}(X=0)-\mathbb{P}(X=1) \\
& =1-\left(\begin{array}{c}
10 \\
0
\end{array}\right) \cdot 0.01^{0} \cdot 0.99^{10}-\left(\begin{array}{c}
10 \\
1
\end{array}\right) \cdot 0.01^{1} \cdot 0.99^{9} \approx 0.0043
\end{aligned}$$
> Poiché ogni scatola, indipendentemente dalle altre, viene resa con probabilità di circa $0.43\%$, a lungo andare sarà reso circa lo $0.43\%$ delle confezioni. Da quanto detto segue inoltre, che acquistando $3$ scatole, il numero di quelle che verranno rese è una variabile aleatoria binomiale di parametri $(3, 0.0043)$, quindi la probabilità richiesta è $$\binom{3}{1}\cdot 0.0043^{1}\cdot 0.9957^{2}\approx 0.013 \quad \square$$

---

Per come è stata definita la variabile aleatoria binomiale di parametri $(n, p)$ (il numero di esperimenti con esito positivo, su $n$ ripetizione indipendenti, ciascuna con probabilità di successo $p$), essa può essere rappresentata come somma di bernoulliane. Più precisamente, se $X$ è binomiale di parametri $(n, p)$, si può scrivere $$X=\sum_{i=1}^{n} X_{i}$$ dove $X_{i}$ è la funzione indicatrice del successo dell' $i-$esimo esperimento: $$X_{i}:= \begin{cases}1 & \text { se la prova } i \text {-esima ha successo } \\ 0 & \text { altrimenti }\end{cases}$$
È evidente che le $X_{i}$ sono benoulliane di parametro $p$, quindi abbiamo che $$
\begin{array}{rlrl}
E\left[X_{i}\right] & =p & & \text { per la (5.1.2) } \\
E\left[X_{i}^{2}\right] & =p & & \text { infatti } X_{i} \equiv X_{i}^{2} \\
\operatorname{Var}\left(X_{i}\right) & =E\left[X_{i}^{2}\right]-E\left[X_{i}\right]^{2} & \\
& =p-p^{2}=p(1-p)
\end{array}$$
Per quanto riguarda $X$, poi dalle proprietà di media e varianza diciamo che $$
\begin{aligned}
E[X] & =\sum_{i=1}^{n} E\left[X_{i}\right]=n p \\
\operatorname{Var}(X) & =\sum_{i=1}^{n} \operatorname{Var}\left(X_{i}\right) \quad \text { per l'indipendenza delle } X_{i} \\
& =n p(1-p)
\end{aligned}$$
