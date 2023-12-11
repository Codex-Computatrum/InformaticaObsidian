---
author: Lorenzo Tecchia
tags:
  - definition
  - probability
  - example
---
Siano $E$ e $F$ due [[Evento|eventi]] qualsiasi. È possibile esprimere $E$ come: $$E = (E \cap F)\cup (E \cap F^{c})$$
Infatti ogni punto che appartiene all'evento $E$, o sta sia in $E$ sia in $F$, oppure sta sia in $E$ ma non in $F$. Inoltre, visto che $E \cap F$ e $E \cap F^{c}$ sono eventi disgiunti, si ha per l'[[Assioma Terzo|assioma]]:

$$\begin{align}
\mathbb{P}(E) &= \mathbb{P}(E \cap F) + \mathbb{P}(E \cap F^{c}) \\
&= \mathbb{P}(E|F)\mathbb{P}(F) + \mathbb{P}(E|F^{c})\mathbb{P}(F^{c})\\
&= \mathbb{P}(E|F)\mathbb{P}(F) + \mathbb{P}(E|F^{c})[1-\mathbb{P}(F)]
\end{align}$$
^formula-di-bayes

L'equazione [[Formula di Bayes#^formula-di-bayes|soprastante]] afferma che la probabilità dell'evento $E$ si può ricavare come [[Valore atteso|media]] pesata delle probabilità condizionali di $E$ sapendo che: $(1)$ che $F$ si è verificato e $(2)$ che non si è verificato. I pesi corretti sono le probabilità degli eventi rispetto a cui si condiziona. 

Questa formula è estremamente utile, in quanto in molte situazioni non è possibile calcolare una probabilità complessa direttamente, mentre essa è facilmente ricavabile dall'equazione [[Formula di Bayes#^formula-di-bayes|soprastante]], condizionando al verificarsi co meno di un secondo evento. L'evento accessorio va scelto in modo che, una volta che si sappia se esso si è verificato o meno, risulti evidente la probabilità dell'evento complesso di partenza, tenendo conto di questa informazione.
>[!example]
> Una particolare analisi del sangue è efficace al $99\%$ nell'individuare una certa malattia quando essa è presente. Si possono però anche verificare dei "falsi positivi" con probabilità dell $1\%$(ovvero una persona sana che si sottoponga al test, con una probabilità di $0.01$ risulta erroneamente affetta dalla malattia in questione). Se l'incidenza cdi questo male sulla [[popolazione]] è dello $0.5\%$, qual è la probabilità che un soggetto sia malato, condizionata al fatto che le analisi abbiano dato esito positivo?
> Sia $M$ l'evento "il soggetto è malato" ed $E$ l'evento "il risultato dell'analisi è positivo". Allora $\mathbb{P}(M|E)$ si trova tramite:$$ \begin{align}
\mathbb{P}(M|E) &= \frac{\mathbb{P}(M \cap E)}{\mathbb{P}(E)} \\
&= \frac{\mathbb{P}(E|M)\mathbb{P}(M)}{\mathbb{P}(E|M)\mathbb{P}(M)+\mathbb{P}(E|M^{c})\mathbb{P}(M^{c})} \\
&= \frac{0.99 \times 0.005}{0.99 \times 0.005 + 0.01 \times 0.995} \approx 0.3322
\end{align}$$
Perciò solo il $33\%$ delle persone che risultano positive alle analisi sono realmente affette dalla malattia. Siccome molti studenti si stupiscono di questo risultato (infatti le caratteristiche del test sembrano buone e ci si aspetterebbe un valore più elevato), vale forse la pena di presentare una seconda argomentazione che anche se meno rigorosa può aiutare a chiarirsi le idee.
Se lo $0.5\% = 1/200$ della [[popolazione]] soffre di questo male, in [[Valore atteso|media]] su $200$ persone vi sarà un solo malato. Se egli si sottopone alle analisi, verrà trovato positivo quasi certamente con (probabilità $0.99$), così che su $200$ individui testati ve ne saranno in media $0.99$ che saranno correttamente individuati come malati. D'altro canto le (in media) 199 persone sane che hanno una probabilità di $0.01$ di risultare positive, e quindi in media su $200$ analisi vi saranno $199 \times 0.01 = 1.99$ falsi positivi. Se consideriamo che ogni $0.99$ positivi veri vi sono in media $1.99$ positivi falsi, ricaviamo nuovamente che la frazione di malati reali tra i soggetti positivi alle analisi è$$\frac{0.99}{0.99 + 1.99} \approx 0.3322$$

>[!note] 
> L'[[Formula di Bayes#^formula-di-bayes|equazione della formula di Bayes]] è utile anche quando si voglia riconsiderare il proprio (personale) convincimento o confidenza su un fatto, alla luce di nuove informazioni.
