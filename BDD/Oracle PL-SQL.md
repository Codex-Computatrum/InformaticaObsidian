---
author: Giulia Gargiulo
---

Procedural Language for the Structured Query Language.

PL/SQL è un linguaggio procedurale di Oracle che permette di includere interrogazioni SQL;  è un linguaggio strutturato a blocchi in cui le unità base sono procedure, funzioni o blocchi anonimi. Esse possono contenere un numero indefinito di sotto-blocchi.

#### Perché PL/SQL?
- Permette di spostare parte del carico computazionale sul server DBMS;
- Ci permette di lavorare sui risultati di una query anche una riga alla volta e non necessita di convertire i tipi (`%TYPE, %ROWTYPE`).
- Si possono utilizzare cursori per lavorare sulle righe risultanti da un'operazione SQL.
---
# Struttura di un blocco
Un blocco PL/SQL è formato da 3 parti:
1. Una parte ***dichiarativa***, in cui vengono dichiarate variabili e oggetti; le dichiarazioni sono locali al blocco e non sono visibili al di fuori di esso. Le variabili possono essere di qualsiasi tipo di dato SQL o tipi aggiuntivi propri di PL/SQL.
2. Una parte ***eseguibile*** in cui tali variabili sono manipolate ed elaborate.
3. Una parte delle ***eccezioni*** in cui vengono gestite le eccezioni o gli errori sorti durante l'esecuzione.

```SQL
[ DECLARE
	-- dichiarazione di variabili e costanti]
BEGIN
	-- istruzioni SQL e codice PL/SQL(obbligatorio)
[ EXCEPTION
	-- eccezioni
]
END;
/   --esegui (riga di comando)
```

- `DECLARE` è opzionale e contiene le variabili che verranno utilizzate nel seguito del programma.
- `BEGIN`/`END` è il blocco che contiene tutte le istruzioni che saranno eseguite (istruzioni,cicli ecc.).
- `EXCEPTION` è opzionale e contiene le istruzioni per gestire le exception.
- Ogni blocco termina con uno slash (/) (Non in PostgreSQL).

>[!example]
>Oracle 'Hello World!':
>```SQL
>DECLARE -- blocco anonimo
>message VARCHAR(100):='Hello, World!'  -- assegnazione
>BEGIN
>DBMS_OUTPUT.put_line(message);   -- stampa a video
>
>EXCEPTION
>	WHEN OTHERS   -- eccezione generica
>	THEN        
>	DBMS_OUTPUT.put_line(SQLERRM);
>END;
>/
>```

>[!example]
>Oracle nested 'Hello World!'
>```SQL
>DECLARE 
>l_message VARCHAR2(100):='Hello'; 
>BEGIN
>	DECLARE
>	l_message2 VARCHAR2(100):= l_message || 'World!';
>	BEGIN 
>		DBMS_OUTPUT.put_line(message); 
>	END;
>
>EXCEPTION
>	WHEN OTHERS   -- eccezione generica
>	THEN        
>	DBMS_OUTPUT.put_line(SQLERRM);
>END;
>/
>```

>[!example]
>PostgreSQL:
> ```SQL
> CREATE SCHEMA IF NOT EXISTS schemaprova;
> CREATE PROCEDURE schemaprova.prova() AS
> $$
> DECLARE
> message VARCHAR(100) :='Hello, World!';
> BEGIN
> 	RAISE NOTICE '%', message;
> EXCEPTION
> WHEN OTHERS
> THEN 
> RAISE EXCEPTION PLPGSQL_ERROR; 
> END
> $$
> LANGUAGE plpgsql;
> 
CALL schemaprova.prova();
> ```

---
## Blocchi con SQL

```SQL
-- sto copiando la definizione del campo last_name della tabella employees

DECLARE
l_name employees.last_name%TYPE;
BEGIN
	SELECT last_name
	INTO l_name -- devo salvare il risultato della SELECT 
				-- dentro una variabile
	FROM employees
	WHERE employee_id = 138;  -- una sola riga
 
	DBMS_OUTPUT.put_line(l_name);
END;
```
---
## Dichiarazione di variabili

