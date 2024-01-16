
![[Pasted image 20231218094733.png]]

- **$MFT** 
	- Ogni file/directory ha almeno una entry (file record). 
	- 1024 byte (boot sector).
	- entry \[0] : $MFT.
	- Starter cluster (boot sector).
- Entry 
	- dim= 1024 byte. 
		- header : 42 byte.
		- attributi: strutture dati. 
	- signature; <\File> / <\Baad>.
	- Stato di allocazione: Attributo $Bitmap nella entry \[0] $MFT.
	- indirizzo sequenziale 48 bit (file number).
	- numero sequenziale: 16 bit (contatore allocazione).

- File system metadata $MFT file 
	- Contiene la master file table. 
		- cluster iniziale : boot sector. 

- Layout 
	- Win 7: cluster 786432. 

- Entry\[0] di MFT
	- $DATA: cluster usati. 
	- $BITMAP: Stato di allocazione delle entry. 

- File system metadata $MFTMirr file 

	- Backup della Master file table.
	- prime 4 entry: $MFT, $MFTMirr, $LogFile, $Volume. 
	- Entry\[1] di MFT.
	- layout 
		- win 7 o superiore: dopo il boot sector (16 settore).
		- prima di win 7: a metà del file System.


- File system metadata $Boot file
	-  Boot sector 
		- Dimensione dei cluster. 
		- nr.settori del file system. 
		- layout MFT
			- cluster iniziale. 
			- dimensione entry. 
		- Entry\[7] di MFT.
	- Layout : primi 16 settori del file system 
		- Signature : 0xAA55.


- File system metadata $Volume File 
	- Info sul volume 
		- etichetta. 
		- versione.
	- Entry \[3] di MFT
		- $Volume_name: nome in unicode del volume 
			- id type: 96.
		- $Volume_information: 
			- versione di ntfs.
			- Dirty status. 
		- $DATA: 0 byte.


- ANALISI:
	- processare il primo settore del file system: Boot sector
		- Layout MFT.
	- Processare la MFT\[0] 
		- $MFTMirr.
	- Processare $volume. 
	- Processare $Attref.
	- processare le altre entry MFT.

- Content category 
	- Contenuto degli attributi 
		- residenti. 
		- non residenti: Cluster esterni. 

	- Cluster 
		- Cluster\[0] = settore\[0] del file system 
			- settore= Cluster x Settori_Cluster.


-  File system metadata $Bitmap File

	- Info sullo stato di allocazione del cluster 
		- Bit\[x] = Cluster\[x].
			- 1= cluster x allocato.
			- 0= non allocato. 
	- entry \[6] MFT.


-  File system metadata $BadClus File
	- Traccia i cluster con settori danneggiati. 

	- Entry\[8] MFT
		- \$Data=\$bad.
			- flag=sparse.
			- size =file system .
			  
![[Pasted image 20231218101853.png]]