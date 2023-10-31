---
author: Simone Parente
tags:
  - Java/modifiers
---
>[!info] 
Si può applicare a classi, metodi e variabili (ma non a costruttori).
> Il concetto base è: un elemento final non può essere modificato
- Una classe `final` non può avere sottoclassi.
- Una variabile `final` è una costante, può solo essere inizializzata.
- Un metodo `final` non può "subire" override in una sottoclasse.
- Non ha senso attribuire `final` a un costruttore, esso non è ereditato dalle sottoclassi e quindi non sarà sovrascrivibile
>[!danger] 
>-Un riferimento `final` ad un oggetto non può essere modificato (cioè non può essere riassegnato ad un altro oggetto), ma l'oggetto al suo interno si.
>- Un array `final` non può essere riassegnato, ma il contenuto dell'array può essere modificato.