```SQL
DECLARE
part_number NUMBER(6);   -- SQL data type
part_name VARCHAR2(20);  -- SQL data type
in_stock BOOLEAN;        -- PL/SQL only data type
part_price NUMBER(6,2);  -- SQL data type
part_description VARCHAR2(50);  --SQL data type
```
- `BOOLEAN` è un data type esclusivo di PL/SQL e PostgreSQL (Oracle non lo supporta).
- `NUMBER`(6,2) indica un numero con 6 digit complessivi, di cui 2 ***dopo la virgola***.

### Naming delle variabili
Per le variabili possono essere usati nomi come:
- X
- t2
- phone#
- credit_limit
- lastName
- oracle$number
- SN##
- try_again_

Non sono ammessi:
- mine&yours
- debit-amount
- on/off
- user id
---
## Costrutti?


---
### Costrutti condizionali

```SQL
IF condizione1
THEN
	istruzione1;
ELSEIF condizione2
THEN
	istruzione2;
ELSE
	istruzione3;
END IF;
```

>[!example]
>Esempio 1:
>```SQL
>IF lSalary BETWEEN 10000 and 20000
>THEN
>	giveBonus(lEmployeeID, 1000);
>ELSE IF lSalary > 20000
>THEN
>	giveBonus(lEmployeeID, 500);
>ELSE
>	giveBonus(lEmployeeID, 0);
>END IF;
>```

>[!example]
>Esempio 2:
>```SQL
>IF lSalary <= 40000  -- se lSalary è NULL viene eseguito il caso ELSE
>THEN
>	giveBonus(lEmployeeID, 0);
>ELSE
>	giveBonus(lEmployeeID, 500);  -- questa istruzione
>END IF;
>```

---
### Costrutti iterativi
- `FOR LOOP` che  viene seguito per un numero fisso di volte
- `SIMPLE LOOP` che viene eseguito fino a quando il ciclo non viene stoppato esplicitamente.
- `WHILE LOOP` che viene eseguito finché non si verifica una determinata condizione.
#### For Loop
Viene eseguito per un numero fisso di volte, specificando il ***lower bound***  (valore di partenza della variabile) e l’***upper bound*** (valore finale della variabile) per la ***variabile di loop***.

La variabile è incrementata o decrementata automaticamente di 1 ogni volta che si fa un nuovo giro nel loop.

```SQL
FOR loopVariable IN [REVERSE] lowerBound..upperBound LOOP
	statements
END LOOP;
```
- `loopVariable` è la variabile che regola il loop.
- `REVERSE` indica se la variabile deve essere incrementata o decrementata ed è opzionale; in ogni caso, il lower bound deve essere specificato prima dell'upper bound.

#### Simple Loop

```SQL
LOOP
	statements
END LOOP;
```

Per terminare il ciclo si può usare:
- `EXIT` per terminare il loop immediatamente;
- `EXIT WHEN` per terminare il loop quando si verifica una determinata condizione

```SQL
vCounter = 0;
LOOP
	vCounter := vCounter + 1;
	EXIT WHEN vCounter = 5;
END LOOP;
```

##### Continue
```SQL
DO $$
    DECLARE
        i int:=0;
        BEGIN
        LOOP
		--qui, quindi i verrà incrementato ancora di 1 (i==4) e "3" non verrà mai stampato
            i:=i+1; 
            raise notice '%', i;
            IF i=2 THEN
                raise notice 'i è 2'; --2 viene stampato dalla funzione precedente
                i:=i+1;               --incremento di 1 i e quindi i==3
                raise notice 'ora è 3';
                CONTINUE;             --il controllo dopo continue arriva

            END IF;
            EXIT WHEN i=10;
        END LOOP;
    END;
$$
```

