---
author: Simone Parente
tags:
  - algebra/grafi/alberi
  - notReviewed
---
Sia $T$ un albero e sia $T$ finito $\implies |V|=|L|+1$.
### Dimostrazione per induzione <span style="color:#ff0000">sbagliata</span>
Se $|L|=0 \implies |V|=1$, e questo verifica il caso base.
Prendiamo $|L_t|=n$ e verifichiamo che $|L_{t'}|=n-1$.
Per il [[Lemma su alberi|lemma precedente]], se a $t'$ togliamo una foglia e il lato ad essa incidente, abbiamo ancora un albero, questo albero avrà $n-1+1=n$  lati e $|V_{t'}|-1$ foglie.
Per ipotesi le foglie di quest'albero sono $n+1 \implies |V_{t'}|-1=n+1 \implies |V_{t'}|=n+1+1=|L_{t'}|+1$.
