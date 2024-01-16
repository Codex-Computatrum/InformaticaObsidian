#### Analisi dei registri di sistema
- Configurazione dell'utente.
- Dispositivi USB. 
- info temporali.
- strumenti
	- regedit.
	- win registry recovery (mitec).
	- registry viewer (Access data). 
	
#### Thumbnails
miniature di immagini presenti nelle cartelle 
per l' analisi di thumbnail non più presenti
- thumbs viewer. 
- thumbcache viewer. 

#### Shellbag 
Personalizzazioni dell'utente delle visualizzazioni del contenuto delle cartelle. 

![[Pasted image 20231218165933.png]]

BagMRU: storico di tutte le cartelle visualizzate dall' utente. 
Bags: impostazioni di visualizzazione delle cartelle contenute in bagMRU. 

Analisi: 
-  si segue la lista delle cartelle presenti in MRUListex.
-  si seleziona e visualizza il valore della chiave relativa.

- Si segue la sotto chiave della cartella. 
- si visualizza la chiave MRUListex e si continua ricorsivamente la sua esplorazione. 


Cosa si può ottenere: 
	- Bag Number: sottochiave bags che contiene le preferenze dell' utente. 
	- Registry key last write time : data del primo accesso o di ultima modifica dell'utente (nodeslot).
	- Folder name: nome della cartella. 
	
Tool: shellbagsview (nirsoft).

#### Application data
Impostazioni dei programmi utilizzati dall' utente e file temporanei. 

![[Pasted image 20231218170703.png]]

Analisi :
Quadro complessivo dell' uso del computer da parte dell' utente
- Posta elettronica.
- Cache.
- Cronologia.
- Log.
- Configurazioni. 
![[Pasted image 20231218170806.png]]


