Esercizi da voto 21 in giù in genere
1. Disegnare memory layout di un codice C o Java
2. Funzioni in [[EserciziP|Prolog]] o [[EserciziML|ML]]
3. [[Exceptions|Come si lancia un'exception, ciclo di vita exception, come si dichiara.]]
4. [[Note esercizi binding#^instanceof|Operatore instanceof]]
5. Quali sono le conversioni possibili.
   - Conversioni implicite: [[Autoboxing]], [[Autounboxing]]
   - [[Cast]]
6. Come funzionano mem-env
		- Linguaggi imperativi: 
		  $env: name \to address$
		  $mem: address \to value$
		- Linguaggi funzionali:
		  $env: name \mapsto value$
7.  Come funziona il salvataggio in memoria delle variabili
   - Variabili locali: variabili dichiarate all'interno di un blocco di codice e con scope limitato a quel blocco, dopo l'uscita dal blocco viene perso il valore perché il blocco viene rimosso dallo stack di esecuzione.
   - Variabili globali: non è possibile utilizzare variabili puramente globali (come in C), ma è possibile fare qualcosa di simile dichiarando una variabile `static` all'interno di una classe, sarà possibile accedere a quella variabile tramite `Nomeclasse.variabile`.
   - Variabili di istanza: variabili definite all'interno di una classe e associate a un'istanza specifica di quella classe (object), esistono fino a quando c'è un riferimento attivo all'object.
8. Perdita di informazioni dopo conversioni
	   - Succede solo tramite [[Cast|conversioni esplicite]], alcuni esempi sono le conversioni di un `double` in `int`, in cui viene persa la parte decimale, oppure di un `long` in `int` per numeri superiori a $2.147.483.647$
9. Esercizio su prolog, dati fatti e regole dire se fanno match utilizzando il MGU
10. Cos'è il [[Unificazione e MGU|MGU]]
11. Differenza tra [[Sostituzione|sostituzione]] e [[Unificazione e MGU|unificazione]] in prolog
12. Come trovare una [[Firme candidate|firma candidata]]
13. [[Binding|Early e late binding]]
14. Differenza tra [[Modificatori|modificatori]].