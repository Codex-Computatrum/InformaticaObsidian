
- Solitamente posizionati nel primo settore. 
- Essenziali: info sul layout dei dati. 

- Analisi 
	- info sulla generalizzazione del file system. 
	- info sul layout. 
	- controllo consistenza: Volume slack.


- Content category 
	- Locazioni di memoria impiegate per la memorizzazione del contenuto dei file 
		- Data unit: raggruppamento in più settori
			- stato: allocato e non. 
			- logical file system address. 


- Strategia del primo disponibile 
	- si cerca una data unit libera ogni volta partendo dall' inizio. 
	
- Prossimo disponibile 
	- si cerca partendo dall' ultima locazione allocata. 

- Più adatto 
	- si cercano data unit libere in modo che possano contenere consecutivamente il file. 

Analisi
- Data unit view: settori noti del file system. 
- logical file system searching: ricerca di un contenuto specifico nei data unit. 
- Data unit allocation status: ricerca nei data unit non referenziali in metadata category. 


- Metadata category 
	- descrivono i file presenti in content category 
		- info temporali. 
		- indirizzo delle data unit allocate per i file.
	- Analisi 
		- ricerca di maggiori info su un file. 
		- ricerca di file in base agli attributi descritti in questa categoria. 


- **Logical file address** : 
	- indirizzo di parte del file allocata nella data unit 
		- è il contenuto nella data unit. 

- **Slack space**:
	- parte non usata di una data unit allocata. 

- **File recovery**: 
	- recupero dei file cancellati analizzando le entry in metadata category con lo stato non allocato. 

- **Compressed file**: 
	- memorizzare i dati in un formato compresso occupano meno data unit. 

	- 3 livelli di compressione 
		- soli dati all' interno del file. 
		- di tutto il file. 
		- eseguita nel file system : invisibile nel lato applicativo e utente. 

- **File name category** 
	- nome assegnato a ciascun file (indirizzo della struttura metadato).

	- **File recovery** 
		- recupero dei file cancellati ricercando i file name con lo stato non allocato 
			- analisi della struttura metadati indirizzata. 

- **Application category** 
	- dati non essenziali al file system. 
		- sono più efficienti se conservati nel file system. 
			- spazio occupato, journaling. 

	- **Journaling**: 
		- conservazione delle modifiche effettuate e da effettuare sui metadati 
			- evitare l' inconsistenza 
				- completamento delle operazioni di modifica. 
				- ripristino dei dati a prime delle modifiche (rollback).
		- Analisi
			- ricostruire eventi di un incidente recente.