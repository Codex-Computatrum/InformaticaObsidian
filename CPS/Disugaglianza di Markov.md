---
author: Lorenzo Tecchia
tags:
  - statistics
  - theorem
---
Se $X$ è una [[variabile aleatoria]] che non è mai negativa, allora per ogni $a > 0$: $$\mathbb{P}(X \geq a) \leq \frac{E[X]}{a}$$
***Dimostrazione***. Diamo la dimostrazione nel caso che $X$ sia [[Continua|continua]] con densità $f$.
$$
\begin{array}{rlrl}
E[X] & :=\int_{0}^{\infty} x f(x) d x & \\
& =\int_{0}^{a} x f(x) d x+\int_{a}^{\infty} x f(x) d x \\
& \geq \int_{a}^{\infty} x f(x) d x & & \text { perché il primo } \\
& \geq \int_{a}^{\infty} a f(x) d x & & \text { addendo è positivo } \\
& =a \int_{a}^{\infty} f(x) d x & & \text { perché } x \geq a \text { nella  ragione di integrazione} \\
& =a \mathbb{P}(X \geq a) &
\end{array}$$
E l'enunciato segue dividendo i termini per $a$.

Come corollario ricaviamo la [[Disugaglianza di Chebyshev]]