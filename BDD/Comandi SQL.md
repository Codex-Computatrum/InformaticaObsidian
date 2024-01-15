---
author: Giulia Gargiulo
tags:
  - SQL
  - definizione
  - comandi
---
#### Proiezione in SQL
```SQL
SELECT Nome,Cognome
	FROM Studente
```
- Stesso numero di righe, cambia il numero di attributi.
---
#### Selezione in SQL
```SQL
SELECT*
	FROM Studente
	WHERE (Voto > 27 and Cognome ='Rossi')
```
- Se la condizione è TRUE la riga viene selezionata;
- Cambia il numero di righe, stesso numero di attributi.

Condizioni di selezione:
- `<attributo> <op_confronto> <valore>`
- `<attributo> <op_relazione> <attributo>`
- `<attributo> IS [NOT] NULL`

`<op_confronto> = <, <=, >, >=, < >`
`<op_relazione> = and, not, or`

---
#### Proiezione e Selezione
```SQL
SELECT [DISTINCT] <listaAttributi>
	FROM <nomeTabella> [AS alias]
	WHERE <espressioneBooleana>
```
$1)$ Viene eseguita prima l'operazione di ***selezione*** delle righe, tramite la ***WHERE***.
$2)$ Dopo viene eseguita l'operazione di ***proiezione***, cioè la selezione delle colonne, tramite la ***SELECT***.

>[!Note]
>Per eliminare i duplicati in SQL devo specificare DISTINCT.

---
#### Unione, intersezione e differenza
Gli operatori binari `UNION, EXCEPT, INTERSECT` lavorano sul risultato di due `SELECT`.

```SQL
SELECT <elenco_attributi>
	FROM tabella1
	WHERE condizione
	
		UNION[DISTINCT]
		--EXCEPT
		--INSERSECT
(
SELECT <elenco_attributi>
	FROM tabella2
	WHERE condizione
)
```

- La select definisce una relazione (tabella) senza nome, contenente un insieme di righe.
- Gli attributi devono essere compatibili.
---
#### Prodotto Cartesiano
Sia  $r$ una tabella su schema $R(A_1,\dots ,A_n)$ e $s$ una tabella su schema $S(B_1,\dots ,B_m)$
Allora il ***prodotto cartesiano*** $r\times s$ è l'insieme di tutte le possibili combinazioni delle righe di $r$ e $s$.
Lo schema risultante è $?(A_1,\dots A_n,B_1,\dots, B_m)$ e contiene tutti gli attributi delle due relazioni.

```SQL
SELECT *
	FROM A,B   -- La , indica il prodotto cartesiano
```
---
### Join
 La relazione che si crea tramite il prodotto cartesiano contiene anche righe che sono semanticamente incorrette, quindi bisogna selezionare solo le righe giuste, attraverso l'uso di una `WHERE`, ad esempio:

```SQL
SELECT *
	FROM Studenti AS S, Esami AS E
	WHERE S.matricola = E.matr_stud
```

`JOIN`: unione di due tabelle in base ad una condizione, detta condizione di join.
Condizione di join $\theta$: 

```SQL
SELECT *
	FROM tabella1 [AS alias]
	JOIN tabella2 [AS alias] ON <condizione_di_join>
```

```SQL
SELECT *
	FROM Studenti AS S
	JOIN Esami AS E ON S.Matricola = E.matr_stud
```
- Le colonne che fanno parte della condizione di join sono presenti entrambe nel risultato, quindi avremo una colonna duplicata.

>[!example]
>Trovare nome e cognome degli studenti che hanno fatto esami.
>S $\leftarrow$Studenti(Matricola, Nome, Cognome)
>E $\leftarrow$Esami(matrStud, Voto, Esame)
>```SQL
>SELECT  Nome, Cognome 
>	FROM Studenti AS S
>EXCEPT
>SELECT Nome, Cognome
>	FROM Studenti JOIN Esami AS E
>		ON S.Matricola = E.matrStud
>```

---
#### Natural Join
Nella `NATURAL JOIN` vengono definiti in modo implicito gli attributi di giunzione, cioè quelli con lo stesso nome; se non ci sono attributi con lo stesso nome si comporta come un prodotto cartesiano.

