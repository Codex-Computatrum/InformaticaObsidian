- Database in cui vengono memorizzate le info di casi precedentemente analizzati 
	  Central repository 
	- conoscere se un file è già stato ricevuto. 
	- evidenza automaticamente un file come di notevole interesse. 
	- case db più leggero.
- Formati supportati 
![[Pasted image 20231213095440.png]]

- **ingest modules**: Sono plug-in responsabili di analizzare i dati presenti all' interno del file immagine 
	- hashing
		- identificazione del file type (bad extension).
		- user activity 
			- analisi registri.
			- web activity. 
		- indexing. 
		- file carving. 
- esegue i processi di analisi in background 
	- i file vengono processati in base alla seguente priorità:
		- cartelle utenti. 
		- program files e altre cartelle nella root. 
		- cartella di windows. 
		- spazio non allocato. 
	- esecuzione parallela di più file immagine. 
	- i risultati sono presenti nella sezione result.  


- **Hash lookup** 
1. calcola l' hash MD5 per ogni file. 
2. li memorizza nel case DB.
3. ricerca gli hash calcolati all' interno della lista "known hash"
	1. as ignorable file (NSLR).
	2. as notable file.
	- ogni file ha 3 valori di known status. 
		- unknown (default).
		- known (ignorable).
			- possono essere ignorati anche dagli altri moduli. 
			- possono essere nascosti dalla views area. 
			- possono essere nascosti dalla vista ad albero. 
		 Velocizza notevolmente l'analisi.  
		- notable (known bad).


- **ingest modules : file type** 
	- Determina la tipologia di file analizzando la signature 
		- modo più accurato di definire un tipo di file. 
	- il file type viene conservato nel case DB
		- molti moduli dipendono da queste info. 

	  - basato su libreria **Tika** (open source)
		  - catalogazione MIME type 
			  - application/zip. 
			  - audio/mpeg.
			  - image/jpeg. 
			  - application/octet-stream.


- **ingest modules : file extension mismatch** 
	- per ogni file confronta l' estensione con la propria categoria 
		- se non sono corrette viene etichettato. 
	- dipende dal modulo file type 
		l' obbiettivo è trovare il file che l' utente ha provato a nascondere. 

- **ingest modules: exif parser**
	- estrae i metadati exif dal file jpeg , memorizzandoli nella sezione result
		- identifica la fotocamera. 
		- timestamp dello scatto. 
		- geolocalizzazione del luogo di scatto. 

- **ingest modules: embedded file extractor** 
	- estrae i file incapsulati in altri file 
		- archivi file.
		- file grafici da documenti. 
	- i file vengono salvati nel case folder 
		- nella sezione tree view. 
	- vengono etichettati se protetti da pass. 

- **ingest modules : email parser** 
	- ricerca e analizza archivi di posta 
		- mbox, pst e eml file. 
	- i risultati sono visualizzabili nella sezione e categoria email messages 
		- gli allegati sono trattati come figli del messaggio. 
		- sono raggruppati in threads.
	- è possibile analizzarli dettagliatamente attraverso la vista comunications.

- **ingest modules : interesting files**
	- etichetta file e cartelle che si pensa essere interessanti 
		- viene modificato il rinvenimento di tali oggetti 
			- iphone backup. 
			- VMware image. 
			- bitcoin wallets.
			- cloude storage client. 


- **ingest modules : encryption detection** 
	- etichetta file e volumi che sono / potrebbero essere cifrati 
		- documenti office e pdf e access DB protetti da password.
		- possibili file o volumi con cifratura basato su 
			- high entropy. 
			- dimensione: multiplo di 512 byte. 
			- tipo di file: sconosciuto. 

- **ingest modules : plaso**
	- Tool open source che esegue il parsing di file log e altri tipi di file per estrarre il timestamp 
		- ne estrae di più possibili per elaborare la timeline. 
		- come operazione è molto lunga. 

- **ingest modules : Virtual machine extractor** 
	- analizza le virtual machine presenti all'interno del reperto
	  1. ricerca file VMDK e VHD.
	  2. crea una copia locale. 
	  3. vengono inseriti in datasources. 

- **ingest modules : data source integrity** 
	- calcola l' hash del reperto 
		- assicura l' integrità delle evidence. 
	1. recupera l' hash dai metadati del disk image oppure da quelli inseriti dal c.f. 
	2. calcola l' hash del disk image. 
	3. invia un alert se la validazione fallisce. 


