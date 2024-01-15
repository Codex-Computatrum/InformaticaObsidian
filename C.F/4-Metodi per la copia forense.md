---
~
---
## Disk image

- Supporti ottici 
	- Formato ISO: più comune
	- Formato .bin = Copia RAW
	- Formato .cue = Metadati

- Formato DD/RAW
Formato semplice è un container dello stream

- Problematiche: 
	- Non conserva metadati dell'evidence: modello, seriale dimensione, etc.
	- Non conserva hash calcolati;
	- Non esegue compressione ;
	- Non può contenere più di un file/stream
	  
- Smart (EWF)
	- obbiettivo: accesso veloce ad una parte dell' immagine 
		- Segmentazione: .s01 ; .s02 ; etc etc 
		- ogni segmento è composto da:
			- headerfile: signature e numero di segmento 
			- una o più sezioni:
				- header section 
				- volume section 
				- table section 
				- next/done sections 
![[Pasted image 20231211145303.png]]

- Encase L01 Logical (EWF)
	- acquisizione di file logici
	- segmentazione:  .l01 ; l02 ; etcetc
	- impiega 15 sezioni (+2 al formato E01)
		- Ltree section 
		- Ltypes section

- Advanced Forensics format (AFF/AFF4)
	- ogni disco separato in 2 layer 
		- disk-rappresentation layer (metadato)
		- data-storage layer (dato). 
		![[Pasted image 20231211145614.png]]
### Guymager 

![[Pasted image 20231211145633.png]]

- Disk image 
	- si sceglie il formato dell' immagine e la dimensione dei segmenti 
	- si inseriscono le informazione di elaborazione 
	- il nome e destinazione del file immagine
	- la scelta dell' HASH , il calcolo del dispositivo target dopo l' acquisizione e il calcolo del hash del file immagine 
	- durante l' elaborazione vengono visualizzate le statistiche sull' elaborazione e il riepilogo delle impostazioni , al termine viene visualizzata una spunta verde 


### FTK imager
![[Pasted image 20231211162508.png]]

- File > Create disk image...
	- tipi di acquisizione 
		- physical drive 
		- logical drive
		- image file 
		- content of folder 
		- fenico device 

Physical Drive :
-   Source drive selection: dispositivo a acquisire
	- Si sceglie il formato immagine 
	- Si inseriscono le informazioni del caso 
	- Definizione del file immagine
		- percorso e nome del file immagine 
		- dimensione dei segmenti dei file immagine 
		- livello di compressione del file immagine 
		- cifratura del file immagine 
	- Add overflow location: calcolo e verifica dell' hash del file immagine col dispositivo target e si decide se aggiungere ulteriore spazio di archiviazione per il file immagine (install version) 
	- è possibile visionare il tempo rimanente l' elaborazione della copia forense 
	- è possibile generare un file CSV di tutti i file e cartelle presenti.
	
	- durante l' elaborazione:
		- dispositivo target 
		- file immagine 
		- indicazioni dello stato del processo 
		- info temporali sull' elaborazione
	- vi è un processo di validazione del file immagine 

	- al termine dell' elaborazione si genera un file con le info riportate.



Apertura del file immagine.
- File > Add evidence item.


Logical Drive 
- File > Create disk image
- è possibile acquisire un supporto ottico 

Image file
- impiegato principalmente per convertire un file immagine da un formato ad un altro:  Es. 
   E01 -> DD

Contents of a Folder 
- Acquisizione logica di file in una determinata cartella 

Custom Content image 
- elaborazione di un immagine personalizzata
	- File -> add evidence item.
	- si visualizzano i file che sono stati selezionati 
	- wild card option 
		- ? = qualunque carattere
		- * = qualunque serie di caratteri 
		- | (pipe) = separatore di directory e file 
		- le distinzioni tra maiuscole e minuscole 
		- si può estendere la ricerca ricorsivamente alle sottocartelle 
		- la ricerca viene eseguita direttamente su tutte le evidence aggiunte e presenti nell' evidence tree

dump memoria volatile 
- File > Capture memory 
	- percorso dove salvare il dump della memoria 
	- nome con il quale vogliamo salvare il dump 
	- si richiede di copiare anche il file di paging di windows 
	- il dump viene incapsulato in un file immagine AD1 





# Nella  fase di verifica 

### Forensic Toolkit  (FTK)
### Autopsy 

## i Volumi 

### Dos Partition 

### Apple Partition Map 

### GUID Partition Table 
#### Gpt Header


## File System 

### FAT file system 
### NT File System 