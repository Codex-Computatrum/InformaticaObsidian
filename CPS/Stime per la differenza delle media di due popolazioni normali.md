---
author: Lorenzo Tecchia
tags:
  - definition
  - probability
  - distribution/normal
  - sampling
  - parametricEstimation
---
Siano $X_{1}, X_{2}, \dots, X_{n}$ e $Y_{1}, Y_{2}, \dots, Y_{m}$ due campioni estratti da popolazioni normali differenti, e denotiamo con $\mu_{1}$ e $\sigma_{1}^{2}$ i parametri della prima, e con $\mu_{2}$ e $\sigma_{2}^{2}$ quelli della seconda. Supponiamo che che i due campioni siano tra loro indipendenti, e tentiamo di stimare $\mu_{1}-\mu_{2}$.
Siccome $\overline{X} := \sum\limits_{i=1}^{n}X_{i}/n$ e $\overline{Y} := \sum\limits_{j=1}^{m}Y_{j}/m$ sono gli [[stimatori di massima verosimiglianza]] di $\mu_{1}$ e $\mu_{2}$, sembra ragionevole (e infatti può essere dimostrato) che $\overline{X} - \overline{Y}$ sia lo stimatore di massima verosimiglianza di $\mu_{1}- \mu_{2}$.

Per ottenere uno stimatore non puntuale, nella forma di un intervallo di confidenza, occorre conoscere la [[distribuzione]] di $\overline{X}- \overline{Y}$. Poiché $$
\bar{X} \sim \mathcal{N}\left(\mu_{1}, \frac{\sigma_{1}^{2}}{n}\right) \quad \text { e } \quad \bar{Y} \sim \mathcal{N}\left(\mu_{2}, \frac{\sigma_{2}^{2}}{m}\right)$$ si può dedurre, dal fatto che la somma di normali indipendenti è ancora una [[variabile aleatoria]] [[Gaussiana|normale]], che $$
\bar{X}-\bar{Y} \sim \mathcal{N}\left(\mu_{1}-\mu_{2}, \frac{\sigma_{1}^{2}}{n}+\frac{\sigma_{2}^{2}}{m}\right)$$ dove abbiamo sfruttato che $E[\overline{X}- \overline{Y}] = E[\overline{X}] -E[\overline{Y}]$ e che $\operatorname{Var}(\overline{X} - \overline{Y}) = \operatorname{Var}(\overline{X})+(-1)^{2} \operatorname{Var}(\overline{Y})$. Perciò, ipotizzando di conoscere $\sigma^{2}_{1}$ e $\sigma_{2}^{2}$, abbiamo che $$
\frac{\bar{X}-\bar{Y}-\left(\mu_{1}-\mu_{2}\right)}{\sqrt{\sigma_{1}^{2} / n+\sigma_{2}^{2} / m}} \sim \mathcal{N}(0,1)$$ e possiamo dedurre,  con i passaggi che si sono ormai familiari, che$$
\mu_{1}-\mu_{2} \in\left(\bar{x}-\bar{y}-z \frac{\alpha}{2} \sqrt{\frac{\sigma_{1}^{2}}{n}+\frac{\sigma_{2}^{2}}{m}}, \quad \bar{x}-\bar{y}+z \frac{\alpha}{2} \sqrt{\frac{\sigma_{1}^{2}}{n}+\frac{\sigma_{2}^{2}}{m}}\right)$$

Gli intervalli di confidenza unilaterali si ottengono in maniera analoga, per cui vi è un livello di confidenza di $1-\alpha$ che $$
\mu_{1}-\mu_{2} \in\left(-\infty, \quad \bar{x}-\dot{\bar{y}}+z_{\alpha} \sqrt{\sigma_{1}^{2} / n+\sigma_{2}^{2} / m}\right)$$