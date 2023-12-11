---
tags:
  - probability
  - definition
  - to-do
  - distribution
  - example
---
>[!todo] Inserire grafico

Supponendo che venga realizzata una prova, o un esperimento, il cui esito può essere solo un "successo" o un "fallimento". Se definiamo la [[variabile aleatoria]] $X$ in modo che sia $X=1$ nel primo caso e $X = 0$ nel secondo, la funzione di massa di probabilità di $X$ è data da $$\begin{align}
\mathbb{P}(X=0)&=1-p \\
\mathbb{P}(X = 1)&= p
\end{align}$$
dove con $p$ abbiamo indicato la probabilità che l'esperimento registri un "successo". Ovviamente dovrà essere $0 \leq p \leq 1$

>[!definition]
> Una variabile aleatoria $X$ si dice di *Bernoulli* o bernoulliana se la sua funzione di massa di probabilità è del tipo delle equazioni soprastanti per una scelta opportuna del parametro $p$

In altri termini, una variabile aleatoria è bernoulliana se può assumere se può assumere solo i valori $0$ e $1$. Il suo [[valore atteso]] è dato da $$E[X]:= 1 \mathbb{P}(X = 1)+ 0 \mathbb{P}(X = 0)= p$$ ed è quindi pari alla probabilità che la variabile aleatoria assuma il valore di $1$
La varianza invece vale: $$\operatorname{Var}(X) = n p (1-p) = npq$$

---
### Intervalli di confidenza approssimati per la media di una distribuzione normale
Consideriamo una popolazione di oggetti, ognuno dei quali indipendente da tutti gli altri soddisfa certi requisiti con probabilità incognita $p$. Nel caso vengano testati $n$ di questi oggetti, rilevando quanti di essi raggiungono tali requisiti, come possiamo usare questa grandezza per ottenere un intervallo di confidenza per $p$?
Se $X$ denota quindi oggetti, sugli $n$ testati, soddisfano i requisiti di interesse, è facile convincersi che $X$ ha distribuzione binomiale di parametri $n$ e $p$. Quindi nel caso $n$ sia un numero elevato, $X$ è approssimativamente normale con media $np$ e varianza $np(1-p)$, e di conseguenza 
$$
\frac{X-n p}{\sqrt{n p(1-p)}} \dot{\sim} \mathcal{N}(0,1)
$$
Preso allora un qualunque valore $\alpha \in (0, 1)$,
$$
P\left(-z_{\frac{\alpha}{2}}<\frac{X-n p}{\sqrt{n p(1-p)}}<z_{\frac{\alpha}{2}}\right) \approx 1-\alpha
$$
Se $x$ è il valore assunto da $X$, quella che segue è una regione che contiene $p$ con livello di confidenza $1-\alpha$, 
$$
\left\{p:-z_{\frac{\alpha}{2}}<\frac{x-n p}{\sqrt{n p(1-p)}}<z_{\frac{\alpha}{2}}\right\}
$$
Tale regione non è un intervallo. Se vogliamo ottenere un intervallo di confidenza vero e proprio, denotiamo con $\hat{p} := X/n$ la frazione degli oggetti del campione che soddisfa i requisiti in esame. Sappiamo che $\hat{p}$ è lo stimatore di massima verosimiglianza di $p$, ed è una buona approssimazione di $p$. Per questo motivo $\sqrt{n\hat{p}(1-\hat{p})}$ è approssimativamente uguale a $\sqrt{np(1-p)}$ e, quindi deduciamo che 
$$
\frac{X-n p}{\sqrt{n \hat{p}(1-\hat{p})}} \ddot{\sim} \mathcal{N}(0,1)
$$
Questa statistica al contrario di [[Stime per la differenza delle media di due popolazioni normali|questa]] ci consente di arrivare rapidamente ad un intervallo di confidenza. Sia $\alpha \in (0, 1)$, allora
$$
\begin{aligned}
1-\alpha & \approx \mathbb{P}\left(-z_{\frac{\alpha}{2}}<\frac{X-n p}{\sqrt{n \hat{p}(1-\hat{p})}}<z_{\frac{\alpha}{2}}\right) \\
& =\mathbb{P}\left(-z_{\frac{\alpha}{2}} \sqrt{n \hat{p}(1-\hat{p})}<n p-X<z_{\frac{\alpha}{2}} \sqrt{n \hat{p}(1-\hat{p})}\right) \\
& =\mathbb{P}\left(\hat{p}-z_{\frac{\alpha}{2}} \sqrt{\hat{p}(1-\hat{p}) / n}<p<\hat{p}+z_{\frac{\alpha}{2}} \sqrt{\hat{p}(1-\hat{p}) / n}\right)
\end{aligned}
$$
e l'ultima formula fornisce un intervallo di confidenza approssimato per $p$.

>[!example]-
> Un campione di $100$ transistor viene estratto da una grossa fornitura e testato. In tutto $80$ pezzi sono adeguati ai requisiti; volendo trovare un intervallo di confidenza al $95\%$ per la percentuale $p$ di transistor accettabili dalla fornitura, scriviamo 
> $$
(0.8-1.96 \sqrt{0.8 \cdot 0.2 / 100}, \quad 0.8+1.96 \sqrt{0.8 \cdot 0.2 / 100})=(0.7216, \quad 0.8784)
> $$
> Quindi possiamo affermare con il $95\%$ di confidenza che sarà accettabile una percentuale di transistor compresa tra il $72.16\%$ e $87.84\%$

#### Riassumendo
##### Intervalli di confidenza ad un livello $1-\alpha$ per il parametro di una distribuzione di Bernoulli
 $$
\begin{gather}
\hat{p}:=\frac{X}{n}, \quad X \; \text{è il numero di valori 1 nel campione bernoulliano}
\end{gather}
$$ 

> [!important]
> 
> | Tipo di intervallo   | Intervallo di confidenza                                                       |
> | -------------------- | ------------------------------------------------------------------------------ |
> | Bilaterale           | $\hat{p} \pm z_{\frac{\alpha}{2}} \sqrt{\hat{p}(1-\hat{p}) / n}$               |
> | Unilaterale sinistro | $\left(-\infty, \quad \hat{p}+z_{\alpha} \sqrt{\hat{p}(1-\hat{p}) / n}\right)$ |
> | Unilaterale destro   | $\left(\hat{p}-z_{\alpha} \sqrt{\hat{p}(1-\hat{p}) / n}, \quad \infty\right)$|

Osserviamo che, come abbiamo visto, l'intervallo bilaterale con livello di confidenza $1-\alpha$, ha lunghezza approssimativamente $b$ quando il numero di elementi del campione è
$$
n=\frac{4 z_{\alpha / 2}^{2}}{b^{2}} p(1-p)
$$
La parabola $g(p):= p(1-p)$ tocca il suo massimo pari a $1/4$ quando $p=\frac{1}{2}$. Qualunque sia il valore di $p$, quindi si avrà sempre 
$$
n \leq \frac{z_{\alpha / 2}^{2}}{b^{2}}
$$
perciò scegliendo un campione di ampiezza $z^{2}_{\alpha/2}/b^{2}$, siamo sicuri di ottenere un intervallo di confidenza non più grande di $b$ senza bisogno di procurarci un campione preliminare. Si tenga presente che questa sovrastima di $n$ non è tanto peggiore quanto più $p$ é vicino a $0$ oppure a $1$.