---
author: Giulia Gargiulo
---

Per creare uno schema di DB si usa il comando:
`CREATE SCHEMA nomeSchema [AUTHORIZATION nomeUtente]`

Uno schema include ***tabelle***, ***domini***, ***viste*** e altri costrutti e può essere definito come un ***contenitore logico***.

---
#### Creazione delle tabelle

```SQL
CREATE TABLE <nomeSchema>.<nomeTabella>(
<nomeAttributo1> <tipo>,
<nomeAttributo2> <tipo>,
COSTRAINT <nomeVincolo> <vincolo>;
)
```

>[!example]
>Creazione tabella Studenti : S $\leftarrow$ Studenti(Nome, Cognome, Matricola(PK), codFisc, dataNascita)
>```SQL
>create table uni.Studenti(  
>	Nome varchar(20) NOT NULL,  
>	Cognome varchar(20),  
>	Matricola varchar(9),
>	codFisc char(16),
>	dataNascita date,
>	CONSTRAINT Matricola PRIMARY KEY(Matricola)  
);
>```

---
#### Tipi di dato
##### Dati numerici
- Interi (Integer, int, smallint)
- Reali (float, real, double precision)
- Numeri formattati (DECIMAL(i ,j),)......

##### Stringhe di caratteri
- A lunghezza fissa (`CHAR(n), CHARACTER(n)`)
- A lunghezza variabile (`VARCHAR(n), CHARVARYING(n))
- Per default il numero minimo di caratteri è 1.

#### Stringhe di bit
- A lunghezza fissa: `BIT(n)`
- ...

#### Boolean
Prevede True o False, ma ha una logica a tre valori, considerata l'esistenza del valore $NULL$.

#### Date
Ha come componenti Year, Month e Day; formato YYYY-MM-DD.

#### Time
Ha almeno 8 posizioni con componenti Hour, Minute, e Second; formato HH:MM:SS.


#### Domain
Tipo di dato che permette di creare ***domini*** personalizzati di valori:
`CREATE DOMAIN <nomeDominio> AS <tipoDatoBase>`
`CHECK <vincolo>

>[!Esempio]
>
>```SQL
>CREATE DOMAIN genere AS CHAR(1)
>CHECK genere = 'M' or genere = 'F'

---
#### Attributi e vincoli
`definizione_attributo = <nomeAttributo> <tipoDato>[<vincoli_su_attributo>]

***vincoli_su_attributo***:
-  `[NULLABLE / NOT NULL] vincolo di totalità
- `[DEFAULT <valore>]
- `[CHECK (espressione booleana)] vincoli di dominio
- `[PRIMARY KEY][UNIQUE] vincoli intra-relazionali.
#### Vincoli su tabella
```SQL
CREATE TABLE tabella
(
<nomeAttributo1> <tipo>,
<nomeAttributo2> <tipo>,
CONSTRAINT <nomeVincolo> <vincolo>
);
```

`<vincolo>:`
- `CHECK (<espressione booleana>)`
- `UNIQUE (<listaAttributi>)`
- `PRIMARY KEY (<listaAttributi>)`
- `FOREIGN KEY (<listaAttributiFK>) REFERENCES <nomeTabella> <listaAttributiPK>`
---
#### Vincolo di Foreign Key
`FOREIGN KEY(listaAttributiFK) REFERENCES <nomeTabella> <listaAttributiPK>
E' un vincolo inter-relazionale perché coinvolge due tabelle diverse e va verificato in fase di inserimento.

Dove:
- listaAttributiFK è la lista dei attributi che sono FK nella tabella che sto creando;
- listaAttributiPK è la lista di attributi che compongono la chiave primaria nella tabella referenziata.

>[!important]
>Gli attributi referenziati devono essere PK nella tabella <nomeTabella> a cui si fa riferimento ed inoltre devono essere in corrispondenza, cioè stesso numero di attributi, stesso tipo e stessa posizione; il nome non conta.

>[!Example]
>Schema: 
>Studente(<u>Matricola</u>, codFisc, Nome, Cognome, dataNascita)
> Corso(<u>Nome</u>, <u>Anno</u>, Descrizione)
> Esame(<u>NomeCorso(FK)</u>, <u> Anno(FK)</u>, <u>Matricola(FK)</u>, Data, Voto, Lode)
> ```SQL
> CREATE TABLE uni.Esame(
> 	NomeCorso char(4) NOT NULL
> 	Anno smallint NOT NULL
> 	MatricolaSt char(8) NOT NULL
> 	Data date NOT NULL
> 	Voto smallint NOT NULL CHECK(Voto >= 18 and Voto <= 30)
> 	Lode boolean
> )
> CONSTRAINT FK_Studente FOREIGN KEY(MatricolaSt) REFERENCES Studente(Matricola)
> CONSTRAINT FK_Corso FOREIGN KEY(NomeCorso, Anno) REFERENCES Corso(Nome,Anno)
> CONSTRAINT Voto_lode CHECK((Voto = 30 and Lode = TRUE) or (NOT Lode = TRUE))
> CONSTRAINT Unique_esame UNIQUE(MatricolaSt, NomeCorso, Anno)
> ```

#### Azioni sul vincolo di FK

Le azioni si specificano sulla FOREIGN KEY per definire cosa accade se la PK referenziata viene cancellata o modificata ed il vincolo di integrità rischia di essere compromesso. Esse sono parte della definizione di FK.

`ON DELETE <azione>`
`ON UPDATE <azione>`

`<azione> = NO ACTION / CASCADE / SET DEFAULT / SET NULL`
`CASCADE`: a cascata, cancella o modifica tutte le tuple collegate alla PK.

```SQL
FOREIGN KEY(listaAttributiFK) REFERENCES <nomeTabella> <listaAttributiPK>
[ON DELETE <azione>]
[ON UPDATE <azione>]
```
---
#### Alter Table
Serve a modificare una tabella già creata:
- aggiungendo o rimuovendo una `CONSTRAIN`;
- attivando o disattivando una `CONSTRAIN`;
- aggiungendo, rimuovendo o modificando un attributo.

```SQL
ALTER TABLE <nomeTabella> SET CONSTRAIN <nomeCostraint> DISABLED / ENABLED
ALTER TABLE <nomeTabella> DROP CONSTRAIN <nomeCostraint>
ALTER TABLE <nomeTabella> CREATE CONSTRAIN <nomeCostrain> <defVincolo>

ALTER TABLE <nomeTabella> ADD <nomeAttributo> <tipoAttributo>
ALTER TABLE <nomeTabella> DROP <nomeAttributo> CASCADE / RESTRICT
ALTER TABLE <nomeTabella> ALTER <nomeAttributo> DROP DEFAULT
```
---
#### Drop
Serve per eliminare una ***tabella*** o uno ***schema***

```SQL
DROP TABLE <nomeTabella> CASCADE / RESTRICT
DROP SCHEMA <nomeSchema> CASCADE / RESTRICT
```