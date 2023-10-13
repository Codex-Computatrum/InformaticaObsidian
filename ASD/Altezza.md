---
author: Lorenzo Tecchia
tags: [definition, dataStructure, operation]
---
L'***altezza*** di un [[Tree|albero]] misura la massima distanza di una foglia dalla radice dell'albero, in termini di numero di archi attraversati. 

---
L'altezza di un [[albero binario]] è:
$$h \geq \lceil log_{2}(n+1)-1\rceil \lor h \geq 
\lfloor log_{2}(n) \rfloor$$
>[!important]
> $2^{h+1} -1 = n \rightarrow 2^{h+1}=n +1 \rightarrow$
>$\log_{2}(2^{h+1})\rightarrow \log_{2}(n+1)\rightarrow h+1 = \log_{2}(n+1) \rightarrow h = \log_{2}(n+1) -1$ 

Se l'albero è [[Albero binario#Albero binario quasi completo|quasi completo]], allora: $h \geq \lceil log_{2}(n+1)-1\rceil$