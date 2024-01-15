---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - parametricEstimation
  - sampling
---
Una qualunque statistica il cui scopo sia quello di dare una stima di un parametro $\theta$ si dice stimatore di $\theta$; gli stimatori sono quindi variabili aleatorie. Il valore deterministico assunto da uno stimatore è detto invece *stima*. Ad esempio, la [[Valore atteso|media]] campionaria $\overline{X} := \sum_{i}X_{i}/n$ di un [[campione]] [[Gaussiana|normale]] $X_{1}, X_{2}, \dots, X_{n}$ costituisce lo stimatore abituale della media $\mu$ della [[distribuzione]]. 
Consideriamo delle variabili aleatorie $X_{1}, X_{2}, \dots, X_{n}$, la cui distribuzione congiunta sia nota a meno di un parametro incognito $\theta$. Un problema di interesse consiste nello stimare $\theta$ usando i valori che vengono assunti da queste variabili aleatorie. Per esemplificare, potremmo immaginare che le $X_{i}$, siano variabili aleatorie esponenziali e indipendenti, tutte di media $\theta$ incognita. In questo caso la loro densità congiunta sarebbe data da $$
\begin{array}{rlrl}
f\left(x_{1}, x_{2}, \ldots, x_{n}\right) & =f_{X_{1}}\left(x_{1}\right) f_{X_{2}}\left(x_{2}\right) \cdots f_{X_{n}}\left(x_{n}\right) & \\
& =\frac{1}{\theta} e^{-x_{1} / \theta} \frac{1}{\theta} e^{-x_{2} / \theta} \cdots \frac{1}{\theta} e^{-x_{n} / \theta}, & x_{i}>0, \quad i=1, \ldots, n \\
& =\frac{1}{\theta^{n}} \exp \left\{-\sum_{i=1}^{n} \frac{x_{i}}{\theta}\right\}, & & x_{i}>0, \quad i=1, \ldots, n
\end{array}$$ 
e il nostro obiettivo consisterebbe nello stimare $\theta$ partendo dai valori osservati $X_{1}, X_{2}, \dots, X_{n}$.

Vi è una classe particolare di stimatori, detti ***stimatori di massima verosimiglianza***[^1], che è largamente utilizzata in statistica. Uno stimatore di questo si ottiene con il ragionamento seguente. Denotiamo con $f(x_{1},x_{2}, \dots, x_{n}|\theta)$ la funzione di massa congiunta di $X_{1}, X_{2}, \dots, X_{n}$ oppure la loro densità congiunta, a seconda che siano variabili aleatorie discrete o continue. Poiché stiamo supponendo che $\theta$ sia un'incognita, mostriamo esplicitamente che $f$ dipende da $\theta$. Se interpretiamo $f(x_{1},x_{2}, \dots, x_{n}|\theta)$ come la verosimiglianza (o plausibilità, o credibilità, in un italiano più diretto) che si realizzi la $n-$upla di dati $x_{1},x_{2}, \dots, x_{n}$, quando $\theta$ è il vero valore assunto dal parametro, sembra ragionevole adottare come stima di $\theta$ quel valore che rende massima la verosimiglianza per i dati osservati. In altri termini, la stima di massima verosimiglianza $\overline{\theta}$ è definita come il valore di $\theta$ che rende massima $f(x_{1},x_{2}, \dots, x_{n}|\theta)$, quando i valori osservati sono $x_{1},x_{2}, \dots, x_{n}$. 

>[!tip]
> La funzione $f(x_{1},x_{2}, \dots, x_{n}|\theta)$ è detta funzione di *likelihood*.

Nel calcolare il valore di $\theta$ che minimizza $f$, conviene spesso usare il fatto che le due funzioni $f(x_{1},x_{2}, \dots, x_{n}|\theta)$ e $\log[f(x_{1},x_{2}, \dots, x_{n}|\theta)]$ assumono il massimo in corrispondenza del valore di $\theta$. Quindi è possibile ottenere $\overline{\theta}$ anche massimizzando $\log[f(x_{1},x_{2}, \dots, x_{n}|\theta)]$, che è detta funzione di *like-likelihood*.

