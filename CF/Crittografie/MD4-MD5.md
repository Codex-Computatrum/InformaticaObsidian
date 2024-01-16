
md= Message Digest 
![[Pasted image 20231212114529.png]]

le operazioni sono efficienti su architetture 32 bit little-endian 
- entrambe hanno come obbiettivi: 
	- una sicurezza forte. 
	- una sicurezza diretta.
	- velocità di esecuzione. 
	- semplicità e compattezza. 

- Processano il messaggio in blocchi da 512 bit. 
- i 2 metodi impiegano diverse operazioni sulle word in input x e y restituendo una nuova word:
- come funzione di compressione: 
	- ogni round prende in input 
		- blocco corrente di 512 bit =16 word.
		- valore corrente del buffer, 4 word ABCD per 128 bit. 
	- ogni round consiste in 16 operazioni.
		- ![[Pasted image 20231212115107.png]]
	- l' output dell'ultima fase viene sommato all'input della prima fase 
		- la somma avviene word a word
	- l'output dell' L-esima frase è il digest a 128 bit 	  
	    
	    ![[Pasted image 20231212115515.png]]

