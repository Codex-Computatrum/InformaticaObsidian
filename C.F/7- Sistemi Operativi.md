# Windows 

#### Analisi dei registri di sistema
- Configurazione dell'utente
- Dispositivi USB 
- info temporali 
- strumenti
	- regedit
	- win registry recovery (mitec)
	- registry viewer (Access data 
	
#### Thumbnails
miniature di immagini presenti nelle cartelle 
per l' analisi di tumbnails non più presenti
- thumbs viewer 
- thumbcache viewer 

#### Shellbag 
Personalizzazioni dell'utente delle visualizzazioni del contenuto delle cartelle 

![[Pasted image 20231218165933.png]]

BagMRU: storico di tutte le cartelle visualizzate dall' utente 
Bags: impostazioni di visualizzazione delle cartelle contenute in bagMRU 

Analisi: 
-  si segue la lista delle cartelle presenti in MRUListex
-  si seleziona e visualizza il valore della chiave relativa

- Si segue la sotto chiave della cartella 
- si visualizza la chiave MRUListex e si continua ricorsivamente la sua esplorazione 


Cosa si può ottenere: 
	Bag Number: sottochiave bags che contiene le preferenze dell' utente 
	Registry key last write time : data del primo accesso o di ultima modifica dell'utente (nodeslot
	Folder name: nome della cartella 
	
Tool: shellbagsview (nirsoft)

#### Application data
Impostazioni dei programmi utilizzati dall' utente e file temporanei 

![[Pasted image 20231218170703.png]]

Analisi :
Quadro complessivo dell' uso del computer da parte dell' utente
- Posta elettronica
- Cache
- Cronologia
- Log
- Configurazioni 
![[Pasted image 20231218170806.png]]





# Linux 

#### Configurazione
Netinfo (Db ad oggetti)
- Controlla diverse configurazioni del SO 
	- Entry statiche di rete 
	- definizione di tutti gli utenti 
Gestione netinfo
/applicazion/utility os x 10.4
/applicazion/utility/utility directory os > 10.4


Configurazioen server 
![[Pasted image 20231218171025.png]]
#### Cifratura 

File vault 
- home directory (/users/\[utente])

File vault 2
- full disk encryption
#### File swap
- Estensione memoria RAM 
	- /private/var/vm/swapfile*
- Congelamento della ram in fase di sospensione 
	- /private/var/sleepimage
#### Portachiavi

Accentramento delle credenziali utente 
- Tramite API
- cifratura AES-128

OS X $\geq$ 10.9 
- integrazione servizio apple iCloud 

#### Analisi 
- Elevato numero di tecnologie proprietarie 
- Strumenti
	- Blacklight: toolkit forense 
	- Macquisition: Tool di acquisizione forense
	- Mac Forensics lab 


- Apple hdlutil: riga di comando 
	- Apple dmg
		- Copia fulldisk
		- copia logica 
		  
- Home directory utente 

	- gran parte dei file utente 
	- dati delle applicazioni
#### Overview 

- Distribuzioni basate su kernel GNU/linux
- Linux Standard Base (LSB)
	- Standardizzazione delle diverse distribuzioni 

- Componenti
	- Kernel
	- Librerie di sistema 


Distribuzioni commerciali 
- Red hat enterprise 
	- Defora 
	- Centos: versione libera senza supporto 
	- Scientific linux 
	- Suse Linux Enterprise
		- openSUSE

Distribuzioni Gratuite 
- Debian: free software foundation 
- Ubuntu

# Mobile 

![[Pasted image 20231218172104.png]]

#### Raccolta 
- Disabilitare le connessioni per evitare :
	- Remote Wipe 
	- Sovrascrittura di info presenti 
-  Sbloccare il dispositivo 
	- IOS
		- passcode a 4/6 o più cifre 
		- pass alfanumerica 
		- Face id / touch id 
	- Android os
		- Passcode da 4 o piu cifre
		- Pass alfanumerica
		- pattern 
		- faceid/touch id 
		- pass di avvio 
	- Sim card 
		- pass 4 cifre (pin) max 3 tentativi 
		- PUK 8 cifre max 10 tentativi 
	 
## Strumenti di acquisizione 
![[Pasted image 20231218172608.png]]

#### SIM card 
Struttura 
- Master file (root)
- Dedicated file (directory)
- Elementary file 

#### Manual extraction

- repertazione fotografica del contenuto 
	- Interagire con la gui 

- Svantaggi
	- Processo lungo 
	- Rischio di modifica/cancellazione dei dati 
- i limiti possono essere
	- Display non funzionante 
	- codice di sblocco 
#### Logical extraction

Estrazione tramite api del dispositivo 

- limiti
	- Dipende dall' api 
		- parziali 
		- solo alcune info 
		- solo alcuni dati 
	- Codice di sblocco 

#### File system extraction
Estrazione dei file tramite API del dispositivo 

Risultato 
- L'output va processato per visualizzare i dati 
	- sono contenuti in DB SQLlite
	- possibilità di vedere i dati cancellati (tramite entry db)
- Limiti 
	- I risultati dipendono dai permessi con cui vengono fatte le richieste 
		- Completo: tutta la struttura della live partition 
		- Parziale: Solo determinate porzioni

#### Physical extraction 

Copia bit a bit della memoria del dispositivo
- Boot loader 
	- Bug del firmware/chipset
- Agent: tool installato nell' SO
	- bug nel SO
- Advanced ADB 
	- bug nel SO 

- Risultato 
	- Va processato per visualizzare i dati 
	- recupero dei file cancellati 
- Limiti 
	- Produttore del dispositivo 
	- Chipset 
	- Versione del SO
	- Patch di sicurezza 
#### Chip off 

Estrazione fisica del chip da scheda madre 
- Distruzione del dispositivo 

- limiti : dispositivo cifrato 









