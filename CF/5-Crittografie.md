
- Un protocollo o schema definisce le interazioni fra le parti per ottenere le proprietà di sicurezza desiderate. 
- le parti sono le entità coinvolte nello schema. 

- i protocolli si basano su una serie di protocolli più semplici detti primitive crittografiche
	- risolvono problemi facili. 
	- possono essere usati per risolvere problemi più complessi. 

le primitive crittografiche risolvono i seguenti problemi: 
- CIFRATURA: cifrati simmetrici o asimmetrici o a chiave pubblica. 
- Autenticazione ed integrità: funzioni hash e MAC.
- Firme digitali. 
- Altro: generazione di numeri pseudo casuali, prove zero knowledge. 


- Il cifrario simmetrico condivide la stessa chiave per la cifratura e la decifrazione 
	- data encryption:
		- standard
		- des triplo, modalità di cifratura.
	- RC2, RC4, RC5, RC6.
	- Advanced encryption standard (AES).
	- Blowfish. 


- Il cifrario asimmetrico impiega 2 chiavi differenti 
	- una pubblica per la cifratura.
	- una privata per la decifratura. 


- La firma digitale consiste nell' apposizione di una firma ad un documento digitale 
	- deve poter essere facilmente prodotta dal firmatario.
	- la firma è univoca , nessuno deve essere in grado di riprodurla 
		- chiunque può facilmente verificarla.
	- Algoritmi
		- RSA.
		- Digital signature standard (DSS).

![[Funzione hash ]]

![[MD4-MD5]]

![[Pasted image 20231212120037.png]]

![[SHS-SHA-1, SHA-256, 512, 384]]
