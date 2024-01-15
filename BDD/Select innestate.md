---
author: Giulia Gargiulo
---

```SQL
SELECT Matricola, Stud1.matrStud, Cognome, Nome
	FROM Studenti NATURAL JOIN
	(SELECT Matricola AS matrStud, Cognome, Nome
		FROM Studenti) AS Stud1	
	WHERE Matricola <> matrStud
```

##### In, Exists nella clausola WHERE
- `[NOT] IN`: verifica che un attributo sia o non sia contenuto nel risultato della sottoselect.
- `[NOT] EXISTS`: verifica se l'insieme che sto cercando tramite la sottoselect esiste o no.

In particolare:
- `NOT EXISTS`= l'insieme calcolato dalla sottoselect è vuoto.
- `EXISTS` = esiste almeno una riga nell'insieme calcolato dalla sottoselect.

>[!example]
> Trovare gli studenti che non hanno svolto esami. Metodo 1:
>```SQL
>SELECT Nome, Cognome
>	FROM Studenti AS S
>	WHERE S.Matricola NOT IN (
>		SELECT matrStud   -- chi ha fatto esami
>		FROM Esami
>	)
>```

***Tabelle:***

| Matricola | Nome | Cognome|          
| ---------- | --------- | --------- |   
| 100 | Thomas | Andersen |                
| 200 | Robin | Hobb |
| 300 | Emmett | Brown |
| 400 | Robin | Hobb |

| matrStud | Voto | Corso |
| ---------- | --------- | --------- |
|100|28|BDD|
|100|30|PR1|
|200|25|BDD|
|100|30|ALG|
|400|19|ALG|
|200|22|PR1|

***Risultato:***

| Nome | Cognome|          
| --------- | --------- |  
| Emmett | Brown |

>[!example]
>Trovare gli studenti che non hanno svolto esami. Metodo 2:
>```SQL
>SELECT *
>	FROM Studenti AS S
>	WHERE NOT EXISTS(
>		SELECT *  --righe di S che non hanno corrispondeza in E
>		FROM Esami AS E
>		WHERE E.matrStud = S. Matricola
>	)
>```

---
#### Forma generale di interrogazione

```SQL
SELECT A1,...,An
	FROM <tabella> / <view> / <join>
	WHERE A1,...,Ak [NOT] IN(
		SELECT B1,...,Bk
		FROM <tabella> / <view> / <join>
		....
	)
```

```SQL
SELECT *
	FROM <tabella> / <view> / <join>
	WHERE [NOT] EXISTS(
		SELECT *
		FROM <tabella>
		WHERE <condizioneBooleana>
	)
```

>[!important]
> Nella sottoselect bisogna selezionare lo stesso numero di attributi e devono avere lo stesso dominio!

---
#### Dipendenza

***Caso 1:***
```SQL
SELECT Nome, Cognome
	FROM Studenti AS S
	WHERE S.Matricola NOT IN (
		SELECT matrStud 
		FROM Esami
	)
```
- La select e la sottoselect sono ***scorrelate***

***Caso 2:***
```SQL
SELECT *
	FROM Studenti AS S
	WHERE NOT EXISTS(
		SELECT * 
		FROM Esami AS E
		WHERE E.matrStud = S. Matricola
	)
```
- Le due select sono ***correlate***, la sottoselect è eseguita tante volte quante matricole ho nella select esterna.

>[!example]
>Trovare tutti gli studenti che hanno fatto tutti gli esami sostenuti dallo studente con matricola = 100.
>```SQL
>SELECT Cognome, Nome
>	FROM Studenti AS S -- visibile nella subselect
>	WHERE NOT EXISTS(
>		SELECT E.corsi    -- gli esami di matricola 100
>			FROM ESAMI AS E
>			WHERE E.matrStud = 100
>	)AND E.corso NOT IN(     -- esami non sostenuti
>		SELECT E2.corso   -- esami di qualsiasi studente 
>			FROM Esami AS E2
>			WHERE E2.matrStud = S.Matricola -- correlate
>	)
>```
>

---
#### Select nella clausola WHERE
```SQL
SELECT <expr1>,...,<exprk>
	FROM <tabella> / <JOIN tabelle> / <view>
	WHERE <attributo> <op_relazionale> <espressione>	
```

```SQL
SELECT Matricola
	FROM Carriera
	WHERE MediaV = (
		SELECT MAX(mediaVoti)
		FROM Carriera
	)
```

#### Where con ANY, ALL
```SQL
SELECT <expr1>,...,<exprk>
	FROM <tabella> / <JOIN tabelle> / <view>
	WHERE <attributo> <op_relazionale> [ANY/ALL] <espressione>	
```
- La select innestata restituisce più valori:
 `ANY`: almeno un valore
 `ALL`: tutti i valori

>[!example]
> Selezionare gli studenti che non hanno fatto esami.
> ```SQL
> SELECT *
> 	FROM Studenti
> 		WHERE Matricola <> ALL(
> 			SELECT matrStud
> 				FROM Esami
> 		)
> ```

---
#### Select nella clausola HAVING

```SQL
SELECT <expr1>,...,<exprk>
	FROM <tabella> / <JOIN tabelle> / <view>
	WHERE <attributo> <op_relazionale> <espressione>
	GROUP BY <condizioneRaggruppamento>
	HAVING <operazioneConteggio> <opRelazionale> <interrScalare>
```
- Sottoselect al cui interno sono visibili le colonne contenute nella `GROUP BY`.
---
#### WHERE con HAVING

```SQL
SELECT AVG(voto) 
FROM Esami AS E
	GROUP BY matrStud
	HAVING AVG(voto) > (
		SELECT AVG(v)
			FROM Esami AS E2
			GROUP BY E2.matrStud
			WHERE matrStud = 100
		)
```

