---
tags:
---
Siano $a,b,m \in \mathbb{Z}$
$$a \equiv_m b \iff \frac{m}{(a,b)} \iff \exists c \in \mathbb{Z} : a-b=cm$$
###### _Esempio 1_
$m =5, \ a=7, \ b=10 \implies 7\equiv_5 10 \iff \frac{5}{7-10} = \frac{5}{-3}$
La congruenza non vale perché $5$ non divide $-3$

---
###### _Esempio 2_
$m = 2, \ a = 11, \ b=3 \implies 11 \equiv_2 3 \iff \frac{2}{11-3} \iff \frac{2}{8}$

---

_Casi Particolari_ ^b0ef1d
- <span style="color:#ffbe0a">Relazione di Uguaglianza</span>
	 $m = 0 : a \equiv_0 b \iff \frac{0}{a-b} \iff a-b = 0 \implies a = b$ ^492ca3
- <span style="color:#ffbe0a">Relazione Totale</span>
	$m = 1 : a \equiv_1 \iff \frac{1}{a-b}$ ^9bc247

---
### Definizioni
- $[a]_m = \{ z \in \mathbb{Z} | x \equiv_m a \}$
- $\mathbb{Z}_m = \{[a]_m | a \in \mathbb{Z}\}$
### Teorema 1
Sia $m \in \mathbb{N}^*$ e $a,b \in \mathbb{Z}$
$$a \equiv_m b \iff rest(a,m) = rest(b,m)$$
##### Dim $\implies$
$a \equiv_m b \iff \frac{m}{a-b} \iff \exists h \in \mathbb{Z} | a-b = hm$
$\implies a = b + hm$
	- $\exists ! \ q,r \in \mathbb{Z}: b = mq + r$ con $0 \leq r < m$
	- $a = mq_1 + r + mq_2 = m(q_1+q_2)+ r$ con $0 \leq r < m$
	$\implies r = rest(a,m) = rest(b,m)$

##### Dim $\impliedby$ 
$a = mq_1 +r$
$a = mq_2 + r$
$a-b = (mq_1 + r) - (mq_2 + r) =$
	$=mq_1 + r - mq_2 - r = mq_1 - mq_2 =$
	$=m(q_1 - q_2)$
$a \equiv_m b \iff \frac{m}{a-b} \iff \exists(q_1+q_2)\in \mathbb{Z}: a-b = m(q_1+q_2)$

### Teorema 2
Sia $m \in \mathbb{N}^*$
L'insieme quoziente $Z_m$ ha ordine $(m)$ e risulta
$$Z_m =\{[0], [1], \ ...\ ,[m-1]  \}$$
##### Esempio
$0 = 0_m + 0$
$1 = 1_m + 1$

$Z_4 = \{ \overline{0}, \overline{1}, \overline{2}, \overline{3} \}$
$Z_5 = \{ \overline{0}, \overline{1}, \overline{2}, \overline{3}, \overline{4} \}$



### Osservazioni
$f: a \in \mathbb{Z} \longrightarrow rest(a,m) \in \mathbb{Z}$
$R_f: \forall a,b \in \mathbb{Z}(aR_f b \iff rest(a,m)=rest(b,m))$
### Proposizioni
#### Proposizione 1
Siano $m \in \mathbb{N}^*, a\in Z$
$$[a]_m = [rest(a,m)]$$
##### <span style="color:#c800ff">Esempio </span>
- $[24]_2 = [2 \cdot 12 + 0] = [0]_2$
- $[75]_6 = [6 \cdot 12 + 3] = [3]_6$

##### <span style="color:#ffbe0a">Dimostrazione</span>
$\exists!\ q, r \in Z (a = mq + r)$ con $0 \leq r < |m| = m$
	$a =mq + r \implies a-r = qm \implies \frac{m}{a-r}$
	$\implies a \equiv_m r \implies [a]_m = [r]_m$

