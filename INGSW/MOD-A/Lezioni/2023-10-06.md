## Modellazione tramite stati e transizioni
### Stato
Situazione in cui permane qualche "invariant condition" che potrà essere:
- Static conditions: il sistema sta aspettando che accada qualcosa
- Dynamic conditions: il sistema sta effettuando un task
Uno stato può essere opzionalmente decorato con una lista di attività interne che sono caratterizzate da una label e da una sequenza di azioni, la label dice *quando* eseguire le azioni, possono inoltre avere:
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
>[!example] Esempio
>Statechart del funzionamento di una finestra di un sistema operativo (prendiamo come base Microsoft Windows)

```plantuml
'!theme superhero-outline
'!theme blueprint
'!theme crt-amber
!theme toy
state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}

state Minimized{

}

Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
```