#### While Loop

```SQL
WHILE condition LOOP
	statements
END LOOP;
```
- Termina quando si verifica una determinata condizione; la condizione viene controllata all'inizio di ogni loop.
>[!example]
>Oracle:
>```SQL
>vCounter := 0
>WHILE vCounter > 6 LOOP
>	vCounter := vCounter + 1;
>END LOOP
>```
>---
>
>PostgreSQL:
> ```SQL
> DO
> $$
> 	DECLARE
> 		i int:=0;
> 	BEGIN
> 		WHILE i<10 LOOP
> 		i:=i+1;
> 		raise notice 'i: %', i;
> 		END LOOP;
> 	END;
> $$;
> ```

---

### Operazione di `SELECT`

Una `SELECT` può ritornare:

1. Una singola riga: posso andare a recuperare i valori restituiti dichiarando in `DECLARE` le variabili restituite associandole all’output della `SELECT` tramite la keyword `INTO`.
2. Un insieme di righe: non so quante righe saranno restituite, necessiterò quindi di un ***cursore*** per scorrere la tabella ottenuta.
3. Nessuna riga.
#### Come gestire i risultati della SELECT

Normalmente le istruzioni di `SELECT`vengono mostrate a video dopo essere state inserite dal prompt dei comandi.

Dopo una `SELECT`posso avere tre situazioni:
1.  La `SELECT` non restituisce nulla (insieme vuoto).
2. La `SELECT` restituisce una sola riga, devo leggere i risultati in variabili appositamente dichiarate tramite `INTO`.
3. La `SELECT` restituisce molte righe, devo usare i ***cursori***.

>[!danger]
> 1. Non si usa la `SELECT`pura senza `INTO` all'interno di corpi procedurali.
> 2. Se la `SELECT` restituisce più righe devo ***obbligatoriamente*** usare un ***cursore***.

##### Select Into

###### SQL:
```SQL
SELECT nome, cognome
	FROM Studente
	WHERE matricola = 'N86001234'
```

###### PL/SQL:
```SQL
DECLARE
	l_nome Studente.nome%TYPE
	l_cognome Studente.cognome%TYPE
BEGIN
SELECT nome, cognome
	FROM Studente
	INTO l_nome, l_cognome   -- la select restituisce una sola riga
	WHERE matricola = 'N86001234'
END	
```

##### Cursori
Quando una `SELECT`restituisce più di una riga il DBMS consente di scorrere una ad una le righe tramite i ***cursori***, allocando un buffer.

Il cursore è un oggetto dichiarato nella parte di `DECLARE` delle variabili, tramite `CURSOR`. Per gestire il cursore si usano:
- `OPEN` apre il cursore, alloca il buffer ed esegue la query collegata al cursore; posiziona il cursore PRIMA della prima riga.
- `FETCH` recupera una singola riga, ha bisogno di strutture di controllo
- `CLOSE`chiude e dealloca il buffer.

>[!example]
> Voglio trovare tutti gli studenti con cognome "Esposito"(Oracle).
> ```SQL
> DECLARE
> 	CURSOR recupera_esposito
> 	IS SELECT nome, cognome, matricola
> 		FROM Studente
> 		WHERE cognome = 'Esposito'
> 	nome_s studente.nome%TYPE
> 	cognome_s studente.cognome%TYPE
> 	matricola_s studente.matricola%TYPE
> BEGIN
> 	OPEN recupera_esposito
> 	LOOP
> 		FETCH recupera_esposito INTO 
> 			nome_s, cognome_s, matricola_s
> 	EXIT WHEN recupera_esposito.NOT_FOUND;
> 		-- fai qualcosa
> 	END LOOP;
> 	CLOSE recupera_esposito;
> END
> ```

