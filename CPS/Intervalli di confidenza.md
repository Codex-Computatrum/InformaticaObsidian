---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - sampling
  - probability
  - parametricEstimation
  - distribution/normal
---
Sia $X_{1}, X_{2}, \dots, X_{n}$ un [[campione]] estratto da una [[popolazione]] [[Gaussiana|normale]] di [[Valore atteso|media]] incognita $\mu$ e [[varianza]] nota $\sigma^{2}$. Avviamo in precedenza dimostrato che $\overline{X} := \sum_{i}X_{i}/n$ è lo stimatore di massima verosimiglianza per $\mu$. Ciò non significa che  possiamo aspettarci che la [[Valore atteso|media]] sia esattamente uguale  $\mu$, ma solo che le sarà vicina.
Perciò, rispetto ad uno stimatore puntuale, è a volte preferibile poter produrre un intervallo per il quale abbiamo un certo livello di fiducia (confidenza), che il parametro $\mu$ vi appartenga. Per ottenere un tale ***intervallo di confidenza***, dobbiamo fare uso della [[distribuzione]] di [[probabilità]] dello stimatore puntuale. 

Ricordiamo intanto che nelle ipotesi in cui ci siamo messi, $\overline{X}$ è [[Gaussiana|normale]] di media $\mu$ e [[varianza]] $\sigma^{2}/n$. Ne segue che $$\frac{\bar{X}-\mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1)$$
Perciò $$\mathbb{P}\left(-1.96<\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<1.96\right) \approx 0.95$$ o equivalentemente,
$$
\mathbb{P}\left(-1.96 \frac{\sigma}{\sqrt{n}}<\bar{X}-\mu<1.96 \frac{\sigma}{\sqrt{n}}\right) \approx 0.95
$$
da cui, moltiplicando le disuguaglianza per $-1$, 
$$
\mathbb{P}\left(1.96 \frac{\sigma}{\sqrt{n}}>\mu-\bar{X}>\ddot{-1.96} \frac{\sigma}{\sqrt{n}}\right) \approx 0.95$$
ovvero, finalmente, 
$$
\mathbb{P}\left(\bar{X}-1.96 \frac{\sigma}{\sqrt{n}}<\mu<\bar{X}+1.96 \frac{\sigma}{\sqrt{n}}\right) \approx 0.95$$

Il $95\%$ circa delle volte $\mu$ starà ad una distanza non superiore a $1.96\sigma/\sqrt{n}$ dalla [[media aritmetica]] dei dati. Se osserviamo il campione, e registriamo che $\overline{X} = \bar{x}$ allora possiamo dire che "con il $95\%$ di confidenza" $$\bar{x}-1.96 \frac{\sigma}{\sqrt{n}}<\mu<\bar{x}+1.96 \frac{\sigma}{\sqrt{n}}$$ 
Stiamo quindi affermando che, con il $95\%$ di confidenza, la media vera della distribuzione appartiene all'intervallo $$\left(\bar{x}-1.96 \frac{\sigma}{\sqrt{n}}, \quad \bar{x}+1.96 \frac{\sigma}{\sqrt{n}}\right)$$
>[!important] Questo intervallo è detto ***intervallo di confidenza ad un livello del $95\%$***, o più semplicemente ***intervallo di confidenza al $95\%$*** per $\mu$

>[!example]-
> Supponiamo che quando un segnale elettrico di valore $\mu$ viene trasmesso dalla sorgente $A$, il ricevente $B$ registri un valore distribuito come una [[Gaussiana|normale]] di [[Valore atteso|media]] $\mu$ e [[varianza]] $4$. Altrimenti detto, se $\mu$ è il segnale inviato, quello ricevuto è $\mu + N$, dove $N$ denota il rumore, ed è $N \approx \mathcal{N}(0, 4)$. Immaginiamo che per riprodurre l'errore, lo stesso segnale è stato trasmesso $9$ volte. I valori registrati da $B$ in ricezione sono stati $$\begin{array}{lllllllll}5 & 8.5 & 12 & 15 & 7 & 9 & 7.5 & 6.5 & 10.5\end{array}$$
> Cerchiamo di ottenere un intervallo di confidenza al $95\%$ per $\mu$.
> Siccome $$\bar{x}=\frac{81}{9}=9$$ ne segue, sotto l'ipotesi aggiuntiva che i valori ricevuti siano indipendenti, che un intervallo di confidenza al $95\%$ per $\mu$ è $$
\left(9-1.96 \frac{2}{3}, \quad 9+1.96 \frac{2}{3}\right)=(7.69,10.31)$$
> Perciò possiamo dire di avere il "$95\%$ di fiducia" che il vero messaggio fosse compreso tra $7,69$ e $10.31$

