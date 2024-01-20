
![[Pasted image 20231211162508.png]]
- è uno strumento per elaborare copie forensi. 
- può eseguire una copia della memoria volatile.

- File > Create disk image…
	- tipi di acquisizione 
		- physical drive. 
		- logical drive.
		- image file. 
		- content of folder. 
		- fenico device. 

Physical Drive :
- Source drive selection: dispositivo a acquisire
	- Si sceglie il formato immagine. 
	- Si inseriscono le informazioni del caso. 
	- Definizione del file immagine
		- percorso e nome del file immagine. 
		- dimensione dei segmenti dei file immagine. 
		- livello di compressione del file immagine. 
		- cifratura del file immagine. 
	- **Add overflow location**: calcolo e verifica dell' [[Funzione hash|hash]] del file immagine col dispositivo target e si decide se aggiungere ulteriore spazio di archiviazione per il file immagine (install version). 
	- è possibile visionare il tempo rimanente l' elaborazione della copia forense. 
	- è possibile generare un file CSV di tutti i file e cartelle presenti.
	
	- durante l'elaborazione:
		- dispositivo target. 
		- file immagine. 
		- indicazioni dello stato del processo. 
		- info temporali sull' elaborazione.
	- vi è un processo di validazione del file immagine. 

	- al termine dell' elaborazione si genera un file con le info riportate.

Apertura del file immagine.
- File > Add evidence item.

Logical Drive 
- File > Create disk image.
- è possibile acquisire un supporto ottico. 

Image file
- impiegato principalmente per convertire un file immagine da un formato ad un altro:  Es. 
   E01 -> DD.

Contents of a Folder 
- Acquisizione logica di file in una determinata cartella. 

Custom Content image 
- elaborazione di un immagine personalizzata
	- File -> add evidence item.
	- si visualizzano i file che sono stati selezionati. 
	- wild card option 
		- ? = qualunque carattere.
		- \* = qualunque serie di caratteri. 
		- | (pipe) = separatore di directory e file. 
		- le distinzioni tra maiuscole e minuscole. 
		- si può estendere la ricerca ricorsivamente alle sottocartelle. 
		- la ricerca viene eseguita direttamente su tutte le evidence aggiunte e presenti nell' evidence tree.

dump memoria volatile 
- File > Capture memory 
	- percorso dove salvare il dump della memoria. 
	- nome con il quale vogliamo salvare il dump. 
	- si richiede di copiare anche il file di paging di windows. 
	- il dump viene incapsulato in un file immagine AD1. 





