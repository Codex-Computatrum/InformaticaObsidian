---
author: Giulia Gargiulo
---

SQL dinamico consente di eseguire istruzioni SQL create dinamicamente nel corpo procedurale di PL/SQL.

A differenza di ***SQL statico*** in cui il comando è scritto dal programmatore nella procedura e poi eseguito, in ***SQL dinamico*** il comando viene prodotto ed eseguito a **runtime**.
## Perchè usare SQL dinamico?

Consideriamo il caso in cui ho tanti operatori e tanti attributi su cui eseguire `SELECT`, dovrei eseguire tante `SELECT`differenti.
Con SQL dinamico creo delle stringhe che poi costruisco a runtime ed eseguo.

---
## Comandi come stringhe

In SQL dinamico ogni ***comando*** è una ***stringa*** di testo, quindi i comandi SQL diventano dati di tipo stringa e qualsiasi istruzione è contenuta in una variabile `VARCHAR`.

>[!example]
>```SQL
>CREATE PROCEDURE seleziona(nomeTabella IN VARCHAR)
>	comando VARCHAR(1000)
>	comando = 'SELECT * FROM' || nomeTabella
>```
- Devo dire al compilatore che quello è un comando e non una stringa.

>[!example]
>```SQL
>CREATE PROCEDURE CANCELLA_TABELLA(table_name IN VARCHAR) 
>AS
>	sql_istr VARCHAR(100);
>BEGIN sql_istr:='DROP TABLE' || table_name;
>		EXECUTE IMMEDIATE(sql_istr);
>	EXCEPTION
>		-- gestione eccezioni;
>END;
>/
>```

---
## Modalità di interazione

La gestione dell’interrogazione avviene in due fasi:
1. `PREPARE`: prevede il controllo sintattico del comando e la creazione del piano di esecuzione;
2. `EXECUTE`: esegue il comando.

Quindi la parte di controllo è separata dalla parte di esecuzione; ha senso quando devo eseguire molte volte lo stesso comando.

L'interrogazione può essere:
1. Eseguita immediatamente;
2. Inserita in un parametro di tipo stringa che contiene il comando;
3. Inserita in un comando specificato direttamente come parametro `EXECUTE IMMEDIATE`.
### Prepare
`PREPARE` analizza l'istruzione SQL e ne prepara una traduzione.

```SQL
PREPARE <nome_comando> FROM <comando_SQL>
```
- `<nome_comando>`è il nome associato da `PREPARE` alla traduzione del comando SQL.
- Il comando SQL può contenere parametri in ingresso rappresentati tramite `?`.

>[!example]
>L’esecuzione del comando `PREPARE` associa alla variabile comandoSQL la traduzione dell’interrogazione, con un parametro in ingresso rappresentante la matricola dello studente.
>```SQL
>PREPARE comandoSQL 
>FROM 'SELECT nome FROM studente WHERE matricola = ?'
>```

### Execute
`EXECUTE` esegue il **comando** precedentemente definito tramite la `PREPARE`.

```SQL
EXECUTE <nome_comando> [INTO variabili_target][USING <lista_parametri>]
```
- `<variabili_target>`contiene l'elenco dei parametri in cui verrà scritto il risultato del comando.
- `<lista_parametri>` specifica i valori da assegnare ai parametri variabili (indicati con `?`).

>[!example]
>Esegue comandoSQL sostituendo `?` con la variabile **matr_studente** e salva il risultato in **nomeStudente**.
> ```SQL
> EXECUTE comandoSQL INTO nomeStudente USING matr_studente
> ```
> Consideriamo il caso in cui **matr_studente** è una variabile in cui è inserita la matricola "N86001234"; l'esecuzione del comando equivale alla seguente query:
> ```SQL
> SELECT nome
> FROM studente
> WHERE matricola = 'N86001234'
> ```

### Execute immediate
`EXECUTE IMMEDIATE` esegue immediatamente il comando; se sono presenti errori vengono riscontrano soltanto nel momento in cui eseguo il comando.