>[!important]
> Gli intervalli di confidenza trovati fin qui sono detti in particolare *bilaterali*, perché hanno due estremi infiniti. 

Altre volte invece siamo interessati a determinare un singolo valore che ci permetta ad esempio di affermare con il $95\%$ di confidenza che $\mu$ è superiore. 
Per trovare un valore siffatto, si noti che se $Z$ e $\mathcal{N}(0, 1)$, allora $$
\begin{aligned}
0.95 & \approx P(Z<1.645) \\
& \approx P\left(\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<1.645\right) \\
& \approx P\left(\bar{X}-1.645 \frac{\sigma}{\sqrt{n}}<\mu\right)
\end{aligned}$$ così che un intervallo di confidenza unilaterale destro ad un livello del $95\%$ per $\mu$ è il seguente, $$\left(\bar{x}-1.645 \frac{\sigma}{\sqrt{n}}, \infty\right)$$ dove $\bar{x}$ è il valore che si osserva per la [[Valore atteso|media]] campionaria.

![](https://cdn.mathpix.com/cropped/2023_11_20_03d5e6ef9957032926fdg-127.jpg?height=242&width=542&top_left_y=206&top_left_x=1924)

Si possono analogamente definire anche gli intervalli di confidenza unilaterali sinistri, e ad esempio dello al $95\%$ per $\mu$ è $$\left(-\infty, \quad \bar{x}+1.645 \frac{\sigma}{\sqrt{n}}\right)$$

>[!example]- Si determino al $95\%$ di confidenza degli intervalli destro e sinistro per il parametro $\mu$ per l'esmpio precedente
> Siccome $$1.645 \frac{\sigma}{\sqrt{n}}=\frac{3.29}{3} \approx 1.097$$ l'intervallo destro al $95\%$ è $$(9-1.097, \infty)=(7.903, \infty)$$ mentre quello sinistro è $$(-\infty, 9+1.097)=(-\infty, 10.097)$$

Si possono ottenere intervalli di confidenza per ogni livello di confidenza assegnato. Si ricordi che avevamo definito i numeri $z_{\alpha}$ in modo tale che $$\mathbb{P}\left(Z>z_{\alpha}\right)=\alpha$$ dove $Z \sim \mathcal{N}(0, 1)$. Questo implica che per ogni $\alpha \in (0,1)$ $$P\left(-z_{\alpha / 2}<Z<z_{\alpha / 2}\right)=1-\alpha$$
Da questa equazione si deduce facilmente che $$
\begin{aligned}
1-\alpha & =P\left(-z_{\alpha / 2}<\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<z_{\alpha / 2}\right) \\
& =P\left(-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}<\bar{X}-\mu<z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right) \\
& =P\left(z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}>\mu-\bar{X}>-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right) \\
& =P\left(\bar{X}-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}<\mu<\bar{X}+z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right)
\end{aligned}$$
Quindi un intervallo di confidenza bilaterale ad un livello di $1-\alpha$ per $\mu$ è $$
\left(\bar{x}-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}, \quad \bar{x}+z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right)$$ dove $\bar{x}$ è il valore che si osserva per la [[Valore atteso|media]] campionaria.
In maniera del tutto analoga, dal fatto che $$Z:=\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}$$ è una [[Gaussiana|normale]] standard, e dalle identità $$
\begin{array}{r}
P\left(Z>z_{\alpha}\right)=\alpha \\
P\left(Z<-z_{\alpha}\right)=\alpha
\end{array}$$ si deducono gli intervalli di confidenza unilaterali per qualunque livello di confidenza. 
In particolare si ottiene che $$
\left(\bar{x}-z_{\alpha} \frac{\sigma}{\sqrt{n}}, \infty\right) \quad \text { e } \quad\left(-\infty, \quad \bar{x}+z_{\alpha} \frac{\sigma}{\sqrt{n}}\right)$$ sono gli intervalli di confidenza unilaterali ad un livello di $1-\alpha$ per $\mu$.

