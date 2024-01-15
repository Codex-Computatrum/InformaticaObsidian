---
author: Lorenzo Tecchia
tags: [definition, example]
---
Sia $\mathcal{F}$ una famiglia di sottoinsiemi di $\Omega$ . Si dice che $\mathcal{F}$ è una **sigma [[algebra]]** (o $\sigma$ algebra) se e solo se:
- $\Sigma_{1}\;\;\;\; \Omega \in \mathcal{F}$
- $\Sigma_{2}\;\;\;\; A \in \mathcal{F}, \;\;\; A^{c}\in \mathcal{F}$
- $\Sigma_{1}\;\;\;\; (A_n)_{n \in \mathbb{N}} \subseteq \mathcal{F}, \;\;\;\; \cup_{n \in \mathbb{N}}A_{n} \in \mathcal{F}$(_proprietà di stabilità rispetto all'unione numerabile_)

>[!important] L'intersezione su una sigma algebra è un operazione chiusa
> Sia $\mathcal{F}$ una sigma algebra e $(A_n)_{n \in \mathbb{N}}\subseteq \mathcal{F}$. Allora: $$\bigcap_{n \in \mathbb{N}} A_{n}=\left(\bigcup_{n \in \mathbb{N}}A_{n}^{c}\right)^{c}\in \mathcal{F}$$

### Esempio
Esperimento aleatorio $\xi$: si lancia una moneta un numero indefinito di volte. Lo [[spazio degli esiti]] è $\Omega = \{T,C\}^{\infty}$ cioè il prodotto cartesiano $\{T,C\} \times \{T,C\} \times \dots$ infinite volte. L'elemento generico di $\Omega$ è una successione ordinata di esiti testa/croce, cioè $\omega = (\omega_{1}, \omega_{2}, \dots)=(\omega_{n})_{n \in \mathbb{N}} \in \Omega$. Il punto campione è dunque una successione.
Consideriamo l'evento $A:\text{"due T consecutivi prima di due C consecutive"}$. Esiti che fanno avverare questo evento possono essere:
![[Pasted image 20231021222405.png|150]]