```SQL
EXECUTE IMMEDIATE <nome_comando>[INTO <listatarget][USING <listaPar>
```

>[!example]
>In questo caso la `PREPARE` non è eseguita esplicitamente.
>```SQL
>comandoSQL:= "DELETE FROM Studente WHERE Matricola = 'N86001941'"
>EXECUTE IMMADIATE comandoSQL;
>```

---
### Funzioni per la manipolazione di stringhe

![[Screenshot 2023-12-15 alle 12.35.41.jpg]]
![[Screenshot 2023-12-15 alle 12.35.51.jpg]]

---
### Funzioni

>[!important]
>Una funzione, a differenza di una procedura, restituisce un valore.
>```SQL
>CREATE [OR REPLACE] FUNCTION function_name
>	[parameter_name (IN | OUT | IN OUT) type[...]]
>RETURN type
>{IS | AS}
>BEGIN
> 	-- function body
> END function_name;
>```

>[!example]
>Esempio funzione PostgresSQL:
>```SQL
>CREATE FUNCTION circle_area(p_radius IN DOUBLE PRECISION) 
>RETURNS DOUBLE PRECISION AS
>$$
>	DECLARE
>		v_pi DOUBLE PRECISION:=3.1415926;
>		v_area DOUBLE PRECISION;
>	BEGIN
>		v_area:=v_pi*POWER(p_radius, 2);
>	RETURN v_area;
>	END
>$$ 
>LANGUAGE plpgsql;
>```

---
### Cursore per SQL 

Mentre in SQL statico la dichiarazione del cursore è agganciata ad una `SELECT`, in SQL dinamico un cursore può anche non essere legato ad una query in particolare, inoltre può essere aperto da qualsiasi query e può essere restituito come output di una **funzione** (tipo cursor).

In SQL dinamico bisogna quindi agganciare il cursore ad una `SELECT` definita in modo dinamico, si lavora usando un ***puntatore*** ad un cursore a cui poi si aggancia dinamicamente la `SELECT`.

#### Cursori Weakly e Strongly Typed

```SQL
-- WEAKLY TYPED
<nomeCursore> SYS_REFCURSOR   -- TIPO PUNTATORE A CURSORE

-- STRONGLY TYPED
<nomeCursore> SYS_REFCURSOR RETURN <tipo> -- <nomeTabella>%ROWTYPE
```

Per associare la dichiarazione di un cursore al comando devo fare una `OPEN` esplicita del cursore:

`OPEN <nomeCursore> FOR <comando>`

```SQL
comandoSQL:= 'SELECT * FROM studente WHERE' || nomeAttributo || '=' || nome valore;
OPEN nomeCursore FOR comandoSQL;
```

##### Come si procede?
1. Definizione della stringa di comando;
2. Definizione del cursore;
3. Costruzione dinamica della stringa di comando;
4. Open del cursore per il comando definito.

>[!Example]
>```SQL
>CREATE OR REPLACE FUNCTION names_for(name_type_in IN VARCHAR2)
>RETURN SYS_REFCURSOR
>IS
>	l_return SYS_REFCURSOR; --weakly typed
>	BEGIN
>		IF name_type_in = 'EMP'
>		THEN
>			OPEN l_return FOR (SELECT last_name FROM employees 
>				ORDER BY employee_id)
>		ELSE IF name_type_in = 'DEPT'
>		THEN
>			OPEN l_return FOR(SELECT departement_name 
>				FROM departements ORDER BY departement_id);
>		END CASE;
>		RETURN l_return;
>END names_for;
>```
>
>```SQL
>DECLARE 
>	l_names SYS_REFCURSOR;
>	l_name VARCHAR(32767);
>BEGIN
>	l_names := names_for('DEPT');
>	LOOP
>		FETCH l_names INTO l_name;
>		EXIT WHEN l_names%NOTFOUND;
>		DBMS_OUTPUT.put_line(l_name);
>	END LOOP;
>	CLOSE l_names;
>END;
>```

---
