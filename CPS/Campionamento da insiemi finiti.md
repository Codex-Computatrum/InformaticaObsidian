---
author: Lorenzo Tecchia
tags:
  - definition
  - statistics
  - sampling
---
Consideriamo una [[popolazione]] di $N$ elementi. Con il concetto di [[campione]] aleatorio (di numerosità $n$ ) estratto da questa [[popolazione]], si intende la scelta di un sottoinsieme di $n$ elementi, fatta in modo tale che tutti i $\left(\begin{array}{l}N \\ n\end{array}\right)$ sottoinsiemi candidati abbiano le stesse [[probabilità]] di essere selezionati. Per esempio, se la [[popolazione]] di partenza consiste dei tre elementi $a, b \; \mathrm{e}\; c$, un campione casuale di due elementi è un sottoinsieme scelto con pari probabilità tra $\{a, b\},\{a, c\} \in\{b, c\}$. Un sottoinsieme casuale può essere individuato in pratica scegliendo uno alla volta i suoi elementi: il primo con pari probabilità tra gli $N$ possibili, il secondo con pari probabilità tra gli $N-1$ restanti, e così via.

Supponiamo ora che alcuni elementi della [[popolazione]] di partenza abbiano una certa caratteristica, e denotiamo con $p$ la frazione di questi rispetto al totale. Vi sono complessivamente $p N$ elementi che posseggono questa caratteristica e $(1-p) N$ che non ce l'hanno. Selezioniamo un campione casuale di ampiezza $n$, e dopo avere numerato i suoi elementi, poniamo, per $i$ che va da 1 a $n$ :$$X_{i}:= \begin{cases}1 & \text { se l'elemento } i \text { del campione possiede la caratteristica } \\ 0 & \text { altrimenti }\end{cases}$$
Consideriamo la somma di queste variabili aleatorie,$$X:=X_{1}+X_{2}+\cdots+X_{n}$$

Siccome ognuna delle $X_{i}$ contribuisce con $1$ o con $0$ alla somma, a seconda che l'elemento $i$ possieda la caratteristica saliente o meno, $X$ conta quanti sono in tutto quelli che la possiedono. Inoltre la [[Valore atteso|media]] campionaria$$\bar{X}=\frac{X}{n}=\frac{1}{n} \sum_{i=1}^{n} X_{i}$$ è pari alla frazione degli elementi del campione che mostrano tale caratteristica.

Passiamo ora ad analizzare le probabilità associate alle statistiche $X$ e $\bar{X}$. Per cominciare, si noti che, siccome ciascuno degli $N$ elementi di partenza ha le stesse  possibilità di essere selezionato come membro $i$-esimo del campione, si ottien $$ P\left(X_{i}=1\right)=\frac{p N}{N}=p$$
Da cui ovviamente segue che $$P\left(X_{i}=0\right)=1-p$$

Le $X_{i}$ sono variabili aleatorie di [[Bernoulliana|Bernoulli]] di parametro $p$.

È bene notare che $X_{1}, X_{2}, \ldots, X_{n}$ non sono indipendenti. Nonostante infatti sia $p$ la probabilità che nella seconda selezione capiti un elemento con la caratteristica, $$ P\left(X_{2}=1\right)=p $$

ciò è vero solo se non si sa nulla di cosa sia successo nelle altre estrazioni. Supponendo ad esempio di sapere che $X_{1}=1$, ovvero che nella prima è stato selezionato un elemento tra i $p N$ con la caratteristica, è chiaro che $$P\left(X_{2}=1 \mid X_{1}=1\right)=\frac{p N-1}{N-1}$$

perché nella [[popolazione]] restano $N-1$ elementi, di cui $n P-1$ con la caratteristica. In maniera del tutto analoga, se si sa che $X_{1}=0$, $$ P\left(X_{2}=1 \mid X_{1}=0\right)=\frac{p N}{N-1}$$

Perciò il sapere se il primo membro selezionato per entrare a fare parte del campione abbia la caratteristica, modifica le probabilità per quelli successivi. Tuttavia, se la numerosità della [[popolazione]] $N$ è molto grande rispetto a quella del campione $n$, questa variazione nelle probabilità sarà in ogni caso molto piccola. Per fare un esempio, se $N=1000$ e $p=0.4$, si ottengono le probabilità $$
\begin{aligned}
& P\left(X_{2}=1 \mid X_{1}=1\right)=\frac{399}{999} \approx 0.3994 \\
& P\left(X_{2}=1 \mid X_{1}=0\right)=\frac{400}{999} \approx 0.4004
\end{aligned}$$ entrambe molto vicine a $$ P\left(X_{2}=1\right)=0.4 $$

In effetti è possibile dimostrare che quando l'ampiezza della [[popolazione]] $N$ è molto maggiore di quella del campione $n$, allora $X_{1}, X_{2}, \ldots, X_{n}$ sono approssimativamente indipendenti. Siccome la somma di bernoulliane indipendenti e identicamente distribuite è una [[variabile aleatoria]] [[binomiale]], ṇe segue - sempre nell'ipotesi che $N$ sia grande rispetto a $n$-che $X:=\sum_{i} X_{i}$ è approssimativamente distribuita come una binomiale di parametri $n$ e $p$.