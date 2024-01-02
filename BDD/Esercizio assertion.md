---
author: Giulia Gargiulo
---

![[Immagine 07-12-23 - 11.23.jpg]]
Schema logico:
- ***Documento*** (<u>DOI</u>, Titolo, Anno)
- ***Libro***(<u>ISBN</u>, casaEd, doiDocumento)
- ***Articolo***(<u>idArticolo</u>, tipoArticolo, ISSNRivista, nomeConf, doiDocumento,...)

1. Un documento deve essere o un articolo o un libro (vincolo di totalità).

```SQL
CREATE ASSERTION A1 CHECK(
NOT EXISTS(
	SELECT 1   -- non mi interessa il contenuto
	FROM Documento AS D
	WHERE (NOT EXISTS(
		SELECT 1 -- documenti che non sono libri
		FROM Libro AS L
		WHERE D.DOI = L.doiDocumento))
	AND(NOT EXISTS(
		SELECT 1 -- documenti che non sono articoli
		FROM Articolo AS A
		WHERE D.DOI = A.doiDocumento))
	)
)
```

2.  Un documento non può essere sia un articolo che un libro (vincolo di disguinzione inter-relazionale).

```SQL
CREATE ASSERTION A2 CHECK(
NOT EXISTS(
	SELECT 1
	FROM Documento AS D
	WHERE (EXISTS
		SELECT 1 -- documento è un libro
		FROM Libro AS L
		WHERE D.DOI = L.doiDocumento))
	AND(EXISTS (
		SELECT 1 -- documento è un articolo
		FROM Articolo AS A
		WHERE D.DOI = A.doiDocumento))
	)
)
```

3. Se tipoArticolo è articoloConferenza allora il collegamento con Rivista deve essere NULL (vincolo di n-upla).

```SQL
ALTER TABLE Articolo ADD CONSTRAINT A3
CHECK((tipoArticolo = articoloConferenza AND ISSNRivista = NULL) OR 
	  ( tipoArticolo = articoloRivista AND ISSNRivista <> NULL))
```

4. Se tipoArticolo è articoloRivista allora il nomeConf (e gli altri attributi di conferenza) devono essere NULL (vincolo di n-upla).
```SQL
ALTER TABLE Articolo ADD CONSTRAINT A4
CHECK((tipoArticolo = articoloRivista AND nomeConf = NULL) OR 
	  ( tipoArticolo = articoloConferenza AND nomeConf <> NULL))
```

---
Se lo schema logico è definito in questo modo invece, i vincoli sono espressi come segue:
 - ***Documento*** (<u>DOI</u>, Titolo, Anno, ISBNLibro, idArticolo)
- ***Libro***(<u>ISBN</u>, casaEd)
- ***Articolo***(<u>idArticolo</u>, ISSNRivista, nomeConf,...)

1. Un documento deve essere o un articolo o un libro.
2. Un documento non può essere sia un articolo che un libro.

```SQL
ALTER TABLE Documento
ADD CONSTRAINT A1 CHECK
((ISBNLibro = NULL AND idArticolo <> NULL) OR 
(ISBNLibro <> NULL AND idArticolo = NULL))
```

Molto più semplice da verificare, ma ho sempre dei valori a NULL nelle colonne.