
La Computer forensics è l' insieme di metodologie scientificamente provate finalizzate alla ricostruzione di eventi ai fini probatori che coinvolgono direttamente o indirettamente un supporto digitale 

### Identificazione

- ricerca della fonte di prova che può dare una svolta alle indagini, è volta ad individuare dove un dato è conservato 
- vanno identificati i seguenti dispositivi 
	- computer / notebook 
	- cellulari e tablet 
	- memory card, pendrive, hdd esterni, cd/dvd
	- fotocamere e videocamere 
	- server 
	- stampanti, fax, router 
	
[legge 48 del 18/03/2008 art. 247 cpp (1bis)]

##### Preview
![[Pasted image 20231206114900.png]]

- consente di eseguire un analisi di primo livello dei dispositivi allo scopo di trovare delle evidenze 
- si utilizzano *write blocker* 
- si rischia di alterare i contenuti con dispersione di una possibile prova 

- **Dead preview**
	- si esegue ad S.O. spento 
	- si usano write block: non altera il dispositivo analizzato
		- hardware (si usano hardware specifici)
		- software: distro linux live 
	- PRO 
		- non altera il dispositivo 
		- si possono usare diversi strumenti per l' analisi 
	- CONTRO 
		- si deve conoscere bene il sistema e i software da analizzare 
		- non è sempre praticabile: sistemi embedded.


- **Live preview**
	- Si esegue ad S.O. acceso 
	- va documentata e verbalizzata 
	
	- PRO 
		- si ha una visione d'ambiente su cui opera l' utente 
		- è veloce nell' analisi di software analizzati 
	- CONTRO 
		- si altera il reperto 
		- gli strumenti sono adeguati al sistema 
##### Cambiamento di stato del dispositivo 
![[Pasted image 20231206114921.png]]

- **Shutdown** 
	- Vanno valutate le seguenti criticità 
		- cifratura
		- software in esecuzione 
		- Dump della RAM
	- **Metodi di shutdown** 
		- Scollegarlo dalla rete elettrica (unplug)
			- potrebbe compromettere il funzionamento del sistema
		- Spegnimento tramite S.O.
			- Vengono eseguite su disco diverse operazioni (Aggiornamenti).

- Accensione 
	- vanno valutate se le informazioni che perderemo sono meno importanti dell' urgenza dell' accertamento
		- ultimo accesso al sistema 
		- esecuzione su disco di diverse operazioni
		
### Raccolta 

