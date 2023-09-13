Data la struttura algebrica $(S, \star): a \in S$ è invertibile $\leftrightarrow \exists b \in S : a \star b = b \star a = \epsilon$
## Proprietà
- Il simmetrico di un elemento è **unico** (per ogni operazione): $b$ è l'unico simmetrico di $a$.
	- In notazione additiva il simmetrico di $a$ è $(-a)$
	- In notazione moltiplicativa il simmetrico di $a$ è $a^{-1}$
- Il simmetrico dell'[[Elemento neutro|elemento neutro]] è l'elemento neutro stesso. $(\epsilon \star \epsilon = \epsilon)$ 
# Invertibile implica [[Elementi cancellabili|cancellabile]]
Sia $(S, \star)$ un [[Monoide|monoide]] e siano $a,x,y \in S$:
- Se $a$ è invertibile (a sinistra o destra) $\implies$ $a$ è cancellabile (a sinistra o destra)
## Dimostrazione
$$a \star x = a \star y$$
$$a^{-1} \star (a \star x) = a^{-1} \star (a \star y)$$
$$\epsilon \star x = \epsilon \star y$$
$$ x = y$$
$\forall x, y \in S (a \star x = a \star y \implies x = y)$ cioè che $a$ è [[Elementi cancellabili|cancellabile]].