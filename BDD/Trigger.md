---
author: Giulia Gargiulo
---

Un trigger è una procedura speciale che viene eseguita automaticamente quando si verifica un evento nel server di un database.

I trigger sono utilizzati nella progettazione di un database per:
1. mantenere **l'integrità referenziale** tra le varie tabelle;
2. mantenere **l'integrità dei dati** della singola tabella;
3. **monitorare** i campi di una tabella ed eventualmente generare eventi.
### Parametri di un trigger
1. Quale evento scatena la reazione?
	- `INSERT`
	- `UPDATE`
	- `DELETE`
2. Quando voglio scatenare la reazione?
	- `BEFORE`
	- `AFTER`
3. Quali sono le condizioni di filtraggio?
	- Se il trigger viene attivato sempre dall'evento o solo per particolari condizioni.
4. La reazione è globale o per ciascuna riga?
	- L'azione viene effettuata sulla singola riga o sull'insieme delle righe coinvolte.

---
### Sintassi

```SQL
CREATE TRIGGER <nomeTrigger>
[BEFORE/AFTER/INSTEAD OF] 
<operazione> -- si applica solo alle view
[FOR EACH ROW]
WHEN <condizione>
BEGIN
	<azione> -- per Oracle PL/SQL, mentre per Postgres ci sarà chiamata a funzione.
END


<operazione = {
INSERT ON <tabella> or
DELETE ON <tabella> or
UPDATE ON <tabella> [OF <attributo>[...]] -- posso specificare i singoli attributi
}
```

#### Old e New
Nel caso in cui si lavora su singole righe, cioè con la clausola `FOR EACH ROW`, il DBMS mette a disposizione due strutture:
- `OLD`: cosa c'era prima dell'operazione
- `NEW`: cosa c'e dopo l'operazione

`OLD e NEW` sono dei ***record***, al loro interno contengono gli attributi della riga con i corrispettivi nomi: `NEW.<nomeAttributo>`e `OLD.<nomeAttributo>`.

Per `DELETE`esiste solo `OLD`, per `INSERT`esiste solo `NEW`, mentre per `UPDATE` esistono entrambe e conservano i valori di tutti gli attributi, siano essi o meno oggetto della `UPDATE`.

---
#### Begin e End
Contengono tutte le azioni che vanno eseguite sulla basi di dati al verificarsi delle condizioni specificate.
- Tutto ciò che è tra `BEGIN`e `END`è una transazione.
- Nella `BEGIN/END`  posso mettere istruzioni base di SQL separate da ";".
---
#### Rimuovere e modificare un trigger
- Cancellazione : `DROP <nomeTrigger>`
- Disabilitazione : `ALTER <nomeTrigger> SET ENABLED/DISABLED`
- Modifica : `CREATE/REPLACE <nomeTrigger>`
---
### DML e Views
Le viste sono sono oggetti non persistenti, cioè sono ***tabelle virtuali***, non materializzate. Per le `SELECT` non ci sono problemi, mentre per le operazioni di DML bisogna capire come agire.

#### Regole per l'automatic update
1. La view contiene il campo chiave della tabella.
2. La view è basata su un'unica tabella.
3. La view contiene tutti gli attributi totali.

>[!example]
>Studenti(<u>Matricola</u>, CF, Nome, Cognome, dataN, Residenza)
>CF, Nome e Cognome sono attributi totali, mentre dataN e Residenza sono parziali.
>```SQL
>CREATE VIEW Studenti2(Matricola,CF, Nome,Cognome) AS(
>	SELECT Matricola, CF, Nome, Cognome
>	FROM Studenti
>)
>DELETE FROM Studenti2 WHERE Matricola = 'N86001000'
>```
>
>```SQL 
>-- su questa view non è possibile effettuare alcuna istruzione di delete/ insert / update
>CREATE VIEW Studenti3(Nome,Cognome) AS(
>	SELECT Nome, Cognome
>	FROM Studenti
>)
>```

---
#### Clausola INSTEAD OF
Un trigger `INSTEAD OF` è un trigger SQL che viene elaborato "invece" di un'istruzione SQL UPDATE, DELETE o INSERT. Diversamente dai trigger SQL `BEFORE e AFTER`,  un trigger `INSTEAD OF` può essere definito solo su una vista, non su una tabella.

Un trigger `INSTEAD OF`consente a una vista, che non è intrinsecamente inseribile, aggiornabile o eliminabile, di essere inserita, aggiornata o eliminata.

Dopo che un trigger SQL `INSTEAD OF` è stato aggiunto a una vista, la vista da cui in precedenza era possibile solo leggere può essere utilizzata come destinazione di un'operazione di inserimento, aggiornamento o eliminazione. Il trigger `INSTEAD OF` definisce le operazioni da eseguire per gestire la vista.

Una vista può essere utilizzata per controllare l'accesso alle tabelle. I trigger `INSTEAD OF` possono semplificare la gestione del controllo accessi alle tabelle.

```SQL
CREATE TRIGGER <nomeTrigger>
INSTEAD OF INSERT / UPDATE / DELETE ON Tabella 
FOR EACH ROW 
[WHEN <condizione>]
BEGIN
	<istruzioni di insert/delete/update sulle tabelle sottostanti>
END
```

>[!example]
>Studente(Matricola, Nome, Cognome)
>Anagrafe(Matricola, CF, Residenza, dataN)
>```SQL
>CREATE VIEW Completa AS
>SELECT *
>FROM Studente JOIN Anagrafe
>CREATE TRIGGER aggStud
>	INSTEAD OF INSERT ON Completa or
>		UPDATE ON Completa or
>		DELETE ON Completa
>	FOR EACH ROW
>	BEGIN
>		IF INSERTING
>			INSERT INTO Studente VALUES(NEW.Matricola, NEW.Nome, NEW.Cognome);
>			INSERT INTO Anagrafe VALUES (NEW.Matricola, NEW.CF,...)
>		END IF
>	END
>```

>[!tip]
>Le view possono essere usate anche come layer di astrazione, cioè per dare accesso a diverse parti delle tabelle ad utenti diversi.

#### Autoincrement ???


