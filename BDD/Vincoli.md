---
author: Giulia Gargiulo
---

#### Vincoli di Dominio
Esprimono delle restrizioni sui valori del dominio di un ***singolo attributo***; sono realizzati tramite:
- una condizione da controllare nella dichiarazione dell'attributo, ad esempio `CHECK(voto>= 18 and voto<=30`
- definendo un tipo tramite da dichiarazione di un ***dominio*** `CREATE DOMAIN`. In questo caso disaccoppio la definizione del vincolo da quella della tabella.

#### Vincoli di N-upla
Sono vincoli che coinvolgono più attributi di una ***stessa*** riga **(n-upla)**; si definiscono tramite `CHECK CONSTRAINT` alla fine della tabella.

>[!Note]
>I vincoli di dominio e di n-upla sono facili da controllare, il controllo viene effettuato all'inserimento o modifica nella tabella.

#### Vincoli Intra-relazionali
Sono vincoli che coinvolgono l'intera tabella; si definiscono tramite:
- `PRIMARY KEY` e `UNIQUE`
- `CONSTRAINT <nome_vincolo> CHECK <espressione>`

#### Vincoli Inter-relazionali
Sono vincoli che coinvolgono più tabelle; si definiscono tramite:
- `FOREIGN KEY`
- `ASSERTION` e `TRIGGER`