>[!example]- Stimatore di massima verosimiglianza del parametro di una [[bernoulliana]]
> Supponiamo che vengano realizzare $n$ prove indipendenti, ciascuna con [[probabilità]] $p$ di successo. Qual è lo stimatore di massima verosimiglianza per $p$?
> I dati a disposizione consistono nei valori di $X_{1}, X_{2}, \dots, X_{n}$, dove $$
X_{i}= \begin{cases}1 & \text { se la prova } i \text {-esima ha successo } \\ 0 & \text { altrimenti }\end{cases}$$
> La distribuzione delle $X_{i}$ è determinata da $$\mathbb{P}\left(X_{i}=1\right)=p=1-\mathbb{P}\left(X_{i}=0\right)$$ o, in maniera più compatta, $$\mathbb{P}\left(X_{i}=k\right)=p^{k}(1-p)^{1-k}, \quad k=0,1$$
> Quindi sfruttando l'indipendenza delle prove, la likelihood (ovvero la funzione di massa congiunta) del campione è data da $$
\begin{aligned}
f\left(x_{1}, x_{2}, \ldots, x_{n} \mid p\right): & =\mathbb{P}\left(X_{1}=x_{1}, X_{2}=x_{2}, \ldots X_{n}=x_{n} \mid p\right) \\
& =p_{\mathrm{p}}^{x_{1}}(1-p)^{1-x_{1}} \ldots p^{x_{n}}(1-p)^{1-x_{n}} \\
& =p^{{ }_{i} x_{i}}(1-p)^{n-{ }^{\mathrm{P}}}{ }_{i} x_{i}, \quad x_{i}=0,1, \quad i=1, \ldots, n
\end{aligned}$$
> Per determinare il valore di $p$ che massimizza questa funzione, prima prendiamo i logaritmi $$
\log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid p\right)=\sum_{i=1}^{n} x_{i} \log p+\left(n-\sum_{i=1}^{n} x_{i}\right) \log (1-p)$$ quindi deriviamo rispetto a $p$, $$
\frac{d}{d p} \log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid p\right)=\frac{1}{p} \sum_{i=1}^{n} x_{i}-\frac{1}{1-p}\left(n-\sum_{i=1}^{n} x_{i}\right)$$ ponendo il secondo termine uguale a zero e risolvendo rispetto a $p$, otteniamo un'espressione per la stima di $\widehat{p}$, $$
\frac{1}{\widehat{p}} \sum_{i=1}^{n} x_{i}=\frac{1}{1-\widehat{p}}\left(n-\sum_{i=1}^{n} x_{i}\right)$$ da cui $$\widehat{p}=\frac{1}{n} \sum_{i=1}^{n} x_{i}$$
>> [!important] 
>> Perciò lo stimatore di massima verosimiglianza di una distribuzione di Bernoulli di media incognita è dato da $$d\left(X_{1}, X_{2}, \ldots, X_{n}\right):=\frac{1}{n} \sum_{i=1}^{n} X_{i}$$
>> Siccome $\sum_{i=1}^{n}X_{i}$ è il numero di prove che hanno avuto successo, si vede che lo stimatore di massima verosimiglianza di $p$ coincide con la frazione di prove che hanno avuto successo. Per veder una applicazione, supponiamo che ogni circuito di $\operatorname{RAM}$ prodotto in un certo stabilimento sia- indipendentemente da tutti gli altri - accettabile con probabilità $p$. Se su un campione di $1000$ pezzi quelli accettabili sono $921$, si ottiene che la stima di massima verosimiglianza per $p$ è $0.921$.

>[!example]- Stimatore di massima verosimiglianza del parametro di una [[poissoniana]]
> Supponiamo che $X_{1}, X_{2}, \dots, X_{n}$ siano variabili aleatorie di Poisson indipendenti, ciascuna con valore atteso $\lambda$. Si determini lo stimatore di massima verosimiglianza per $\lambda$.
> La funzione di likelihood è data da $$
\begin{aligned}
f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \lambda\right) & =\frac{\lambda^{x_{1}} e^{-\lambda}}{x_{1} !} \cdots \frac{\lambda^{x_{n}} e^{-\lambda}}{x_{n} !} \\
& =\frac{\lambda^{p}{ }^{x_{i}} e^{-n \lambda}}{x_{1} ! \cdots x_{n} !}
\end{aligned}$$ ovvero, $$
\log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \lambda\right)=\sum_{i=1}^{n} x_{i} \log \lambda-n \lambda-\log c$$ dove $c := x_{1}| \dots x_{n}|$ non dipende da $\lambda$. Derivando si trova che $$
\frac{d}{d \lambda} \log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \lambda\right)=\frac{1}{\lambda} \sum_{i=1}^{n} x_{i}-n$$
> Uguagliando infine a zero questa espressione si ottiene una formula per la stima $\widehat{\lambda}$ in funzione delle osservazioni $x_{1},x_{2}, \dots, x_{n}$, $$
\widehat{\lambda}=\frac{1}{n} \sum_{i=1}^{n} x_{i}$$ 
> La stessa formula applicata al campione $X_{1}, X_{2}, \dots, X_{n}$ fornusce lo stimatore desiderato. $$d\left(X_{1}, X_{2}, \ldots, X_{n}\right) :=\frac{1}{n} \sum_{i=1}^{n} X_{i}$$
> >[!important]-
> > Volendo citare un caso pratico, supponiamo che il numero di persone che ogni giorno entra in un negozio sia un variabile aleatoria di Poisson avente una certa  media $\lambda$ che vogliamo stimare. Se in $20$ giorni il numero totale di persone entrate nel negozio è di $857$, allora la stima di massima verosimiglianza per $\lambda$ è $\frac{857}{20}=42.85$ Quindi stimiamo che in media ogni giorno entreranno $42.85$ persone.

