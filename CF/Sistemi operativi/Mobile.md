

![[Pasted image 20231218172104.png]]

#### Raccolta 
- Disabilitare le connessioni per evitare :
	- Remote Wipe. 
	- Sovrascrittura di info presenti. 
-  Sbloccare il dispositivo 
	- IOS
		- passcode a 4/6 o più cifre. 
		- pass alfanumerica. 
		- Face id / touch id. 
	- Android os
		- Passcode da 4 o piu cifre.
		- Pass alfanumerica.
		- pattern. 
		- faceid/touch id. 
		- pass di avvio. 
	- Sim card 
		- pass 4 cifre (pin) max 3 tentativi. 
		- PUK 8 cifre max 10 tentativi. 
	 
## Strumenti di acquisizione 
![[Pasted image 20231218172608.png]]

#### SIM card 
Struttura 
- Master file (root).
- Dedicated file (directory).
- Elementary file. 

#### Manual extraction

- repertazione fotografica del contenuto 
	- Interagire con la gui. 

- Svantaggi
	- Processo lungo. 
	- Rischio di modifica/cancellazione dei dati. 
- i limiti possono essere
	- Display non funzionante. 
	- codice di sblocco. 
#### Logical extraction

Estrazione tramite api del dispositivo 

- limiti
	- Dipende dall' api 
		- parziali. 
		- solo alcune info. 
		- solo alcuni dati. 
	- Codice di sblocco.

#### File system extraction
Estrazione dei file tramite API del dispositivo. 

Risultato 
- L'output va processato per visualizzare i dati 
	- sono contenuti in DB SQLlite.
	- possibilità di vedere i dati cancellati (tramite entry db).
- Limiti 
	- I risultati dipendono dai permessi con cui vengono fatte le richieste 
		- Completo: tutta la struttura della live partition.
		- Parziale: Solo determinate porzioni.

#### Physical extraction 

Copia bit a bit della memoria del dispositivo
- Boot loader 
	- Bug del firmware/chipset.
- Agent: tool installato nell' SO
	- bug nel SO.
- Advanced ADB 
	- bug nel SO. 

- Risultato 
	- Va processato per visualizzare i dati. 
	- recupero dei file cancellati.
- Limiti 
	- Produttore del dispositivo. 
	- Chipset. 
	- Versione del SO.
	- Patch di sicurezza. 
#### Chip off 

Estrazione fisica del chip da scheda madre 
- Distruzione del dispositivo. 
- limiti : dispositivo cifrato. 









