---
author: Lorenzo Tecchia
tags: [definition, probability]
---
Per tutta una serie di esperimenti è naturale assumere che ogni [[esito]] di uno [[Spazio degli esiti|spazio]] $S$ abbia la stessa [[probabilità]] di realizzarsi. Ciò può accadere solo se $S$ è un insieme finito, e in questo caso, si può assumere senza perdita di generalità che sia $S = {1, 2, \dots, N }$ in queste ipotesi l’equiprobabilità degli esiti si scrive:$$\mathbb{P}(\{1\})=\mathbb{P}(\{2\})= \dots = \mathbb{P}(\{N\}):= p$$ Dal [[Assioma Primo|primo]] e dal [[Assioma Secondo|secondo]] assioma segue che:$$1=\mathbb{P}(\Omega)=\mathbb{P}(\{1\})=\mathbb{P}(\{2\})= \dots = \mathbb{P}(\{N\})=N_{p}$$da cui si deduce che $\mathbb{P}(\{i\}) = p = \frac{1}{N}$ , per tutti gli $i = 1, 2, \dots, N$ . Da questo risultato e ancora dal [[Assioma Terzo|terzo assioma]] si conclude che per ogni evento $E$:$$\mathbb{P}(E)=\frac{|E|}{N}$$
>[!important] Detta proprietà di equiprobabilità

^17d378

>[!success] In altre parole
> Se si assume che ogni esito di $\Omega$ abbia la medesima probabilità, allora la probabilità di un qualunque evento $E$ è pari al rapporto tra il numero di esiti contenuti in $E$ e il numero totale di esiti di $\Omega$. 
> Una conseguenza notevole di questo risultato è che occorre sapere contare efficacemente il numero degli esiti differenti appartenenti ad un [[evento]]. A questo scopo faremo uso del [[PF del calcolo combinatorio|Principio fondamentale del calcolo combinatorio]] dove per sotto-procedure si intendono gli esiti possibili.