>[!example]- Stimatore di massima verosimiglianza per una [[popolazione]] normale
> Siano $X_{1}, X_{2}, \dots, X_{n}$ variabili aleatorie normali e indipendenti, con media $\mu$ e deviazione standard $\sigma$, entrambe incognite. La densità congiunta, e quindi la likelihood, è data da $$
\begin{aligned}
f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \mu, \sigma\right) & =\prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma} \exp \left\{-\frac{\left(x_{i}-\mu\right)^{2}}{2 \sigma^{2}}\right\} \\
& =\left(\frac{1}{2 \pi}\right)^{n / 2} \frac{1}{\sigma^{n}} \exp \left\{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}\right\}
\end{aligned}$$ La *log-likelihood* corrispondente è data da $$
\log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \mu, \sigma\right)=-\frac{n}{2} \log (2 \pi)-n \log \sigma-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}$$
> Per trovare le stime di $\widehat{\mu}$ e $\widehat{\sigma}$ che contemporaneamente massimizzano la *log-likelihood*, occorre porre uguali a zero le due derivate parziali, e mettere a sistema le due equazioni trovate $$
\begin{aligned}
\frac{\partial}{\partial \mu} \log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \mu, \sigma\right) & =\frac{1}{\sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right) \\
\frac{\partial}{\partial \sigma} \log f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \mu, \sigma\right) & =-\frac{n}{\sigma}+\frac{1}{\sigma^{3}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}
\end{aligned}$$ da cui il sistema $$
\left\{\begin{array}{l}
\frac{1}{\widehat{\sigma^{2}}} \sum_{i=1}^{n}\left(x_{i}-\widehat{\mu}\right)=0 \\
-\frac{n}{\widehat{\sigma}}+\frac{1}{\widehat{\sigma}^{3}} \sum_{i=1}^{n}\left(x_{i}-\widehat{\mu}\right)^{2}=0
\end{array}\right.$$ la cui risoluzione ci porta alle seguenti formule per le stime, $$
\begin{aligned}
& \widehat{\mu}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
& \widehat{\sigma}=\left\{\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\widehat{\mu}\right)^{2}\right\}^{1 / 2}
\end{aligned}$$
> Quindi, gli stimatori di massima verosimiglianza di $\mu$ e $\sigma$ sono dati rispettivamente da $$\bar{X} \quad \text { e } \quad \sqrt{\frac{1}{n} \sum_{i}\left(X_{i}-\bar{X}\right)^{2}}$$
> È bene notare che lo stimatore di massima verosimiglianza per la deviazione standard non coincide con la deviazione standard campionaria, $$S:=\sqrt{\frac{1}{n-1} \sum_{i}\left(X_{i}-\bar{X}\right)^{2}}$$ in quanto nel primo si divide per $\sqrt{n}$ e nel secondo per $\sqrt{n-1}$. In ogni caso, per $n$ non troppo piccolo questi due stimatori di $\sigma$ saranno approssimativamente uguali.

>[!example]- Stimatore di massima verosimiglianza per la media di una distribuzione uniforme
> Sia $X_{1}, X_{2}, \dots, X_{n}$, un campione proveniente da una distribuzione [[uniforme]] sull'intervallo $(0, \theta)$, con $\theta$ incognita. La densità congiunta è data da $$f\left(x_{1}, x_{2}, \ldots, x_{n} \mid \theta\right)= \begin{cases}\frac{1}{\theta^{n}} & 0<x_{i}<\theta, \quad i=1, \ldots, n \\ 0 & \text { altrimenti }\end{cases}$$
> Questa densità si massimizza scegliendo $\theta$ il più piccolo possibile. Siccome $\theta$ deve essere comunque maggiore di tutti i valori osservati $x_{i}$, ne segue che la più piccola scelta possibile per $\theta$ è $\operatorname{max}(x_{1},x_{2}, \dots, x_{n})$. Lo stimatore di massima verosimiglianza per $\theta$ è quindi $$\hat{\theta}=\max \left(X_{1}, X_{2}, \ldots, X_{n}\right)$$ da cui segue subito che lo stimatore di massima verosimiglianza della media della distribuzione (media che è pari a $\theta/2$) verosimiglianza è $\operatorname{max}(X_{1}, X_{2}, \dots, X_{n})/2$.

[^1]: È di uso molto comune l'acronimo $\operatorname{MLE}$, dall'inglese *maximum likelihood estimator*
