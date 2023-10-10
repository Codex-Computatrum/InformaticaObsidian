---
author: Lorenzo Tecchia
tags: [definition, probability, example]
---
Sia $\xi$ un esperimento non deterministico (non prevedibile, aleatorio). In particolare poniamo $\xi$ uguale al lancio di un dado onesto. Lo spazio degli esiti è quindi $\Omega = \{1, 2, 3, 4, 5, 6\}$. 
Ci troviamo nella situazione in cui ogni esito ha la stessa probabilità di verificarsi. Ci mettiamo nell’ambito delle scommesse.
Supponiamo che sia possibile scommettere su questi due eventi $A$ e $B$:
- $A = {2, 4, 6}$, cioè esce un punteggio pari
- $B = {5, 6}$, cioè esce un punteggio alto
>[!note] Ci domandiamo quali possano essere tutti i possibili [[Evento|eventi]] di questo gioco

Questi sono tutti gli eventi ottenibili a partire dagli eventi $A$ e $B$. E’ possibile scommettere su $A \cup B$ ad esempio, oppure su $A \cap B$:$$\begin{align}
&\mathbb{P}(A) = \frac{3}{6}&=\frac{1}{2} \\
&\mathbb{P}(B) = \frac{2}{6}&=\frac{1}{3} \\
&\mathbb{P}(A \cap B) &= \frac{1}{6}\\
&\mathbb{P}(A \cup B) &= \frac{1}{6}
\end{align}$$
>[!important] 
> Ma sono eventi anche $A^c$ oppure $B^c$ (punteggio **medio** o **basso**).

>[!note] Ci domandiamo come possiamo ottenere la ***famiglia degli atomi***, cioè tutti quegli eventi che non sono ulteriormente scomponibili

Possiamo ricorrere alla tecnica molto semplice del ***metodo degli atomi***. Ad esempio, la famiglia degli atomi di questo gioco è ottenibile in questo modo (applicando il metodo degli atomi):$$\begin{align}
&A \cap B = \{6\}\\
&A \cap B^{c} = \{2,4\}\\
&A^{c} \cap B = \{5\}\\
&A^{c} \cap B^{c} = \{1,3\}
\end{align}$$
Ed ecco quindi che gli eventi $A$ e $B$ vengono chiamati ***eventi generatori*** e la loro aggregazione definisce la ***famiglia degli eventi generatori***, che in questo caso è:$$\mathcal{G}:= \{A \cap B,A \cap B^{c}, A^{c} \cap B,A^{c} \cap B^{c} \}$$

---
Definiamo adesso l’operazione **sigma** (denotata con $\sigma$) sulla famiglia degli eventi generatori che è la ***famiglia degli eventi generata dalla famiglia degli eventi generatori*** applicando $\cup$, $\cap$ e il complemento $c$ in tutti i modi possibili. In questo caso otteniamo:$$\begin{align}
\sigma(\mathcal{G}) = &\{\{5\},\{6\},\{1,3\},\{2,4\},\{5,6\},\{1,3,5\},\{2,4,5\}, \{1,3,6\},\{2,4,6\},\{1,2,3,4\},\\ &\{1,3,5,6\},\{2,4,5,6\},\{1,2,3,4,5,6\},\{1,2,3,4,5\},\Omega,\emptyset\}
\end{align}$$

Un altro esempio di famiglia di eventi generatori dove l’applicazione dell’operazione sigma su di essa corrisponde esattamente alle parti di $\Omega$, cioè $\mathcal{P}(\Omega)$:$$\begin{align}
\mathcal{G}&=\{\{1\}, \{2\}, \{3\}, \{4\}, \{5\}, \{6\}\} \\
\sigma(\mathcal{G})&=\mathcal{P}(\Omega)
\end{align}$$
>[!note] 
> Notiamo che comunque prendiamo due elementi dalla famiglia degli eventi generata dalla famiglia degli eventi generatori ed eseguiamo una qualsiasi operazione insiemistica su questi due elementi, il risultato continua ad appartenere alla famiglia.