```SQL
SELECT Matricola
	FROM Studenti JOIN Esami
```
- Se uno studente non ha esami, non sarà nella tabella risultante, mentre il viceversa è sempre garantito dal vincolo di FK.

---
#### External / Outer Join

`LEFT JOIN`: contiene anche le righe di $S$ che hanno attributi i cui valori non soddisfano la condizione di join $\theta$; gli attributi che non hanno corrispondenza sono messi a $NULL$.

`RIGHT JOIN`: contiene anche le righe di $E$ che hanno attributi i cui valori non soddisfano la condizione di join $\theta$; gli attributi che non hanno corrispondenza sono messi a $NULL$.

`EXTERNAL o OUTER JOIN`: è una `LEFT`+ `RIGHT JOIN` in cui si conservano le righe di entrambe le relazioni.

>[!example]
>Trovare nome e cognome degli studenti che NON hanno fatto esami.
>S $\leftarrow$Studenti(Matricola, Nome, Cognome)
>E $\leftarrow$Esami(matrStud, Voto, Esame)
>```SQL
>SELECT  Nome, Cognome 
>	FROM Studenti AS S LEFT JOIN  Esami AS E
>		ON S.Matricola = E.matrStud
>	WHERE E.matrStud IS NULL
>```

---
#### Self-Join
Serve per lavorare su coppie di righe della stessa tabella e necessita di un'operazione di renaming su una delle due tabelle; può essere ottenuta con prodotto cartesiano o join.

>[!example]
>Data la relazione I, trovare il cognome degli impiegati che lavorano allo stesso progetto a cui lavora Rossi.
>I $\leftarrow$Impiegati(Id, Impiegato, Progetto)
>```SQL
>SELECT Imp2.Impiegato
> 	FROM uni.Impiegati AS Imp JOIN uni.Impiegati AS Imp2 
> 		ON Imp.Progetto = Imp2.Progetto  
> 	WHERE Imp.Impiegato = 'Rossi' and Imp2.Impiegato <> 'Rossi'
>```

| Id | Impiegato | Progetto|
| ---------- | --------- | --------- |
| 1 | Rossi | A |
| 2 | Neri | A |
| 3 | Neri | B |
| 4 | Bianchi | B |

---
### Ordine delle istruzioni in SQL

In SQL l'ordine delle operazioni è prestabilito:

```SQL
SELECT S.Nome, S.Cognome, S.Matricola, -- 3. Proiezione
	E.matrStud, E.Corso AS NomeEsame -- 4. Renaming
	
	FROM Studente AS S JOIN Esami AS E
	ON S.Matricola = E.matrStud -- 1. Join

	WHERE Voto > 25 -- 2. Selezione
	
```
- La stessa cosa non vale in ***algebra relazionale***.
---
### In, Between e Like in SQL

```SQL
SELECT <expr1>,...,<exprk>
	FROM <tabella> / <JOIN tabelle> / <view>
	WHERE <condizioneBooleana>
```

`<condizioneBooleana> = <attributo> <operatore> <valore>`

- `IN: <nomeAttributo> IN (valore1, valore2,...)`è una forma abbreviata di `OR`.
- `BETWEEN: <nomeAttributo> BETWEEN valore1 AND valore2` Esempio:  `voto BETWEEN 27 and 30`
- `LIKE: <attributo> LIKE <pattern>`, in cui `<attributo`deve essere una stringa (char, varchar); serve a fare il matching su stringhe.

	%: match di un numero indefinito di caratteri variabili
	$\_$ : match di un singolo carattere variabile

	>[!example]
	>```SQL
	> WHERE nome LIKE 'Mario'  -- Solo le stringhe che contengono Mario come nome
	> WHERE nome LIKE 'Mari_'  -- Trova solo Mario, Maria, Marie... varia solo un carattere, ma deve esserci!
	> WHERE nome LIKE '_ _ _ '  -- Trova nomi con 3 caratteri
	> WHERE nome LIKE 'Mari%'  --Trova tutti i nomi che iniziano con "Mari"
	> WHERE nome LIKE '%Mari%'  -- Trova tutto ciò che contiene "Mari"
	>```
	
---



