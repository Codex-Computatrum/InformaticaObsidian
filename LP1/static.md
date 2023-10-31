---
author: Simone Parente
tags:
  - Java/modifiers
---

>[!info] 
>Una caratteristica `static` appartiene a una classe, essa è unica, a prescindere dal numero di istanze di quella classe.
>Si applica ad
>- attributi
>- metodi
>- blocchi di codice *esterni ai metodi*

### Attributi
L'inizializzazione di un attributo `static` avviene quando la classe viene caricata in memoria.
L'accesso a un attributo `static` può avvenire (tramite dot-notation):
- tramite un riferimento ad un'istanza di quella classe
- tramite il nome stesso della classe.
### Metodi
Appartengono alle classe e possono essere invocati a partire dal nome della classe (di nuovo tramite dot-notation).
Non possono "subire" override.
### Blocchi di codice
Una classe può contenere blocchi di inizializzazione marcati `static`, questi blocchi vengono eseguiti una singola volta, quando la classe viene caricata in memoria.
Vengono utilizzati in genere per inizializzare gli attributi `static`.
