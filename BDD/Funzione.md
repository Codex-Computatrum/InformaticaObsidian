---
author: Giulia Gargiulo
---
Per definire una nuova funzione in PL/SQL si utilizza il comando `CREATE [OR REPLACE]FUNCTION`

>[!important]
>Una funzione, a differenza di una procedura, restituisce un valore.
>

---
## Sintassi:

#### Oracle
```SQL
CREATE [OR REPLACE] FUNCTION function_name
	[(parameter_name (IN | OUT | IN OUT) type[...])]
RETURN <type> {IS | AS}
	DECLARE
		-- dichiarazione variabili;
	BEGIN
	 	-- corpo della funzione
	RETURN <valore_ritorno>;
	END function_name;
/
```

#### PostgreSQL
```SQL
CREATE [OR REPLACE] FUNCTION function_name
	([parameter_name (IN | OUT | IN OUT) type[...]])
RETURN <type> {IS | AS}
$$
	DECLARE
		-- dichiarazione variabili;
	BEGIN
	 	-- corpo della funzione
	RETURN <valore_ritorno>
	END;
$$
LANGUAGE plpgsql;
```


>[!example]
>Esempio funzione che calcola l'area di un cerchio in PostgresSQL:
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
>	END;
>$$ 
>LANGUAGE plpgsql;
>```

---
## Chiamata a funzione

Una funzione può essere richiamata da un ***blocco anonimo*** o all'interno di una `SELECT`dalla clausola `FROM`.

DA FARE