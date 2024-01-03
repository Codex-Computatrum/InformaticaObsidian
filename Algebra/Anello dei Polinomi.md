Sia $A$ un anello commutativo unitario.
Si definisce anello dei polinomi nell'indeterminata $x$ l'anello indicato con $A[x]$ che contiene $A$ e a cui appartiene un elemento $x$ tale che:
$$\forall f \in A[x], \ f=a_0+a_1x+ a_2x^2+ \dots + a_nx^n$$
$$A[x]=\{ f=a_0+a_1x+ a_2x^2+ \dots + a_nx^n | a_i \in A, n \in \mathbb{N} \}$$
- Ponendo $a_i = 0 \ (\forall i >n)$ gli $a_i \in A$ si dicono coefficienti di $f$.
- Due polinomi sono uguali se e solo se i loro coefficienti coincidono

#### <span style="color:#ffbe0a">Esempio</span>:
Per quali $m$ si ha $f = g$?  $A = \mathbb{Z}_m$
$f = \overline{3} + \overline{25}x^2$
$g = \overline{3} + \overline{22}x^2$

$f = g \iff \overline{25} = \overline{22} \iff 25 \equiv_m 22$
$f = g \iff m | (25-22) \iff m | 3 \iff m=3$
