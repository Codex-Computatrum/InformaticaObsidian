

il Valore hash è una rappresentazione non ambigua e non falsificabile del messaggio. 
- impiego:
	- firma digitale. 
	- integrità dei dati. 
	- certificazione del tempo. 
- Integrità: 
 ![[Pasted image 20231212110411.png]]

- funzione message Autentication Code (MAC).
![[Pasted image 20231212110628.png]]
- impiego: 
	- integrità dei dati. 
	- autenticità dei dati: verificare il mittente. 

- Proprietà di sicurezza
	- Confidenzialità: protezione da un soggetto estraneo.
	- Autenticazione: certezza di identificare l' interlocutore. 
	- integrità: verificare che il messaggio non sia stato modificato durante la trasmissione.
		- solo chi è autorizzato può modificare l' attività di un sistema o le info trasmesse.
	- non-Ripudio: negare il disconoscimento del messaggio al mittente o al destinatario. 
	- Anonimia: nascondere l' identità di chi ha compiuto un'azione nel contesto crittografico. 



#### Proprietà di una funzione hash 
- **One - way (pre-image resistant)**
	- dato un hash y,  è computazionalmente difficile trovare M | y=h(M).

- **Sicurezza debole (2nd pre image resisitance)**
	- dato m è computazionalmente difficile trovare una variazione di M, M' |h(M').

- **Sicurezza forte (Collision resistance)**
	- è computazionalmente difficile trovare 2 diversi messaggi con lo stesso valore hash.


#### Definizioni
- **One way Hash function (OWHF)**:
	- verifica proprietà pre image e 2nd pre image resistance. 
	- viene detta weak one-way hash function. 
- **Collision resistant hash function (CRHF)**
	- verifica la proprietà di collision resistance. 
	- viene detta strong one-way hash function. 


#### Costruzione 
Messaggi di lunghezza arbitraria sono trattati utilizzando hash con input fisso 

- il messaggio viene diviso in k blocchi di lunghezza fissa. 
- essi vengono trattati in modo seriale/iterato e parallelo. 