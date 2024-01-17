
- Va eseguita su una copia. 
- Riproducibilità. 
- Stesso risultato ottenibile da diverse operazioni e strumenti di analisi. 
- ricostruzione degli eventi passati mediante la lettura di dati digitali. 


![[Pasted image 20231212120815.png]]

### Volumi

- Volume system: gestisce i volumi per 2 obbiettivi 
	- unione di più volumi.
	- suddivisione del volume in partizioni. 

- Volume: insieme di settori per memorizzare i dati. 
- Partizione: insieme di settori consecutivi in un volume. 


- indirizzamento dei settori 
	- Phisical address (LBA) : calcolato in base al primo settore del disco. 
	- Logical disk Volume address: indirizzo del settore calcolato in base al primo settore del volume. 
	- Logical volume partition address: l' indirizzo è calcolato in base al primo settore della partizione. 


- **DOS partition** 
	- è il sistema di partizione più comune. 
	- MBR (Master boot record): primo settore 
		- boot code. 
		- partition table: max 4 entry 
			- Starting CHS address.
			- Ending CHS address.
			- Starting LBA address. 
			- number of sectors in a partition. 
			- type of partition.
			- flags.
		- signature : 0x55AA.
	- Primary File system partition: contiene un file system. 
	- Primary extended partition: contiene altre partizioni.
		- Tabella della partizione.
		- Secondary file system partition 
			- Tabella di partizione. 
			- Secondary file system partition. 
			- Secondary extended partition. 
	- il Boot code è situato nei primi 446byte del primo settore (MBR)
		- **Microsoft boot code**: processa la tabella di partizione e ricerca ed identifica quella c.d bootable tramite il Flag. 
		- possibile incapsulamento di virus. 
	- il settore MBR viene allocato all'inizio del disk volume e di ogni extended partition. 
		- EBR (extended boot record)
			- la parte riservata al boot code è inutilizzata. 
			- la parte riservata alle altre 2 entry nella partition table è vuota. 
			  
![[Pasted image 20240117122442.png]]


![[Pasted image 20231213124651.png]]

-  Apple partition Map 
	- Apple partition (APM)
		- impiegato soprattutto dai vecchi sistemi basati su processori non Intel.
		- nessun limite massimo di partizioni. 
		- gestisce volumi fino a 2TB.
	  - partition map : secondo settore (512 byte)
		  - ogni entry descrive una partizione. 
		  - la prima entry descrive la partition map. 

- Guid partition table 
	- Sistema di partizionamento utilizzato da Efi. 
		- massimo 128 partizioni.
		- Volumi piu grandi di 2tb. 
	- 5 aree/sezioni 
		- protective MBR: Dos partition table (1^ settore). 
		- GPT Header: definisce il layout delle aree.
		- Partition table: ogni entry descrive la partizione. 
		- Partition area: locazione riservata alla partizione. 
		- Backup area: copia di backup del GPT header e della partition table. 

