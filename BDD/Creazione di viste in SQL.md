---
author: Giulia Gargiulo
---

```SQL
CREATE VIEW <nomeVista> <B1,...,Bk>
AS(
	SELECT <expr_1> AS A, ..., <expr_k> AS K
	FROM <tabella> / <JOIN tabelle> / <view>
	WHERE <condizioneBooleana>
	GROUP BY <criterioRaggruppamento>
	HAVING <condizioneGruppi>
	ORDER BY <Ordinamento>
)
```
- Questa tabella non è salvata, ma è calcolata ogni volta; però posso usarla come una tabella.

>[!example]-
>Trovare coppie (nome, cognome) di studenti omonimi:
>(matr1,matr2,nome,cognome).
>```SQL 
>CREATE VIEW Stud2 AS(
>	SELECT Matricola AS matrStud, Cognome, Nome
>	FROM Studenti
>)
>SELECT Matricola, matrStud, Nome, Cognome
>	FROM Studenti NATURAL JOIN Stud2
>	WHERE Matricola <> matrStud
>```

---