- **ingest modules  : recent activity** 
	- estrae le attività recenti dell' utente 
		- analisi dei web browser. 
		- analisi dei registri 
			- usb. 
			- lista utenti. 
			- programmi installati. 
			- programmi eseguiti.
		- analisi del cestino. 
	- i risultati vanno inseriti in extracted content. 
	![[Pasted image 20231213102528.png]]
	![[Pasted image 20231213102544.png]]

- **ingest modules: keyword search** 
	- genera/aggiorna un text index 
		- ricerca testuale. 
	1. si estrae ogni word da ogni file. 
	2. se la word non esiste viene aggiornata. 
	3. associa ogni word all' id del file. 
- uso di **apache solr**
	- indice memorizzato all' interno del case folder. 
	- contiene. 
		- file name. 
		- testo estratto dal contenuto file. 
		- testo estratto dagli artefatti. 

- **ingest modules keyword search** 
	- uso di apache **tika** per estrarre il contenuto dei file e dei metadati 
		- per il file non riconosciuti o corrotti : string extractor 
			- ricerca per byte. 
		-  uso di un proprio HTML text extractor 
			- estrae anche i commenti e java script. 
		- normalizzazione 
			- ricerche case insensitive. 
			- unicode. 


- **ingest modules: correlation engine** 
	- ricerca dei file del caso all'interno del central repository
		- correlare il caso corrente con i casi passati. 
			- evidenzia i file/item che erano stati etichettati come notable nei casi precedenti. 
	- aggiorna il central repository con i file del caso corrente 
		- consente di correlare nuovi casi al caso corrente. 

	- central repository conserva: 
		- valore. 
		- caso. 
		- data source. 
		- file path. 
		- commento del CF.
		- notable status. 


 - **ingest modules: photo rec carver** 
	- recupero dei file cancellati mediante photo rec 
		- open source tool. 
		- data carving. 
		- lavora su unallocated space. 
	- i risultati sono nella vista ad albero $carvedFile. 


- **ingest modules: android analyzer** 
	- analizza i dispositivi android 
		- database di android e app di terze parti. 
		- acquisizione fatta mediante altri strumenti. 
	- estrae 
		- registro chiamate. 
		- contatti. 
		- messaggistica. 
		- browser. 
		- geolocalizzazione.

		

#### Viste specializzate

- **Time Graphic interface**
	- consente di visualizzare graficamente le attività del sistema ordinate temporalmente 
		- file time estratti dal file system. 
		- web activity estratti dal recent activity. 
		- exif. 
		- plaso. 

	- obbiettivo 
		- quando è stato usato il sistema?
		- cosa è accaduto in un certo tempo?
		- cosa è accaduto prima e dopo certi eventi?


- **Image gallery** 
	- Visualizza velocemente un insieme di immagini e video 
		- materiale pedopornografico. 
		- revenge porn. 
		- documenti scansionati. 
	- viene visualizzato il contenuto di una cartella alla volta 
		- priorità. 
			- risultati positivi sull' hash. 
			- numero di immagini/video.

- **Comunication interface** 
	- Visualizza i dati delle comunicazioni in modo differente 
		- email parser. 
		- android analyzer.
	- Orientato intorno agli account 
		- vengono visualizzate tutte le attività associate. 
		- visualizza le relazioni con altri account. 

- **Geolocation** 
	- Riepiloga tutti gli artefatti in cui sono state estratte le info sulle posizioni 
		- exif parser.

- **Tagging** 
	- Crea un riferimento ad un file/item di interesse 
		- consente di commentarlo. 
		- consente di etichettare solo una parte di una immagine. 
	- sono associati all' esaminatore 
		- conoscere chi li ha etichettati. 
		- possono essere nascoste le etichette degli altri esaminatori. 
	- obbiettivo 
		- ritrovare facilmente il file di interesse. 
		- evidenziarlo ed esportarlo nel report. 

- **Reporting**:
	 -  Portable case
		 - versione più piccola del caso originale 
			 - solo i file etichettati.
			- solo i file presenti nella categoria interesting item. 
		- ha un proprio database SQLite.
		- i file sono esportati nel case folder.
- **Extensible** 
	- Autopsy è costituito da moduli plug-in
		- datasource processor. 
		- ingest module. 
		- content viewer. 
		- machine translation. 
		- report module. 

- gli utenti possono creare e pubblicare dei plug-in.

- utilizzano i linguaggi java e python. 

- **Java module.** 
	- Sono file con estensione .nbm. 
		- possono contenere più moduli. 
		- netbeans consente di auto aggiornarli e scaricarli. 
	- Tools->plugins. 


- **Python module** 
	- sono cartelle che contengono file con estensione .py. 
		- copia manuale delle cartelle nella directory. 
		- possono essere solo ingest module e report module. 

