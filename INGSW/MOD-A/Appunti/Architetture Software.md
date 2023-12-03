## Introduzione
>Le architetture software rappresentano la struttura fondamentale su cui si basa un sistema (software), definiscono le modalità con cui i diversi componenti interagiscono tra di loro.

Lo scopo principale è di dividere il sistema in tanti sottosistemi, in modo tale da:
- semplificare l'implementazione complessiva.
- parallelizzare lo sviluppo.
- agevolare eventuali modifiche future, consentendo il riutilizzo del codice, etc..

## Definire un'architettura
L'architettura di un sistema software viene definita nella prima fase di [[System Design]].
>Definire un'architettura significa associare le funzionalità a moduli distinti  seguendo i concetti di [[Alta coesione Basso accoppiamento|alta coesione e basso accoppiamento]].

In principio, per definire un'architettura bisogna:
- identificare i sottoinsiemi coinvolti e specificare le relazioni che li legano
- definire delle politiche di controllo

### Identificazione dei sottoinsiemi
Principio da adottare: [[Dividi et impera]].
È possibile dividere un sistema software in *Layers*, ogni layer contiene diversi *subsystems*, ogni subsystem può essere diviso in diversi *packages*, ogni package è composto da diverse *classi*, ogni classe è composta da diversi *metodi* e *attributi*.
### Layering
![[layering.png]]
Una struttura a layer ha una specifica gerarchia:
- ogni layer raggruppa diversi sottosistemi che forniscono servizi correlati, realizzati eventualmente utilizzando servizi di altri layer.
- un layer può dipendere *solo* da layer di livello più basso.
- un layer **non è a conoscenza** dei layer di livello più alto.
Questo tipo di architettura può essere di due tipi:
- **Chiusa**: ogni layer può accedere solo a layer di livello immediatamente inferiore. Questo implica una limitazione alle funzionalità, ma fornisce anche una maggiore manutenibilità e portabilità.
- **Aperta**: è possibile per un layer accedere a qualsiasi layer ai livelli sottostanti. In questo modo si ottiene una maggiore efficienza a runtime.
## Principali architetture
### Architettura client-server
>Architettura distribuita in cui i dati e l'elaborazione di questi ultimi passano attraverso una rete.

Questa rete è composta da nodi di due tipi diversi:
- **Server**: quelli che forniscono le informazioni
- **Client**: macchine su cui vengono eseguite le applicazioni utente
#### Server
- Hanno maggiore potenza di calcolo rispetto ai client.
- Si occupano di gestire file system, traffico di rete, compilazione, calcolo.
- Non hanno bisogno di conoscere identità o il numero di client connessi.
#### Client
- Fanno da tramite tra utente e server.
- Conoscono i servizi offerti dal server.
- Devono essere a conoscenza di nomi e natura dei server a cui si collegano.
### Repository
>Architettura che prevede una singola struttura dati comune utilizzabile a tutti i sottosistemi.

I sottosistemi sono *relativamente indipendenti*, non possono interagire direttamente tra loro, ma solo tramite le modifiche apportate alla repository
#### Vantaggi
- Efficiente per la condivisione di grandi moli di dati.
- Ogni sottosistema non deve interessarsi di come gli altri sottosistemi interagiscono con i dati.
- Gestione centralizzata.
- È molto facile aggiungere nuovi sottosistemi all'architettura (grazie all'indipendenza).
#### Svantaggi
- Adottare un nuovo modello di dati è molto complesso.
- Diversi sottosistemi possono avere diversi requisiti di backup o sicurezza, che non sono per forza supportati dalla repository.
- È difficile distribuire la repository su più macchine mantenendo i dati consistenti ed evitando ridondanze.
### Architettura a 3 livelli
>In questa architettura ogni livello ha un compito molto specifico.

- Il **livello 1** si occupa di gestione dei dati (comunicazione con i DBMS, file XML, ...).
- Il **livello 2** si occupa di processare i dati.
- Il **livello 3** si occupa dell'interfaccia utente.
Ogni livello è indipendente sotto il punto di vista implementativo e strutturale:
- Il livello 1 e 3 non comunicano direttamente, è il livello 2 che processa gli eventuali dati presi dall'utente e li invia al livello 1 (o viceversa).
- Ogni livello opera come se fosse **unico** e non come parte di un sistema più grande ([[Alta coesione Basso accoppiamento]])
#### Vantaggi
- Flessibilità e modificabilità delle varie componenti.
- Possibilità di usare le componenti in diversi contesti contemporaneamente.
- Ricerca di bug semplificata.
#### Svantaggi
- Poco efficiente.
- La comunicazione tra componenti richiede uso di librerie per lo scambio di informazioni (ciò porta a dover scrivere molto più codice).
- Difficile adattare software vecchio (e monolitico) a questa architettura.

### Architetture a N livelli
>Evoluzione delle architetture a 3 livelli

Gli elementi fondamentali sono:
- **Interfaccia utente**: si occupa di gestire l'interazione con gli utenti, può essere un'applicazione, un browser, ecc..
- **Presentation logic**: definisce cosa presenta l'interfaccia e come gestire le richieste dell'utente.
- **Business logic**: gestisce le regole di business dell'applicazione.
- **Infrastructure services**: forniscono funzionalità supplementari all'applicazione.
- **Data layer**