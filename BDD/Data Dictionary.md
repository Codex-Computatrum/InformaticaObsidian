---
author: Giulia Gargiulo
---

Un ***data dictionary*** contiene la definizione di tutti gli oggetti che sono contenuti in un database, inclusi i valori di default, i vincoli di integrità, i trigger...

Inoltre contiene le informazioni sullo spazio usato/ allocato per ogni schema di DB, il nome degli utenti, i ruoli e i privilegi assegnati.

Tutte queste informazioni sono contenute in tabelle su cui non è possibile fare alcun tipo di modifica; in realtà solo il DBMS lavora su queste tabelle, gli utenti lavorano su delle **view** costruite a partire da queste tabelle.

- Per avere informazioni su nomi e caratteristiche di tabelle:`ALL_ALL_TABLES`
- Per avere informazioni su nomi di colonne e le loro caratteristiche: `ALL_TAB_COLUMNS`.

>[!example]
>Si scrivano le funzioni che controllano l'esistenza di nomi di tabelle e di colonne.
>```SQL
>CREATE OR REPLACE FUNCTION check_table_name(
>	nome_tabella ALL_ALL_TABLES.table_name%TYPE)
>RETURN INTEGER
>	DECLARE
>		res integer := 0
>	BEGIN
>		SELECT COUNT(*)
>		INTO res
>		FROM ALL_ALL_TABLES T
>		WHERE table_name = UPPER(nome_tabella)
>	RETURN res
>	END check_table_name;
>```
>
>```SQL
>CREATE OR REPLACE FUNCTION check_column_name(
>	nome_tabella ALL_TAB_COLUMNS.table_name%TYPE,
>	nome_colonna ALL_TAB_COLUMNS.column_name%TYPE)
>RETURN INTEGER
>	DECLARE
>		res integer :=0
>	BEGIN
>		SELECT COUNT(*)
>		INTO res
>		FROM ALL_TAB_COLUMNS T
>		WHERE table_name = UPPER(nome_tabella)
>		AND column_name = UPPER(nome_colonna)
>	RETURN res
>	END  check_column_name;
>```
