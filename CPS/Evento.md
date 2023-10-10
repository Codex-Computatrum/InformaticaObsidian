---
author: Lorenzo Tecchia
tags: [definition, probability]
---
I sottoinsiemi dello [[spazio degli esiti]] si dicono ***eventi***, quindi un ***evento*** $E$ è un insieme i cui elementi sono ***esiti possibili***. Se l’[[esito]] dell’esperimento è contenuto in $E$, diciamo che l’evento $E$ si è verificato.

>[!important] 
> - Gli **eventi** sono oggetti di $\mathcal{F}$ (della sigma algebra)
> - Gli eventi che contengono un solo elemento vengono chiamati *eventi singoletti*.

## Unione $E \cup F$
L’ unione $E \cup F$ di due eventi $E$ e $F$ dello stesso spazio degli esiti $\Omega$, è definita come l’insieme formato dagli esiti che stanno o in $E$ o in $F$. Quindi l’evento $E \cup F$ si verifica se almeno uno tra $E$ e $F$ si verifica.
## Intersezione $E \cap F$
L'intersezione $E \cap F$ di due eventi $E$ e $F$ dello stesso spazio degli esiti $\Omega$ è l’insieme formato dagli esiti che sono presenti sia in $E$, sia in $F$. Come evento, rappresenta il verificarsi di entrambi gli eventi $E$ e $F$.

>[!note] Evento "impossibile"
> Denotiamo l'evento vuoto con $\emptyset$, tale evento è tale che non contiene ***eventi possibili*** per l'esperimento. Se $E \cap F = \emptyset$, ovvero se $E$ e $F$ non possono verificarsi entrambi, li diremo eventi mutuamente esclusivi o eventi disgiunti.

>[!note] Complementare
> Per ogni evento $E$, definiamo l’evento $E^c$, che diciamo complementare di $E$, come l’insieme formato dagli esiti di $\Omega$ che non stanno in $E$. Quindi $E^c$ si verifica se e solo se non si verifica $E$. Si noti infine come valga la ovvia relazione $\Omega^{c} = \emptyset$. 