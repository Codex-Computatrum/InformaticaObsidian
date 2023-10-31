---
tags: [definition, probability, aleatoryVariable]
author: Lorenzo Tecchia
---
Una [[variabile aleatoria]] [[DiscretaVA|discreta]] che possa assumere un infinità non numerabile di valori, non potrà essere discreta. Si dirà invece ***continua*** se esiste una funzione non negativa $f$, definita su tutto $\mathbb{R}$ avente la proprietà che per ogni insieme $B$ di numeri reali, $$\mathbb{P}(X \in B) = \int_{B}f(x)dx$$
La funzione che compare nella soprastante equazione è la ***funzione di densità di probabilità*** o più semplicemente la **densità** della variabile aleatoria $X$. 

Tale equazione dice che la probabilità che una ***variabile aleatoria continua*** $X$ appartenga a un insieme $B$ si può trovare integrando la sua densità su tale insieme. Poiché $X$ deve assumere un qualche valore di $\mathbb{R}$ la sua densità deve soddisfare:$$1=\mathbb{P}(X \in \mathbb{R}) = \int_{-\infty}^{+\infty}f(x)dx$$

Una relazione che lega la [[funzione di distribuzione]] $F$ alla densità $f$ è la seguente:$$F(a):=\mathbb{P}(X \in (- \infty, a]) = \int_{\infty}^{a}f(x)dx$$
Derivando entrambi i membri si ottiene la relazione fondamentale:
>[!important] La densità è la derivata della funzione di distribuzione
> $$\frac{d}{da}F(a)=f(a)$$

Inoltre vogliamo notare:
>[!note]
> $$\mathbb{P}\left(a - \frac{\varepsilon}{2} \leq X \leq a +\frac{\varepsilon}{2}\right)= \int_{a- \frac{\varepsilon}{2}}^{a+\frac{\varepsilon}{2}}f(x)dx \approx \varepsilon f(a)$$
> Da notare quindi che la probabilità che $X$ stia in un intorno di $a$ di ampiezza $\varepsilon$ è approssimativamente $\varepsilon f(a)$, e quindi $f(a)$ rappresenta una indicazione di quanto probabile che $X$ cada "vicino" ad $a$

>[!note] Ricordare che per la [[DegenereVA|variabile aleatoria degenere]] $\{X = a\}$ ha probabilità $0$

>[!important]
>![[Distribuzione]]