###### Dichiarazioni, Open, Close
- La dichiarazione NON esegue la `SELECT`.
- La `OPEN <nomeCursore>` esegue l'interrogazione, aggiorna il buffer con il risultato e aggiorna la posizione del cursore a prima della prima riga.
- La `CLOSE` rilascia il buffer e mi permette di riutilizzare il cursore.

>[!example]-
> Oracle:
> ```SQL
> DECLARE
> 	CURSOR estrai_cognome IS
> 	SELECT S.Nome, S.Matricola
> 	FROM STUDENTI AS S
> 	WHERE S.Cognome='Barra';
> 	riga_corrente estrai_cognome%ROWTYPE
> BEGIN
> 	OPEN estrai_cognome
> 	FETCH estrai_cognome INTO riga_corrente
> 	CLOSE estrai_cognome
> END
> ```
> ---
> PostgreSQL:
> ```SQL
> DECLARE
> 	estrai_cognome CURSOR FOR
> 	SELECT S.Nome, S.Matricola
> 	FROM STUDENTI AS S
> 	WHERE S.Cognome='Barra'
> 	riga_corrente estrai_cognome%TYPE
> BEGIN
> 	OPEN estrai_cognome
> 	FETCH estrai_cognome INTO riga_corrente
> 	CLOSE estrai_cognome
> END
> ```
###### Fetch:
`FETCH` recupera le informazioni dalle righe;
`FETCH <nomeCursore> INTO variabile_1,...,variabile_N`:
- Ci deve essere corrispondenza di numero e di definizione tra i campi della `SELECT`e le variabili `INTO` in cui si legge.
- La `FETCH`deve essere inserita in un `LOOP`che consente di scorrere tutte le righe contenute nel buffer.
- `%NOTFOUND` = TRUE quando non ci sono più righe
- `%ROWCOUNT` restituisce il numero esatto di righe della `SELECT`.
Altrimenti posso utilizzare un `FOR` speciale:

```SQL
DECLARE 
	CURSOR <nomeCursore> IS -- ...
BEGIN
	FOR <rigaCorrente> IN <nomeCursore>
	LOOP
		-- accesso ai campi di <nomeRiga> tramite notazione puntata
	END LOOP;
END
```
- Non ci sono dichiarazioni di variabili di appoggio, non c'è open, close, fetch, close, ne controlli se ci sono righe.

Al posto di definire i singoli campi posso definire un record:
`<nome_variabili> <nome_cursore>%ROWTYPE`
Il record contiene tutti i campi che sono stati definiti nella `DECLARE`del cursore, e posso accedere ai singoli campi utilizzando la notazione puntata.


>[!example]
>```SQL
>rigacorrente recupera_esposito%ROWTYPE
> -- altro
> LOOP
> FETCH recupera_esposito INTO rigacorrente
> EXIT -- condizione
> --accedo ai campi usando:
> rigacorrente.nome
> rigacorrente.cognome
>```

###### Dichiarazioni nel FOR
```SQL
FOR <rigaCorrente> IN (SELECT... FROM WHERE)
-- in questo caso non ho la DECLARE del cursore, la dichiaro direttamente nel FOR

FOR <tuttiCinema> IN (SELECT nome_cinema FROM Cinema)
-- ha senso solo per SELECT molto piccole
```

---
## Procedura

>[!important]
>Una procedura non ritorna alcun valore.
>```SQL
>CREATE [OR REPLACE] PROCEDURE procedure_name
>	[(parameter_name [IN | OUT | IN OUT] type [, ...])]
>{IS | AS}
>BEGIN
>-- procedure_body;
>END <procedure_name>;
>```

- `IN` implica che il parametro può essere utilizzato nella procedure ma non può essere modificato (passaggio per valore).
- `OUT` implica che a esso può essere assegnato un valore nella procedura ma non può essere utilizzato esternamente alla funzione (passaggio per riferimento).
- `IN OUT` implica che il parametro può essere utilizzato sia in lettura che in scrittura.
---
## Eccezioni

