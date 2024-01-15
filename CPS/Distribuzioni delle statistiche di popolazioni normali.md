---
author: Lorenzo Tecchia
tags: [definition, example, recap, statistics, probability]
---
Sia $X_{1}, X_{2}, \dots, X_{n}$ un [[campione]] estratto da una [[distribuzione]] [[Gaussiana|normale]] gaussiana, anche $\overline{X}$ è normale. La sua [[Valore atteso|media]] e la sua varianza, come nel caso generale, sono $\mu$ e varianza $\sigma^{2}/n$ rispettivamente, e quindi $$
\frac{\bar{X}-\mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1)$$ è una [[variabile aleatoria]] normale standard[^1]

[^1]: A differenza di questo [[Media campionaria#^a77156|caso]] non vi sono approssimazioni: il risultato ottenuto è esatto, grazie all'ipotesi aggiuntiva che $X_{i}$ fossero guassiane. Inoltre, quanto detto qui vale anche quando $n$ è piccolo.

---
## Distribuzione congiunta di $\overline{X}$ e $S^{2}$
Deriveremo la distribuzione della [[varianza]] campionaria $S^{2}$, ma enunciamo anche il fatto fondamentale che $\overline{X}$e $S^{2}$ sono variabili aleatorie indipendenti, con $$(n-1) \frac{S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}$$
Per iniziare si noti che, assegnati dei numeri $x_{1}, x_{2}, \dots, x_{n}$ e posto $y_{i}:= x_{i}- \mu$ per $i=1, 2, \dots, n$ dall'identità $$
\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}=\sum_{i=1}^{n} y_{i}^{2}-n \bar{y}^{2}$$ si deduce che $$
\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}=\sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}-n(\bar{x}-\mu)^{2}$$
Se applichiamo questa seconda identità ad un [[campione]] $X_{1}, X_{2}, \dots, X_{n}$ di una [[popolazione]] normale con media $\mu$ e varianza $\sigma^{2}$, otteniamo che $$
\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{X}\right)^{2}}{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{\sigma^{2}}-\frac{n(\bar{X}-\mu)^{2}}{\sigma^{2}}$$ o equivalentemente $$
\sum_{i=1}^{n}\left(\frac{X_{i}-\mu}{\sigma}\right)^{2}=\frac{\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}}{\sigma^{2}}+\left[\frac{\sqrt{n}(\bar{X}-\mu)}{\sigma}\right]^{2}$$

>[!important] ### Teorema
> Se $X_{1}, X_{2}, \dots, X_{n}$ è un campione proveniente da una distribuzione normale di media $\mu$ e varianza $\sigma^{2}$, allora $\overline{X}$ e $S^{2}$ sono variabili aleatoria indipendenti. 
> Inoltre, $\overline{X}$ è normale con media $\mu$ e varianza $\sigma^{2}/n$, e $(n-1)S^{2}/\sigma^{2}$ è una [[chi-quadro]] con $n-1$ gradi di libertà.
> > [!note]-
> > Questo teorema non solo ci fornisce le distribuzioni di $\overline{X}$ e $S^{2}$ per le popolazioni gaussiane, ma stabilisce anche l'importante proprietà, unica della distribuzione normale, che queste statistiche sono indipendenti.

>[!example]-
>Il tempo impiegato da un microprocessore ad eseguire alcuni processi è una variabile aleatoria normale con media di $30$ secondi e deviazione standard di $3$ secondi. Se si osserva l'esecuzione di un campione di $15$ processi, qual è la [[probabilità]] che la [[varianza campionaria]] risultante sia maggiore di $12$?
>Siccome l'ampiezza del campione è $n=15$, e $\sigma^{2}=9$, scriviamo$$
\begin{aligned}
\mathbb{P}\left(S^{2}>12\right) & =\mathbb{P}\left((n-1) \frac{S^{2}}{\sigma^{2}}>14 \cdot \frac{12}{9}\right) \\
& \approx \mathbb{P}\left(\chi_{14}^{2}>18.67\right) \\
& \approx 1-0.8221=0.1779
\end{aligned}$$

>[!important] ### Corollario
> Sia $X_{1}, X_{2}, \dots, X_{n}$ un campione proveniente da una [[popolazione]] gaussiana di media $\mu$. Se $\overline{X}$ e $S^{2}$ denotano la media e la varianza campionaria, allora $$\frac{\bar{X}-\mu}{S / \sqrt{n}} \sim t_{n-1}$$
> Quindi, se si normalizza $\overline{X}$ sottraendo la sua media $\mu$ e dividendo per la sua deviazione standard $\sigma/\sqrt{n}$, si ha una [[distribuzione t]] con $n-1$ gradi di libertà.
> ***Dimostrazione:*** Si ricordi che la $t$ *di Student* con $m$ gradi di libertà, è per definizione, la distribuzione del rapporto $$\frac{Z}{\sqrt{\chi_{m}^{2} / m}}$$ dove $Z \sim \mathcal{N}(0, 1), \chi^{2}_{m}$ è una [[chi-quadro]] con $m$ gradi di libertà, e queste due variabile aleatorie sono prese indipendenti. Allora, usando il fatto che $$\frac{\bar{X}-\mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1) \quad(n-1) \frac{S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}$$ e inoltre che queste due statistiche sono indipendenti per il teorema soprastante, si ottiene che $$\frac{\bar{X}-\mu}{\sigma / \sqrt{n}} \sqrt{\frac{\sigma^{2}}{S^{2}} \frac{n-1}{n-1}}=\frac{\bar{X}-\mu}{S }{ \sqrt{n}} \qquad \square $$ è una $t$ *Student* con $n-1$ gradi di libertà.


