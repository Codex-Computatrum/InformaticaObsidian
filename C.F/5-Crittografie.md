
- Un protocollo o schema definisce le interazioni fra le parti per ottenere le proprietà di sicurezza desiderate 
- le parti sono le entità coinvolte nello schema 

- i protocolli si basano su una serie di protocolli più semplici detti primitive crittografiche
	- risolvono problemi facili 
	- possono essere usati per risolvere problemi più complessi 

le primitive crittografiche risolvono i seguenti problemi: 
- CIFRATURA: cifrati simmetrici o asimmetrici o a chiave pubblica 
- Autenticazione ed integrità: funzioni hash e MAC
- Firme digitali 
- Altro: generazione di numeri pseudo casuali, prove zero knowledge 


- Il cifrario simmetrico condivide la stessa chiave per la cifratura e la decifrazione 
	- data encryption:
		- standard
		- des triplo, modalità di cifratura
	- RC2, RC4, RC5, RC6
	- Advanced encryprion standard (AES)
	- Blowfish 


- Il cifrario asimmetrico impiega 2 chiavi differenti 
	- una pubblica per la cifratura
	- una privata per la decifratura 


- La firma digitale consiste nell' apposizione di una firma ad un documento digitale 
	- deve poter essere facilmente prodotta dal firmatario
	- la firma è univoca , nessuno deve essere in grado di riprodurla 
		- chiunque può facilmente verificarla
	- Algoritmi
		- RSA
		- Digital signature standard (DSS)

## Funzione hash 

il Valore hash è una rappresentazione non ambigua e non falsificabile del messaggio. 
- impiego:
	- firma digitale 
	- integrità dei dati 
	- certificazione del tempo 
- Integrità: 
 ![[Pasted image 20231212110411.png]]

- funzione message Autentication Code (MAC)
![[Pasted image 20231212110628.png]]
- impiego: 
	- integrità dei dati 
	- autenticità dei dati: verificare il mittente 

- Proprietà di sicurezza
	- Confidenzialità: protezione da un soggetto estraneo
	- Autenticazione: certezza di identificare l' interlocutore 
	- integrità: verificare che il messaggio non sia stato modificato durante la trasmissione
		- solo chi è autorizzato può modificare l' attività di un sistema o le info trasmesse.
	- non-Ripudio: negare il disconoscimento del messaggio al mittente o al destinatario 
	- Anonimia: nascondere l' identità di chi ha compiuto un'azione nel contesto crittografico 



#### Proprietà di una funzione hash 
- One - way (pre-image resistant)
	- dato un hash y,  è computazionalmente difficile trovare M | y=h(M)

- Sicurezza debole (2nd pre image resisitance) 
	- dato m è computazionalmente difficile trovare una variazione di M, M' |h(M')

- Sicurezza forte (Collision resistance)
	- è computazionalmente difficile trovare 2 diversi messaggi con lo stesso valore hash.


#### Definizioni
- One way Hash function (OWHF):
	- verifica proprietà pre image e 2nd pre image resistance 
	- viene detta weak one-way hash function 
- Collision resistant hash function (CRHF)
	- verifica la proprietà di collision resistance 
	- viene detta strong one-way hash function 


#### Costruzione 
Messaggi di lunghezza arbitraria sono trattati utilizzando hash con input fisso 

- il messaggio viene diviso in k blocchi di lungheza fissa 
- essi vengono trattati in modo seriale/iterato e parallelo 

#### MD4/MD5
md= Message Digest 
![[Pasted image 20231212114529.png]]

le operazioni sono efficienti su architetture 32 bit little-endian 
- entrambe hanno come obbiettivi: 
	- una sicurezza forte 
	- una sicurezza diretta
	- velocità di esecuzione 
	- semplicità e compattezza 

- Processano il messaggio in blocchi da 512 bit 
- i 2 metodi impiegano diverse operazioni sulle word in input x e y restituendo una nuova word:
- come funzione di compressione: 
	- ogni round prende in input 
		- blocco corrente di 512 bit =16 word
		- valore corrente del buffer, 4 word ABCD per 128 bit 
	- ogni round consiste in 16 operazioni 
		- ![[Pasted image 20231212115107.png]]
	- l' output dell'ultima fase viene sommato all'input della prima fase 
		- la somma avviene word a word
	- l'output dell' L-esima frase è il digest a 128 bit 
	  
	  
	        ![[Pasted image 20231212115515.png]]


![[Pasted image 20231212120037.png]]
#### SHS/SHA-1/ SHA-256, 512, 384

SHS= Secure Hash Standard 
SHA= Secure Hash Algorithm

- operazioni efficienti su architetture a 32bit big-endian 
- stessi principi di MD4/5 ma più sicuro

SHA processa blocchi da 512 bit (ogni blocco da 16 parole di 32 bit) 
Espansione blocco ed iterazioni
- 4 round di 20 operazioni ciascuna (80)
- per ogni iteraziona una parola X\[i] viene calcolata dal blocco input  
![[Pasted image 20231212120132.png]]![[Pasted image 20231212120149.png]]

