---
author: Simone Parente
tags:
  - algebra/grafi
  - notReviewed
---
Siano $G=(V,L,f)$ e $G'=(V',L',f')$ due [[Multigrafo semplice|multigrafi]], un isomorfismo è una coppia di applicazioni biettive: 
$$\alpha:V \to V'\text{ e }\beta:L \to L'$$$$\text{ tali che } \; \forall l \in L,\; \forall a,b \in V\, :\, a \text{ e } b \text{ sono gli estremi di } l \iff \alpha(a) \text{ e } \alpha(b) \text{ sono gli estremi di }\beta(l)$$ Per i grafi semplici basta che $\forall a,b \in V \; \; \{a,b\} \in L \iff \{\alpha(a), \alpha(b)\} \in L$
$\implies$ due grafi isomorfi hanno lo stesso numero di vertici e di lati.
### Esempio di grafi isomorfi
![[grafiIsomorfi.jpg]]
Questi grafi sono isomorfi perché hanno stesso numero di vertici, lati e stessa adiacenza<span style="color:#ff0000">?</span>
### Esempio di grafi non isomorfi
![[grafiNonIsomorfi.jpg]]
Questi grafi non sono isomorfi perché hanno diversa adiacenza.