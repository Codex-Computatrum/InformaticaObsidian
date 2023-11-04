Sia $f \in A[x] / \{ 0 \} | f=a_0+a_1x+ a_2x^2+ \dots + a_nx^n$ 

Si definisce <span style="color:#c800ff">grado del polinomio</span> $f$:
$$\delta (f) = max(T)$$
$T=\{ m\in \mathbb{N} | a_m \neq 0 \}$
$\delta(f) = n$

- $a_n$ è parametro direttore di $f$
- $a_n = 1$ $\implies$ $f$ si dice <span style="color:#ffbe0a">monico</span>
#### Gradi Particolari
- $f \in A/\{ 0 \}$        $\delta(f) = 0$
- $f = 0$                $\delta(f) = -\infty$ 
### Proposizione
Siano $f,g \in A[x]$ con $\delta(f)=n e \delta(g)=m$
- $\delta(f+g) \leq max\{ \delta(f), \delta(g) \}$
- $\delta(f \cdot g) \leq \delta(f)+\delta(g)$
#### <span style="color:#ffbe0a">DIM</span>
$$f = 0 \implies \delta(g) \leq max \{ -\infty, \delta(g) \} \implies \delta(g) \leq \delta(g)$$
Poniamo $f, g \neq 0$ e $n,m \geq 0$
$\delta(f+g) = max\{ \delta(f), \delta(g) \}$
$f=x+1, \ g=x+2, \ f+g=2x+3$
$\delta(f+g)=1 \leq max\{ 1,1 \} \implies \delta(f+g)=max\{ \delta(f), \delta(g) \}$
$f=x+1, \ g=-x+1, \ f+g=2$
$\delta(f+g)=0 < 1$

### Regola di Addizione dei gradi
Se $A$ è un [[Dominio di integrità]]
$\delta(f\cdot g) = \delta(f) + \delta(g)$