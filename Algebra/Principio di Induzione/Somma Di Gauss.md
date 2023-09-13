Supponiamo di voler dimostrare 
	$P(n)$ = la somma dei primi $n \in \mathbb{N}$ è $\frac{n(n+1)}{2}$ 

BASE
	$n_0 = 1 \implies P(1)$  è vera;
		$\frac{1(1+1)}{2} = \frac{2}{2} = 1$

PASSO
	$\forall n>1 (P(n-1) \implies P(n))$ 
		$P(n-1) = 1+2+3+...+n-1 =\frac{(n-1)n}{2}$
		$P(n) = 1+2+3+...+n-1+n =\frac{(n-1)n}{2} + n$
		$P(n) = \frac{n(n-1)+2n}{2} = \frac{n^2 + n}{2} = \frac{n(n+1)}{2}$