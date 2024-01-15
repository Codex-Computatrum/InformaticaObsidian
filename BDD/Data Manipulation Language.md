---
author: Giulia Gargiulo
---

sono istruzioni che consentono di lavorare sui dati, cioè sul contenuto delle tabelle.

`INSERT`: per inserire dati nelle tabelle (popolamento delle tabelle).
`UPDATE`: per modificare il contenuto delle tabelle (singoli campi).
`DELETE`: per eliminare righe intere da una tabella.

#### Delete
```SQL
DELETE 
FROM <nomeTabella>
[WHERE <condizioneBooleana>]
```

>[!important]
> Se la WHERE non è specificata viene svuotata l'intera tabella, altrimenti vengono elminiate solo le righe in cui la condizione è verificata.

```SQL
--ESEMPI
DELETE FROM Esami -- la tabella viene svuotata

DELETE FROM Esami
WHERE matrStud = 'N86001234' -- vengono elminiate tutte le righe con una specifica matricola
```

---
#### Insert
La insert può avvenire in due modi diversi:
1. Inserimento esplicito di valori.
2. Inserimento di valori calcolati o estratti tramite subselect.

###### Inserimento esplicito di valori
```SQL
INSERT INTO <nomeTabella> [<elencoAttributi>]
	VALUES(listaValori),[(listaValori)]
```

>[!example]
>Inserimento dati nelle tabelle Studenti ed Esami:
>```SQL
>INSERT INTO uni.Studenti (Nome,Cognome,Matricola) VALUES
>	('Giulia', 'Gargiulo', 'N86001234'),  
>	('Lorenzo', 'Tecchia', 'N86005678'),  
>	('Fortunata','D urso','N86004000'),  
>	('Miriam', 'Gaetano','N86001111');
>
>INSERT INTO uni.Esami(matr_stud, voto, esame, Lode) VALUES
>	('N86004670',28,'BDD',FALSE),  
>	('N86004446',30,'ASD', TRUE),  
>	('N86001111',25,'EDIT',FALSE),  
>	('N86004000',28,'BDD',FALSE);

- Se ometto l'elenco degli attributi devo inserire i valori nell'ordine in cui gli attributi sono definiti nella tabella.

###### Inserimento di valori calcolati o estratti tramite subselect

```SQL
INSERT INTO <nomeTabella> [<elencoAttributi>]
	( SELECT <attributi>
		FROM
		...
	)
```
- Non si usa la clausola `VALUES`
- La lista negli attributi nella `SELECT`deve corrispondere alla lista degli attributi della `INSERT` o alla lista degli attributi di definizione della tabella.

>[!example]
>
>```SQL 
>-- inserimento dei corsi dell'anno 2022
>INSERT INTO uni.Corsi
( 
>	SELECT C.nomeCorso, 2023, C.Descrizione, C.idDoc
>	FROM Corsi AS C
>	WHERE C.Anno = 2022 
>```
>```SQL
>INSERT INTO Carriera
>(
>	SELECT S.Matricola, S.Nome, S.Cognome, 
>		 COUNT(idCorso),AVG(Voto), COUNT(Lode)
>	FROM Studente AS S LEFT JOIN Esame AS E
>	GROPU BY (E.matrStud, S.Nome, S.Cognome
>)
>```

---
#### Update

```SQL
UPDATE <nomeTabella>
	SET <nomeAttributo> = <espressione>
		[<nomeAttributo> = espressione>]
	[WHERE <condizioneBooleana>]
```

- Funziona su uno o più attributi di una tabella tramite la `SET`, non è detto che coinvolga l'intera tabella.
- Se è specificata la `WHERE`, lavora su sottoinsiemi di righe.
- Se non è specificata la `WHERE`, viene cambiato l'attributo(o gli attributi) specificati dalla `SET`su ***tutte*** le righe della tabella.
- `<espressione>`può essere una subselect.

>[!example]
> Corsi (<u>nomeCorso</u>, <u>anno</u>, descrizione, idDoc)
> ```SQL
> UPDATE Corsi
> 	SET idDoc = 1
> 
> UPDATE Corsi
> 	SET idDoc = 1
> 	WHERE nomeCorso = 'BDD' AND anno = 2022
> 	
> ```

>[!example]
> Carriera (<u>Matricola</u>, nome, cognome, nEsami, mVoti, nLodi)
> ```SQL
> UPDATE Carriera
> 	SET (nEsami, mVoti, nLodi) = (
> 		SELECT COUNT(IdCorso), AVG(Voto), COUNT(nLodi)
> 			FROM Esami AS E
> 			WHERE Matricola = E.matrStud
> 		    GROUP BY(E.matrStud)
> 	)
> ```

###### Sequenza operazioni:
1. Selezione della tabella su cui si lavora
2. Selezione delle righe corrispondenti alla condizione della `WHERE`
3. Applico le modifiche specificate nella `SET`alle righe selezionate.
---