Le eccezioni sono utilizzate per gestire **errori a tempo di esecuzione** in statement PL/SQL.

```SQL
DECLARE 
-- declarations
BEGIN
-- statements

EXCEPTION
	WHEN ex_name1 THEN statements1 -- exception handler
	WHEN ex_name2 OR ex_name3 THEN statements_2  -- exception handler
	WHEN OTHERS THEN statements_3  -- exception handler
END;
```

- Il blocco `EXCEPTION` recupera le exceptions e le gestisce come (e se) specificato.
- La keyword `OTHERS` si utilizza per gestire tutte le exceptions non precedentemente gestite.

Gli errori vengono intercettati quando sono nella ***parte eseguibile*** del blocco; una volta individuato, il comando viene passato alla ***parte delle eccezioni*** per: operazioni di log, rerasing di altre eccezioni, rollback. Se un'eccezione non viene catturata e c'è `WHEN OTHERS` allora è il gestore che si occupa di capire quale eccezione è scattata (comporta un overhead). 

![[Immagine 14-12-23 - 23.35.jpg]]
### Eccezioni predefinite

1. `CURSOR_ALREADY_OPEN`: il programma sta cercando di aprire un cursore già aperto; un cursore deve essere chiuso prima di poter essere riaperto. Un cursore con un `FOR LOOP` apre automaticamente il cursore, quindi il programma non può aprire quel cursore all'interno del loop.

2. `DUP_VAL_ON_INDEX` : Your program attempts to store duplicate values in a database column that is constrained by a unique index.

3. `INVALID_CURSOR`: Your program attempts an illegal cursor operation such as closing an unopened cursor.

4. `INVALID_NUMBER`: In a SQL statement, the conversion of a character string into a number fails because the string does not represent a valid number.

5. `NO_DATA_FOUND` : A `SELECT INTO` statement returns no rows, or your program references a deleted element in a nested table or an uninitialized element in an index-by table. SQL aggregate functions such as AVG and SUM always return a value or a null. So, a `SELECT INTO`statement that calls an aggregate function never raises `NO_DATA_FOUND`. The `FETCH` statement is expected to return no rows eventually, so when that happens, no exception is raised. A `SELECT INTO`statement returns more than one row.

6. `VALUE_ERROR`: An arithmetic, conversion, truncation, or size-constraint error occurs. For example, when your program selects a column value into a character variable, if the value is longer than the declared length of the variable, PL/SQL aborts the assignment and raises VALUE ERROR. In procedural statements, VALUE_ERROR is raised if the conversion of a character string into a number fails. (In SQL statements, INVALID_NUMBER is raised.)

7.  `ZERO_DIVIDE`: Your program attempts to divide a number by zero.

### Eccezioni definite dall'utente

>[!example]
>Creo una **exception** che controlla al momento dell'inserimento dei dati se gli impiegati sono maggiorenni:
>```SQL
>CREATE OR REPLACE PROCEDURE validate_employee
>	(birthdate_in IN DATE) IS
>BEGIN
>	IF birthdate_in > ADD_MONTHS(SYSDATE, -12 * 18)
>	THEN
>		RAISE APPLICATION_ERROR(-20500, 'Employee must be at least 18 years old.');
>	END IF;
>END validate_employee;
>```

>[!example]
>```SQL
>CREATE OR REPLACE PROCEDURE process_balance (balance_in IN NUMBER)
>IS
>e_balance_too_low EXCEPTION;   -- variabile di tipo exception
>PRAGMA EXCEPTION_INIT (e_balance_too_low, -20000) 
>	-- istruzione al precompilatore
>BEGIN
>	IF balance_in < 1000
>	THEN
>		RAISE e_balance_too_low;
>	END IF
>EXCEPTION
>	WHEN e_balance_too_low THEN
>		-- gestisco l'errore
>END;
>``` 

- `RAISE` genera un'eccezione definita precedentemente.
---
