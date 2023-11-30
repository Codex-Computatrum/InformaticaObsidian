---
author: Simone Parente
tags: 
Lezione: "20"
---

## Sicurezza informatica
È la branca che si occupa di attacchi informatici e possibili soluzioni per prevenirli.
### Tipi di attacchi
#### Malwares
>[!info] 
>Un malware è un software maligno che può essere trasferito da un computer a un altro attraverso una rete (download di file, allegato ad una mail, ecc.)

Possono essere divisi in ulteriori sottocategorie:
- **Adware**: forzano il computer a mostrare annunci pubblicitari indesiderati
- **Scareware**: mostrano falsi messaggi d'allarme per indurre gli utenti a scaricare (ulteriori) malware.
- **Wiper**: cancellano i file senza il consenso dell'utente.
- **Ransomware**: bloccano i file chiedendo spesso una "ricompensa" per sbloccarli.
- **Spyware**: rubano i dati sensibili presenti sulla macchina.
	- Keylogger: software che registra e salva ogni tanto premuto sulla tastiera.
- **Rootkit**: ottiene i privilegi di root del sistema operativo.
- **Zombie** o **botnet**: rende il computer infettato uno *slave* o un punto d'appoggio per infettare altri computer.

I malware attuali sono spesso "auto-replicanti", una volta che infettano un host, provano ad infiltrarsi su altri host in giro per internet, diffondendosi a velocità esponenziale. Possiamo dividerli in *virus* e *worm*:
- i **virus** sono malware che hanno bisogno di qualche tipo di interazione da parte dell'utente per infettare un host, possono diffondersi, ad esempio, tramite allegati a mail, inviando allegati simili a tutti i contatti del primo host infettato.
- i **worms** sono più pericolosi perché possono infettare dispositivi senza una diretta interazione dell'utente, ad esempio diffondendosi in una rete che accetta il worm senza intervenire direttamente.
#### Denial of Service (DoS)
>[!info] 
>Sono attacchi abbastastanza comuni, mirano a rendere inutilizzabile una specifica infrastruttura (un host, una rete, dei server, DNS, ecc.).

Ne esistono di 3 tipi:
1. Vulnerability attack: inviano specifici messaggi a applicazioni o sistemi operativi vulnerabili costringendoli a "stopparsi".
2. Bandwith flooding: consistono nell'inviare ingenti quantità di pacchetti a un determinato host, in modo tale da non rendere possibile ai pacchetti "previsti" di raggiungere il server.
3. Connection flooding: stabilire un gran numero di connessioni **TCP** all'host bersaglio, così da non rendergli possibile di stabilirne di nuove.
#### Packet Sniffing
>[!info] 
>Prevede che un *ricevitore passivo* (*sniffer*) crei delle copie di pacchetti inviati da un host in modo tale da rubare informazioni sensibili (eavesdropping)

Questi sniffer possono essere distribuiti in tutti i tipi di [[reti broadcast]], semplicemente copiando i pacchetti destinati altrove invece di scartarli.
Sono molto difficili da individuare perché non creano traffico aggiuntivo sulla rete (sono per questo detti passivi).
#### IP Spoofing
>[!info] 
>È una tecnica che consente a host malitenzionati di inviare pacchetti con l'IP dei mittenti "falsato".

Possono sfruttare le vulnerabilità delle applicazioni per attaccare specifici host "mascherando" la propria identità dietro quella di un diverso utente.

Può essere utilizzato anche per attacchi *man-in-the-middle* in cui l'utente malintenzionato si trova tra due host che stanno comunicando, "mascherandosi" da entrambi.
### Basi di sicurezza informatica
Visti i diversi tipi di attacco, è ora possibile definire delle proprietà che una **connessione sicura** dovrebbe garantire:
1. **Confidenzialità**: solo il mittente e il destinatario dovrebbero essere in grado di leggere il contenuto dei messaggi trasmessi.
2. **Integrità dei messaggi**: il contenuto della comunicazione non deve essere alterato. Né da utenti malintenzionati, né per errori.
3. **Autenticazione end-point**: sia il mittente che il destinatario devono essere in grado di confermare l'identità dell'altra parte coinvolta nella comunicazione.
4. **Operational security**: fare affidamento su un'infrastruttura di rete che previene l'intrusione di utenti malintenzionati sulla rete.
Le prime 3 proprietà sono *software-based*, l'ultima si basa su hardware specifico (ad esempio un firewall).
### Crittografia
Una "tecnica crittografica" permette a un mittente di rendere incomprensibile i dati per un intruso, allo stesso tempo, il destinatario deve essere in grado di recuperare i dati originali da quelli "resi incomprensibili".

Il messaggio nella forma iniziale è detto *plaintext* ed è leggibile per chiunque, prima di essere inviato l'host utilizza un algoritmo crittografico così da renderlo illeggibile (questo messaggio ora sarà *ciphertext*) e dovrà essere decriptato all'arrivo al destinatario.

#### Chiavi
Nella maggior parte dei sistemi di crittografia moderni, la tecnica crittografica è ben nota, la parte sconosciuta è la parte di *encrypt* e *decrypt* (le chiavi).

Queste chiavi sono delle stringhe alfanumeriche che devono essere fornite agli algoritmi di encrypt/decrypt per criptare o decriptare i messaggi. Possono essere identiche (crittografia simmetrica) o diverse (crittografia asimmetrica).

##### Crittografia simmetrica
> Esiste un'unica chiave utilizzata sia per criptare che decriptare i messaggi.

Encryption: il plaintext e la chiave vengono passati all'algoritmo di criptazione, il ciphertext vine quindi inviato

Decryption: il ciphertext e la chiave vengo passati all'algoritmo di decrypt per ricreare il plaintext

##### Key exchange
Il problema della crittografia simmetrica è che la chiave deve necessariamente essere comunicata al destinatario, di conseguenza è necessario utilizzare un canale sicuro per la comunicazione o utilizzare dei protocolli che permettono loro di "convergere" su una chiave condivisa.
##### Crittografia asimmetrica
Vi sono due diverse chiavi, una per criptare, una per decriptare