#### Proposizione 2
Siano $m \in \mathbb{N}^*, a\in Z$
$$[a]_m = \{ a+mk \ | \ k \in Z \}$$
##### <span style="color:#ffbe0a">Dimostrazione</span>
$\forall x \in \mathbb{Z},\ x\in [a]_m \iff x \equiv_m a \iff \frac{m}{x-a} \iff \exists k \in \mathbb{Z} (x-a = km)$
	$x = a+km \implies x \in \{ a + km | k \in \mathbb{Z} \}$

## Parte 2

### Struttura $(Z_m, +, \cdot)$
È un anello commutativo unitario
#### Compatibilità
La relazione di congruenza modulo $m$ è compatibile rispetto alla somma ed al prodotto.
$$(a \equiv_m b) \land (c \equiv_m d) \implies a + c \equiv_m b+d \implies a \cdot c \equiv_m b \cdot d$$

### <span style="color:#ffbe0a">Esercizio</span>
Per quali $m$?
$\overline{7} \cdot \overline{5} = \overline{1}$
	$\overline{35} = \overline{1} \iff 35 \equiv_m 1 \iff \frac{m}{34}$
	$\iff m=2 \lor m=17$

### Invertibilità di una classe in $Z_m$
#### Teorema di Bezout
$$d = MCD(a,b) \implies \exists h,k \in Z(d = ah+bk)$$
In generale $\impliedby$ non vale
$1 = MCD(a,b) \iff \exists h,k \in Z (1 = ah+bk)$

##### <span style="color:#ffbe0a">Esempio</span>
<span style="color:#c800ff">Esempio 1</span>
$a = 37, \ b=15$
$37 = 15 \cdot 2 + 7 \implies 7 = 37-15 \cdot 2$
$15 = 7 \cdot 2 + 1$
$1 = 15-7 \cdot 2$
$1 = 15 - (37 - 15 \cdot 2) \cdot 2$
$1 = 15 + 37(-2) + 15(4) = 37(-2) + 15(5)$
- quindi $h = -2, \ k = 5$

<span style="color:#c800ff">Esempio 2</span>
$a=12, \ b=7, \ MCD(7,12)=1$
$\implies \exists h,k \in \mathbb{Z} (1 = 7h + 12k)$

$12 = 7 \cdot 1 + 5$
$7 = 5 \cdot 1 + 2$
$5 = 2 \cdot 2 + 1$
 _Scrivi tu mi sto ingrippando, grz_





















### Invertibilità di una classe
Sia $m \in \mathbb{N}^*$ e sia $a \in Z_m / \{\overline{0}\}$
$$\overline{a} \ è \ invertibile \iff MCD(>0)(a,m)=1$$

In parole povere, se tra un elemento della classe ed il modulo l'MCD è 1, l'elemento è invertibile
#### Dim $\implies$
$\overline{a} \ invertibile \iff \exists \overline{b} \in Z_m: \overline{b} \cdot \overline{a} = 1$
$\implies \exists \overline{b} \in Z_m: \overline{ab}=\overline{1}$
$\implies \exists b \in Z: \frac{m}{(ab-1)}$
$\implies \exists b,h \in Z : ab-1=mh$
$\implies 1 = ab-mh$
$\overset{Bezout}{\implies} \exists h,h \in Z (ah - mk = 1) \implies a,m \ sono \ coprimi \implies MCD(a,m)=1$
#### Dim $\impliedby$
$MCD(a,m) = 1 \overset{Bezout}{\implies} \exists h,k \in Z (1 = ha +km)$
$\implies \overline{1} = \overline{ha+km} \implies \overline{1} = \overline{h} \cdot \overline{a} + \cancel{\overline{k} \cdot \overline{m}}$ poiché $\overline{m} \in Z_m$ è $0$
Quindi $\overline{a}$ è invertibile e $\overline{h}$ è il suo inverso.

