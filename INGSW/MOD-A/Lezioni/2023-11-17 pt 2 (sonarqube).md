---
author: Simone Parente
tags:
  - todo
---
Obiettivo: valutare e migliorare la qualità del software durante il ciclo di vita di quest'ultimo
### Analisi statica
Il codice viene analizzato (non a runtime) per
- trovare problemi (code smells),
- bug 
- problemi di sicurezza
- valutare la complessità generale del codice, duplicazione di quest'ultimo, ecc.

Ѐ praticamente impossibile andare a analizzare staticamente il codice manualmente, soprattutto se si parla di codebases di migliaia di righe, questo è uno dei motivi per cui si utilizza SonarQube.
### Analisi dinamica
Comprende varie tecniche e metodi di analisi e valutazione del software durante l'esecuzione di quest'ultimo
Aspetti chiave: debugging, profiling (misurare la quantità di spazio o di tempo "utilizzato" per determinati metodi, ecc.), softw testing, etc.

## SonarQube
Identifica tre tipi di problemi specifici:
- Bugs: errori di codice che possono portare errori o comportamenti "inaspettati"
- Vulnerabilità: punti nel codice "aperti" per attacchi
- Code smells
### Issues
inserire roba precedente
#### Ciclo di vita degli issues
Possono avere diversi stati:
- Open: settato automaticamente quando sonarqube trova un nuovo problema
- Confimed: esistenza dell'problema confermaa  manualmente da un utente
- Resolved
- Reopened: settato automaticamente quando sonarqube rileva che i problemi precedentemente trovati non sono stati risolti
- Closed: settato automaticamente quando sonarqube rileva che un issue è stato effettivamente risolto <span style="color:#ff0000">(successivamente ad un set a resolved(?))</span>
### Assegnazione di issues

#### Regole
Esistono delle regole (standard o buone pratiche di programmazione che dovrebbero essere seguite) che, se violate, fanno creare degli issues a sonarqube <span style="color:#ff0000">(da rivedere il modo in cui è scritta sta roba)</span>

### Quality gate
"quality gate is a set of condition to enforce a quality policy in you organization"

Per esempio: "non ci sono **blocker issues**"
#### Definizione del quality gate?
Un esempio di definizione è
"sergio di meglio incompetente"
true
always

#### Technical debt
SonarQube fa una stima del tempo totale necessario per risolvere i problemi del codice.
Una misura di "effort" per risolvere tutti i problemi