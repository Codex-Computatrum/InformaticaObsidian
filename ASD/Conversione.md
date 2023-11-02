---
tags:
  - definition
  - example
author: Lorenzo Tecchia
---
Qualsiasi [[algoritmo]] ricorsivo può essere trasformato in iterativo e viceversa.  
La [[ricorsione]] permette di risolvere problemi difficili in modo semplice rispetto all’iterazione, però è svantaggiosa in termini di [[memoria]], dato che ogni chiamata alloca memoria per tenere traccia delle variabili locali, il valore di ritorno, e così via.
![[Pasted image 20230911152220.png]]
Questa funzione è **tail recursive** (ricorsiva in coda), cioè la chiamata ricorsiva è eseguita come ultima istruzione. Inoltre modifico $x$ senza riutilizzare il suo vecchio valore, quindi si spreca solo memoria.
($x$ viene modificata in riga $5$, dato che la chiamata ricorsiva sostituisce $x$ con $x.sx$)

### Esempio
Scorrimento in [[Order-pre|pre-ordine]] e [[Order-post|post-ordine]] su una [[Lista Concatenata|lista]]
- $L$ lista
- $F$ funzione che effettua operazioni sull'accumulatore
- $a$ accumulatore: variabile che sarà restituita come risultato della funzione
![[Pasted image 20230911153613.png]]
La funzione ricorsiva è **tail recursive**, inoltre $L$ ed a vengono modificati ma non utilizzati dopo la chiamata ricorsiva, $F$ invece viene modificato ma con lo stesso valore (è come se non venisse mai cambiato).
Quindi non c’è bisogno dello [[stack]].

![[Pasted image 20230911153706.png|400]]
Nella versione in Post-Order, non essendo tail recursive, non si può applicare lo stesso ragionamento

Se si hanno delle variabili locali, quindi anche i parametri della funzione, che sono utilizzati prima della chiamata ricorsiva e utilizzati dopo, allora serve salvarli.

Dato che nella versione iterativa si avrà che quella variabile ad ogni iterazione verra sovrascritta dal nuovo valore, se dopo averla modificata si volesse utilizzare il valore precedente, non si potrebbe, quindi va salvato.

Nelle tail recursive il valore può essere sovrascritto senza problemi, tanto non ci saranno utilizzi dopo la chiamata.

Nelle non-tail recursive salviamo le variabili in uno **stack**. Non è possibile quindi fare a meno di uno stack, ma si farà a meno dello stack di sistema.

## Traduzione di un algoritmo
Questo è un algoritmo che lavora su un [[Tree|albero]]; non c’è semantica, serve solo come esempio per vedere la traduzione da ricorsivo a iterativo.

![[Pasted image 20230911154113.png|400]]
$F$, in generale, è una certa funzione che elabora i dati e restituisce un valore, il pedice di ognuna serve solo per dare un minimo di significato.
- $F_{ini}\;\;$ **ini**ziale, viene eseguita all'inizio della funzione ricorsiva
- $F_{\bot}\;\;$ viene eseguita quando $x=\bot$
- $F_{pre}\;\;$ eseguita in **[[Order-pre|pre-ordine]]**
- $F_{post}\;\;$eseguita in **[[Order-post|post-ordine]]**
- $F_{in}\;\;$eseguita in **[[Order-in|in-ordine]]**
- $F_{fin}\;\;$eseguita alla fine della funzione ricorsiva

#### Analizziamo quali variabili hanno bisogno dello stack, iniziamo con i parametri:
- $\textbf{x}$:
	- riga $7$, viene sostituita con $x.sx$ (viene sostituito il primo parametro nella chiamata ricorsiva, cioè $x$)
	- riga 8, viene letta $x$ che però ho perso avendola sostituita prima
	- ***Ha bisogno dello stack***
- $\textbf{i}$:
	- riga $7$, viene sovrascritto con lo stesso valore, quindi non crea problemi
	- riga $9$, viene sostituita con $k_R$ , ma i non verrà utilizzata dopo, quindi non crea problemi
	- ***Non ha bisogno dello stack***
- $\textbf{j}$:
	- riga $7$, viene sostituita con $k_{L}$ 
	- riga $9$, viene letta $j$ che però ho perso avendola sostituita prima
	- ***Ha bisogno dello stack***
