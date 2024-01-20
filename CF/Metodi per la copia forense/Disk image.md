

- Supporti ottici 
	- Formato ISO: più comune.
	- Formato .bin = Copia RAW.
	- Formato .cue = Metadati.

- Formato DD/RAW.
Formato semplice è un container dello stream

- Problematiche: 
	- Non conserva metadati dell'evidence: modello, seriale dimensione, etc.
	- Non conserva hash calcolati.
	- Non esegue compressione.
	- Non può contenere più di un file/stream.
	  
- Smart (EWF)
	- obbiettivo: accesso veloce ad una parte dell' immagine. 
		- Segmentazione: .s01 ; .s02 ; etc... etc... 
		- ogni segmento è composto da:
			- headerfile: signature e numero di segmento. 
			- una o più sezioni:
				- header section. 
				- volume section. 
				- table section. 
				- next/done sections. 
![[Pasted image 20231211145303.png]]

- Encase L01 Logical (EWF)
	- acquisizione di file logici
	- segmentazione:  .l01 ; l02 ; etcetc...
	- impiega 15 sezioni (+2 al formato E01)
		- Ltree section. 
		- Ltypes section.

- Advanced Forensics format (AFF/AFF4)
	- ogni disco separato in 2 layer. 
		- disk-rappresentation layer (metadato).
		- data-storage layer (dato). 
		![[Pasted image 20231211145614.png]]