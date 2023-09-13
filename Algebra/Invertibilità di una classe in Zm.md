Sia $m \in \mathbb{N} \backslash \{0\}$ e sia $a \in \mathbb{Z} \backslash \{\overline{0}\}$.
$\overline{a}$ è invertibile in $Z_m \iff MCD(a,m)[>0]=1$
### Dimostrazione
#### Dim $\textcolor{red}{\implies}$
$\overline{a}$ è invertibile $\overset{def}{\iff} \exists \overline{b} \in \mathbb{Z}_m : \overline{b} \cdot \overline{a} = \overline{1} \implies \exists \overline{b} \in \mathbb{Z}_m : \overline{ab} = \overline{1}$ 
$\implies \exists b \in \mathbb{Z} : m|ab-1$
$\implies m|ab-1 \iff \exists b,h \in \mathbb{Z}:ab-1=mh \implies 1=ab-mh$
Per il [[Teorema di Bezout|teorema di Bezout]] $\implies \exists h,k \in \mathbb{Z} (ah \cdot mk = 1) \implies a,m$ sono [[Numeri coprimi|coprimi]] $\implies MCD(a,m)=1$.
#### Dim $\textcolor{red}{\impliedby}$
$MCD(a,b) = 1 \implies \exists h,k \in \mathbb{Z} (1=ha+km)$
$\implies \overline{1} = \overline{ha+km} \implies \overline{1} = \overline{h} \overline{a} + \overline{k}\overline{m}$
Dove $\overline{k} \overline{m} = 0$, di conseguenza $\overline{a}$ è invertibile, con inverso $k$.

#### Esercizio
Sia $\mathbb{Z}_6$ l'insieme delle classi 