#### Analizziamo le variabili interne 
- $\textbf{a}$:
	- viene letta prima delle chiamate ricorsive, ma mai dopo
	- ***Non ha bisogno dello stack***
- $\textbf{m}$:
	- non viene mai letta
	- ***Non ha bisogno dello stack***
- $\textbf{z}_R$:
	- viene scritta in riga $9$ e letta in riga $10$, ma la scrittura avviene dopo le chiamate ricorsive
	- ***Non ha bisogno dello stack***
- $\textbf{k}_{R},\textbf{k}_{L}$:
	- vengono scritte prima di una chiamata ricorsiva, ma non lette dopo
	- ***Non hanno bisogno dello stack***
- $\textbf{h}_{R},\textbf{h}_{L}, \textbf{z}_{L}$:
	- vengono sia scritte che lette dopo una chiamata ricorsiva
	- ***Hanno bisogno dello stack***

Hanno bisogno dello stack: $x, j, h_{R} , h_{L} , z_{L}$
Utilizziamo una variabile booleana call per capire se è stata fatta una chiamata ricorsiva (quindi sto ”scendendo”, call = `TRUE`) oppure è stato fatto un return (quindi sto ”risalendo”, call = `FALSE`)

Quando c’è più di una chiamata ricorsiva, bisogna tenere traccia da quale (due in questo caso) si sta ritornando.  
In questo caso utilizziamo come discriminante il fatto che la prima chiamata venga fatta sul figlio sinistro di x e la seconda chiamata sul figlio destro. Quindi si salva nella variabile last l’ultimo nodo utilizzato. Con un opportuno controllo è possibile sapere quindi se si ritorna dalla prima o dalla seconda chiamata.

Il ***return*** viene simulato assegnando il valore da restituire in una variabile (ret, ad esempio)

![[appuntiIngenito.pdf#page=53]]

call è inizialmente `TRUE` perché sta simulando la prima chiamata, oltre al fatto che gli stack sono inizialmente tutti vuoti.

C’è lavoro da fare finché ci sono ancora valori negli stack. In questo caso basta controllare solo lo stack di un parametro della funzione, svuotato quello sicuro lo saranno anche gli altri.

L’$if$ in riga $25$ simula il caso in cui $x.dx = \bot$. Questo perché il caso in cui è il sinistro ad essere $\bot$ viene gestito dall’if in riga $7$, ma non viene gestito il caso del figlio destro.  
Questa simulazione viene fatta quando si sta ritornando dalla chiamata ricorsiva sul figlio sinistro, per questo motivo si trova all’interno dell $if\;last = x.sx$ 

### Se la funzione è tail recursive
>[!summary] 
> - Inizializzo un accumulatore prima della $while$
> - Uso la negazione del caso base come condizione del $while$ 
> - Uso il corpo della funzione ricorsiva(escludendo la chiamata ricorsiva della funzione) come il corpo del $while$
> -  Alla fine del $while$ aggiungo all'accumulatore il caso base e ritorno l'accumulatore come output

### In generale
>[!summary] 
> Ricapitolando:
> - Individuare gli stack
> - $call \leftarrow true$
> - Il $while$ scorre finché è in discesa ($call = true$) oppure finchè gli stack non sono vuoti.
> - Al suo interno viene gestita la discesa e la risalita:
> 	- Se $call = true$ allora la funzione scende, altrimenti risale
> 	- Dopodiché ricopio il corpo della funzione ricorsiva finché non si incontra un return oppure una chiamata ricorsiva
> - Se incontro un $return$
> 	- Inserisco in $ret$ il valore restituito
> 	- Imposto il discriminante $last$
> 	- Eseguo il $Pop$ delle variabili utilizzate (pushate in precedenza)
> 	- Imposto il $call \leftarrow false$ perché dopo il $return$ la funzione risale
> - Se incontro una chiamata ricorsiva:
> 	1. Preparo gli stack, quindi faccio il push delle variabili che sono state utilizzate
> 	2. Sostituisco le variabili dei parametri con gli argomenti della chiamata
> 	3. Imposto $call \leftarrow true$ perché dopo la $chiamata ricorsiva$ la funzione scende
