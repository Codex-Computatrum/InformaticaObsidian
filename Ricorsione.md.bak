---
author: Simone Parente
---
>[!summary] Riassunto
>Una funzione ricorsiva è una funzione espressa in termini di sé stessa, suddividendo il problema in tanti piccoli(ssimi) sottoproblemi di più facile soluzione.

```c
void stampaInfinita(){
	printf("sono una funzione che stampa all'infinito\n");
	stampaInfinita();
}
```
Questa sopra è una funzione che richiama sé stessa, quindi è per definizione ricorsiva, ma stampa all'infinito una stringa senza possibilità di terminare il programma (se non aspettando che la memoria sia satura o terminandolo forzatamente). Proviamo qualcosa che *almeno* possa terminare dopo un numero finito di passaggi.
```c
void stampaFinita_v1(int numeroDiVolte){
	if(numeroDiVolte==0){
		printf("Questa sarà la prima stringa ad essere stampata\n");
	}
	else{
		printf("Questa è la stringa numero [%d]\n", numeroDiVolte);
		stampaFinita_v1(numeroDiVolte-1);
	}
}
```
Supponiamo di avere una chiamata nel `main` del tipo `stampaFinita_v1(3)`, prova a scrivere l'output del programma.
\
\
\
\

$$\textcolor{red}{\text{NON SCENDERE PRIMA DI AVER LETTO TUTTO QUEL CHE C'È PRIMA}}$$

---
---
---
---
---
---
---
L'output sarà il seguente:

	Questa è la stringa numero [5]
	Questa è la stringa numero [4]
	Questa è la stringa numero [3]
	Questa è la stringa numero [2]
	Questa è la stringa numero [1]
	Questa sarà l'ultima stringa ad essere stampata
>[!attention] Spiegazione
Questo perché la funzione controlla prima di tutto che la condizione 
`if(numeroDiVolte==0)` sia rispettata.
Nella chiamata iniziale (quella dal main) avremo `numeroDiVolte` uguale a `5`, di conseguenza andremo avanti, verrà stampata la stringa `Questa è la stringa numero [5]` e la funzione richiamerà sé stessa, passando come parametro `numeroDiVolte` decrementato di `1` (per i meno bravi in matematica: è come scrivere `stampaFinita_v1(4)`).
Andremo avanti così fino alla chiamata `stampaFinita_v1(0)`: a questo punto la condizione `if(numeroDiVolte==0)` sarà vera, entreremo nel corpo dell'`if` e verrà stampato `Questa sarà la prima stringa ad essere stampata`.
L'istruzione `return;` passerà di nuovo il controllo al main, facendo terminare la funzione.

---

È possibile fare una piccolissima modifica a questa funzione per ottenerne una molto diversa.
```c
void stampaFinita_v2(int numeroDiVolte){
	if(numeroDiVolte==0){
		printf("Quando verrà stampata questa scritta?\n");
	}
	else{
		stampaFinita_v2(numeroDiVolte-1);
		printf("Questa è la stringa numero [%d]\n", numeroDiVolte);
	}
}
```
Ho soltanto invertito l'ordine delle istruzioni nell' `else`, prova a indovinare l'output adesso, se nel main avessi una chiamata del tipo `stampaFinita_v2(5)`.

\
\
\
\

$$\textcolor{red}{\text{NON SCENDERE PRIMA DI AVER LETTO TUTTO QUEL CHE C'È PRIMA}}$$

---
---
---
---
---
---
---

L'output sarà:

	Quando verrà stampata questa scritta?
	Questa è la stringa numero [1]
	Questa è la stringa numero [2]
	Questa è la stringa numero [3]
	Questa è la stringa numero [4]
	Questa è la stringa numero [5]

>[!attention] Spiegazione
>La situazione è molto simile alla precedente, ma andiamo per passi:
>1. La funzione viene chiamata dal main ed ha numeroDiVolte=5
>2. La condizione `if(numeroDiVolte==0)` ritorna false, di conseguenza non si entra nel corpo dell'`if`.
>3. Viene effettuata la chiamata `stampaFinita_v2(numeroDiVolte-1)`
>4. La funzione viene eseguita, quindi la chiamata `stampaFinita_v2(5)` viene "lasciata in sospeso" (nell'esatto punto in cui si è fermata) e il controllo passa alla chiamata `stampaFinita_v2(4).
>5. Ripeti dal punto 2. fino alla chiamata `stampaFinita_v2(0)`
>6. A questo punto la condizione `if(numeroDiVolte==0)` sarà vera, verrà stampata la stringa `Quando verrà stampata questa scritta?`, dopodiché verrà effettuata una `return;`
>7. Questa return terminerà la chiamata e darà il controllo all'ultima chiamata di funzione effettuata prima di `stampaFinita_v2(0)`
>8. Cioè la chiamata `stampaFinita_v2(1)`, che ricomincerà **ESATTAMENTE** da dove si era fermata precedentemente, cioè subito prima dell'istruzione 
>   `printf("Questa è la stringa numero [%d]\n", numeroDiVolte);`, questa istruzione stamperà (ovviamente): `Questa è la stringa numero [1]`
>9. Non c'è nessun'altra istruzione da eseguire , la chiamata `stampaFinita_v2(1)` termina, continuando con `stampaFinita_v2(2)` e, iterando dal punto 8, fino a raggiungere la chiamata `stampaFinita_v2(5)`, che stamperà `Questa è la stringa numero [5]` e terminerà il programma.

Ora che abbiamo (spero) capito come funzionano le chiamate ricorsive, possiamo passare a qualcosa di leggermente più difficile.
## Liste concatenate
Darò per scontato che conosciate un minimo come funzioni questa struttura dati, i cui nodi saranno definiti come segue:
```c
typedef struct Nodo{
	int val;
	struct Nodo *next;
}Nodo;
```
Ora inizieremo a dividere i problemi in sottoproblemi più semplici, quindi diremo che, una lista può avere:
- Un nodo
- Nessun nodo `(NULL)`
A loro volta, i nodi possono avere il campo `next`:
- `==NULL` (uguale a `NULL`) (nessun elemento successivo)
- `!=NULL` (diverso da `NULL`) (almeno un elemento successivo)
Dopo aver definito "_rigorosamente_" questa struttura possiamo passare alla più semplice delle funzioni:
### Stampa di una lista
>[!done] 
>Dopo aver appurato che una lista può essere vuota (cioè non avere nessun nodo), abbiamo già trovato il caso base: **la lista vuota**.
>Il passo di ricorsione sarà stampare il campo `val` della `struct Nodo` e richiamare la funzione sul nodo successivo (`->next`)
```c
typedef struct Nodo{
	int val;
	struct Nodo *next;
}Nodo;

	void printList(Nodo node){
		if(node==NULL){ //cioè la lista è vuota
			printf("NULL\n");
			return;
		} else{ //cioè quando la lista contiene almeno un nodo
			printf("%d --> ", node->val);
			printList(node->next);
		}
	}
```
>[!attention] Nota bene
>Se si inverte l'ordine dei comandi `printf(...)` e `printList(node->next)` si ottiene la stampa al contrario della lista.

>[!hint] 
Prova adesso a fare la funzione che mi hai chiesto, tenendo a mente che se la lista è vuota non puoi fare operazioni sul nodo (perché `==NULL`), di conseguenza la chiamata alla funzione che rimuove i nodi con `val>M` dovrà necessariamente essere nel passo di ricorsione.


