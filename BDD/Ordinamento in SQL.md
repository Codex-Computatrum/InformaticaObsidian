---
author: Giulia Gargiulo
---

L'ordinamento è proprio di SQL, non esiste in algebra relazionale; si esprime tramite la clausola `ORDER BY <attributo> / <espressione>`.

>[!example]
>```SQL
>SELECT S.Matricola, S.Nome, S.Cognome
>	FROM Studenti AS S
>	ORDER BY S.Cognome, S.Nome
>	
>SELECT S.Matricola, S.Nome, S.Cognome
>	FROM Studenti
>	ORDER BY S.Matricola DESC     -- Ordine decrescente
>```