---
>[!tip] ## Confidenza, non [[probabilità]]
> L'espressione "vi è un livello di confidenza del $95\%$ che $\mu$ stia nell'intervallo" può portare a interpretazioni erronee. È bene notare che *non stiamo affermando* che la probabilità che $\mu \in (\bar{x} - 1.96\sigma / \sqrt{n})$ è di $0.95$, infatti in questo enunciato non compaiono variabili aleatorie. Quello che affermiamo , invece, è che la tecnica adottata per arrivare a questo intervallo, nel $95\%$ dei casi in cui viene impiegata, produce un intervallo che contiene il valore vero di $\mu$. In altri termini, prima di osservare i dati possiamo dire che vi è il $95\%$ di probabilità che l'intervallo che otterremo contenga $\mu$, mentre dopo l'osservazione dei dati possiamo solo asserire che l'intervallo contiene $\mu$ "col $95\%$ di confidenza"

---
### Intervalli di confidenza per la media di una distribuzione normale, quando la varianza non è nota
Sia ora $X_{1}, X_{2}, \dots, X_{n}$ un campione di una popolazione $\mathcal{N}(\mu, \sigma^{2})$, con entrambi i parametri ignoti. Vogliamo nuovamente costruire un intervallo di confidenza per $\mu$ ad un livello prescritto di $1-\alpha$. Siccome la deviazione standard $\sigma$ non è nota, non possiamo più basarci sul fatto che $\sqrt{n}\frac{\overline{X}-\mu}{\sigma}$ è una normale standard. Tuttavia, se $$S^{2}:=\frac{1}{n-1} \sum_{i}\left(X_{i}-\bar{X}\right)^{2}$$ denota la varianza campionaria, allora segue che $$ \frac{\bar{X}-\mu}{S / \sqrt{n}} \sim t_{n-1}$$ è una variabile aleatoria di [[Distribuzione t|tipo]] $t$ con $n-1$ gradi di libertà. Allora, poiché la densità delle distribuzioni $t$ è simmetrica rispetto a zero come quella densità normale standard, abbiamo per $\alpha \in (0, 1/2)$

