---
author: Giulia Gargiulo
tags:
  - SQL
  - definizione
  - comandi
  - vincoli
---
Le assertion servono per creare [[vincoli]] ***intra-relazionali*** e ***inter-relazionali***, assicurano che la base di dati sia sempre in uno stato coerente.

```SQL
CREATE ASSERTION <nomeVincolo>
CHECK <espressioneBooleana>
```
- Il vincolo ha un nome che è utile per attivare o disattivare il vincolo.
- Il vincolo è ***violato*** se la condizione booleana della assert è falsa.

#### Assertion e NOT EXISTS
Nella maggior parte dei casi su una la forma `NOT EXISTS`per controllare che una condizione non si presenti mai, si cerca quindi la violazione del vincolo.
Lavoriamo quindi in ***logica negata***: controllo che non si verifichi mai la ***condizione negativa***.
`<espressioneBooleana> = NOT EXISTS(SELECT...FROM...)`

```SQL
CREATE ASSERTION A1
CHECK NOT EXISTS(
	SELECT <attributi>
		FROM
		....
)
```

Per avere `TRUE` come risultato, e per avere quindi il vincolo rispettato, il risultato della `SELECT` all'interno del `NOT EXISTS`deve essere sempre ***vuoto***.

>[!example]
> Il presidente deve essere unico, vincolo intra-relazionale.
> ```SQL
> CREATE ASSERTION soloUnPresidente
> CHECK 
> (
> 	(SELECT COUNT(*)
> 		FROM Impiegati AS I
> 		WHERE I.Ruolo = 'Presidente') <= 1
> )
> ```

>[!example]
>```SQL
>CREATE ASSERTION noStagistiSedeBoston
>CHECK(
>	NOT EXISTS(
>		SELECT 'stagistaABoston'
>		FROM Impiegato AS I, Dipartimento AS D
>		WHERE I.numeroDipartimento = d.idDipartimento
>		AND I.tipoContratto = 'Stagista' AND D.sede = 'Boston'
>	)
>)
>```

---
