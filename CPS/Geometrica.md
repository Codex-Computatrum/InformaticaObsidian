---
author: Lorenzo Tecchia
tags:
  - definition
  - probability
  - distribution
---
In un esperimento di prove ripetute, sia $p$ la [[probabilità]] di successo in ciascuna prova e $q = 1-p$ la [[probabilità]] di insuccesso. Supponiamo di essere interessati al primo successo. 
Sia, dunque, $X$ la [[variabile aleatoria]] che conta il numero di prove necessarie per vedere il primo successo.
Ad essa si dà il nome di variabile Geometrica, $X\sim G(p)$ $$S_{X}=\{1, 2, \dots \}$$
La massa $p_{X}(x)$ rappresenta la probabilità di contare esattamente $x-1$ insuccessi e $1$ successo all'ultima prova. Quindi la sequenza che soddisfa l'[[evento]] richiesto è una sola ed ha probabilità di occorrenza pari a $pq^{x-1}$ (ricordando che le prove sono indipendenti)[^1].
$$
\begin{gathered}
p_X(i)=p q^{i-1} \quad(i=1,2, \ldots) \\
\sum_{i=1}^{\infty} p q^{i-1}=p \sum_{i=1}^{\infty} q^{i-1}=p \underbrace{\sum_{s=0}^{\infty} q^{s}=p \frac{1}{1-q}=\frac{p}{p}=1}_\text{Somma della serie geometrica} \\
F_X(x)=\sum_{i=1}^x p q^{i-1}=p \sum_{i=1}^x q^{i-1}=p\underbrace{ \sum_{s=0}^{x-1} q^s=p \frac{1-q^x}{1-q}}_\text{serie geometrica arrestata}=1-q^x .
\end{gathered}
$$

>[!important] ## Proprietà di assenza di memoria della [[variabile aleatoria]] Geometrica
> Sia $X \sim G(p), r, s \in \mathbb{N}$, allora $$\mathbb{P}(X>r+s \mid X>r)=\mathbb{P}(X>s)$$
> ***Dimostrazione:*** $$\begin{gathered}
\mathbb{P}(X>r+s \mid X>r)=\frac{\mathbb{P}(\{X>r+s\} \cap\{X>r\})}{\mathbb{P}(X>r)}=\frac{\mathbb{P}(\{X>r+s\})}{\mathbb{P}(X>r)} \\
=\frac{1-F_X(r+s)}{1-F_X(r)}=\frac{q^{r+s}}{q^r}=q^s=1-F_X(s) .
\end{gathered}$$

[^1]: Riepilogo serie geometrica $h \in \mathbb{R}, 1+h+h^2+\ldots+h^n=\frac{1-h^{n+1}}{1-h}$ (progressione geometrica di ragione $h$ - somma parziale) $|h|<1 \quad S=\lim _{n \rightarrow \infty} \frac{(1-h)^{n+1}}{1-h}=\frac{1}{1-h}$ (è il limite della somma parziale)