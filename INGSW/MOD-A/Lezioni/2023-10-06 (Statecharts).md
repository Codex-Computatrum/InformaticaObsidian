---
author: Simone Parente
---

## Modellazione tramite stati e transizioni
### Stato
Situazione in cui permane qualche _condizione invariante_ che potrà essere:
- Statica: il sistema sta aspettando che accada qualcosa
- Dinamica: il sistema sta effettuando un task
Uno stato può essere opzionalmente decorato con una lista di attività interne che sono caratterizzate da un label e da una sequenza di azioni, la label dice *quando* eseguire le azioni, possono inoltre avere:
- Il compartimento del nome
- la lista delle attività da svolgere
- ulteriori regioni interne (che lo rendono uno stato composito, gli stati in una regione interna si chiamano substates) \[automi gerarchici]
#### Stati compositi
Consente ai modellatori di definire una struttura gerarchica.
Possono contenere diverse regioni, che rappresentano comportamenti che potrebbero accadere in parallelo, quando si esce da un composite state, tutte le sue regioni vengono terminate
### Transizione
Rappresenta possibili cambiamenti di stato.
Possono essere decorate con delle label <span style="color:#ffbe0a">trigger</span> <span style="color:#00ccff">[guard]</span> <span style="color:#c800ff">\actions</span> (opzionali)
Dove trigger sono gli eventi che devono verificarsi per indurre un cambiamento di stato
guard è una condizione booleana
actions è la lista di operazioni da eseguire quando la transizione "fires".
Transizione "fireable" (percorribile):

Se più di una transizione è fireable, ne verrà eseguita comunque solo una.

## Regioni, vertici, transizioni
Ogni Statechart UML contiene una regione top-level che contiene *vertici* e *transizioni*.
Ogni vertice rappresenta uno stato, le transizoni sono raffigurate

## Pseudostati e stati finali
Ogni regione contiene uno pseudostato iniziale e questi pseudostati sono utilizzati per definire lo stato "default" (iniziale). Gli stati finali modellano una situazione in cui la computazione è stata completata (vorrà dire che il sistema non eseguirà azioni aggiuntive)

### Deep History Pseudostate (H*)
Puntatore non solo all'ultimo stato attivo della regione corrente ma tiene traccia anche di tutti gli altri stati della subregion.

---

