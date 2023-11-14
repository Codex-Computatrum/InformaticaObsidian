---
author: Simone Parente
tags:
  - UML/statecharts
---
### Stati semplici
>Sono disegnati come dei rettangoli con i bordi arrotondati.

```plantuml
!theme crt-amber
state Stato

note right of Stato : Questo è uno stato semplice
```
### Pseudostati iniziali
>Sono utilizzati per indicare lo **stato iniziale default**, ogni regione può contenerne al massimo uno.

```plantuml
!theme crt-amber
State Stato

[*] --> Stato

note "Il vertice nero è uno pseudostato iniziale" as InitPseudoState
```
#### Attività interne
>Gli stati composti possono contenere una lista di attività interne, ogni attività possiede un label che indica **quando** l'attività verrà invocata.

>[!danger] Label riservate 
>- *entry*, indica attività da svolgere dopo l'entrata nello stato
>- *do*, attività da svolgere fintanto che si rimane nello stato (dopo che le attività di *entry* sono state completate)
>- exit, attività da svolgere dopo l'uscita dallo stato

>[!example] Esempio di vita vissuta
>```plantuml
>!theme crt-amber
state "Fare l'università" as uni : entry / paga le tasse e non studiare
uni : do / piangi perché non hai studiato dall'inizio
uni : exit / festeggia la laurea triennale conseguita in soli 17 anni

### Stati composti
>A differenza degli stati normali possono contenere **regioni interne**, gli stati all'interno di una regione interna sono detti **stati interni**.

Questi stati permettono di definire strutture gerarchiche, le regioni interne definiscono il comportamento dello stato a cui appartengono.

Possono inoltre avere delle regioni parallele, tali regioni rappresentano dei comportamenti che possono avvenire parallelamente.
>[!example] Esempio
>![[EsameIngSw.svg]]

### Shallow History Pseudostates (H)
>Salva la configurazione di stato attiva quando si è usciti l'ultima volta dallo stato composto).

>[!danger] Attenzione
>- Ogni stato può contenere al massimo un Deep History Pseudostate.
>- Ѐ utilizzabile solo in stati composti.
>- Non salva la configurazione interna degli stati a livelli di profondità maggiori di quello in cui si trova (vedere [[Stati#^deephistory|Deep History Pseudostates]])

>[!example] Una lampada con 3 livelli di luminosità
>![[Lampada.svg]]

### Deep History Pseudostates ($H^*$) ^deephistory
>Come i precedenti, però salva anche la configurazione degli stati interni.

>[!example] Un lettore musicale
>![[Spotify.svg]]



### Fork and Join Pseudostates
![[Forks]]
![[Joins]]
>[!example] Esempio d'uso
>![[ForkJoin.svg]]





