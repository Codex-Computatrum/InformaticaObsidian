
![[Pasted image 20231214102205.png]]


- Analisi 
	- Recuperare info sul layout. 
	
	 - Controllare  possibili dati nascosti 
		 - bootcode. 
		 - settori in reserved areas 
			 - FSINFO.
		- confronto tra boot sector ed il backup del boot sector. 

- **Content category** 
	- contenuto di file e directory. 
	- Cluster: $2^x$ settori (max 32k)
		- primo: indirizzo 2. 
		- solo in data area.


- **FAT**
	- identificare lo stato di allocazione dei cluster. 
	- successivo cluster: cluster chain. 
	- layout: boot sector. 
	- entry di ugual dimensione: FAT12: 12 bit, FAT16, FAT32.
		- entry = cluster.
			- cluster non allocato: zero.
			- cluster allocato 
				- prossimo. 
				- eof.
		- cluster danneggiato.
- Indirizzamento 
	- la prima entry è l' indirizzo 0. 
	- indirizzo entry = indirizzo cluster. 
		- 0 =info dei media. 
		- 1= dirty status. 

- **Metadata category** 
	- info su file e directory 
		- indirizzo del primo cluster. 
	- parent directory 
		- directory entry: 32k
			- file. 
			- directory. 
		- posizionata nella data area (cluster)
		- file name category. 
			- nome file (8 chars) + estensione (3 chars).
			- \> long file name directory.

	- info temporali (non essential)
		- data creazione (win).
			- nuovo file/copia => nuova data. 
			- sposto/rinomino => copia data.

		- Data modifica (Win) : modifica del contenuto. 
		- Data accesso (Win): modifica anche visualizzando le proprietà. 
	- Mappare le strutture (metadata) con etichetta 
		- filename. 
	- Directory entry: insieme ai metadata category 
		- filename 11 chars. 
		- long file name  directory entry: +13  chars. 
