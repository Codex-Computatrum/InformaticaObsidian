---
author: Giulia Gargiulo
---

- `COUNT`: conta il numero di righe, per un attributo $NULL$ vale 0.
- `MAX, MIN`: calcola il massimo e minimo valore di un attributo, in cui si suppone che l'attributo abbia domini in cui c'è una relazione di ordinamento.
- `AVG`: calcola la media di valori di attributi
- `SUM`: calcola la somma di valori di attributi

 `AVG e  SUM` presuppongono numeri.
##### Criterio di raggruppamento
Sia $R(A_1,\dots, A_n)$ lo schema, individuo un sottoinsieme $B_1,\dots, B_m \subseteq\{A_1,\dots,A_n\}$ che mi determina ***sottoinsiemi di tuple*** della relazione in cui gli attributi $B_1,\dots, B_m$ hanno lo stesso valore.
L'insieme $B_1,\dots, B_m$ è detto ***criterio di raggruppamento***; può anche essere vuoto: in questo caso lavoro su tutte le righe della tabella.

>[!example]
>
Calcolare il numero di esami sostenuti, la media e il numero di lodi di ogni studente.
>```SQL
>SELECT
> 	COUNT(corso) AS numEsami, AVG(voto) AS Media, 
> 		COUNT(lode) AS numLodi
>	FROM Esami
>	GROUP BY (matrStud) -- Criterio di raggruppamento

- La `GROUP BY` consente di esprimere il criterio di raggruppamento; se la ometto lavoro sull'intera tabella.
---
##### Conteggio in SQL
- `COUNT(*)`: conta tutte le righe nel raggruppamento, compresi null e duplicati.
- `COUNT(attributo)`: conta tutte le righe di quello specifico attributo che sono `NOT NULL`.
- `COUNT DISTINCT(attributo)`: conta tutte le righe di uno specifico attributo che sono `NOT NULL` e senza ***ripetizioni***.

>[!example]
> Calcolare il numero di esami sostenuti, la media e il numero di lodi di ogni studente, compresi quelli che non hanno sostenuto alcun esame.
>```SQL
>SELECT S.Matricola, S.Nome, S.Cognome
>	COUNT(corso), AVG(voto), COUNT(lode) 
>	FROM Studenti AS S LEFT JOIN Esami AS E
>	ON S.Matricola = E.matrStud
>	GROUP BY (S.Matricola, S.Cognome, S.Nome)

- Attenzione: posso selezionare nome e cognome perché sono nella `GROUP BY`.
---
##### Clausola Having
Con la clausola `HAVING` si esprimono condizioni sui ***raggruppamenti*** 
(`COUNT, AVG, SUM`).

>[!important]
> Non bisogna confondere la clausola `WHERE`con la `HAVING`!
> Nella `WHERE`dichiaro le selezioni sui valori degli attributi delle tabelle, mentre nella `HAVING`dichiaro le condizioni sui valori ***calcolati*** tramite raggruppamento.