![](https://cdn.mathpix.com/cropped/2023_11_20_03d5e6ef9957032926fdg-129.jpg?height=572&width=1104&top_left_y=234&top_left_x=1632)

$$
\mathbb{P}\left(-t_{\frac{\alpha}{2}, n-1}<\frac{\bar{X}-\mu}{S / \sqrt{n}}<t_{\frac{\alpha}{2}, n-1}\right)=1-\alpha
$$
o equivalentemente, 
$$
P\left(\bar{X}-t_{\frac{\alpha}{2}, n-1} \frac{S}{\sqrt{n}}<\mu<\bar{X}+t_{\frac{\alpha}{2}, n-1} \frac{S}{\sqrt{n}}\right)=1-\alpha
$$
Così, se i valori osservati sono $\overline{X} = \bar{x}$ e $S = s$, possiamo dire "con un livello di confidenza di $1-\alpha$" che $$\mu \in\left(\bar{x}-t_{\frac{\alpha}{2}, n-1} \frac{s}{\sqrt{n}}, \quad \bar{x}+t_{\frac{\alpha}{2}, n-1} \frac{s}{\sqrt{n}}\right)$$
>[!example]-
> Consideriamo di nuovo l'esempio precedente, ma questa volta immaginiamo di non conoscere $\sigma$. Determiniamo un intervallo di confidenza al $95\%$ per $\mu$, usando i $9$ dati ricevuti. $$\begin{array}{lllllllll}5 & 8.5 & 12 & 15 & 7 & 9 & 7.5 & 6.5 & 10.5\end{array}$$ Un calcolo diretto permette di verificare che $$\begin{aligned}\bar{x} & =9 \\s^{2} & =\frac{\sum_{i} x_{i}^{2}-9\bar{x}^{2}}{8}=9.5 \\s & \approx 3.082\end{aligned}$$
> Quindi, poiché $t_{0.025,8} \approx 2.306$, un intervallo di confidenza del $95\%$ per $\mu$ è quello dato da $$9 \pm 2.306 \cdot \frac{3.082}{3}\;\; \text{ovvero} \;\;(6.63, 11.37)$$ che è un intervallo più largo ottenuto precedentemente.
> Il motivo per cui abbiamo ottenuto un intervallo di confidenza più ampio è duplice. In primo luogo abbiamo usato qui una stima di $\sigma$ maggiore del valore accettato in precedenza. Infatti in quella sede ci era dato che la varianza era 4 , mentre qui abbiamo dovuto usare la stima fornita dai dati che è di 9.5. In secondo luogo, è bene notare che anche se avessimo trovato una stima della varianza pari a 4, l'intervallo di confidenza sarebbe risultato comunque più largo; infatti disponendo solo di una stima della varianza, siamo tenuti ad usare una distribuzione di tipo $t$ anziché quella normale standard, che avrebbe una varianza minore (si veda ancora la Figura $5.15 \mathrm{di}$ pagina 193: la distribuzione di tipo $t$ ha le code pesanti). Per chiarire, se avessimo trovato $\bar{x}=9$ e $s^{2}=4$, il nostro intervallo ci confidenza sarebbe stato $$9 \pm 2.306 \cdot \frac{2}{3} \quad \text { ovvero }(7.46,10.54)$$ che è ancora un poco più ampio di quello dell'esempio precedentemente.

---

Possiamo fare le seguenti osservazioni:
1. Gli intervalli di confidenza per $\mu$ quando $\sigma$ è nota si basano sul fatto che $\sqrt{n}(\overline{X}- \mu)/\sigma$ ha distribuzione normale standard. Quando invece $\sigma$ non è conosciuta, la stima con $S$ e poi si usa il fatto che $\sqrt{n}(\overline{X}- \mu)/S$ ha distribuzione di tipo $t$ con $n-1$ gradi di libertà
2. L'ampiezza di un intervallo di confidenza ad un livello fissato, non è per forza maggiore quando non si conosce la varianza. La sua misura infatti è pari a $2z_{\alpha}\sigma/\sqrt{n}$ quando $\sigma$, ed a $2t_{\alpha, n-1}S/\sqrt{n}$ in caso contrario, ed è certamente possibile che la deviazione standard campionaria risulti molto minore di $\sigma$. Tuttavia è anche possibile dimostrare che la lunghezza *media* dell'intervallo è maggiore quando la varianza è incognita. Ovvero si può dimostrare rigorosamente che $$t_{\alpha, n-1} E[S] \geq z_{\alpha} \sigma$$

---

### Intervalli di confidenza per la varianza di una distribuzione normale
Se $X_{1}, X_{2}, \dots, X_{n}$ è un campione da una distribuzione normale con parametri $\mu$ e $\sigma^{2}$ entrambi incogniti, possiamo costruire degli intervalli di confidenza per $\sigma^{2}$ basandoci sul fatto che 
$$
(n-1) \frac{S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
$$
Infatti, 
$$
\begin{aligned}
1-\alpha & =P\left(\chi_{1-\frac{\alpha}{2}, n-1}^{2}<(n-1) \frac{S^{2}}{\sigma^{2}}<\chi_{\frac{\alpha}{2}, n-1}^{2}\right) \\
& =P\left(\frac{\chi_{1-\frac{\alpha}{2}, n-1}^{2}}{(n-1) S^{2}}<\frac{1}{\sigma^{2}}<\frac{\chi_{\frac{\alpha}{2}, n-1}^{2}}{(n-1) S^{2}}\right) \\
& =P\left(\frac{(n-1) S^{2}}{\chi_{\frac{\alpha}{2}, n-1}^{2}}<\sigma^{2}<\frac{(n-1) S^{2}}{\chi_{1-\frac{\alpha}{2}, n-1}^{2}}\right)
\end{aligned}
$$
Quindi, se $S^{2} = s^{2}$, il seguente costituisce un intervallo di confidenza (bilaterale) per $\sigma^{2}$ ad un livello di confidenza di $1-\alpha$:
$$
\left(\frac{(n-1) s^{2}}{\chi_{\frac{\alpha}{2}, n-1}^{2}}, \frac{(n-1) s^{2}}{\chi_{1-\frac{\alpha}{2}, n-1}^{2}}\right)
$$
>[!example]-
> Una certa procedura automatizzata deve produrre rondella con una variabilità di spessore molto ridotta. Supponiamo di scegliere a caso $10$ rondelle e misurare lo spessore, che risulta, 
> $$
> \begin{array}{llllllllll}0.123 & 0.133 & 0.124 & 0.125 & 0.126 & 0.128 & 0.120 & 0.124 & 0.130 & 0.126\end{array}
> $$
> qual è l'intervallo di confidenza al $90\%$ per la deviazione standard dello spessore delle rondelle?
> Un calcolo diretto mostra che $s^{2} \approx 1.366 \times 10^{-5}$, si trova che $\chi^{2}_{0.05, 9} \approx 16.917$ e $\chi^{2}_{0.95, 9} \approx 3.334$, quindi 
> $$
\begin{aligned}
& \frac{(n-1) s^{2}}{\chi_{\frac{\alpha}{2}, n-1}^{2}} \approx \frac{9 \times 1.366 \times 10^{-5}}{16.917} \approx 7.26 \times 10^{-6} \\
& \frac{(n-1) s^{2}}{\chi_{1-\frac{\alpha}{2}, n-1}^{2}} \approx \frac{9 \times 1.366 \times 10^{-5}}{3.334} \approx 36.87 \times 10^{-6}
\end{aligned}
> $$
> per cui 
> $$
> \sigma^{2} \in\left(7.26 \times 10^{-6}, 36.87 \times 10^{-6}\right)
> $$
> con il $90\%$ di confidenza, o equivalentemente, prendendo le radici quadrate, 
> $$
> \sigma \in\left(2.69 \times 10^{-3}, 6.07 \times 10^{-3}\right)
> $$
> > [!important]
> > Gli intervalli di confidenza unilaterali per $\sigma^{2}$ si ottengono in maniera del tutto analoga, e sono presentati nella tabella sottostante che riassume tutti i risultati di questa nota

---

#### Intervalli con livello di confidenza $1-\alpha$ per campioni normali

>[!tip]
> $$
> \begin{gathered}
X_{1}, X_{2}, \dots, X_{n} \sim \mathcal{N}(\mu, \sigma^{2}) \\
\bar{X}:=\frac{1}{n} \sum_{i=1}^{n} X_{i}, \quad S:=\left(\frac{1}{n-1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\right)^{1 / 2}
\end{gathered}
> $$

| Ipotesi               | $\theta$     | Intervallo bilaterale                                                                                               | Intervallo sinistro                                                                      | Intervallo destro                                                 |
| --------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| $\sigma^{2}$ nota     | $\mu$        | $\bar{X} \pm z_{\frac{\alpha}{2}} \frac{\sigma}{\sqrt{n}}$                                                          | $\left(-\infty, \bar{X}+z_\alpha \frac{\sigma}{\sqrt{n}}\right)$                         | $\left(\bar{X}-z_\alpha \frac{\sigma}{\sqrt{n}}, \infty\right)$   |
| $\sigma^{2}$ non nota | $\mu$        | $\bar{X} \pm t_{\frac{\alpha}{2}, n-1} \frac{S}{\sqrt{n}}$                                                          | $\left(-\infty, \bar{X}+t_{\alpha, n-1} \frac{S}{\sqrt{n}}\right)$                       | $\left(\bar{X}-t_{\alpha, n-1} \frac{S}{\sqrt{n}}, \infty\right)$ |
| $\mu$ non nota        | $\sigma^{2}$ | $\left(\frac{(n-1) S^2}{\chi_{\frac{\alpha}{2}, n-1}^2}, \frac{(n-1) S^2}{\chi_{1-\frac{\alpha}{2}, n-1}^2}\right)$ | $\left(\begin{array}{cc}0, & \frac{(n-1) S^2}{\chi_{1-\alpha, n-1}^2}\end{array}\right)$ | $\left(\frac{(n-1) S^2}{\chi_{a, n-1}^2}, \infty\right)$                                                                  |

