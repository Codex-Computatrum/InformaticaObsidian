---
author: Lorenzo Tecchia
tags:
  - statistics
  - theorem
  - example
---
Se $X$ è una variabile aleatoria con [[Valore atteso|media]] $\mu$ e [[varianza]] $\sigma^{2}$, allora per ogni $r > 0$:$$\mathbb{P}(|X-\mu| \geq r) \leq \frac{\sigma^{2}}{r^{2}}$$

***Dimostrazione***: Gli eventi $\{|X - \mu| \geq r\}$ e $\{(X -\mu)^{2} \geq r^{2}\}$ coincidono e sono quindi equiprobabili. Visto che $(X - \mu)^{2}$ è una variabile aleatoria non negativa, possiamo applicarle la disuguaglianza di Markov con $a = r^{2}$, ottenendo che: $$
\begin{aligned}
P(|X-\mu| \geq r) & =P\left((X-\mu)^{2} \geq r^{2}\right) \\
& \leq \frac{E\left[(X-\mu)^{2}\right]}{r^{2}}=\frac{\sigma^{2}}{r^{2}}
\end{aligned}$$

L'importanza delle disuguaglianze di Markov e Chebyshev, sta nel fatto che permettono di limitare la probabilità di eventi rari che riguardano variabili aleatorie di cui conosciamo solo la [[Valore atteso|media]], oppure la media e la varianza. Naturalmente, quando la distribuzione è nota, tali probabilità possono essere calcolate esattamente e non vi  è necessità di ridursi all'utilizzo di maggiorazioni.

>[!example]
> Il numero di pezzi prodotti da una fabbrica durante una settimana è una variabile aleatoria di media $50$. Cosa si può dire sulla probabilità che la produzione superi occasionalmente i $75$ pezzi? Se si suppone nota anche la varianza pari a $25$, cosa si può dire sulla probabilità che la produzione sia compresa tra i $40$ e o $60$ pezzi?
> Denotiamo con $X$ la variabile aleatoria che indica il numero di pezzi prodotti in una settimana. Per la disuguaglianza di Markov:$$P(X \geq 75) \leq \frac{E[X]}{75}=\frac{50}{75}=\frac{2}{3}$$
> Applicando la disuguaglianza di Chebyshev:$$P(|X-50| \geq 10) \leq \frac{25}{10^{2}}=\frac{1}{4}$$
> Quindi $$P(40 \leq X \leq 60)=P(|X-50| \leq 10) \geq 1-\frac{1}{4}=\frac{3}{4}$$
> Perciò la probabilità che la produzione sia compresa tra i $40$ e i $60$ pezzi è pari al $75\%$
> > [!important] 
> > Se nella disuguaglianza di Chebyshev si pone $r = k\sigma$, essa assume la forma seguente: $$\mathbb{P}(|X - \mu| > k\sigma) \leq \frac{1}{k^{2}}$$

In altri termini, la probabilità che una variabile aleatoria differisca dalla sua media per più di $k$ volte la deviazione standard, non può superare il valore $\frac{1}{k^{2}}$