#### Sequestro 
- Dopo aver identificato i dispositivi o dati di interesse investigativo si procede al sequestro, di tipo 
  
	- Fisico: Prendere fisicamente il supporto di interesse.
		- Si prende il supporto contenente i dati , posticipando le problematiche derivanti dall' acquisizione del dato
		- Preoccuparsi solo di identificare e verbalizzare i reperti 
			- [[2- Fasi del trattamento, identificazione e raccolta#Catena di custodia|catena di custodia]]
		- Non è sempre fattibile 
			- su sistemi che non possono essere fermati/spenti 
			- sistemi distribuiti su decine di rack
				  
	- Logico: si esegue una copia totale o parziale della memoria.
		- si esegue una [[2- Fasi del trattamento, identificazione e raccolta#Copia forense|copia forense]] 
		- si ha una garanzia di ripetibilità dei successivi accertamenti che verranno eseguiti sulla copia forense 
#### Catena di custodia 

- Uno o più documenti in cui devono essere riportate tutte le info sul dispositivo che è stato sottoposto a sequestro 
	- Luogo data e operatore che ha reperito e collezionato la fonte della prova 
	- Luogo data e operatore che ha gestito e/o esaminato la fonte di prova 
	- chi ha la responsabilità della custodia delle digital evidences 
	- metodo di conservazione del reperto 
	- eventuali trasferimenti di location dell' evidenza 
#### Copia forense 

- Copia fisica 
	- Copia bit a bit dell' intero supporto di memoria: dati di qualsiasi info sullla gestione dei dati
- Clonazione: si ottiene un supporto pressoché identico all' originale 
	- facilmente alterabile e si usa solo in casi particolari e va inserito nel proprio habitat per analizzarlo 
- La generazione di un file immagine ha come risultato un file rappresentabile il supporto originale 
	- maneggevole 
	- può essere usato per creare un disco clone 

				![[Pasted image 20231206120944.png]]



### Hash 

- l' algoritmo restituisce una stringa di lunghezza fissa in esadecimali a partire da un flusso di dati di dimensione qualsiasi 
	- la stringa è univoca per ogni file e ne è l' identificatore 
	- l' algoritmo non è invertibile, quindi non è possibile ricostruire il dato originale a partire dall' output 


va ricordata la differenza tra accertamenti ripetibili [[2- Procedimento penale e civile#Accertamento tecnico (359 cpp)|(359c.p.p)]] e irripetibili [[2- Procedimento penale e civile#Accertamento tecnico irripetibile (art 360 cpp)|(360c.p.p)]], il secondo tipo va compiuto: 
- su memorie di massa non in buono stato 
- Live Acquisition: il sistema operativo del dispositivo va avviato per realizzare la copia forense 
- cloud 
- dispositivo di origine non disponibile nel tempo 


- Log file 
	- file descrittivo con info sulla copia forense
		- strumenti impiegati: nome versione 
		- disco di origine: modello capacità S/N
		- info dell' immagine forense: nr. di file, dimensioni 
		- altre info: data e ora, nr di settori saltati, etc 
			- **HASH**: [[5-Crittografie#MD4/MD5|MD5]], [[5-Crittografie#SHS/SHA-1/ SHA-256, 512, 384|SHA1, SH256, SHA512]], etc.



## Validazione
- Garantisce che la copia forense sia identica al dato originale 
#### Evidence mutevole 
![[Pasted image 20231211124728.png]]

## Preservazione

- Garantisce che non vengano eseguite modifiche/alterazioni alla copia forense, se ciò avviene l'hash cambierà

## Analisi 
- Va eseguita su una copia 
- Riproducibilità 
- Stesso risultato ottenibile da diverse operazioni e strumenti di analisi 
- ricostruzione degli eventi passati mediante la lettura di dati digitali 

				![[Pasted image 20231212120815.png]]

### Volumi

- Volume system: gestisce i volumi per 2 obbiettivi 
	- unione di più volumi
	- suddivisione del volume in partizioni 

- Volume: insieme di settori per memorizzare i dati 
- Partizione: insieme di settori consecutivi in un volume 


- indirizzamento dei settori 
	- phisical address (LBA) : calcolato in base al primo settore del disco 
	- Logical disk Volume address: indirizzo del settore calcolato in base al primo settore del volume 
	- Logical volume partition address: l' indirizzo è calcolato in base al primo settore della partizione 


- DOS partition 
	- è il sistema di partizione più comune 
	- MBR (Master boot record): primo settore 
		- boot code 
		- partition table: max 4 entry 
			- Starting CHS address.
			- Ending CHS address.
			- Starting LBA address. 
			- number of sectors in a partition. 
			- type of partition.
			- flags.
		- signature : 0x55AA.
	- Primary File system partition: contiene un file system 
	- Primary extended partition: contiene altre partizioni 
		- Tabella della partizione 
		- Secondary file system partition 
			- Tabella di partizione 
			- Secondary file system partition 
			- Secondary extended partition 
	- il Boot code è situato nei primi 446byte del primo settore (MBR)
		- **Microsoft boot code**: processa la tabella di partizione e ricerca ed identifica quella c.d bootable tramite il Flag 
		- possibile incapsulamento di virus 
	- il settore MBR viene allocato all'inizio del disk volume e di ogni extended partition. 
		- EBR (extended boot record)
			- la parte riservata al boot code è inutilizzata. 
			- la parte riservata alle altre 2 entry nella partition table è vuota. 
	
	
![[Pasted image 20231213124651.png]]

-  Apple partition Map 
	- Apple partition (APM)
		- impiegato soprattutto dai vecchi sistemi basati su processori non Intel.
		- nessun limite massimo di partizioni 
		- gestisce volumi fino a 2TB
	  - partition map : secondo settore (512 byte)
		  - ogni entry descrive una partizione 
		  - la prima entry descrive la partition map 

- Guid partition table 
	- Sistema di partizionamento utilizzato da Efi 
		- massimo 128 partizioni 
		- Volumi piu grandi di 2tb 
	- 5 aree/sezioni 
		- protective MBR: Dos partition table (1^ settore) 
		- GPT Header: definisce il layout delle aree
		- Partition table: ogni entry descrive la partizione 
		- Partition area: locazione riservata alla partizione 
		- Backup area: copia di backup del GPT header e della       partition table 






## Relazione tecnica 

![[Pasted image 20231218174049.png]]

- Parte descrittiva : 
	- dettagliata ed accurata 
	- Documentazione fotografica 
- Parte valutativa 
	- Motivazioni 
	- descrizione dell' iter logico 
	- Giuridicamente non è vincolante 
- Forma 
	- Parte epigrafica 
	- Parte Descrittiva
	- Parte Valutativa 
	- Parte Riassuntiva 
- Chiara ed intellegibile 
	- impegno di grafici, illustrazioni, tabelle 