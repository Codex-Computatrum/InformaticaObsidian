---
author: Giulia Gargiulo
---

## Select con una sola riga risultante

```SQL
CREATE PROCEDURE info_by_id(id_film_in IN film.id_film%TYPE)

DECLARE
	titolo_film film.titolo%TYPE
	regista_film film.regista%TYPE
BEGIN
	SELECT titolo, regista
	INTO titolo_film, regista_film
	FROM film
	WHERE id_film = id_film_in
		-- vengono usati i dati
END
```

---
## Select con più di una riga

```SQL
CREATE PROCEDURE info_film(cinema IN cinema.nome_cinema%TYPE, film film.nome_film%TYPE)

DECLARE
	CURSOR proiezioni IS
	SELECT P.data, P.ora, P.sala
	FROM Cinema C NATURAL JOIN Sala S NATURAL 
		JOIN Proiezione P NATURAL JOIN Film F
	WHERE C.nome_cinema = cinema 
		AND F.nome_film = film
BEGIN
	FOR rigacorrente IN proiezioni 
	LOOP
		-- uso i dati
		l_message = 'Data' || rigacorrente.Data || -- ecc...
		DBMS_OUTPUT.putline(l_message)
	END LOOP;
END
```

---
