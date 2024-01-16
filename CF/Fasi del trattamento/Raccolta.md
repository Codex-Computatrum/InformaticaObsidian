
#### Sequestro 
- Dopo aver identificato i dispositivi o dati di interesse investigativo si procede al sequestro, di tipo 
  
	- **Fisico**: Prendere fisicamente il supporto di interesse.
		- Si prende il supporto contenente i dati , posticipando le problematiche derivanti dall' acquisizione del dato.
		- Preoccuparsi solo di identificare e verbalizzare i reperti 
			- [[Raccolta#Catena di custodia|catena di custodia]].
		- Non è sempre fattibile 
			- su sistemi che non possono essere fermati/spenti. 
			- sistemi distribuiti su decine di rack.
				  
	- **Logico**: si esegue una copia totale o parziale della memoria.
		- si esegue una [[Raccolta#Copia forense|copia forense]]. 
		- si ha una garanzia di ripetibilità dei successivi accertamenti che verranno eseguiti sulla copia forense. 
#### Catena di custodia 

- Uno o più documenti in cui devono essere riportate tutte le info sul dispositivo che è stato sottoposto a sequestro 
	- Luogo data e operatore che ha reperito e collezionato la fonte della prova. 
	- Luogo data e operatore che ha gestito e/o esaminato la fonte di prova. 
	- chi ha la responsabilità della custodia delle digital evidences. 
	- metodo di conservazione del reperto. 
	- eventuali trasferimenti di location dell' evidenza. 
#### Copia forense 

- Copia fisica 
	- Copia bit a bit dell' intero supporto di memoria: dati di qualsiasi info sulla gestione dei dati.
- Clonazione: si ottiene un supporto pressoché identico all' originale 
	- facilmente alterabile e si usa solo in casi particolari e va inserito nel proprio habitat per analizzarlo. 
- La generazione di un file immagine ha come risultato un file rappresentabile il supporto originale 
	- maneggevole. 
	- può essere usato per creare un disco clone. 
	  
	  
![[Pasted image 20231206120944.png]]
### Hash 

- l' algoritmo restituisce una stringa di lunghezza fissa in esadecimali a partire da un flusso di dati di dimensione qualsiasi 
	- la stringa è univoca per ogni file e ne è l' identificatore. 
	- l'algoritmo non è invertibile, quindi non è possibile ricostruire il dato originale a partire dall' output. 


va ricordata la differenza tra accertamenti ripetibili [[Procedimento penale#Accertamento tecnico (359 cpp)|(359c.p.p)]] e irripetibili [[Procedimento penale#Accertamento tecnico irripetibile (art 360 cpp)|(360c.p.p)]], il secondo tipo va compiuto: 
- su memorie di massa non in buono stato. 
- Live Acquisition: il sistema operativo del dispositivo va avviato per realizzare la copia forense. 
- cloud. 
- dispositivo di origine non disponibile nel tempo. 


- Log file 
	- file descrittivo con info sulla copia forense
		- strumenti impiegati: nome versione. 
		- disco di origine: modello capacità S/N.
		- info dell' immagine forense: nr. di file, dimensioni. 
		- altre info: data e ora, nr di settori saltati, etc.
			- **HASH**: [[MD4-MD5|MD5]], [[SHS-SHA-1, SHA-256, 512, 384|SHA1, SH256, SHA512]], etc.
