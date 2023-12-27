---
author: Giulia Gargiulo
---
Per definire una ***procedura*** in PL/SQL si utilizza il comando `CREATE [OR REPLACE] PROCEDURE`

>[!important]
>Una procedura, a differenza di una funzione, non ritorna alcun valore.

---
## Sintassi

#### Oracle:
```SQL
CREATE [OR REPLACE] PROCEDURE procedure_name
	[(parameter_name [IN | OUT | IN OUT] type [, ...])]
{IS | AS}
	DECLARE
		-- dichiarazione variabili;
	BEGIN
		-- corpo procedura;
	END <procedure_name>;
```

#### PostgreSQL
```SQL
CREATE [OR REPLACE] PROCEDURE procedure_name
	[(parameter_name [IN | OUT | IN OUT] type [, ...])]
{IS | AS}
$$
	DECLARE
		-- dichiarazione variabili;
	BEGIN
		-- corpo procedura
	END;
$$
LANGUAGE plpgsql;
```

- `IN` implica che il parametro può essere utilizzato nella procedure ma non può essere modificato (passaggio per valore).
- `OUT` implica che a esso può essere assegnato un valore nella procedura ma non può essere utilizzato esternamente alla funzione (passaggio per riferimento).
- `IN OUT` implica che il parametro può essere utilizzato sia in lettura che in scrittura.