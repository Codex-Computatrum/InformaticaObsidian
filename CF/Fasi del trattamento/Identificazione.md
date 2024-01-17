

- ricerca della fonte di prova che può dare una svolta alle indagini, è volta ad individuare dove un dato è conservato.. 
- vanno identificati i seguenti dispositivi 
	- computer / notebook. 
	- cellulari e tablet. 
	- memory card, pendrive, hdd esterni, cd/dvd.
	- fotocamere e videocamere.
	- server. 
	- stampanti, fax, router. 
	
[[legge n.48 del 18-03-2008|legge n48 del 18/03/2008 art. 247 cpp (1bis)]]

##### Preview
![[Pasted image 20231206114900.png]]

- consente di eseguire un analisi di primo livello dei dispositivi allo scopo di trovare delle evidenze. 
- si utilizzano *write blocker*. 
- si rischia di alterare i contenuti con dispersione di una possibile prova. 

- **Dead preview**
	- si esegue ad S.O. spento. 
	- si usano write block: non altera il dispositivo analizzato.
		- hardware (si usano hardware specifici).
		- software: distro linux live.
	- PRO 
		- non altera il dispositivo. 
		- si possono usare diversi strumenti per l' analisi. 
	- CONTRO 
		- si deve conoscere bene il sistema e i software da analizzare. 
		- non è sempre praticabile: sistemi embedded.


- **Live preview**
	- Si esegue ad S.O. acceso. 
	- va documentata e verbalizzata. 
	
	- PRO 
		- si ha una visione d'ambiente su cui opera l' utente. 
		- è veloce nell' analisi di software analizzati. 
	- CONTRO 
		- si altera il reperto. 
		- gli strumenti sono adeguati al sistema. 
##### Cambiamento di stato del dispositivo 
![[Pasted image 20231206114921.png]]

- **Shutdown** 
	- Vanno valutate le seguenti criticità
		- cifratura.
		- software in esecuzione. 
		- Dump della RAM.
	- **Metodi di shutdown** 
		- Scollegarlo dalla rete elettrica (unplug).
			- potrebbe compromettere il funzionamento del sistema.
		- Spegnimento tramite S.O.
			- Vengono eseguite su disco diverse operazioni (Aggiornamenti).

- **Accensione** 
	- vanno valutate se le informazioni che perderemo sono meno importanti dell' urgenza dell' accertamento
		- ultimo accesso al sistema.
		- esecuzione su disco di diverse operazioni.
		